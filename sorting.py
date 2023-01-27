#imports
import os

#define text file to open
#my_file = open('results/names.txt', 'r')

#read text file into list 
#names = my_file.readlines()
names = os.listdir('results')

#my_file.close()

numNames = len(names)

for x in names:
    answersFile = open('results/' + x.strip(), 'r')
    answers = answersFile.readlines()
    answersFile.close()
    numQuestions = len(answers)
    for y in names:
        match = 0
        if y == x:
            break
        compAnswersFile = open('results/' + y.strip(), 'r')
        compAnswers = compAnswersFile.readlines()
        compAnswersFile.close()
        for iteration, z in enumerate(answers, start=0):
            if z.strip() == compAnswers[iteration].strip():
                match += 1
        print(x.strip('.txt') + ' has a ' + str(round(match / numQuestions * 100, 2)) + ' percent compatability with ' + y.strip('.txt'))