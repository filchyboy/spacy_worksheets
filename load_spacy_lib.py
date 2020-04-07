# Import the English language class
from spacy.lang.en import English

# Create the nlp object
nlp = English()

# contains the processing pipeline
# includes language-specific rules for tokenization etc.

# At the center of spaCy is the object containing 
# the processing pipeline. We usually call this 
# variable "nlp".

# For example, to create an English nlp object, 
# you can import the English language class from 
# spacy dot lang dot en and instantiate it. You 
# can use the nlp object like a function to analyze text.

# It contains all the different components in the 
# pipeline.

# It also includes language-specific rules used 
# for tokenizing the text into words and punctuation. 
# spaCy supports a variety of languages that 
# are available in spacy dot lang.


# Created by processing a string of text with the nlp object
doc = nlp("Hello world!")

# Iterate over tokens in a Doc
for token in doc:
    print(token.text)

# When you process a text with the nlp object, 
# spaCy creates a Doc object – short for "document". 
# The Doc lets you access information about the 
# text in a structured way, and no information is lost.

# The Doc behaves like a normal Python sequence by the 
# way and lets you iterate over its tokens, or get 
# a token by its index. But more on that later!

# Index into the Doc to get a single Token
token = doc[1]

# Get the token text via the .text attribute
print(token.text)

# Token objects represent the tokens in a document 
# – for example, a word or a punctuation character.

# To get a token at a specific position, you 
# can index into the Doc.

# Token objects also provide various attributes 
# that let you access more information about the 
# tokens. For example, the dot text attribute 
# returns the verbatim token text.

# A slice from the Doc is a Span object
span = doc[1:4]

# Get the span text via the .text attribute
print(span.text)

#  A Span object is a slice of the document 
# consisting of one or more tokens. It's only a 
# view of the Doc and doesn't contain any data itself.

# To create a Span, you can use Python's slice notation. 
# For example, 1 colon 3 will create a slice starting 
# from the token at position 1, up to – but not 
# including! – the token at position 3.

doc = nlp("It costs $5.")

print('Index:   ', [token.i for token in doc])
print('Text:    ', [token.text for token in doc])

print('is_alpha:', [token.is_alpha for token in doc])
print('is_punct:', [token.is_punct for token in doc])
print('like_num:', [token.like_num for token in doc])

# Here you can see some of the available token attributes:

# "i" is the index of the token within the parent document.

# "text" returns the token text.

# "is alpha", "is punct" and "like num" return boolean values 
# indicating whether the token consists of alphabetic characters,
# whether it's punctuation or whether it resembles a number. For 
# example, a token "10" – one, zero – or the word "ten" – T, E, N.

# These attributes are also called lexical attributes: they refer 
# to the entry in the vocabulary and don't depend on the token's context.