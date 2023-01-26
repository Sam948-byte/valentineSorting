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
        compAnswersFile = open('results/' + y.strip() + '.txt', 'r')
        compAnswers = compAnswersFile.readlines()
        compAnswersFile.close()
        for z in answers:
            if z.strip() != compAnswers[answers.index(z)].strip():
                continue
            match += 1
        print(x.strip() + ' has a ' + str(match / numQuestions * 100) + ' percent compatability with ' + y.strip())
    

#display content of text file
#print(data[0].strip())