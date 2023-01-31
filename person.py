#imports
import os
import sys

names = os.listdir('answers')


answersFile = open('answers/' + sys.argv[1].strip() + '.txt', 'r')
answers = answersFile.readlines()
answersFile.close()
numQuestions = len(answers)

for y in names:
    match = 0
    if y.strip('.txt') == sys.argv[1]:
        continue
    compAnswersFile = open('answers/' + y.strip(), 'r')
    compAnswers = compAnswersFile.readlines()
    compAnswersFile.close()
    for iteration, z in enumerate(answers, start=0):
        if z.strip() == compAnswers[iteration].strip():
            match += 1
    print(str(sys.argv[1]) + ' has a ' + str(round(match / numQuestions * 100, 2)) + '% compatability with ' + y.strip('.txt'))