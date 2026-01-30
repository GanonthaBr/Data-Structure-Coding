def solution(queries):
    lst = []
    output = []
   
    for query in queries:
        
            
        if query[0] == 'ADD':
            lst.append(query[1])
            output.append("")
        
        
        
            
        if query[0] == 'EXISTS' and query[1] in lst:
            output.append('true')
        elif query[0] == 'EXISTS' and query[1]  not in lst:
            output.append('false')
            
            
        if query[0] == 'REMOVE':
            if query[1] in lst:
                lst.remove(query[1])
                output.append('true')
            else:
                output.append('false')
                
        #GET NEXT
        if query[0] == 'GET_NEXT':
            inner_lst=sorted([int(val) for val in lst])
            for item in inner_lst:
                if int(item) > int(query[1]):
                    output.append(str(item))
                    break
            else:
                output.append("")
            
                
    return output
            


    
            

queries = [["ADD","1"], 
 ["ADD","2"], 
 ["ADD","2"], 
 ["ADD","3"], 
 ["EXISTS","1"], 
 ["EXISTS","2"], 
 ["EXISTS","3"], 
 ["REMOVE","2"], 
 ["REMOVE","1"], 
 ["EXISTS","2"], 
 ["EXISTS","1"]]


if __name__ == "__main__":
    print(solution(queries))