from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import numpy as np

'''
def vectorize_command(command, model):
    return np.mean([model.wv[word] for word in simple_preprocess(command)], axis=0)
'''
# Ignore the non-existing word
def vectorize_command(command, model):
    vectorized_words = [model.wv[word] for word in simple_preprocess(command) if word in model.wv]
    if vectorized_words:
        return np.mean(vectorized_words, axis=0)
    else:
        return None

# Give commands
def get_user_command():
    return input("Please give a command: ")

def find_the_most_similar_command(new_command):
    # Load the model from the file
    model = Word2Vec.load("word2vec_model")

    known_commands = ["move forward", "left", "pick", "stop", 
                    "right", "backward", "go straight"]

    known_command_vectors = [vectorize_command(command, model) for command in known_commands]


    new_command_vector = vectorize_command(new_command, model)

    # Calculate cosine similarities
    similarities = [np.dot(new_command_vector, vec)/(np.linalg.norm(new_command_vector)* np.linalg.norm(vec)) for vec in known_command_vectors]

    # Find the most similar command
    most_similar_command = known_commands[np.argmax(similarities)]
    print("Most similar command is:", most_similar_command)
