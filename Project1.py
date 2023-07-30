print('Welcome to my computer quiz');
play=input('Do you want to play the game?');
if play.lower()!='yes':
    quit()
print("Okay let's play");
questions=['CPU','GPU','PSU','RAM'];
answers=['central processing unit','graphics processing unit','power supply','random access memory'];
score=0;
for x in range (len(questions)): 
 answer=input('What does '+ questions[x]+  ' stand for?');
 if answer.lower()==answers[x]:
    print('Correct!');
    score+=1;
 else:
    print('Incorrect!');
print("You've got "+ str(score) +" questions correct!");
print("You've got "+ str((score/len(questions))*100) +"%.");

