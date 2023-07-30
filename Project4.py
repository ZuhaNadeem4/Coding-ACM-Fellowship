name=input('Type your name: ');
print('\n')
print("Welcome! ",name, " to this adventure.");
print('\n')
answer=input("You've come to a dirt road,it has come to an end and can go left or right. Which way do you wanna go?").lower()
print('\n')
if answer=='left':
   answer=input("You are on the left path. There's a lake you wanna cross it or walk along the dry path? (swim/walk)").lower();
   print('\n')
   if answer=='swim':
       print('You tried to swim but got eaten by the alligators.\n"')
   elif answer=='walk':
       print('You walked for miles and died due to dehydration.\n"')
   else:
       print('Not a valid option.You lose!')
elif answer=='right':
      answer=input("You are on the right path. There's a shaky bridge you wanna cross it or wanna head back? (back/cross)").lower()
      print('\n')
      if answer=='cross':
          answer=input("You've met a stranger. Do you wanna say Hi to him or ignore him.(Hi/ignore)" ).lower()
          print('\n')
          if answer=='hi':
              print("He gave you the game map.You won!\n")
          elif answer=='ignore':
              print("You got lost on the track and died.\n")
          else:
              print('Not a valid option.You lose!\n"')
      elif answer=='back':
          print("You've lost!");
      else:
          print('Not a valid option.You lose!\n"')
         
else:
    print('Not a valid option.You lose!')
