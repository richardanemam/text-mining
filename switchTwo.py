#@author: Richard Anemam
#Date: Sep 6, 2018
#Entirely based on Norvig's spell checker
# To a better understanding:
#[0]: https://en.wikipedia.org/wiki/Levenshtein_distance
#[1]: Search for Norvig's spell checker
#[2]: Norvig's spell checker in Haskell by Richard Anemam & Juliane Cunha - Code & Tutorial (https://github.com/richardanemam/paradgmas-de-programa-ao)

#Final considerations: apply sentiment analysis. Check https://github.com/richardanemam/twitter-sentment-analysys-npl out for a better understanding

import re
from collections import Counter
regex = r"[-'a-zA-ZÀ-ÖØ-öø-ÿ]+" 


def itDoesEverything(word):
    word = word.split()
    newWords = []
    for w in word:
        newWords.append(correction(w))
    corrected = ' '.join(newWords)
    return corrected

def words(text): 
    return re.findall(regex, text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


if __name__ == '__main__':
    # Testes
    while True:

        word = input("\nType your sentence: ")
        print (itDoesEverything(word))