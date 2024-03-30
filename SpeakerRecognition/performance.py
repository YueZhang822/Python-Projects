import sys
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from markov import identify_speaker

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            f"Usage: python3 {sys.argv[0]} <filenameA> <filenameB> <filenameC> <max-k> <runs>"
        )
        sys.exit(1)

    # extract parameters from command line & convert types
    filenameA, filenameB, filenameC, max_k, runs = sys.argv[1:]
    max_k = int(max_k)
    runs = int(runs)

    # open files & read text
    fd1 = open(filenameA)
    speech1 = fd1.read()
    fd2 = open(filenameB)
    speech2 = fd2.read()
    fd3 = open(filenameC)
    speech3 = fd3.read()

    # run performance tests
    implementations = ("hashtable", "dict")
    ks = range(1, max_k+1)
    num_runs = range(1, runs+1)
    stats = []
    avg_stats = []
    for implem in implementations:
        for k in ks:
            k_time = 0
            for r in num_runs:
                if implem == "hashtable":
                    start = time.perf_counter()
                    tup = identify_speaker(speech1, speech2, speech3, k, use_hashtable=True)
                    elapsed = time.perf_counter() - start
                else:
                    start = time.perf_counter()
                    tup = identify_speaker(speech1, speech2, speech3, k, use_hashtable=False)
                    elapsed = time.perf_counter() - start
                k_time += elapsed
                stats += [(implem, k, r, elapsed)]
            avg_stats += [(implem, k, k_time/runs)]
    stats_df = pd.DataFrame(stats, columns=["Implementation", "K", "Run", "Time"])
    print(stats_df)
    avg_df = pd.DataFrame(avg_stats, columns=["Implementation", "K", f"Average Time (Runs={runs})"])
    sns.lineplot(data=avg_df, x="K", y=f"Average Time (Runs={runs})", hue="Implementation", linestyle="-", marker="o")
    # write execution_graph.png
    plt.savefig('execution_graph.png')
