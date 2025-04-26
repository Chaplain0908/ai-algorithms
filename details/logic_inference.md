# Logic Inference

This section focuses on logic inference.

Logic inference refers to the process of deriving new conclusions or judgments based on known facts, rules, or premises, through analysis, comparison, hypothesis, and verification.

Before diving into the algorithms, it is important to understand some essential background knowledge.

# Logic Inference Subsections

- [Logic Inference](#logic-inference)
- [Logic Inference Subsections](#logic-inference-subsections)
- [Knowledge Background](#knowledge-background)
  - [Analysis of Compound Statement](#analysis-of-compound-statement)
    - [Target:](#target)
    - [Statement Operations](#statement-operations)
    - [Other Statements](#other-statements)
  - [Conditional](#conditional)
    - [Target](#target-1)
    - [Implication](#implication)
    - [bi-conditional](#bi-conditional)
  - [Inference Rules](#inference-rules)
    - [Inference](#inference)
    - [Modus Ponens](#modus-ponens)
    - [Contrapositive (Modus Tollens)](#contrapositive-modus-tollens)
    - [Rules of Inference](#rules-of-inference)
    - [First-Order Logic](#first-order-logic)
      - [Relationship between Universal and Existential Quantifiers](#relationship-between-universal-and-existential-quantifiers)
  - [Proof Techniques](#proof-techniques)
    - [Logical Equivalence](#logical-equivalence)
    - [Direct Proof](#direct-proof)
    - [Proof by Contrapositive](#proof-by-contrapositive)
    - [Proof by Contradiction](#proof-by-contradiction)
    - [Proof by Example](#proof-by-example)
    - [Proof by Induction](#proof-by-induction)
    - [Strong Induction](#strong-induction)
    - [Proof by Minimal Counterexample](#proof-by-minimal-counterexample)
- [Problems](#problems)
  - [kb-wumpus](#kb-wumpus)
  - [kb-rules](#kb-rules)
- [Algorithm](#algorithm)
  - [DPLL-SAT](#dpll-sat)
  - [Resolution Proof](#resolution-proof)
- [Results](#results)
  - [DPLL](#dpll)
    - [kb\_wumpus](#kb_wumpus)
    - [kb\_rules](#kb_rules)
  - [Resolution](#resolution)

# Knowledge Background

## Analysis of Compound Statement
### Target: 
- Understand the structure of a statement.
- Learn how to determine whether a statement is True or False based on its structure.

Now, suppose we are given a statement$P$, and we need to determine whether$P$is True or False.
We approach this by breaking down$P$into smaller component statements that together form$P$.

Assume we have statements$Q$,$A$and$B$, where:
-$Q$may be related to$P$through negation,
-$A$and$B$are components (sub-statements) of$P$.

### Statement Operations
In order to combine these component statements and analyze their truth values, we use a set of basic operations:

| Operation         | Symbol                                         | Definition       | Truth Condition                                       |
|:------------------|:----------------------------------------------:|:-----------------|:------------------------------------------------------|
| Negation          |$P = \neg Q$                                  | NOT $Q$          | $P$is True if $Q$ is False; False if $Q$ is True      |
| Conjunction (AND) |$P = A \land B$                               | $A$ AND $B$      | $P$is True only if both $A$ and $B$ are True          |
| Disjunction (OR)  |$P = A \lor B$                                | $A$ OR $B$       | $P$is True if at least one of $A$ or $B$ is True      |
| Exclusive OR (XOR)|$P = (A \land \neg B) \lor (\neg A \land B)$  | $A$ XOR $B$      | $P$is True if $A$ and $B$ have different truth values |
| Biconditional (IFF)|$P = (A \land B) \lor (\neg A \land \neg B)$ | $A$ iff $B$      | $P$is True if $A$ and $B$ have the same truth value   |
| Implication       |$P = \neg A \lor B$                           | If $A$ then $B$  | $P$is False only when $A$ is True and $B$ is False    |

### Other Statements
And we also have some interesting statements:
- Tautologies: Are true for any truth value of their sub-statements.
  - Symbol: $A \lor \neg A$
- Unsatisfiable: Are true for any truth value of their sub-statements.
  - Symbol: $A \land \neg A$

## Conditional

### Target 
- Understand and use the structure of *if-then* statements (Implications).

### Implication
Now, suppose we have a statement $P$ and its sub-statements $A$ and $B$ .  
The implication operator is expressed as:   
$$P = A \implies B$$

which means that if the Hypothesis $A$ is true, then the Conclusion $B$ must also be true.
To prove that $A \implies B$ is true, we often use *Tautologies* by constructing the contrapositive:   

$$A \implies B \Leftrightarrow \neg B \implies \neg A$$

### bi-conditional
The implication $A \implies B$ is a **one-way** condition.  
There also exists a **bi-conditional** relationship, expressed as:
$$A \Leftrightarrow B$$
which means **"A if and only if B"**.
Similarly, we can use *Tautologies* to prove the truth of a bi-conditional:   
$$(A \Leftrightarrow B) \Leftrightarrow (B \implies A) \land (B \implies \neg A)$$
and equivalently:
$$(A \Leftrightarrow B) \Leftrightarrow (B \implies A) \land (A \implies B)$$

## Inference Rules
### Inference

Given a knowledge set and an initial premise, we assume them to be True.  
Based on these, we can infer the truth value of related statements by applying valid inference rules.

### Modus Ponens

**Initial Premise:**  
- $( P \implies Q )$i s True.  
- $( P )$ is True.  

**Conclusion:**  
- $Q$ must be True.

It can be expressed using a *Tautology*:
$$[(P \implies Q) \land P] \implies Q$$

### Contrapositive (Modus Tollens)

**Initial Premise:**  
- $( P \implies Q )$ is True.  
- $( \neg Q )$ is True.

**Conclusion:**  
- $( \neg P )$ must be True.

It can be expressed using a *Tautology*:
$$[(P \implies Q) \land \neg Q] \implies \neg P$$

### Rules of Inference

Given a collection of Premises, the Conclusion must logically follow.

Here are some commonly used rules:

| Rule Name | Logical Form                                           | Explanation                                                                                  |
|:----------|:-------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| Conjunction Simplification | $(P \land Q) \implies P$                               | If $( P \land Q )$ is True, then $P$ is True.                                                |
| Disjunctive Syllogism | $(P \lor Q) \land \neg Q \implies P$                   | If $( P \lor Q )$ is True and $( Q )$ is False, then $P$ must be True.                       |
| Bi-conditional Inference | $(P \Leftrightarrow Q) \land Q \implies P$             | If $( P )$ and $( Q )$ are logically equivalent, and $( Q )$ is True, then $P$ must be True. |
| Resolution Inference Rule | $(P \lor Q) \land (\neg P \lor R) \implies (Q \lor R)$ | Combines two clauses to eliminate $( P )$ and infer $( Q \lor R)$ .                          |

### First-Order Logic

First-Order Logic extends Propositional Logic by allowing statements about objects in a domain.

We introduce two important types of quantification:

- **Universal Quantification**:
  The statement "for all $x$ in the domain,$P(x)$ holds" is written as:
 $$\forall x : P(x)$$

- **Existential Quantification**:
  The statement "there exists an $x$ in the domain such that $P(x)$ holds" is written as:
 $$\exists x : P(x)$$

#### Relationship between Universal and Existential Quantifiers

Universal and existential quantifiers are duals under negation:

$$\neg [\forall x : P(x)] \Leftrightarrow \exists x : \neg P(x)$$
$$\neg [\exists x : P(x)] \Leftrightarrow \forall x : \neg P(x)$$

This means:
- If a statement is not true for all objects, then there exists an object for which it is false.
- If there does not exist any object satisfying a statement, then it must be false for all objects.

## Proof Techniques

### Logical Equivalence

When dealing with a compound statement $P$ , it is often helpful to simplify or expand it into a logically equivalent form.

For example:
$$P = (A \lor \neg B) \land (\neg A \lor B) \land A$$  

Through logical equivalences, we can simplify it step-by-step: 
$$P = A \land B$$

Simplifying a statement can make it much easier to verify or prove its truth.

### Direct Proof
In direct proof, we assume the known facts and proceed by a sequence of logical deductions to arrive at the desired conclusion.

Example:  
If a number $n$ is even, then $n = 2k$ for some integer $k$ .  
Thus:
$$n^2 = (2k)^2 = 4k^2 = 2(2k^2)$$

Since $2k^2$ is an integer, $n^2$ is also even.

### Proof by Contrapositive

Rather than proving $A \implies B$ directly, we can prove its contrapositive:

$$\neg B \implies \neg A$$

Since an implication and its contrapositive are logically equivalent, proving one proves the other.

Example:  
To prove "if $n^2$ is odd, then $n$ is odd",  
we instead prove "if $n$ is even, then $n^2$ is even".

### Proof by Contradiction

In proof by contradiction, we assume that the negation of the statement we want to prove is true, and then show that this assumption leads to a logical contradiction.

Example:  
Suppose $n$ is odd, but $n^2$ is even.  
Then:
$$n = 2a + 1$$

thus:
$$n^2 = (2a+1)^2 = 4a^2 + 4a + 1 = 2(2a^2 + 2a) + 1$$

This expression is odd, not even — contradiction!

Thus, the original statement must be true:  
> If $n$ is odd, then $n^2$ is odd.

### Proof by Example

When the claim is existential (i.e., of the form $\exists x : P(x)$ ), we can prove it by finding a specific example that satisfies $P(x)$ .

Example:  
The statement "there exists a positive integer $n$ such that $n^2 - n + 41$ is not prime" can be proved by taking $n = 41$ :

$$n^2 - n + 41 = 41^2 - 41 + 41 = 41^2$$

which is clearly not prime.
Thus, the existential claim is proved.

### Proof by Induction

Proof by induction is used to prove statements for all natural numbers.

**Basic structure:**
1. Prove the **base case(s)** $P(0)$ , $P(1)$ , ..., $P(k-1)$ .
2. Prove the **inductive step**:  
   Assume $P(n-1), P(n-2), \dots, P(n-k)$ are true, and show that $P(n)$ must also be true.

Formal representation:

$$\left[ (P(0) \land \dots \land P(k-1)) \land \left( \forall n \geq k : (P(n-k) \land \dots \land P(n-1)) \implies P(n) \right) \right] \implies (\forall n \geq 0 : P(n))$$

Example:  
Proving bounds for Fibonacci numbers using double-step induction.

### Strong Induction

In **strong induction**, when proving $P(n)$ , we assume $P(m)$ holds for **all** $m < n$ , not just the immediate predecessors.

This method is necessary when $P(n)$ depends on multiple prior cases in a nontrivial way.

Formal structure:

$$[P(0) \land (\forall n \geq 1 : (P(0) \land P(1) \land \dots \land P(n-1)) \implies P(n))] \implies (\forall n \geq 0 : P(n))$$

### Proof by Minimal Counterexample

To prove that a property $P(n)$ holds for all $n \geq 2$ , assume the contrary:  
Suppose there exists a smallest counterexample $n'$ .

- If $n'$ is prime, then the property holds trivially.
- If $n'$ is composite, say $n' = a \times b$ , where $a, b < n'$ ,  
  then by minimality of $n'$ , $P(a)$ and $P(b)$ must be true.  
  This leads to $P(n')$ also being true, contradicting $n'$ being a counterexample.

Thus, no counterexample exists, and the property holds universally.

# Problems
## kb-wumpus

- Definition:  
  - Construct a set of CNF(Conjunctive Normal Form) clauses representing the logic of a simple 4×4 Wumpus World.  
  - The world contains pits, a Wumpus, breezes, stenches, and gold. Logical rules encode the relationships between the presence of pits/Wumpus and the observed breezes/stenches.

- Target:  
  Use propositional logic to model the knowledge about the environment, allowing logical inference to determine possible locations of hazards (pits, Wumpus) or goals (gold) based on partial observations.

- Evaluation:  
  A valid knowledge base should correctly represent the following:
  - If a Wumpus is in a square, then its adjacent squares must have stenches.
  - If a pit is in a square, then its adjacent squares must have breezes.
  - Observed stenches and breezes imply possible adjacent hazards.
  - A square cannot simultaneously contain both a pit and a Wumpus.
  - Observations about the environment must be included as facts.

- Required Inference:  
  - From observed breezes or stenches, infer the possible presence or absence of pits or Wumpus in nearby cells.
  - Use resolution or DPLL algorithms to deduce safe squares or hazard locations based on the CNF clauses.

## kb-rules

- Definition:  
  Build a simple propositional logic knowledge base by using CNF clauses, to represent logical relationships among variables (A, B, C, D, E).

- Target:  
  Encode implications and disjunctions between variables, allowing inference chains to propagate through multiple logical steps.

- Evaluation:  
  A valid knowledge base should satisfy the following:
  - If $A$ is true, then $B$ must be true.
  - If $B$ is true, then $C$ must be true.
  - $A \lor D$ means at least one of $A$ or $D$ must be true.
  - If $C$ is true, then $D$ must be false.
  - If $D$ is true, then $E$ must be true.
  - $E$ must be false.

- Required Inference:  
  - From the given clauses, infer the truth value of each variable.
  - Resolve chains of implications to deduce contradictions or validate conclusions.
  - Identify which assignments satisfy or falsify the overall knowledge base.

# Algorithm
## DPLL-SAT
- Propose:  
  - Solve the SAT (Satisfiability) problem for a given CNF formula.  
  - Determine whether the formula is satisfiable, and if so, find a satisfying assignment.

- Input & Output:
  - **Input:**
    - `clauses`: A list of lists, representing the CNF formula. Each sublist is a clause composed of literals.
    - `assignment` : A dictionary mapping variables to their assigned boolean values.
  - **Output:**
    - If satisfiable: Return the assignment dictionary that satisfies all clauses.
    - If unsatisfiable: Return `None`.

- Idea:
  - The DPLL algorithm improves on basic backtracking search by introducing:
    - **Unit Propagation**: Assign variables that must take a certain value because they appear in unit clauses (If$A$appear in unite clause, it is True).
    - **Pure Literal Elimination**: Assign variables that always appear with the same polarity ($A$but not$\neg A$in CNF).
    - **Variable Selection**: Choose an unassigned variable and recursively attempt assignments.

- Algorithm Step :
    ```
    def DPLL(clauses, assignment):
        clauses, assignment = unit_propagate(clauses, assignment)
        if clauses is None:
            return None

        clauses, assignment = pure_literal_assign(clauses, assignment)

        if clauses is empty:
            return assignment

        if any clause is empty:
            return None

        literal = choose_literal(clauses, assignment)
        if literal is None:
            return assignment

        var = variable of literal

        for value in [True, False]:
            new_assignment = copy(assignment)
            new_assignment[var] = value
            new_clauses = deepcopy(clauses)

            result = DPLL(new_clauses, new_assignment)
            if result is not None:
                return result

        return None
    ```

## Resolution Proof
- Propose:  
  - Perform theorem proving in propositional logic using the Resolution method.  
  - Check whether a given query can be logically inferred from a set of premises.

- Input & Output:
  - **Input:**
    - `clauses`: A list of clauses (lists of literals) representing the premises.
    - `query`: A literal representing the statement we want to prove.
  - **Output:**
    - Return `True` if the query can be derived (i.e., the negation of the query leads to a contradiction).
    - Return `False` if the query cannot be derived.

- Idea:
  - Add the negation of the query to the set of clauses (proof by contradiction).
  - Iteratively apply the resolution rule:
    - Select pairs of clauses that contain complementary literals.
    - Resolve them to produce new clauses.
  - If an empty clause (contradiction) is derived, the query is proved.
  - If no new information can be generated, the query cannot be proved.

- Algorithm Step (Pseudocode):
    ```
    def PL_Resolution(clauses, query):
        negate_query = negate_literal(query)
        clauses.append([negate_query])

        new_clauses = []

        loop:
            for each pair (ci, cj) in clauses:
                resolvents = resolve(ci, cj)

                for clause in resolvents:
                    if clause is empty:
                        return True
                    if clause not in clauses and not in new_clauses:
                        new_clauses.append(clause)

            if new_clauses is empty:
                return False

            clauses.extend(new_clauses)
            new_clauses.clear()
    ```
  
# Results
## DPLL
### kb_wumpus
Given
```
# Stench rules: If there's a Wumpus in (x, y), then stench in adjacent squares
# W23 → S13 ∧ S22 ∧ S24 ∧ S33 == ['¬W23', 'S13'], ['¬W23', 'S22'], ...
clauses += [['¬W23', 'S13'], ['¬W23', 'S22'], ['¬W23', 'S24'], ['¬W23', 'S33']]

# Breeze rules: If there's a pit, then breeze around
clauses += [['¬P12', 'B11'], ['¬P12', 'B22'], ['¬P12', 'B13']]

# If there is stench in (1,2), then Wumpus must be in one of its neighbors
clauses += [['¬S12', 'W11', 'W22', 'W13']]

# If breeze in (2,2), then pit must be in one of neighbors
clauses += [['¬B22', 'P12', 'P21', 'P32', 'P23']]

# One square can't have both pit and Wumpus
clauses += [['¬P22', '¬W22']]

# Add some facts (observations)
clauses += [['S12'], ['B22'], ['¬B11']]  # Observed true/false
```
Result
<td><img src="https://github.com/Chaplain0908/ai-algorithms/raw/main/details/visualize_result/logic_inference/dpll_kb_wumpus.png" alt="dpll_kb_wumpus" style="width:100%"></td>

### kb_rules
Given
```
kb_rules:
        ['¬A', 'B'],  # A → B
        ['¬B', 'C'],  # B → C
        ['A', 'D'],  # A ∨ D
        ['¬C', '¬D'],  # C → ¬D
        ['¬D', 'E'],  # D → E
        ['¬E']  # E must be false
```
Result
<td><img src="https://github.com/Chaplain0908/ai-algorithms/raw/main/details/visualize_result/logic_inference/dpll_kb_rules.png" alt="dpll_kb_rules" style="width:100%"></td>

## Resolution
```
Resolution Result
-----------------
Knowledge Base: [['¬A', 'B'], ['¬B', 'C'], ['A', 'D'], ['¬C', '¬D'], ['¬D', 'E'], ['¬E']]
Query: C
The knowledge base entails 'C' (Provable)
```











