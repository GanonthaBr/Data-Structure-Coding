"""
- for a pain of all adjancent elements in the array
- set their product as key and them as value
- then go through all keys, return the largest
"""

def adjancentElements(a):
    product = {}
    list_of_products = []
    for i in range(len(a)-1):
        p = a[i] * a[i+1]
        product[p] = (a[i],a[i+1])


    for k,v in product.items():
        list_of_products.append(k)

    
    return max(elt for elt in list_of_products)
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    adj = adjancentElements([3,6,-2,-5,7,3])
    print(adj)
    