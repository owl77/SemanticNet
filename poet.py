import random
# import os

#to generate roget file do something like
#cat roget.txt | tr '[:upper:]' '[:lower:]' | tr -c '[:alnum:]\n\r' ' ' | tr ' ' '\n'  |  tr -d '\r' |  sort | uniq > roget

f = open('roget','r') 
preroget = f.read()
f.close()
roget = preroget.split('\n')
length = len(roget)

for n in range(0,17):

 x = random.randint(0,length-1)
 word = roget[x]
 print(word)
# com = "curl -s https://en.wiktionary.org/wiki/" + word +  " > dic/" + word + ".html"
# os.system(com)


#HAIKU OF RANDOM WORDS FROM ROGET
