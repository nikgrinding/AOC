## Part 1

Given a list of replacement rules and a starting molecule, count how many unique molecules can be formed by applying **one replacement** anywhere in the molecule

**Examples:**
Input:
```
H => HO
H => OH
O => HH
```
Molecule: `HOH`

Output:
```
4
```

### Idea
Store the replacements in a dictionary mapping each LHS to possible RHS strings
For each match of a LHS in the input molecule, replace it with each RHS and collect the resulting molecules in a set

## Part 2

Given the final medicine molecule, compute the **minimum number of steps** needed to construct it starting from `'e'` using the available replacements

**Examples:**
Input:
```
e => H
e => O
H => HO
H => OH
O => HH
```
Molecule: `HOH`
Output:
```
3
```

### Idea
- Reverse the replacement rules and randomly apply them until we reach `'e'`
- If stuck, shuffle the rules and try again