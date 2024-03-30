import sys
from markov import identify_speaker

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            f"Usage: python3 {sys.argv[0]} <filenameA> <filenameB> <filenameC> <k> <hashtable-or-dict>"
        )
        sys.exit(1)

    # extract parameters from command line & convert types
    filenameA, filenameB, filenameC, k, hashtable_or_dict = sys.argv[1:]
    k = int(k)
    if hashtable_or_dict not in ("hashtable", "dict"):
        print("Final parameter must either be 'hashtable' or 'dict'")
        sys.exit(1)

    # open files & read text
    fd1 = open(filenameA)
    text1 = fd1.read()
    fd2 = open(filenameB)
    text2 = fd2.read()
    fd3 = open(filenameC)
    text3 = fd3.read()

    # call identify_speaker & print results
    prob1, prob2, winner = identify_speaker(text1, text2, text3, k, hashtable_or_dict=="hashtable")
    print(f"Speaker A: {prob1}\nSpeaker B: {prob2}\n")
    # Conclusion: Speaker X is most likely
    print(f"Conclusion: Speaker {winner} is most likely")