#History Quiz
#The purpose of this project is to create a quiz about history.
#Author: Thomas Fiske
#Date: 8/9/2022

import time

def startMenu():
    print("_____________________________________________________________________________________")
    print()
    print("Welcome to the History Quiz made by Thomas Fiske")
    print("You will be asked 10 questions, each one is worth 1 point for a total of 10 points")
    print("Good luck!")
    print()
    print("_____________________________________________________________________________________")


class questionClass:
    pass


question1 = questionClass()
question1.question = "What day did Franklin D. Roosevelt Die?" #April 12, 1945
question1.answer1 = "1. April 12, 1945"
question1.answer2 = "2. April 15, 1945"
question1.answer3 = "3. March 30, 1945"
question1.answer4 = "4. April 10, 1945"
question1.correctAnswer = 1

question2 = questionClass()
question2.question = "In what year did child labor laws start in the United States?" #1938
question2.answer1 = "1. 1952"
question2.answer2 = "2. 1938"
question2.answer3 = "3. 1945"
question2.answer4 = "4. 1923"
question2.correctAnswer = 2

question3 = questionClass()
question3.question = "When was the Battle of Gettysburg fought during the Civil War?" #July 1 through July 3, 1863
question3.answer1 = "1. July 5 through July 7, 1863"
question3.answer2 = "2. June 1 through June 3, 1863"
question3.answer3 = "3. July 4 through July 8, 1863"
question3.answer4 = "4. July 1 through July 3, 1863"
question3.correctAnswer = 4

question4 = questionClass()
question4.question = "Who was the first ruler of the Mongol Empire?" #Genghis Khan
question4.answer1 = "1. Tolui Khan"
question4.answer2 = "2. Genghis Khan"
question4.answer3 = "3. Güyük Khan"
question4.answer4 = "4. Möngke Khan"
question4.correctAnswer = 2

question5 = questionClass()
question5.question = "What year did the North American Free Trade Agreement (NAFTA) go into effect?" #1994
question5.answer1 = "1. 1994"
question5.answer2 = "2. 1995"
question5.answer3 = "3. 1993"
question5.answer4 = "4. 1990"
question5.correctAnswer = 1

question6 = questionClass()
question6.question = "In what year is the Bubonic Plague believed to have started in Europe and Asia?" #1346
question6.answer1 = "1. 1358"
question6.answer2 = "2. 1337"
question6.answer3 = "3. 1346"
question6.answer4 = "4. 1325"
question6.correctAnswer = 3

question7 = questionClass()
question7.question = "What was the name of the Ukrainian nuclear power plant that was the site of a nuclear disaster in April 1986?" #Chernobyl
question7.answer1 = "1. Bezhetsk"
question7.answer2 = "2. Chernobyl"
question7.answer3 = "3. Gusinoozyorsk"
question7.answer4 = "4. Chernogolovka"
question7.correctAnswer = 2

question8 = questionClass()
question8.question = "Who was the first Emperor of Rome?" #Augustus
question8.answer1 = "1. Julius Caesar"
question8.answer2 = "2. Arcadius"
question8.answer3 = "3. Maximinus I"
question8.answer4 = "4. Augustus"
question8.correctAnswer = 4

question9 = questionClass()
question9.question = "What year was Nelson Mandela freed from prison?" #1990
question9.answer1 = "1. 1991"
question9.answer2 = "2. 1992"
question9.answer3 = "3. 1990"
question9.answer4 = "4. 1989"
question9.correctAnswer = 3

question10 = questionClass()
question10.question = "How many years did the 100 years war last?" #116 years
question10.answer1 = "1. 116 years"
question10.answer2 = "2. 100 years"
question10.answer3 = "3. 101 years"
question10.answer4 = "4. 103 years"
question10.correctAnswer = 1

#Game Start
startMenu()
time.sleep(5)

userScore = 0

#question 1
print(question1.question)
print()
print(question1.answer1)
print(question1.answer2)
print(question1.answer3)
print(question1.answer4)
print()
print("Enter your answer as a number ")

ans1 = int(input())


if ans1 == 1:
    userScore += 1
    print("Correct!")
else:
    print("Incorrect!")


print("You're score is now: ", userScore)
print("Lets move onto the next question")
print()
time.sleep(3)

#question 2
print(question2.question)
print()
print(question2.answer1)
print(question2.answer2)
print(question2.answer3)
print(question2.answer4)
print()
print("Enter your answer as a number ")

ans2 = int(input())


if ans2 == 2:
    userScore += 1
    print("Correct!")
else:
    print("Incorrect!")


print("You're score is now: ", userScore)
print("Lets move onto the next question")
print()
time.sleep(3)

#question 3
print(question3.question)
print()
print(question3.answer1)
print(question3.answer2)
print(question3.answer3)
print(question3.answer4)
print()
print("Enter your answer as a number ")

ans3 = int(input())


if ans3 == 4:
    userScore += 1
    print("Correct!")
else:
    print("Incorrect!")


print("You're score is now: ", userScore)
print("Lets move onto the next question")
print()
time.sleep(3)

#question 4
print(question4.question)
print()
print(question4.answer1)
print(question4.answer2)
print(question4.answer3)
print(question4.answer4)
print()
print("Enter your answer as a number ")

ans4 = int(input())


if ans4 == 2:
    userScore += 1
    print("Correct!")
else:
    print("Incorrect!")


print("You're score is now: ", userScore)
print("Lets move onto the next question")
print()
time.sleep(3)

#question 5
print(question5.question)
print()
print(question5.answer1)
print(question5.answer2)
print(question5.answer3)
print(question5.answer4)
print()
print("Enter your answer as a number ")

ans5 = int(input())


if ans5 == 1:
    userScore += 1
    print("Correct!")
else:
    print("Incorrect!")


print("You're score is now: ", userScore)
print("Lets move onto the next question")
print()
time.sleep(3)

#question 6
print(question6.question)
print()
print(question6.answer1)
print(question6.answer2)
print(question6.answer3)
print(question6.answer4)
print()
print("Enter your answer as a number ")

ans6 = int(input())


if ans6 == 3:
    userScore += 1
    print("Correct!")
else:
    print("Incorrect!")


print("You're score is now: ", userScore)
print("Lets move onto the next question")
print()
time.sleep(3)

#question 7
print(question7.question)
print()
print(question7.answer1)
print(question7.answer2)
print(question7.answer3)
print(question7.answer4)
print()
print("Enter your answer as a number ")

ans7 = int(input())


if ans7 == 2:
    userScore += 1
    print("Correct!")
else:
    print("Incorrect!")


print("You're score is now: ", userScore)
print("Lets move onto the next question")
print()
time.sleep(3)

#question 8
print(question8.question)
print()
print(question8.answer1)
print(question8.answer2)
print(question8.answer3)
print(question8.answer4)
print()
print("Enter your answer as a number ")

ans8 = int(input())


if ans8 == 4:
    userScore += 1
    print("Correct!")
else:
    print("Incorrect!")


print("You're score is now: ", userScore)
print("Lets move onto the next question")
print()
time.sleep(3)

#question 9
print(question9.question)
print()
print(question9.answer1)
print(question9.answer2)
print(question9.answer3)
print(question9.answer4)
print()
print("Enter your answer as a number ")

ans9 = int(input())


if ans9 == 3:
    userScore += 1
    print("Correct!")
else:
    print("Incorrect!")


print("You're score is now: ", userScore)
print("Lets move onto the next question")
print()
time.sleep(3)

#question 10
print(question10.question)
print()
print(question10.answer1)
print(question10.answer2)
print(question10.answer3)
print(question10.answer4)
print()
print("Enter your answer as a number ")

ans10 = int(input())


if ans10 == 1:
    userScore += 1
    print("Correct!")
else:
    print("Incorrect!")


print("That is the final question")
print("Calculating final score")
print()
time.sleep(5)

userScorePercent = userScore * 10


print("_____________________________________________________________________________________")
print("Thank you for playing")
print("you're final score is ", userScore, "/ 10 or ", userScorePercent, "Percent")
print("_____________________________________________________________________________________")
