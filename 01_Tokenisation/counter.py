import sys

countern = 0 #variable for saving counts
counterv = 0 #variable for saving counts

for c in sys.stdin.read():
    if c == 'и': #count a specific consonant
        countern = countern + 1
    elif c in 'аэиоу': #else if it is a vowel print counter
        counterv = counterv + 1
print(counterv)
print(countern)
