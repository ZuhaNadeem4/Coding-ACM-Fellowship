import cProfile
def sum():
    o=0;
    lists=[];
    while o<5:
     print(1,3);
     lists.append(o)
     o+=1;
cProfile.run('sum()')