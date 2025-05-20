## Part 1

Santa is bringing his list of string literals as a **digital file** this year, and he needs to know how much space they will take up when stored on his sleigh’s computer.

Each line in the file contains a **string literal**, represented the way it would appear in source code — with **escape sequences** like:

- `\"` — escaped double quote  
- `\\` — escaped backslash  
- `\x??` — hexadecimal escape sequence (e.g., `\x27` for a `'`)

Your task is to calculate:

The total number of **characters of code** for all string literals ***MINUS***   The total number of **characters in memory** once those escape sequences are parsed.

**Example**

Input:
```
""
"abc"
"aaa\"aaa"
"\x27"
```
Output: 12 

{Total code chars: 2 + 5 + 10 + 6 = 23, Total memory chars: 0 + 3 + 7 + 1 = 11, Answer: 23 - 11 = `12`}

### Idea

We only care about the **extra characters in the code** that don’t appear in memory.

- Iterate over each character in the input string
- For each:
  - `"` → contributes 1 extra character (only part of code, not memory)
  - `\\` or `\"` → represents a single character in memory, but takes 2 in code ⇒ 1 extra character
  - `\xHH` → hex escape takes 4 characters in code but becomes 1 in memory ⇒ 3 extra characters
- Accumulate these extra characters to get the final difference between code and memory

## Part 2

Now that Santa has stored his string literals efficiently in memory, it's time to **re-encode** them to be saved safely for transmission — with **extra escaping**.

Each original string literal will be **encoded into a new representation**, and your task is to calculate:

The total number of characters in the **newly encoded representation**  ***MINUS*** The number of characters in the **original code representation**

**Example**

Input:
```
""
"abc"
"aaa\"aaa"
"\x27"
```
Output: 19 
{Total code chars: 2 + 5 + 10 + 6 = 23, Total encoded chars: 6 + 9 + 16 + 11 = 42, Answer: 42 - 23 = `19`}

### Idea

We have to encode each string. So, for each line:

1. Start with `+2` (for new surrounding quotes)
2. For each character:
   - If it's `"` or `\`, add `+1` (because it will be escaped)
3. Sum this over all lines