nums = [0,1,2,2,3,0,4,2]
val = 2;
len_nums=len(nums);
iterator=0;
while iterator<len_nums:
    if nums[iterator]==val:
        nums.remove(val);
        iterator=0
        len_nums=len(nums)
    iterator+=1
print(nums)