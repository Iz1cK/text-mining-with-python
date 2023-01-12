import nltk
from nltk.probability import FreqDist
import pandas as pd
from nltk.stem import WordNetLemmatizer
from matplotlib import pyplot as plt

# nltk.download('words')
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('names')

lemmatizer = WordNetLemmatizer()
english_vocab = sorted(set(w.lower() for w in nltk.corpus.words.words()))
stopwords = set(nltk.corpus.stopwords.words("English"))
df = pd.read_csv('Twitter_data.csv')
descriptions = df['twitter_desc'].astype(str)
all_names=df['twitter_name'].astype(str)

allInDesk=[]
for sent in descriptions:
    if sent != None and type(sent) != float:
        for word in nltk.word_tokenize(sent):
            allInDesk.append(word.lower())
            
# word_lemmatization = [lemmatizer.lemmatize(word) for word in allInDesk]
# without_stopwords = [word for word in word_lemmatization if word not in stopwords]
# english_vocab_set=set(english_vocab)
# just_english_vocab = [word for word in without_stopwords if word in english_vocab_set]
# word_lemmatization_freq=FreqDist(just_english_vocab)
# most_common_30 = word_lemmatization_freq.most_common(30)

# print(most_common_30)

# plot_words=[]
# plot_frequencies=[]
# for w,f in most_common_30:
#     plot_words.append(w)
#     plot_frequencies.append(f)
# print(plot_words)
# print(plot_frequencies)

# plt.figure(figsize=(20,5), dpi= 70)
# plt.bar(plot_words, plot_frequencies, width=.5,color = '#1DA1F2')
# plt.gca().set_xticklabels(plot_words, rotation=45, horizontalalignment= 'right')
# plt.title("Word frequencies", fontsize=15)
# plt.ylabel('Frequency')
# plt.ylim(0, 4000)
# plt.xlabel('Word')
# plt.show()

names=nltk.corpus.names
# names.fileids()
male_names = names.words('male.txt')
female_names = names.words('female.txt')
# male=[]
# female=[]
# for name in all_names:
#     formatted_name = name.split()[0]
#     if formatted_name not in stopwords:
#         if formatted_name in male_names and formatted_name not in female_names:
#             male.append(formatted_name) 
#         if formatted_name not in male_names and formatted_name in female_names:
#             female.append(formatted_name)   
            
# print('male number is ',len(male))
# print('female number is ',len(female))
# male_percentage = (len(male)/(len(male)+len(female)))*100
# female_percentage = 100-male_percentage
# labels = ['Male '+str(round(male_percentage, 2))+'%', 'Female '+str(round(female_percentage, 2))+'%']
# plt.pie([male_percentage,female_percentage],colors=['#347DC1','#B85887'] ,labels = labels, startangle = 90)
# plt.show() 

# male_frequency = FreqDist(male)
# female_frequency = FreqDist(female)
male=[]
# female=[]
# for name in all_names:
#     first_name = name.split()[0]
#     if first_name not in stopwords:
#         if first_name in male_names and first_name not in female_names:
#             male.append(first_name)
#         if first_name not in male_names and first_name in female_names:
#             female.append(first_name)
# print('male number is ',len(male))
# print('female number is ',len(female))
# male_frequency = FreqDist(male)
# most_common_male_names = male_frequency.most_common(30)
# female_frequency = FreqDist(female)
# most_common_female_names = female_frequency.most_common(30)

# male_descriptions=[]
# female_descriptions=[]
# for i in range(len(descriptions)):
#     current_name = all_names[i]
#     current_description = descriptions[i]
#     if current_name.split()[0] in male:
#         for word in nltk.word_tokenize(current_description):
#             male_descriptions.append(word.lower())
#     if current_name.split()[0] in female:
#         for word in nltk.word_tokenize(current_description):
#             female_descriptions.append(word.lower())

# male_words_lemmatization=[lemmatizer.lemmatize(word) for word in male_descriptions]
# print("done 1")
# male_words_no_stopwords = [word for word in male_words_lemmatization if word not in stopwords]
# print("done2")
# # male_english_words = [word for word in male_words_no_stopwords if word in set(english_vocab)]

# male_english_words=[]
# english_vocab_set=set(english_vocab)
# count = 0
# for word in male_words_no_stopwords:
#     print(word)
#     if word in english_vocab:
#         male_english_words.append(word)
#     count+=1
#     print(str(len(male_words_no_stopwords)) +  " " +str(count))
# print("done 3")

# MusicalArtist_desc=[]
not_MusicalArtist_desc=[]
# for desc in df[df['type1']=='MusicalArtist']['twitter_desc']:
#     MusicalArtist_desc.append(str(desc))
for desc in df[df['type1']!='MusicalArtist']['twitter_desc']:
    for word in desc.split():
        not_MusicalArtist_desc.append()
print("done 1")
# print("done 2")
# MusicalArtist_desc_words=nltk.word_tokenize('  '.join(MusicalArtist_desc))
# print("done 3")
# print(MusicalArtist_desc_words)
not_MusicalArtist_desc_words=nltk.word_tokenize('  '.join(not_MusicalArtist_desc))
print("done 2")


musical_artist_data = df[df['type1']=='MusicalArtist']['twitter_desc']
non_musical_artist_data = df[df['type1']!='MusicalArtist']['twitter_desc']
print(len(non_musical_artist_data))
musical_artist_descriptions = nltk.word_tokenize(" ".join([str(description) for description in musical_artist_data]))
print("donezzzzzzz 1")
non_musical_artist_descriptions = nltk.word_tokenize(" ".join([str(description) for description in non_musical_artist_data]))

print("donezzzzzzz 2")





