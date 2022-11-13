text = open('HW1/text.txt',encoding="utf8")
string = text.read().lower()

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


words = {}
string = string.split(' ')
for word in string:
    words[str(word)] = words.get(str(word),0) + 1
four_letter_words = {word:count for word,count in words.items() if len(word) >=4}
max_word = [word for word,count in four_letter_words.items() if count == max(four_letter_words.values())]
print(max_word[0] + ": " + str(words.get(max_word[0])))

bigrams = {}
for i in range(len(string)-1):
    bigrams[str(string[i] + " " + string[i+1])] = bigrams.get(str(string[i] + " " + string[i+1]),0) + 1
max_bigram = [word for word,count in bigrams.items() if count == max(bigrams.values())]
print(max_bigram[0] + ": " + str(bigrams.get(max_bigram[0])))

three_letter_plus_words = []
count = 0
for word in string:
    if len(word) >= 3:
        count += 1
        three_letter_plus_words.append(word)
distinct_words = set(three_letter_plus_words)
print("Count of all words with 3 or more letters is: " + str(count))
print("Count of all distinct words with 3 or more letters is: " + str(len(distinct_words)))