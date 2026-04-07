# Authors
Gabriel Schreiber (UFID: 76976820) & Tanner Holland (UFID: 21167710)

# Instructions
To run this program, complete the following steps:
- Open terminal to the Highest-Value-Longest-Common-Sequence directory
- Run the program using this terminal command:

      python main.py test/example.in test/output.out

- This will run the highest value computation, backtracking algorithm, and the verifier.
- The results will be written into data/output.out
- The matchings listed in example.out correspond to example.in

# Assumptions
Refer to the example input and output files (`data/example.in` and `data/example.out`) for formatting of input data and output matches.

After running the command above, `output.out` will be the output matchings for `example.in` or any other input file provided. 

The python terminal line requires at least an input file path to be specified to run. The output path is optional.

# Question 1: Empirical Comparison

Use at least 10 nontrivial input files (i.e., contain strings of length at least 25). Graph the runtime of the 10 files.

<img width="597" height="370" alt="Algos - Programming Assignment 3" src="https://github.com/user-attachments/assets/7282928a-5bce-4b63-a49b-273d6a6a4615" />

# Question 2: Recurrence Equation

Give a recurrence that is the basis of a dynamic programming algorithm to compute the HVLCS of strings A and B. You must provide the appropriate base cases, and explain why your recurrence is correct.

$$
\text{OPT}(i,j) = \begin{cases} 
0 \text{,} & i = 0 \text{ or } j = 0 \\
\max(\text{OPT}(i-1,j) \text{, OPT}(i,j-1)) \text{,} & A_i \ne B_j \\
\max(v[A_i \text{ or } B_j] + \text{OPT}(i-1,j-1) \text{, OPT}(i-1,j), \text{, OPT}(i,j-1)) \text{,} & A_i = B_j
\end{cases}
$$

Base Case: `i = 0` or `j = 0`

Starting from the beginning of both strings, if either string is empty, the only possible common subsequence is the empty string. Therefore, the highest value is 0.

Case 2: `A[i]` != `B[j]`

When i and j are both characters in the strings A and B but they are not the same, we must skip either `A[i]` or `B[j]` and continue. Therefore, the highest value is the maximum of the two options.

Case 3: `A[i]` == `B[j]`

When i and j are both characters in the strings A and B and they are the same, the highest value is the maximum between skipping the character in either string (previous case), or adding the value of the current character plus the previous highest value substring without `A[i]` or `B[j]`.

The recurrence is correct because at every step, we take the best possible outcome from every decision possible.

If `A[i] == B[j]`, there are three options available:

- Skip `A[i]`
- Skip `B[j]`
- Or match `A[i]` and `B[j]` and add the value to whatever was the previous highest value substring before `A[i]` and `B[j]`.

If `A[i] != B[j]`, there are only two options available:

- Skip `A[i]`
- Or skip `B[j]`

We try both options and take whichever gives a better result.

# Question 3: Big-Oh

Pseudocode:
def highestVal(A, B, alphabet):
      for i = 0 to len(A):
                  m[i] = [0 for j in len(B)]

      for i in range(len(m)):
            for j in range(len(m(i)):
                  if i == 0 or j == 0 -> m[i][j] = 0
                  else if A[i] != B[j]:
                        m[i][j] = max(m[i-1][j], m[i][j-1])
                  else if A[i] == B[j]:
                        m[i][j] = max(
                              v(A(i)) + m[i-1][j-1],
                              m[i-1][j],
                              m[i][j-1])
      return m[len(A)][len(B)]

The Big-Oh runtime of the algorithm is is O(nm) where n is the length of A and m is the length of B.
                              
                  
