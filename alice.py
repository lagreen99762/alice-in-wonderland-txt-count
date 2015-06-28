import string

f = open("/Users/yongcho822/Coding/Development/PycharmProjects/Practice/alice-in-wonderland-txt-count/alice.txt", "r")
count = {}
exclude = set(string.punctuation)
for aline in f:
    f = ''.join(ch for ch in aline if ch not in exclude)
    for word in f.split():

        #word.translate(None, string.punctuation) - this doesn't work for some reason
        #gives an output of 221 words instead of the correct 385.
        
        #word = word.replace('-', '').replace('"','').replace(',','').replace('.','').replace('_','').replace('?','')
        #word = word.replace('?', '').replace('!', '').replace("'",'').replace('(','').replace(')','').replace(':','')
        #word = word.replace('[','').replace(']','').replace(';','')

        word = word.lower()

        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1
keys = list(count.keys())
keys.sort()

out = open("output.txt", 'w')

for word in keys:
    out.write(word + " " + str(count[word]))
    out.write('\n')
print("The word 'alice' appears " + str(count['alice']) + " times in the book.")