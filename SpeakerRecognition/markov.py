import math
from hashtable import *


HASH_CELLS = 57
TOO_FULL = 0.5
GROWTH_RATIO = 2

class Markov:
    def __init__(self, k, text, use_hashtable):
        """
        Construct a new k-order markov model using the text 'text'.
        """
        self.k = k
        self.text = text
        self.wrapped_text = text + text[:k]   # glue the k characters from front to the end
        self.uniqe_len = len(set(text))
        if use_hashtable:
            self._table = Hashtable(HASH_CELLS, 0, 0.5, 2)
        else:
            self._table = dict()
        for i in range(len(self.text)):
            kstr = self.wrapped_text[i:i+k]
            kstr1 = self.wrapped_text[i:i+k+1]
            for string in [kstr, kstr1]:
                self._table[string] = self._table.get(string, 0) + 1

    def log_probability(self, s):
        """
        Get the log probability of string "s", given the statistics of
        character sequences modeled by this particular Markov model
        This probability is *not* normalized by the length of the string.
        """
        k = self.k
        wrapped = s + s[:k]
        total = 0
        for i in range(len(s)):
            kstr = wrapped[i:i+k]
            kstr1 = wrapped[i:i+k+1]
            total += math.log((self._table.get(kstr1,0)+1) / (self._table.get(kstr,0)+self.uniqe_len))
        return total


def identify_speaker(speech1, speech2, speech3, k, use_hashtable):
    """
    Given sample text from two speakers (1 and 2), and text from an
    unidentified speaker (3), return a tuple with the *normalized* log probabilities
    of each of the speakers uttering that text under a "order" order
    character-based Markov model, and a conclusion of which speaker
    uttered the unidentified text based on the two probabilities.
    """
    speaker1 = Markov(k, speech1, use_hashtable)
    speaker2 = Markov(k, speech2, use_hashtable)
    l = len(speech3)
    prob1 = speaker1.log_probability(speech3) / l
    prob2 = speaker2.log_probability(speech3) / l
    if prob1 > prob2:
        return prob1, prob2, "A"
    return prob1, prob2, "B"


def main(speech1, speech2, speech3, k, use_hashtable):
    return identify_speaker(speech1, speech2, speech3, k, use_hashtable)


if __name__ == "__main__":
    main()