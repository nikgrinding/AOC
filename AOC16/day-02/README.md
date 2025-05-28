## Part 1

You’re given a sequence of instructions to move around a keypad using the directions `U`, `D`, `L`, and `R`. Each line of instructions leads you to one digit of the bathroom code. The keypad looks like this:
```
1 2 3
4 5 6
7 8 9
```

You start at `5`, and for each move, you ignore instructions that would take you off the keypad. At the end of each line, record the button you’re on as part of the code.

**Example:**
```
ULL
RRDDD
LURDL
UUUUD
```
→ `1985`

### Idea

Start at the center of a 3x3 grid. For each character in the instruction, move if the direction is valid. At the end of each line, append the current button to the password.

## Part 2

The keypad is now shaped like this:

```
1
2 3 4
5 6 7 8 9
A B C
D
```

You still start at `5` and follow the same movement rules, except now you must check for invalid positions in a non-rectangular grid. If a move would take you to a non-button (represented as 0 in your code), you ignore it.

**Example:**
```
ULL
RRDDD
LURDL
UUUUD
```
→ `5DB3`

### Idea

Represent the keypad as a 5x5 grid where invalid positions are marked as `0`. Use bounds and value checks to ensure you only move to valid keys. At the end of each line, append the current button to the password.