from datetime import *
from time import ctime
from random import randint
import webbrowser

#User Input
inhour = str(input("Set Hour in form XX: "))
inminute = str(input("Set Minute in form XX: "))
inampm = str(input("Enter 0 for military, 1 for AM, 2 for PM: "))

#Generates Random Link from Text File
def random_link(txt):
  return randint(0, sum(1 for line in open(txt)) - 1)

#Checks if Current time and alarm time are equal
def check_time(currtime):
    if inampm == "0":
        if currtime[0] == inhour and currtime[1] == inminute:
            return True
    elif inampm == "1":
        if currtime[0] == inhour and currtime[1] == inminute:
            return True
    elif inampm == "2":
        pmtime = str(int(inhour) + 12)
        if pmtime == currtime[0] and currtime[1] == inminute:
            return True
    else:
        print ("Try Again with Correct Input for AM/PM")
        return True

def get_time(list):
    #Gets current time
    t = str(datetime.now()).split()
    clocktime = t[1]
    hrm = str(clocktime)
    #sets current time
    currhr = hrm[:2]
    currmin = hrm[3:5]
    list = [currhr, currmin]
    return list

def main(text):
    line = random_link(text)
    finished = False
    while finished == False:
        l = []
        l = get_time(l)
        if check_time(l) == True:
            #reads text file
            f = open(text)
            lines = f.readlines()
            #opens in browser
            webbrowser.open_new(lines[line])
            #close text file
            f.close()
            finished = True

main("youtubelinks.txt")
