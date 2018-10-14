from collections import defaultdict

#solution without dictionary
def singleNumber1(nums):
    nums.sort()
    i = 0
    while i < len(nums):
        if nums[i] == nums[-1]:
            return nums[i]
        if nums[i] != nums[i+1]: 
            return nums[i]
        i = i + 2
    #if #return 

#solution with dictionary
def singleNumber2(nums):
    d = defaultdict(int)
    for num in nums:
        d[num] += 1
    for k in d.keys():
        if d[k] < 2:
            return k
    
    
print(singleNumber2([1,2,3,3,4,1,4]))
