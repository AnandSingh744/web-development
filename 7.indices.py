def find_occurrences(string1, string2):
   
    indices = []
    
   
    index = string1.find(string2)
    
    
    while index != -1:
        indices.append(index)
       
        index = string1.find(string2, index + 1)
    
   
    if not indices:
        return -1
    
    return indices
