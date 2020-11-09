##Behaves like the unix 'cat' command
import sys

text = sys.stdin.read() #Reads in everything from standard input

sys.stdout.write(text) #Output everything to standard output
