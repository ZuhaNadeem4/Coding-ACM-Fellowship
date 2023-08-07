# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 21:14:00 2023

@author: ZUHA NADEEM
"""
class Solution(object):
    def __init__(self,nums):
        self.nums=nums
    def removeDuplicates(self, nums):
        len_dup=len(nums)
        iterator=0;
        while iterator<len_dup:
            while nums.count(nums[iterator])!=1:
                nums.remove(nums[iterator])
            len_dup=len(nums)
            iterator+=1
        k=len(nums)
        print(k)
class object:
    pass
nums=[0,0,1,1,1,2,2,3,3,4]
sol=Solution(nums);
sol.removeDuplicates(nums)

