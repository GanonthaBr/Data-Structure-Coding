import time
from collections import defaultdict


class CloudStore:
    def __init__(self):
        # Level 1: Basic storage
        self.store = {}
        
        # Level 2: Versioning - stores list of (version, value) tuples
        self.versions = defaultdict(list)
        self.version_counter = 0
        
        # Level 3: TTL - stores (expiration_time, None means no expiry)
        self.ttl_store = {}
        
        # Level 4: Access frequency tracking
        self.access_count = defaultdict(int)
    
    # ==================== LEVEL 1: Basic CRUD ====================
    
    def SET(self, key, value):
        """Set a key-value pair."""
        self.version_counter += 1
        self.store[key] = value
        self.versions[key].append((self.version_counter, value))
        # Clear any TTL when setting without TTL
        if key in self.ttl_store:
            del self.ttl_store[key]
        return True
    
    def GET(self, key):
        """Get the latest value for a key."""
        # Check if key exists
        if key not in self.store:
            return None
        
        # Check TTL expiration (Level 3)
        if key in self.ttl_store:
            if time.time() > self.ttl_store[key]:
                # Key has expired - delete it
                self._delete_key(key)
                return None
        
        # Track access (Level 4)
        self.access_count[key] += 1
        
        return self.store[key]
    
    # ==================== LEVEL 2: Versioning ====================
    
    def GET_AT(self, key, version):
        """Get the value at a specific version."""
        if key not in self.versions:
            return None
        
        # Check TTL expiration
        if key in self.ttl_store:
            if time.time() > self.ttl_store[key]:
                self._delete_key(key)
                return None
        
        # Find the value at or before the specified version
        # We want the latest version that is <= the requested version
        result = None
        for ver, val in self.versions[key]:
            if ver <= version:
                result = val
            else:
                break
        
        if result is not None:
            # Track access (Level 4)
            self.access_count[key] += 1
        
        return result
    
    # ==================== LEVEL 3: TTL/Expiration ====================
    
    def SET_WITH_TTL(self, key, value, ttl):
        """Set a key-value pair with a time-to-live in seconds."""
        self.version_counter += 1
        self.store[key] = value
        self.versions[key].append((self.version_counter, value))
        self.ttl_store[key] = time.time() + ttl
        return True
    
    def _delete_key(self, key):
        """Internal method to delete a key and all its data."""
        if key in self.store:
            del self.store[key]
        if key in self.versions:
            del self.versions[key]
        if key in self.ttl_store:
            del self.ttl_store[key]
        if key in self.access_count:
            del self.access_count[key]
    
    # ==================== LEVEL 4: Filtering/Analysis ====================
    
    def GET_TOP_KEYS(self, n):
        """
        Get the top n most accessed keys.
        Sorted by frequency (descending), then lexicographically (ascending).
        """
        # Clean up expired keys first
        self._cleanup_expired()
        
        # Get keys with their access counts
        keys_with_counts = [
            (key, count) for key, count in self.access_count.items()
            if key in self.store  # Only include keys that still exist
        ]
        
        # Sort by: frequency descending (-count), then key ascending (key)
        keys_with_counts.sort(key=lambda x: (-x[1], x[0]))
        
        # Return top n keys
        return [key for key, count in keys_with_counts[:n]]
    
    def _cleanup_expired(self):
        """Remove all expired keys."""
        current_time = time.time()
        expired_keys = [
            key for key, expiry in self.ttl_store.items()
            if current_time > expiry
        ]
        for key in expired_keys:
            self._delete_key(key)


# ==================== TESTING ====================

if __name__ == "__main__":
    print("=" * 50)
    print("LEVEL 1: Basic CRUD")
    print("=" * 50)
    
    store = CloudStore()
    store.SET("name", "Alice")
    store.SET("age", 25)
    print(f"GET('name'): {store.GET('name')}")  # Alice
    print(f"GET('age'): {store.GET('age')}")    # 25
    print(f"GET('unknown'): {store.GET('unknown')}")  # None
    
    print("\n" + "=" * 50)
    print("LEVEL 2: Versioning")
    print("=" * 50)
    
    store2 = CloudStore()
    store2.SET("data", "v1")  # version 1
    store2.SET("data", "v2")  # version 2
    store2.SET("data", "v3")  # version 3
    print(f"GET('data'): {store2.GET('data')}")           # v3 (latest)
    print(f"GET_AT('data', 1): {store2.GET_AT('data', 1)}")  # v1
    print(f"GET_AT('data', 2): {store2.GET_AT('data', 2)}")  # v2
    print(f"GET_AT('data', 3): {store2.GET_AT('data', 3)}")  # v3
    
    print("\n" + "=" * 50)
    print("LEVEL 3: TTL/Expiration")
    print("=" * 50)
    
    store3 = CloudStore()
    store3.SET_WITH_TTL("temp", "expires_soon", 2)
    print(f"GET('temp') immediately: {store3.GET('temp')}")  # expires_soon
    print("Waiting 3 seconds...")
    time.sleep(3)
    print(f"GET('temp') after 3 seconds: {store3.GET('temp')}")  # None (expired)
    
    print("\n" + "=" * 50)
    print("LEVEL 4: Top Keys by Access Frequency")
    print("=" * 50)
    
    store4 = CloudStore()
    store4.SET("apple", 1)
    store4.SET("banana", 2)
    store4.SET("cherry", 3)
    store4.SET("date", 4)
    
    # Access keys different number of times
    for _ in range(5):
        store4.GET("apple")
    for _ in range(3):
        store4.GET("banana")
    for _ in range(3):
        store4.GET("cherry")
    for _ in range(1):
        store4.GET("date")
    
    print(f"GET_TOP_KEYS(2): {store4.GET_TOP_KEYS(2)}")  # ['apple', 'banana']
    print(f"GET_TOP_KEYS(4): {store4.GET_TOP_KEYS(4)}")  # ['apple', 'banana', 'cherry', 'date']
    # Note: banana and cherry both have 3 accesses, so sorted lexicographically
    
    print("\n" + "=" * 50)
    print("All tests completed!")
    print("=" * 50)
