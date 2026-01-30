# IMPLEMENTING A KEY-VALUE STORE WITH EXTRA FEATURES

# LEVEL 1 (Basic CRUD)
class CloudStore:

   # Level 1
   def __init__(self):
       self.store = {}
       self.version = 0

   def SET(self, key, value):
    #    if key in self.store.keys:
        
       self.store[key] = [value,self.version]
       self.version += 1
   

   def GET(self, key):
       return self.store.get(key,'Not available')
   
   def GET_AT(self, key, version):
       
       for k, v in sorted(self.store.items(), key=lambda item: item[1][1]):
           if k == key and v[1] == version:
               return v
               
   

   # Level 2: modify SET to store versions

    



if __name__ == "__main__":
    store1 = CloudStore()

    store1.SET("electronic1","Laptop")
    store1.SET("electronic1","Laptop")
    store1.SET("electronic1","Laptop")
    val1 = store1.GET('electronic1')

    store1.SET("electronic2","Laptop")
    val2 = store1.GET('electronic2')

    store1.SET("electronic3","Laptop")
    val3 = store1.GET('electronic3')

    print(f"The retrieve val 1 is: {val1}")

    at_version = store1.GET_AT('electronic2',1)
    print(f"The retrieve at version 2 is: {at_version}")
    at_version = store1.GET_AT('electronic3',2)
    print(f"The retrieve at version 3 is: {at_version}")

    latest_version = store1.GET('electronic1')
    print(f"The latest version of electronic1 is: {latest_version}")



    print(store1.store)