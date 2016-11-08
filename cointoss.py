#This generates the random numbers
import random
#This generates that we are doing math and calculating the number of coin tosses
import math
#This will print starting the program
print "Starting the program"
#setting variable head_count to 0 to start with as a default
head_count= 0
#same with tail_count
tail_count = 0
#setting the range from 1-5000
for a in range(1,5001):
    #setting variable rand to generate random numbers
    rand = round(random.random())
    #if variable rand is equal to 0
    if rand == 0:
        # and the face of the coin toss is "tail"
        face = "tail"
        #then change the tail count plus 1
        tail_count += 1
    else:
        #othwewise if the face of the coin toss is "head"
        face = "head"
        #then change the head count plus 1
        head_count += 1
        #print out "attempt # 1" Throwing a coin..its a (heads or tails) Got (1 heads) and (0 tails) so far
        print "attempt #" + str(a) +: Throwing a coin..Its a "+face"..Got "+str(head_count)+" head(s) and "+str(tail_count)+" tail(s) so far"
        print "end"
