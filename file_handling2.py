with open('writing_file.txt','w')as file:
  file.write('Hi I am Swapnil from Kathmandu')
file.close()

with open('writing_file.txt','r')as file:
  filelines=file.readlines()
  print("Splitted words:")
  for line in filelines:
    word=line.split()
    print(word)
file.close()

new_file=open('Newfile.txt','x')
new_file.close()

import os
print("Existence Checking: ")
if os.path.exists('Myfile.txt'):
  os.remove('Myfile.txt')
else:
  print("The file doesn't exist")
  

my_file=open('Myfile.txt','w')
my_file.write("Hello! I am Swapnil")
my_file.close


inputfile=open('Repeated.txt','r')
outputfile=open('Outputfile.txt','w')
lines_seen_so_far=set()
print("Eliminating Duplicate")

for line in inputfile:
  if line not in lines_seen_so_far:
    outputfile.write(line)
    lines_seen_so_far.add(line)

inputfile.close()
outputfile.close()

with open('codingal.txt') as fp:
  data1=fp.read()
  
with open('sample.txt') as fp:
  data2=fp.read()
  
data1 += '\n'
data1 += data2
print('Merging: ')

with open("mergedfile.txt",'w')as fp:
  fp.write(data1)
  