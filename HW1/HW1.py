text = open('./text.txt',encoding="utf8")
i=0
nonletters = set()
for line in text.readlines():
    wordsinline = line.split(' ')
    for word in wordsinline:
        for char in word.lower():
            if(char <= 'a' or char >= 'z'):
                if not char[0] == '\n':    
                    nonletters.add(char)
print(nonletters)
    