f1 = open("input.txt", "r")      #open input file
lines=f1.readlines()      #read lines from input file
items=[]
noofemp=int(lines[0][-2])
for i in range(4,len(lines)):
  a,b = lines[i].split(':')
  b=b.rstrip()
  items.append([a,int(b)])      #appending items to list
items=sorted(items,key=lambda x:x[1]) # sorting the list 

diff=max(items,key=lambda x:x[1])    #assigning max value in list
diff=diff[1]
limit=len(items)-noofemp+1    #length of iteration

for i in range(0,limit):     #finding min difference
  vdiff=items[i+noofemp-1][1]-items[i][1]
  if vdiff<diff:
    minindex=i
    diff=vdiff
f1.close()       #close input file

f2 = open("output.txt", "w")        #open output file
f2.write("The goodies selected for distribution are:\n\n")
for i in range(minindex,minindex+noofemp):
  f2.write(str(items[i][0])+": "+str(items[i][1])+"\n")
f2.write("\n")
f2.write("And the difference between the chosen goodie with highest price and the lowest price is "+ str(diff))

f2.close()