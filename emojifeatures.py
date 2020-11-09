
import re
#from nltk.tokenize import TweetTokenizer
#tweet_tokenizer = TweetTokenizer()


with open('/Users/hollylopezlong/LING-L545/05_FinalProject/data/tweebopos.txt') as f:
    lines = [line.rstrip() for line in f]
    case =[]
    allcases =[]
    for line in lines:
        txt = line.split('\t')#separates by tab, and saves list of tabbed items in a list
        tweet = txt[0] #twokenized tweet
        pos = txt[1] #pos tags from Tweebo's tagger
        anno = txt[5:] #last 3 items after is taget emoji annotation, number of that emoji in tweet
        tokens = tweet.split(' ')
        case.append(tokens)
        case.append(pos)
        case.extend(anno)
        allcases.append(case)
        case = []

for case in allcases:
    search = case[2]
    tweett = case[0]
    pos = case[1].split(' ')
    if search in tweett:
        f1 = len(case[2]) #length of emoji token
        f2 = case[3] #the number of the emoji token
        #f3 = len(case[0]) # length of tweet
        x = tweett.index(search)
        if x == 0:
            posb4 = "null" # posb4 is the POS tag of the item preceeding the target token
            before = "null" # toke preceeding the target token
        else:
            posb4 = pos[x-1]
            if posb4 == ',':
                posb4 = 'comma'
            before = tweett[x-1]
            if before.startswith('@'):
                before = 'attag'
            elif before.startswith('#'):
                before = 'htag'
            elif before == ',':
                before = 'comma'
        if x == len(tweett)-1:
            posaft = "null"
            after = "null"
        else:
            posaft = pos[x+1]
            after = tweett[x+1]
            if posaft == ',':
                posaft = 'comma'
            if after.startswith('@'):
                after = 'attag'
            elif after.startswith('#'):
                after = 'htag'
            elif after == ',':
                after = 'comma'
            else:
                after = after
        print(f1, end ='\t')
        print(f2, end = '\t')
        #print(f3, end = '\t')
        print(posb4, end = '\t')
        print(before, end ='\t')
        print(posaft, end = '\t')
        print(after, end ='\t')
        print(case[-1])
