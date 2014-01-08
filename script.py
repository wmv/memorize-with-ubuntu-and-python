#!/usr/bin/python
# -*- coding: utf8 -*-
  
import sys, os, subprocess
from time import sleep
  
quotes = []
glossary = "glossary-business.txt"  #<------- REPLACE PATH HERE
MAX_LENGTH = 120
  
def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return
     
def shortenedQuotes():
    global quotes
    new_array = []
    for quote in quotes:
        chunks = len(quote)/MAX_LENGTH
        for i in range(chunks):
            l = i * MAX_LENGTH
            r = l + MAX_LENGTH
            new_array.append(quote[l:r])
        new_array.append(quote[r:])
    return new_array
  
def getListOfQuotes():
    global glossary
    global quotes
    counter = -1
    if (os.stat(glossary)[6]!=0):
        for lines in open(glossary, 'r'):
            a = lines.strip()
            quotes.append(a)
        sendmessage("There are " + str(len(quotes)) + " quotes before shortening. Recalculating...")
        sleep(20)
        temp = shortenedQuotes()
        quotes = temp
        sendmessage("There are " + str(len(quotes)) + " quotes now. ")
        sleep(20)
 
    else:
        sendmessage("OOPS! THE LIST IS EMPTY!")
        sys.exit()
  
def main():
    counter = 0
    answer = 'y'
    global contents
    getListOfQuotes()
    if len(quotes) != 0:
        sendmessage("Displaying " + str(len(quotes)) + " businessquotes")
        sleep(20)
    for quote in quotes:
        counter = counter + 1
        sendmessage(quote)
        sleep(20)
    sendmessage("No more quotes. Go to the terminal to repeat or terminate the script")
  
    if answer == raw_input("Please enter 'y' to continue or any other key to terminate"):
        main()
    else:
        sendmessage("Bye!")
        sys.exit()
  
if __name__ == '__main__':
    main()
