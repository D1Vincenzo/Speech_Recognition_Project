from word_embedding_test import *
text = 'go backward'

if find_the_most_similar_command(text):
    print("command received:", find_the_most_similar_command(text)) 
else: 
    print("Command not recognized. Please try again.")