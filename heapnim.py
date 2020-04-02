import random
import copy
import sys
def main():
    print('Enter a valid integer value for each pile.')
    pile1 = int(input("Enter the size of pile A: "))
    pile2 = int(input("Enter the size of pile B: "))
    pile3 = int(input("Enter the size of pile C: "))

    dict = {'A':pile1,'B': pile2,'C':pile3}
    while sum(dict.values()) > 0:
        nimsum = dict['A']^dict['B']^dict['C']
        print ("A   B   C")
        print (str(dict['A'])+'   '+ str(dict['B'])+'   '+str(dict['C']))
        print ("Current Nim-Sum %s (%s) \n" % (nimsum, str(int2bin(nimsum)).lstrip('0') ))
        print ("Current winning strategy is:\n")
        print (strategy(dict))
        valid = False
        while(valid==False):
            pickpile = input("Player 1, enter which pile to take from :")
            if pickpile == 'A' or pickpile=='B' or pickpile=='C':
                valid = True
        
        valid = False
        while(valid ==False):
            takenum = input("Player 1, enter how many stones to take from pile %s :" % pickpile)
            if takenum.isalnum() and not(takenum.isalpha()):
                if int(takenum)<= dict[pickpile]:
                    valid = True
        dict[pickpile]= dict[pickpile]-int(takenum)
        nimsum = dict['A']^dict['B']^dict['C']
        if sum(dict.values()) == 0:
            print ('Congratulations, player 1 wins!')
            break
        print ("A   B   C")
        print (str(dict['A'])+'   '+ str(dict['B'])+'   '+str(dict['C']))
        print ("Current Nim-Sum %s (%s) \n" % (nimsum, str(int2bin(nimsum)).lstrip('0') ))
        print ("The winning strategy is:\n")
        print (strategy(dict))
        valid = False
        while(valid==False):
            pickpile = input("Player 2, enter which pile to take from :")
            if pickpile == 'A' or pickpile=='B' or pickpile=='C':
                valid = True
        
        valid = False
        while(valid ==False):
            takenum = input("Player 2, enter how many stones to take from pile %s :"% pickpile) 
            if takenum.isalnum() and not(takenum.isalpha()):
                if int(takenum) <= dict[pickpile]:
                    valid = True
        dict[pickpile]= dict[pickpile]-int(takenum)
        nimsum = dict['A']^dict['B']^dict['C']
        if sum(dict.values()) == 0:
            print ('Congratulations, player 1 wins!')
            break

def strategy(dict):
    # Strategy function takes a dictionary of key(pile name): value(pile size)
    ndict = copy.deepcopy(dict)
    nimsum = 0
    for item in ndict.values():
        nimsum = nimsum ^ item #xor of all the pile sizes
    # if the nimsum is 0, no winning strategy
    if nimsum ==0: return 'NimSum 0. You have no winning strategy unless your opponent makes a mistake'
    # else, there must be a winning strategy!
    else:
        nimsumb = int2bin(nimsum) #nimsum in binary
        nimsumb_str = str(nimsumb).lstrip('0') #removes all the leading 0s
        mostsig = len(nimsumb_str) # most significant power of 2
        #pile that has at least 2**(mostsignificant-1) stones, and the pile to take from
        highest = 2**(mostsig-1)
        mostk = ''
        takeaway = -1 #initializing take
        while takeaway <1:
            for item in ndict.keys():
                if ndict[item] >= highest:
                    mostk = item # find the pile with at least 2**(mostsig-1) stones
            #start with pile mostk
            #pickk = nimsum +* mostk          
            pickk = nimsum ^ int(ndict[mostk]) #Appropriate number of stones to take         
            takeaway = ndict[mostk]-pickk
            del ndict[mostk]
        return "Take %s away from pile %s " %(takeaway, mostk) # returns current winning strategy
    
def int2bin(n, count=24):
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])
    
main()
