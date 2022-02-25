'''
Author: Ben Alcoe

Function: Unit test calculation file for langcalc.py file code

'''

from langcalc import ari
import string
    
# testing simple string sentence count score
def test_simple_string_sentence_count():
    # establish input string
    s = 'The cat sat on the mat'
    
    # calculation from langcalc.py
    sentence_count = s.count('.')
    if sentence_count == 0:
        sentence_count = 1
    
    # assert expected output
    assert sentence_count == 1
    
# testing punctuation removal
def test_punc_removal():
    s = 'The cat sat, on the mat.'
    
    # calculation from langcalc.py
    s = s.translate(str.maketrans('', '', string.punctuation))
    
    # assert expected output
    assert s == 'The cat sat on the mat'
        
# testing simple string word count score
def test_simple_string_word_count():
    # establish input string
    s = 'The cat sat on the mat'
    
    # calculation from langcalc.py
    word_list = s.split()
    word_count = len(word_list)
    
    # assert expected output
    assert word_count == 6

# test simple string character count score
def test_simple_string_char_count():
    # establish input string
    s = 'The cat sat on the mat'
    
    # calculation from langcalc.py
    word_list = s.split()
    character_count = 0
    for word in word_list:
        character_count += len(word)
        
    # assert expected output 
    character_count == 17 
    
# testing simple string ARI score
def test_simple_string_ari_score():
    # establish input string
    s = 'The cat sat on the mat.'
    
    # calculation from langcalc.py
    ari_score = ari(s)
    
    # assert expected output
    assert ari_score == 1, '5-6'

   
    