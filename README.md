# prime-sequence
An analysis of a special sequence of primes

Let $P$ be the sequence of increasing prime numbers, and $p$ some prime. This repo considers a sequence of primes $S^P_p(n)$ defined as follows. Suppose that $p$ has representation $p = d_1d_2 \dots d_n$, and define $\text{Rev}(p) := d_n d_{n-1} \dots d_1$. Note that $\text{Rev}(p)$ is not necesserily a member of $P$. The definition of $S^P_p(n)$ is then:

- $S^P_p(0) = p$ 
- $S^P_p(n)$ is the first $x \in P$ such that $x > \text{Rev}(S^P_p(n-1)$. 

For example, for $p = 11$, the sequence is:

$$11, \quad 13, \quad 37, \quad 79, \quad 101, \quad 103, \quad 307, \quad 709, \quad \dots.$$