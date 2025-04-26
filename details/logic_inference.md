# Logic Inference

This part is about logic inference.

The logic inference is according to the known facts, rules, or premiss, deriving new conclusions or judgements, by analysis, comparison, hypothesis and verification.

Before staring algorithm, some knowledge bases are needed to know.

# Knowledge Base

## Analysis of Compound Statement
Target: 
- Understand the structure of a statement.
- Learn how to determine whether a statement is True or False based on its structure.

Now, suppose we are given a statement $P$, and we need to determine whether $P$ is True or False.
We approach this by breaking down $P$ into smaller component statements that together form $P$.

Assume we have statements $Q$, $A$ and $B$, where:
- $Q$ may be related to $P$ through negation,
- $A$ and $B$ are components (sub-statements) of $P$.

In order to combine these component statements and analyze their truth values, we use a set of basic operations:

| Operation         | Symbol                                       | Definition                | Truth Condition |
|:------------------|:--------------------------------------------:|:---------------------------|:----------------|
| Negation          | \( P = \neg Q \)                             | NOT \( Q \)                | \( P \) is True if \( Q \) is False; False if \( Q \) is True |
| Conjunction (AND) | \( P = A \land B \)                          | \( A \) AND \( B \)         | \( P \) is True only if both \( A \) and \( B \) are True |
| Disjunction (OR)  | \( P = A \lor B \)                           | \( A \) OR \( B \)          | \( P \) is True if at least one of \( A \) or \( B \) is True |
| Exclusive OR (XOR)| \( P = (A \land \neg B) \lor (\neg A \land B) \) | \( A \) XOR \( B \)         | \( P \) is True if \( A \) and \( B \) have different truth values |
| Biconditional (IFF)| \( P = (A \land B) \lor (\neg A \land \neg B) \) | \( A \) iff \( B \)         | \( P \) is True if \( A \) and \( B \) have the same truth value |
| Implication       | \( P = \neg A \lor B \)                      | If \( A \) then \( B \)     | \( P \) is False only when \( A \) is True and \( B \) is False |

