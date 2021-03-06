from random import randint


#From 186
# 20  = Simple Addition
#From 20-50 = Two Digit Addition
#From 50-60 = Three Digit Addition
#From 60-70 = Four Digit Addition
from datetime import datetime
from ResultWriter import writeToResultsFile
from datetime import date

today = date.today()
# Textual month, day and year	
todayDate = "Date: " +  today.strftime("%B %d, %Y")
print(todayDate)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
startTimeStr = "Start Time ="+ str(current_time)
print(startTimeStr)


#ADJUST THIS AND MAKE A PLAN 
#Make Him do this 3 times
#First Time do not raise difficulty after question 50
#Second Time do not raise the difficulty after question 60
#Thrid Time run the programme as designed

correct_counter = 0
wrong_counter = 0

for m in range(80):
    a = 0
    b = 0
    if(m<=20):
        a = randint(10, 20)
        b = randint(0, 10)
    elif(20<m<=50):
        a = randint(99, 200)
        b = randint(13, 99)
    elif(50<m<=60):
        a = randint(999, 3000)
        b = randint(100, 999)
    elif(60<m<=80):
        a = randint(3000, 4000)
        b = randint(1000, 3000)
    print("Question number: " + str(m))
    print("What is: "+ str(a) + " - " + str(b))
    user_anwser = input("Enter Anwser: ")
    if(str(user_anwser) == str(a-b)):
        print("Correct");
        correct_counter +=1 
    else:
        print("Wrong!")
        wrong_counter +=1
        stuck = True
        while(stuck):
            print("What is: "+ str(a) + " - " + str(b))
            user_anwser = input("Enter Anwser: ")
            if(str(user_anwser) == str(a-b)):
                print("Correct");
                
                stuck = False
            else:
                print("Wrong!")
                wrong_counter +=1
        
     
correctStr = "You got " + str(correct_counter) +" Correct!"
wrongStr = "You got " + str(wrong_counter) +" Wrong!"
print(correctStr)
print(wrongStr)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
EndTimeStr = "End Time: "+ str(current_time)
print(EndTimeStr)


writeToResultsFile("Test is: Subtraction",todayDate,startTimeStr, correctStr, wrongStr, EndTimeStr)
