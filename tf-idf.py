import string
import argparse
import math

def load_stop_words(filename):
  if (filename is not None):
    return set(line.strip() for line in open(filename))
  else:
    return None

parser = argparse.ArgumentParser(description='TF-IDF')
parser.add_argument('-l', '--language', action="store", dest='language_file', default=None)
parser.add_argument('-n', '--number', action="store", dest='n', default=3, type=int)
parser.add_argument('-f', '--files', action="store", dest='files', type=argparse.FileType('r'), nargs='+')

ARGS = parser.parse_args()
STOP_WORDS = load_stop_words(ARGS.language_file)
FILE_LIST = []

def split_file(file):
  return [word.lower().strip(string.punctuation) for line in file for word in line.split() if validate_word(word.lower())]
    
def validate_word(word):
  if (STOP_WORDS is not None):
    return (word not in string.punctuation and word.strip(string.punctuation) not in STOP_WORDS)
  else:
    return word not in string.punctuation
  
def tf(word, word_list):
  return word_list.count(word) / len(word_list)

def idf(word, file_list):
  number_of_document_with_word = 0
  for file in file_list:
    if word in file:
      number_of_document_with_word = number_of_document_with_word+ 1
  if number_of_document_with_word > 0:
    return 1 + math.log(len(file_list) / number_of_document_with_word)
  return 1.0

def tfidf(word, word_list, file_list):
  return tf(word, word_list) * idf(word, file_list)

for file in ARGS.files:
  FILE_LIST.append(split_file(file))

for i, word_list in enumerate(FILE_LIST):
  print("Top {} words in document {}".format(ARGS.n, i + 1))
  scores = { word: tfidf(word, word_list, FILE_LIST) for word in word_list }
  sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
  for word, score in sorted_words[:ARGS.n]:
    print("\tWord: {}, score: {}".format(word, round(score, 5)))