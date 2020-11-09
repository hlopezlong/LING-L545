#Directory ~/LING-L545/05_FinalProject



emojitext = open('emojioutput_520.json.text', 'r')
selected = open('selected_cases.txt','w')

cases = []
elim = []

for i in emojitext:
    text = i.replace("\n", "")
    #for idx in text:
    if '😜' in text: # unicode \u2026😜
        cases.append(i)
    else:
        elim.append(i)

for case in cases:
    selected.write(case)

emojitext.close()
selected.close()
