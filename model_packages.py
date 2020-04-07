# What’s not included in a model package that you can load into spaCy?

# 1. A meta file including the language, pipeline and license.
# 2. Binary weights to make statistical predictions.
# 3. >>>> The labelled data that the model was trained on. <<<<<<<
# 4. Strings of the model's vocabulary and their hashes.

# That's correct! Statistical models allow you to generalize based 
# on a set of training examples. Once they’re trained, they use 
# binary weights to make predictions. That’s why it’s not necessary 
# to ship them with their training data.