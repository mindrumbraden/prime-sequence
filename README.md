# prime-sequence
An analysis of a special sequence of primes

## Definition
Let $P$ be the sequence of increasing prime numbers, and $p$ some prime. This repo considers a sequence of primes $S^P_p(n)$ defined as follows. Suppose that $p$ has representation $p = d_1d_2 \dots d_n$, and define $\text{Rev}(p) := d_n d_{n-1} \dots d_1$. Note that $\text{Rev}(p)$ is not necesserily a member of $P$. The definition of $S^P_p(n)$ is then:

- $S^P_p(0) = p$ 
- $S^P_p(n)$ is the first $x \in P$ such that $x > \text{Rev}(S^P_p(n-1))$. 

For example, for $p = 11$, the sequence $S^P_{11}(n)$ is:

$$11, \quad 13, \quad 37, \quad 79, \quad 101, \quad 103, \quad 307, \quad 709, \quad \dots.$$

The definition of this sequence depends upon $P$ and $p$, and further sequences could be analyzed by modifying the sequence $P$. For example, if $P = Q$ were the square numbers then we have

$$S^Q_{9} = 9, \quad 16, \quad 64, \quad 49, \quad 100, \quad 4, \quad 9, \quad \dots.$$

The Repo could be easily modified to allow for such a modification. Moreover, the sequence $P$ need not be increasing. However, in its current state, the Repo requires that the sequence be increasing to utilize bisection searches. 

We shall only consider $P$ as the increasing sequence of prime numbers for now. 

## The Repo
For now, this Repo producing a pandas dataframe according to 4 variables: $n_1$, $n_2$, $m$, and $P$. Let

$$R = \{x \in P : n_1 \leq x \leq n_2 \} = \{p_1, p_2, \dots p_{|R|}\}.$$

Then the dataframe is $m \times |R|$ where column $i$ shows the first $m$ elements of $S^P_{p_i}(n)$. Once, however, a repeated element is found, the subsequent entries are filled with a $0$.

## Questions/Ideas/Commentaries
- Rigorously prove that every sequence ends in a cycle. Characterize the lengths of cycles.
- Characterize the lengths of the sequences before they enter into a cycle.
- It seems that these sequences are rather self-contained based upon the number of digits of prime $p$. That is, if $p$ has $d$ digits, then every element of $S^P_p(n)$ also has $d$ digits. This is not universally true, but it becomes increasingly likely as $d$ increasing. 
- For which sets $P$ can $S^P_p(n)$ be unbounded?