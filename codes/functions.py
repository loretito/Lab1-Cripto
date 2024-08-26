import re 
from collections import Counter
from helpers import expected_frequency, common_connectors

def count_frequency(phrase):
    phrase = phrase.upper()
    frequency = Counter(phrase)
    total_letters = sum(frequency.values())
    
    frec_per = {letter: (counter / total_letters) * 100 for letter, counter in frequency.items() if letter.isalpha()}
    
    return frec_per

def evaluate_consistency(phrase):
    frequency_phrase = count_frequency(phrase)
    deviation = 0
    for letter, percentage in frequency_phrase.items():
        expected = expected_frequency.get(letter, 0)
        deviation += abs(percentage - expected)
    
    avg_deviation = deviation / len(frequency_phrase)
    
    phrase = re.sub(r'[^\w\s]', '', phrase).lower()
    words = set(phrase.split())
    connectors_found = words.intersection(common_connectors)
    percentage_connectors = (len(connectors_found) / len(words)) * 100 if len(words) > 0 else 0
    
    if avg_deviation < 5 and percentage_connectors > 20: 
        return True
    else:
        return False


def cesar(text, shift, cypher=True):
    def shift_char(char, shift):
        if char.isupper():
            base = ord('A')
        elif char.islower():
            base = ord('a')
        elif char.isdigit():
            return str((int(char) + (shift if cypher else -shift)) % 10)
        else:
            return chr(ord(char) + (shift if cypher else -shift))
        return chr((ord(char) - base + (shift if cypher else -shift)) % 26 + base)

    result = ""
    for char in text:
        if char == " ":
            result += " "
        else:
            result += shift_char(char, shift)

    return result


