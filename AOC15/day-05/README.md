## Part 1

Santa needs help figuring out which strings in his text file are **naughty** or **nice**.

A **nice string** must satisfy **all** of the following conditions:

1. **It contains at least three vowels** (`a`, `e`, `i`, `o`, `u`).
   - Examples: `aei`, `xazegov`, `aeiouaeiouaeiou`

2. **It contains at least one letter that appears twice in a row.**
   - Examples: `xx`, `abcdde` (contains `dd`), `aabbccdd` (contains `aa`, `bb`, `cc`, `dd`)

3. **It does not contain the substrings** `ab`, `cd`, `pq`, or `xy`.

**Examples:**

- `ugknbfddgicrmopn` is **nice**:
  - Vowels: `u, i, o` → rule-1 satisfied
  - Double letter: `dd` → rule-2 satisfied
  - Forbidden substrings: none → rule-3 satisfied

- `aaa` is **nice**:
  - Vowels: 3 x `a` → rule-1 satisfied
  - Double letter: `aa` → rule-2 satisfied
  - Forbidden substrings: none → rule-3 satisfied

- `jchzalrnumimnmhp` is **naughty**:
  - No double letter → rule-2 violated

- `haegwjzuvuyypxyu` is **naughty**:
  - Contains `xy` → rule-3 violated

- `dvszwmarrgswjxmb` is **naughty**:
  - Only 1 vowel → rule-1 violated

Our job is to find how many of the given strings are nice.

### Idea

We can solve this using the in-built re module:

- **Rule 1:** Count vowels using `re.findall(r"a|e|i|o|u", string)`
- **Rule 2:** Look for repeated letters using a pattern like `aa|bb|...|zz`
- **Rule 3:** Check for forbidden substrings using `re.findall(r"ab|cd|pq|xy", string)`

## Part 2

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is **naughty** or **nice**. None of the old rules apply anymore.

A **nice string** must now meet **both** of the following conditions:

1. **It contains a pair of any two letters that appears at least twice in the string without overlapping.**
   - Examples: 
     - `xyxy` → contains `xy` twice
     - `aabcdefgaa` → contains `aa` twice
     - ❌ `aaa` does not count — overlapping `aa`

2. **It contains at least one letter which repeats with exactly one letter between them.**
   - Examples:
     - `xyx` → `x` repeats with `y` in between
     - `abcdefeghi` → `e` repeats with `f` in between (`efe`)
     - `aaa` → `a` repeats with `a` in between

**Examples:**

- `qjhvhtzxzqqjkmpb` is **nice**:
  - Contains `qj` twice → rule-1 satisfied
  - Contains `zxz` → rule-2 satisfied

- `xxyxx` is **nice**:
  - Contains `xx` twice → rule-1 satisfied
  - Contains `x` repeated with one in between (`xyx`) → rule-2 satisfied

- `uurcxstgmygtbstg` is **naughty**:
  - Has a repeated pair (`tg`) → rule-1 satisfied
  - But **no** letter repeats with one in between → rule-2 violated

- `ieodomkazucvgmuy` is **naughty**:
  - Has a `odo` → rule-2 satisfied
  - But **no** repeated pair → rule-1 violated

### Idea

We can again use the `re` module:

- **Rule 1:** Look for a **pair of any two letters** that appears at least twice without overlapping using  
  `re.findall(r"(..).*\1", string)`

- **Rule 2:** Look for a **repeating letter with exactly one letter between** using  
  `re.findall(r"(.).\1", string)`