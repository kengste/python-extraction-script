import json
import biggers
import bag_of_words

sampleText = ""

def main():
  getKeySentences(sampleText, 'general')

def getKeySentences(text, concept):
	try:
		l=bag_of_words.big_bag()
		tokenized = biggers.tokenization(text)
		sentence = biggers.getKeySentences({ concept: l[concept] }, tokenized)
		print(sentence)
	except Exception as e:
		return e

if  __name__ =='__main__':main()