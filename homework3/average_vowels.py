# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.
# print(ord("a")) #97
# print(ord("e"))
# print(ord())


def counting_vowels_and_consonants(str) : 
    num_vowels = 0
    num_consonants = 0
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    for x in str :
        if x in vowels : 
            num_vowels += 1
        elif x not in vowels and x in consonants : 
            num_consonants += 1 
    return(num_vowels,num_consonants)
print(counting_vowels_and_consonants("hell yea!"))


# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(p) : 
    num_vowels = 0 
    num_consonants = 0 
    num_sentences = 0 

    p == p.lower()

    p = p.replace("!", ".")
    p = p.replace("?", ".")
    sentences = p.split(".")

    for sentence in sentences : 
        if sentence != "" :  
            num_sentences += 1 
            (sentence_vowels,sentence_consonants) = counting_vowels_and_consonants(sentence)
            num_vowels += sentence_vowels
            num_consonants += sentence_consonants

    vowel_avg = num_vowels / num_sentences 
    consonant_avg = num_consonants / num_sentences

    return(num_sentences,vowel_avg,consonant_avg )

        


        


# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
     "Fall in love with some activity, and do it! "
     "Nobody ever figures out what life is all about, and it doesn't matter. "
     "Explore the world. "
     "Nearly everything is really interesting if you go into it deeply enough. "
     "Work as hard and as much as you want to on the things you like to do the best. "
     "Don't think about what you want to be, but what you want to do. "
     "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
 )

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

print(average_vowels_and_consonants(paragraph))

def paragraph_information(p) : 
    num_sentence = 0
    num_vowels = 0
    num_consonants = 0 
    
    p = p.replace("!", ".")
    p = p.replace("?", ".")
    sentences = p.split(".")

    p = p.lower()

    for sentence in sentences : 
            if sentence != "" :   
                num_sentence += 1

                (sentence_vowels,sentence_consonants) = counting_vowels_and_consonants(sentence)

                num_vowels += sentence_vowels 
                num_consonants += sentence_consonants 

    vowel_avg = num_vowels / num_sentence 
    consonants_avg = num_consonants / num_sentence
    print(f"the paragraph has {num_sentence} sentences,")
    print(f"the average vowels per sentence is {vowel_avg}")
    print(f"and the average consonants per sentence is {consonants_avg} ")

paragraph_information(paragraph)

        
        

