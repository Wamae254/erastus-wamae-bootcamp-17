wordstring = 'Run if you can run faster if they can not'

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("List\n" + str(wordlist) +  str(wordfreq) +"\n")
