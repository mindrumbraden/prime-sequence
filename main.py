#%%

import pandas as pd
from bisect import bisect_right, bisect_left
import matplotlib.pyplot as plt
import numpy as np

#%%

primes = pd.read_csv("output.csv")
primes = list(primes["Num"])

#%%

def get_next_prime(prime: str, list_p: list):
    prime = prime[::-1]
    prime = int(prime)
    idx = bisect_right(list_p, prime)
    return list_p[idx]

def gen_list(length: int, start_prime: int, list_p: list):
    seen_primes = set()
    output = [start_prime]
    prime = str(start_prime)
    for i in range(length-1):
        next_prime = get_next_prime(prime, list_p)
        output.append(next_prime)
        prime = str(next_prime)
        if prime in seen_primes:
            return output
        seen_primes.add(prime)
    return output

def gen_list_of_start_primes(n1: int, n2: int, list_p: list):
    idx1 = bisect_left(list_p, n1)
    idx2 = bisect_right(list_p, n2)
    return list_p[idx1:idx2]  

def get_df_of_sequences(n1: int, n2: int, max_l: int, list_p: list):
    start_primes = gen_list_of_start_primes(n1, n2, list_p)
    df = pd.DataFrame(0, index=[i for i in range(max_l)],
                      columns=start_primes)
    for prime in start_primes:
        seq = np.array(gen_list(max_l, prime, list_p))
        if len(seq) < max_l:
            seq = np.pad(seq, (0, max_l-len(seq)), "constant", 
                         constant_values=0)
        df[prime] = seq
    return df #df.replace(0, pd.NA)
        
        
#%%

df = get_df_of_sequences(10, 100, 30, primes)
df.plot()
