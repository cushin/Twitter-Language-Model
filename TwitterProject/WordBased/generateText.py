from random import randint
from pickle import load
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
 
# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'rb')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
 
# generate a sequence from a language model
def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
	result = list()
	in_text = seed_text
	# generate a fixed number of words
	for _ in range(n_words):
		# encode the text as integer
		encoded = tokenizer.texts_to_sequences([in_text])[0]
		# truncate sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
		# predict probabilities for each word
		yhat = model.predict_classes(encoded, verbose=0)
		# map predicted word index to word
		out_word = ''
		for word, index in tokenizer.word_index.items():
			if index == yhat:
				out_word = word
				break
		# append to input
		in_text += ' ' + out_word
		result.append(out_word)
	return ' '.join(result)
 
# load cleaned text sequences
in_filename = 'tweet_sequences.txt'
doc = load_doc(in_filename)
doc = doc.decode("utf-8")
lines = doc.split('\n')
seq_length = len(lines[0].split()) - 1
 
# load the model
model = load_model('model.h5')
 
# load the tokenizer
tokenizer = load(open('tokenizer.pkl', 'rb'))
 
# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n4." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n5." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n6." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n7." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n8." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n9." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n10." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n11." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n12." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n13." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n14." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n15." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n16." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n17." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n18." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n19." +generated)

# select a seed text
seed_text = lines[randint(0,len(lines))]
print(seed_text + '\n')
 
# enerate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print("\n20." +generated)


