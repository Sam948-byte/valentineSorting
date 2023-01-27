#initial variables
numQuestions = 10

#define text file to open
my_file = open('results/names.txt', 'r')

#read text file into list 
data = my_file.readlines()

my_file.close()

numNames = len(data)

for x in data:
    answersFile = open('results/' + x.strip() + '.txt', 'r')
    answers = answersFile.readlines()
    answersFile.close()
    for y in data:
        match = 0
        if y == x:
            break
        compAnswersFile = open('results/' + y.strip() + '.txt', 'r')
        compAnswers = compAnswersFile.readlines()
        compAnswersFile.close()
        for iteration, z in enumerate(answers, start=0):
            #print(z.strip())
            #print(compAnswers[answers.index(z)].strip())
            if z.strip() == compAnswers[iteration].strip() and (z.strip() == 'A' or z.strip() == 'B' or z.strip() == 'C' or z.strip() == 'D' or z.strip() == 'E'):
                match += 1
        print(x.strip() + ' has a ' + str(match / numQuestions * 100) + ' percent compatability with ' + y.strip())
    

#display content of text file
#print(data[0].strip())