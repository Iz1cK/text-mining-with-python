text = open('HW1/text.txt',encoding="utf8")
string = text.read().lower()
words = {}

nonletters = set('\n')
for line in string:
    wordsinline = line.split(' ')
    for word in wordsinline:
        for char in word.lower():
            if(char < 'a' or char > 'z'):
                if not char == '\n':
                    nonletters.add(char)

for char in nonletters:
    string = string.replace(char,"")


string = string.split(' ')
for word in string:
    words[str(word)] = words.get(str(word),0) + 1
four_letter_words = {word:count for word,count in words.items() if len(word) >=4}
max_word = [word for word,count in four_letter_words.items() if count == max(four_letter_words.values())]
print(max_word[0] + ": " + str(words.get(max_word[0])))
    