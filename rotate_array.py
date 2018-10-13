def rotate(list,k):
    if k > len(list):
        k = k % len(list)
    list.reverse()
    list1 = list[:k]
    list2 = list[k:]
    
    if len(list1) > 1:
        list1.reverse()
    if len(list2) > 1:
        list2.reverse()
    
    list[:] = list1 + list2
    return list
    
print(rotate([1,2,3,4],1))


#Alternate solution
def rotate(list,k):
    if k > len(list):
        k = k % len(list)
    return list[k:] + list[:k]
