

#solution without dictionary
def arrayIntx1(list1,list2):
    result = []
    for num in list1:
        if num in list2:
            result.append(num)
            list2.remove(num)
    return result

def arrayIntx2(list1,list2): 
    result = []
    for num in set(list1):
        countnum = min(list1.count(num),list2.count(num))
        for j in range(countnum):
            result.append(num)
    return result        
        
    
print(arrayIntx2([1,2,3,3,4],[2,2,3,3,4,1,1]))
    
