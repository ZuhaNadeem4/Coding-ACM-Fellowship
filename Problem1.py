numbers=input('Enter numbers to calculate their average:').lower();
n=1;
while True:
     number=input('Enter next number or enter end to stop:');
     if number=='end':
          break;
     elif number.isdigit()==False:
          print('Enter a number!')
          continue
     elif numbers.isdigit() and number.isdigit():
          n+=1
          numbers=str(int(numbers)+int(number))
print("The average of entered numbers is ",int(numbers)/n)