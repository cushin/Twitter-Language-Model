from pickle import load
from numpy import array
from random import randint
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences


# generate a sequence of characters with a language model
def generate_seq(model, mapping, seq_length, seed_text, n_chars):
	in_text = seed_text
	# generate a fixed number of characters
	for _ in range(n_chars):
		# encode the characters as integers
		encoded = [mapping[char] for char in in_text]
		# truncate sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
		# one hot encode
		encoded = to_categorical(encoded, num_classes=len(mapping))
		# predict character
		yhat = model.predict_classes(encoded, verbose=0)
		# reverse map integer to character
		out_char = ''
		for char, index in mapping.items():
			if index == yhat:
				out_char = char
				break
		# append to input
		in_text += char
	return in_text
    
# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'rb')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

# load the model
model = load_model('model.h5')
# load the mapping
mapping = load(open('mapping.pkl', 'rb'))

in_filename = 'tweets.txt'
doc = load_doc(in_filename)
doc = doc.decode("utf-8")
lines = doc.split('\n')

# select a seed text
seed_text = lines[randint(0,len(lines))]

# test random
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
print(generate_seq(model, mapping, 10, "\n"+seed_text, 140))
seed_text = lines[randint(0,len(lines))]
