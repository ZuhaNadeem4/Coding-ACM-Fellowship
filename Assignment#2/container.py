heights=[1,8,6,2,5,4,8,3,7];
len_height=len(heights);
outer_list=[]
iterator2=0;
while(iterator2<len_height-1):
    inner_list=[]
    iterator=iterator2;
    while iterator<len_height-1:
       min_height=min(heights[iterator2],heights[iterator+1]);
       inner_list.append(min_height)
       iterator+=1
    outer_list.append(inner_list)
    iterator2+=1
len_min=len(outer_list);
iterator3=0;
while iterator3<len_min-1:
    iterator4=0;
    len_inlist=len(outer_list[iterator3]);
    while iterator4<len_inlist:
           outer_list[iterator3][iterator4]=outer_list[iterator3][iterator4]*(iterator4+1)
           iterator4+=1
    iterator3+=1
iterator5=0;
max_list=[]
while iterator5<len_min:
     max_list.append(max(outer_list[iterator5]))
     iterator5+=1
output=max(max_list);
print(output)