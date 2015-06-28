"""using defaultdict and sort by word count values"""

import string
from collections import defaultdict

word_counts = defaultdict(int)
exclude = set(string.punctuation)

with open("alice.txt", "r") as f, open("outputcount.txt", "w") as o:
    for aline in f:
        punct_free = ''.join(ch for ch in aline if ch not in exclude)
        for word in punct_free.split():
            if word.isalpha():
                word = word.lower()
                word_counts[word] += 1
                
    sorted_word_counts = sorted(word_counts.iteritems(), key = lambda (k,v):v, reverse = True)
    
    for word_pair in sorted_word_counts:
        o.write('"' + word_pair[0] + '"' + " comes up " + str(word_pair[1]) + " times.")
        o.write('\n')
        
print "The word \"alice\" comes up", word_counts['alice'], "times."

top_list=[]
for i,n in sorted_word_counts[:5]:
    top_list.append(i)
adding_quotes = map(lambda x:'"' + x + '"', top_list) 

print "The 5 most common words are", ", ".join(adding_quotes)+"."