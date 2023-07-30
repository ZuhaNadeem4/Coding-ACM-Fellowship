import time
start_time=time.time();
n=int(input('Enter the natural number upto which you want to find the sum:'));
sum=(n*(n+1))/2;
print("The sum is ",sum);
end_time=time.time();
print(end_time-start_time);