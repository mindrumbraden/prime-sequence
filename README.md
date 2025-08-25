# prime-sequence
An analysis of a special sequence of primes

Let $\mathcal{P}$ be the sequence of increasing prime numbers, and $p$ some prime. This repo considers a sequence of primes $S^{\mathcal{P}}_p(n)$ defined as follows. Suppose that $p$ has representation $p = d_1d_2 \dots d_n$, and define $\bar{p} := d_n d_{n-1} \dots d_1$. Note that $\bar{p}$ is not necesserily a member of $\mathcal{P}$. The definition of $S^{\mathcal{P}}_p(n)$ is then:

- $S^{\mathcal{P}}_p(0) = p$ 
- $S^{\mathcal{P}}_p(n)$ is the first $x \in \mathcal{P}$ such that $x > \bar{S^{\mathcal{P}}_p(n-1)}$. 

For example, for $p = 11$, the first elements of the sequence is:
$$11, \quad 13, \quad 37, \quad 79, \quad 101, \quad 103, \quad 307, \quad 709, \quad \dots.$$