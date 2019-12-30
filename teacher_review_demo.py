import pandas as pd
data=pd.read_csv("form2.csv")
data.head()

d=data.iloc[:,2:3].values
print(d)
ro=d.shape
row=ro[0]

for i in range(row):
    print((d[i][0]))

//OUTPUT-[['nice sir']
        ['good']]
       nice sir
       good
       
from nltk.tokenize import word_tokenize
for i in range(row):
    text=nltk.word_tokenize(d[i][0])
    print(nltk.pos_tag(text))   
//OUTPUT-[('nice', 'JJ'), ('sir', 'NN')]
         [('good', 'JJ')]

nltk.help.upenn_tagset('NN')
//OUTPUT-
NN: noun, common, singular or mass
    common-carrier cabbage knuckle-duster Casino afghan shed thermostat
    investment slide humour falloff slick wind hyena override subhumanity
    machinist ...
    
 nltk.help.upenn_tagset('JJ')
 //OUTPUT-
JJ: adjective or numeral, ordinal
    third ill-mannered pre-war regrettable oiled calamitous first separable
    ectoplasmic battery-powered participatory fourth still-to-be-named
    multilingual multi-disciplinary ...
    
from nltk.tokenize import word_tokenize                                            //FINDS OUT NUMBER OF WORDS AND THE ADJECTIVES
for i in range(row):
    text=nltk.word_tokenize(d[i][0])
    
    print(len(nltk.pos_tag(text)),nltk.pos_tag(text))
    true_list=nltk.pos_tag(text)
    for j in range(0,len(true_list)):
        if true_list[j][1] == 'JJ':
            print(true_list[j][0])
//OUTPUT-
2 [('nice', 'JJ'), ('sir', 'NN')]
nice
1 [('good', 'JJ')]
good

from nltk.tokenize import word_tokenize                                           //removes stop_words
for i in range(row):
    text=nltk.word_tokenize(d[i][0])
    
    meaningful_words = [w for w in text if not w in stops]
    print(meaningful_words)
    print(len(nltk.pos_tag(text)),nltk.pos_tag(meaningful_words))
    true_list=nltk.pos_tag(meaningful_words)
    for j in range(0,len(true_list)):
        if true_list[j][1] == 'JJ':
            print(true_list[j][0])
//OUTPUT-
['nice', 'sir']
2 [('nice', 'JJ'), ('sir', 'NN')]
nice
['good']
2 [('good', 'JJ')]
good
['good']
2 [('good', 'JJ')]
good

TEXTBLOB

FINAL

from nltk.corpus import stopwords                                              //IMPORTING STOPWORDS
from textblob import TextBlob                                                  //TEXTBLOB FOR SENTIMENT ANALYSIS
stops = set(stopwords.words("english")) 
import pandas as pd
data=pd.read_csv("form2.csv")
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')




from nltk.tokenize import word_tokenize
for i in range(row):
    text=nltk.word_tokenize(d[i][0])
    
    meaningful_words = [w for w in text if not w in stops]
    print(meaningful_words)
    blob=TextBlob(str(meaningful_words))
    print(len(nltk.pos_tag(text)),nltk.pos_tag(meaningful_words))
    true_list=nltk.pos_tag(meaningful_words)
    for j in range(0,len(true_list)):
        if true_list[j][1] == 'JJ':
            print(true_list[j][0])
            print(blob.sentiment)
  //OUTPUT

['nice', 'sir']
2 [('nice', 'JJ'), ('sir', 'NN')]
nice
Sentiment(polarity=0.6, subjectivity=1.0)
['good']
2 [('good', 'JJ')]
good
Sentiment(polarity=0.7, subjectivity=0.6000000000000001)
['good']
2 [('good', 'JJ')]
good
Sentiment(polarity=0.7, subjectivity=0.6000000000000001)
            
