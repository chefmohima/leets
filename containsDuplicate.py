def containsDuplicate1(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        seen = []
        seen.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.append(nums[i])
        return False
        
def containsDuplicate2(nums):
    stack = []
    nums.sort()
    stack.append(nums[0])
    for i  in range(1,len(nums)):
        if nums[i] == stack[-1]:
            return True
        else:
            stack.append(nums[i])
    return False

def containsDuplicate3(nums):
    s = set(nums)
    if len(s) < len(nums):
        return True
    else:
        return False
 
print(containsDuplicate2([1,2,4,10,2,1]))   

    
    
    
    
