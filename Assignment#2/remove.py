class Solution(object):
    def __init__(self,nums,val):
        self.nums=nums
        self.val=val
    def removeElement(self, nums, val):
        len_nums=len(nums);
        iterator=0;
        while iterator<len_nums:
            if nums[iterator]==val:
                nums.remove(val);
                iterator=0
                len_nums=len(nums)
            iterator+=1
        k=len_nums
        print(k)
class object:
    pass
nums = [0,1,2,2,3,0,4,2]
val = 2;
sol=Solution(nums, val)
sol.removeElement(nums, val)