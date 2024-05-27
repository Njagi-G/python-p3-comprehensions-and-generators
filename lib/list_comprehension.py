#!/usr/bin/env python3

# Question 1
def return_evens(num_list):
    pass
    evens_list = [n for n in num_list if n % 2 == 0]
    return evens_list

return_evens([0, 1, 3, 5, 7, 8, 9])
print(return_evens([0, 1, 3, 5, 7, 8, 9]))


# Question 2
def make_exclamation(sentence_list):
    pass
    exclaimed_sentences = [n + "!" for n in sentence_list]
    return exclaimed_sentences

make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))