import random
user_wins=0;
computer_wins=0;
options= ['rock','paper','scissor'];
while True:
    user_input=input("Type Rock/Paper/Scissor or Q to quit: ");
    if user_input.lower()=='q':
        break
    if user_input.lower() not in options:
        continue
    random_number=random.randint(0,2);
    computer_pick=options[random_number];
    if user_input.lower()=='rock' and computer_pick=='scissor':
        print("You've won!");
        user_wins+=1;
    elif user_input.lower()=='scissor' and computer_pick=='paper':
        print("You've won!");
        user_wins+=1;
    elif user_input.lower()=='scissor' and computer_pick=='paper':
        print("You've won!");
        user_wins+=1;
    else:
        print("You've lost!");
        computer_wins+=1;
print("You've won "+ str(user_wins)+" times")
print(print("Computer has won "+ str(computer_wins)+" times"))
print('Goodbye');
    
