import random
top_of_range=input('Type a number:');
if top_of_range.isdigit():
    top_of_range=int(top_of_range);
    if top_of_range <=0:
        print('Please enter a number larger than 0 next time');
        quit();
else:
    print('Please enter a number next time');
    quit();
random_number=random.randint(0,top_of_range);
guesses=1;
while True:
    user_guess=input('Type a number:');
    if user_guess.isdigit():
       user_guess=int(user_guess);
       if user_guess <=0:
            print('Please enter a number larger than 0 next time');
            quit();
    else:
        print('Please enter a number next time');
        quit();
        continue
    if user_guess==random_number:
        print("Congrats! You've got it!")
        break
    else:
        if user_guess>random_number:
            print("You were above the number!");
        else:
            print("You were below the number!");
        guesses+=1
print("You got it in "+ str(guesses) + " guesses.")