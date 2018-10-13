def removedupes1(list):
    result = []
    
    for i in range(len(list)):
        unique = True
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                unique = False
                break
        if unique:
            result.append(list[i])
    return result

from collections import defaultdict   
def removedupes2(list):
    result = defaultdict(int)
    for item in list:
        result[item] += 1
    return [k for k in result.keys()]
        
def removedupes3(list):
    return [x for x in set(list)]
    
def removeDuplicates4(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = []
        seen.append(nums[0])
        i = 1
        
        while i < len(nums):
            if nums[i] in seen:
                del(nums[i])
                
            else:
                seen.append(nums[i])
                i += 1
        return nums
def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setn = set(nums)
        sum = 0
        for i in setn:
            sum += 1
        return sum
print(removeDuplicates([1,2,2,3,4,5,5,5,6]))
    
