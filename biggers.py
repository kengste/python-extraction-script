import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

from nltk import word_tokenize, pos_tag, tokenize, stem
import bag_of_words

def lemmatize(txtwordtokenizer):
	lemmtizer = stem.WordNetLemmatizer()
	words = [lemmtizer.lemmatize(word) for word in txtwordtokenizer]
	return words

def filter(text):    #return the text with or without the stopwords, regarding the if condition
	words = word_tokenize(text)
	words = lemmatize(words)
	filtered_sentence = []
	for w in words:
		filtered_sentence.append(w)
	return ' '.join(filtered_sentence)
    
def tokenization(sample_text):
	cust_tokenizer = tokenize.PunktSentenceTokenizer(train_text) 
	text =filter(sample_text)
	# Then we can actually tokenize, using:
	return cust_tokenizer.tokenize(text) #tokenize in sentences

def getKeySentences(l, tokenized):
	try:
		tab=[]
		for i in tokenized:
			words =word_tokenize(i)
			wordslow=[words[k].lower() for k in range (len(words))]
			tagged=pos_tag(words)
			p=[]
			for j in tagged:
				if j[1]=='NNP' and (j[0] in bag_of_words.unwanted_entities) == False:
					p.append(j[0])
					listt=[]
					for cle,valeur in (l.items()):
						k = 0
						while k< len(valeur)-1:
							if (valeur[k] in (lemmatize(wordslow))):
								listt = listt + [cle]
								k = len(valeur)
							else :
								k += 1
						
					if listt != []:
						if p!=[]:
							tab.append((listt, p))
						return i
		return ''
	except Exception as err:
		print(err)

train_text = "\
Nazaruddin launches fresh attack against former president\
Former Democratic Party treasurer Muhammad Nazaruddin alleged on Wednesday that former\
president Susilo Bambang Yudhoyono had used dirty money to finance his reelection bid in the\
2009 presidential election.\
Nazaruddin, whose testimonies in a number of high-profile graft cases led to the prosecution of\
high-ranking Democratic Party officials, said that the procurement of medical facilities at Udayana\
University�s hospital in Bali, worth Rp 16 billion (US$1.2 million), was one of the many state\
projects rigged to fund Yudhyono�s reelection bid.\
Nazaruddin said the Democratic Party had assigned party chairman Anas Urbaningrum to handle\
the procurement project to ensure that money siphoned off the project would flow into the party�s\
coffers prior to the election.\
The health medical equipment procurement was a multiyear project that ran from 2009 to 2011, and\
the Corruption Eradication Commission (KPK) is investigating alleged misuses of the budget,\
specifically from 2009.\
The KPK said, however, that it would also investigate the alleged misuse of budgets in the project\
in 2010 and 2011 if its investigators could collect enough evidence to support the investigation.\
The government allocated\
Rp 16 billion to Udayana University in 2009 to improve its health facilities at its hospital in Bali.\
More than Rp 7 billion was embezzled from the project, according to data provided by the KPK.\
�The Udayana case is one of many state projects handled by Anas. The money from the projects\
was later funneled to help the presidential bid. I will tell everything to the KPK in my questioning\
session today,� Nazaruddin told reporters at the KPK headquarters on Wednesday.\
The KPK grilled Nazaruddin as a witness in the university graft case to complete the dossiers on PT\
Mahkota Negara director Marisi Matondang, who was Nazaruddin�s confidant, and Udayana�s\
public administration and financial division head Made Meregawa, both of whom were named\
suspects in the case in December 2014.\
Mahkota Negara, the company that won the project, was a subsidiary of PT Permai Group. \
Nazaruddin said that he and Anas established Permai Group to hide slush funds collected from\
ministries and state institutions led by Democratic Party politicians under the tenure of Yudhoyono.\
Every year, Permai Group collected up to Rp 800 billion from allegedly rigging state projects.\
Nazaruddin further said that Yudhoyono�s son, Edhie �Ibas� Baskoro, who is currently the\
Democratic Party�s secretary-general, knew about the flow of money from the university project to\
the party�s coffers. �Ibas knew everything,� Nazaruddin said.\
Yudhoyono, who is the Democratic Party chairman, and his running mate Boediono, former Bank\
Indonesia (BI) governor, won the 2009 election with a landslide of about 60 percent of the vote.\
Late last year, Anas also claimed that part of the Rp 6.7 trillion bailout given to ailing Bank Century\
by Boediono in 2008 when he served as the BI governor was funneled to the party coffers to\
prepare for Yudhoyono�s bid.\
Separately, Democratic Party spokesman Ruhut Sitompul lambasted Nazaruddin, who has been \
sentenced to four years and 10 months in a separate graft case, for accusing his boss Yudhoyono of\
using dirty money to win the 2009 election.\
�What Nazaruddin said about the campaign, Pak Yudhoyono and Ibas is not true. He has a headache\
from being implicated in many graft cases and that is why he aims his gun at other people w\
"