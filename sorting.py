#define text file to open
my_file = open('results/names.txt', 'r')

#read text file into list 
data = my_file.readlines()

my_file.close()

numNames = len(data)

for x in data:
    print('results/' + data[x].strip() + '.txt')
    #answersFile = open('results/' + data[x].strip() + '.txt', 'r')
    #answers = answersFile.readLines()
    #for y in data:
        #print(answers[y].strip())

#display content of text file
#print(data[0].strip())