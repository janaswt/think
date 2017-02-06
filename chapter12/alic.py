from builtins import str
f = open("alice.txt", "r")

count = {}
for line in f:
    for word in line.split():
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')
        word = word.lower()
        
        if word.isalpha():
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
keys = list(count.keys())
keys.sort()

out = open('alice_words.txt', 'w')
for word in keys:
    out.write(word + " " + str(count[word]))
    out.write("\n")
    
print("The word 'alice' apears " + str(count['alice']) + " times in the book" )