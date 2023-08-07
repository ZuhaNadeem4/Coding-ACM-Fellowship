from itertools import combinations
class Solution(object):
    def __init__(self,nums):
        self.nums=nums
    def threeSum(self, nums): 
        r=3;
        combination = combinations(nums, r);
        comb_list=[]
        for i in combination:
            comb_list.append(i)
        max_val=len(comb_list)
        iterator=0
        sum_zero=[]
        while iterator<max_val:
            iterator2=0
            sum=0;
            while iterator2<r:
                sum+=comb_list[iterator][iterator2]
                iterator2+=1
            if sum==0:
                sum_zero.append(list(comb_list[iterator]))
            iterator+=1
        if len(sum_zero)>0:
            print(sum_zero)
        else:
            print("No such triplets exist that'll sum upto zero")    
class object:
    pass
nums=[-1,0,1,2,-1,-4];
sol=Solution(nums);
sol.threeSum(nums)
