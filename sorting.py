#imports
import os

names = os.listdir('answers')

for x in names:
    answersFile = open('answers/' + x.strip(), 'r')
    answers = answersFile.readlines()
    answersFile.close()
    numQuestions = len(answers)
    for y in names:
        match = 0
        if y == x:
            break
        compAnswersFile = open('answers/' + y.strip(), 'r')
        compAnswers = compAnswersFile.readlines()
        compAnswersFile.close()
        for iteration, z in enumerate(answers, start=0):
            if z.strip() == compAnswers[iteration].strip():
                match += 1
        print(x.strip('.txt') + ' has a ' + str(round(match / numQuestions * 100, 2)) + '% compatability with ' + y.strip('.txt'))