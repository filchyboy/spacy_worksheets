# What are statistical models?
# Enable spaCy to predict linguistic attributes in context
# Part-of-speech tags
# Syntactic dependencies
# Named entities
# Trained on labeled example texts
# Can be updated with more examples to fine-tune predictions

# Some of the most interesting things you can analyze are 
# context-specific: for example, whether a word is a verb or 
# whether a span of text is a person name.

# Statistical models enable spaCy to make predictions in context. 
# This usually includes part-of speech tags, syntactic dependencies 
# and named entities.

# Models are trained on large datasets of labeled example texts.

# They can be updated with more examples to fine-tune their 
# predictions – for example, to perform better on your specific data.
########
##### Remember this python command to download and make the model available
##### when running on the command line
########
# $ python -m spacy download en_core_web_sm
########

# import spacy

# nlp = spacy.load('en_core_web_sm')

# Binary weights
# Vocabulary
# Meta information (language, pipeline)

# spaCy provides a number of pre-trained model packages you can 
# download using the "spacy download" command. For example, the 
# "en_core_web_sm" package is a small English model that supports 
# all core capabilities and is trained on web text.

# The spacy dot load method loads a model package by name and returns 
# an nlp object.

# The package provides the binary weights that enable spaCy to make 
# predictions.

# It also includes the vocabulary, and meta information to tell 
# spaCy which language class to use and how to configure the processing 
# pipeline.

import spacy

# Load the small English model
nlp = spacy.load('en_core_web_sm')

# Process a text
doc = nlp("She ate the pizza")

# Iterate over the tokens
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)
    

# Let's take a look at the model's predictions. In this example, 
# we're using spaCy to predict part-of-speech tags, the word types 
# in context.

# First, we load the small English model and receive an nlp object.

# Next, we're processing the text "She ate the pizza".

# For each token in the Doc, we can print the text and the "pos underscore"
# attribute, the predicted part-of-speech tag.

# In spaCy, attributes that return strings usually end with an underscore
# – attributes without the underscore return an ID.

# Here, the model correctly predicted "ate" as a verb and "pizza" 
# as a noun.

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
    
# In addition to the part-of-speech tags, we can also predict how the 
# words are related. For example, whether a word is the subject of the sentence or an object.

# The "dep underscore" attribute returns the predicted dependency label.

# The head attribute returns the syntactic head token. You can also 
# think of it as the parent token this word is attached to.  

# Visualization of the dependency graph for 'She ate the pizza'
# dep_example.png
# Label	Description	Example
# nsubj	nominal subject	She
# dobj	direct object	pizza
# det	determiner (article)	the  

# To describe syntactic dependencies, spaCy uses a standardized label 
# scheme. Here's an example of some common labels:

# The pronoun "She" is a nominal subject attached to the verb – in this 
# case, to "ate".

# The noun "pizza" is a direct object attached to the verb "ate". It is 
# eaten by the subject, "she".

# The determiner "the", also known as an article, is attached to the 
# noun "pizza".

# Process a text
doc = nlp(u"Apple is looking at buying U.K. startup for $1 billion")

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)
    
# Named entities are "real world objects" that are assigned a name – 
# for example, a person, an organization or a country.

# The doc dot ents property lets you access the named entities 
# predicted by the model.

# It returns an iterator of Span objects, so we can print the entity 
# text and the entity label using the "label underscore" attribute.

# In this case, the model is correctly predicting "Apple" as an 
# organization, "U.K." as a geopolitical entity and "$1 billion" as money.

# Tip: the explain method
# Get quick definitions of the most common tags and labels.
spacy.explain('GPE')
spacy.explain('NNP')
spacy.explain('dobj')

# A quick tip: To get definitions for the most common tags and labels, 
# you can use the spacy dot explain helper function.

# For example, "GPE" for geopolitical entity isn't exactly intuitive – 
# but spacy dot explain can tell you that it refers to countries, cities and states.

# The same works for part-of-speech tags and dependency labels.
