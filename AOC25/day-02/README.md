# Day 2: Gift Shop

## Part 1

The gift shop database has invalid product IDs that need to be identified. A product ID is **invalid** if it consists of a sequence of digits repeated exactly twice (e.g., `55`, `6464`, `123123`).

**Input format:**
- A single line containing comma-separated ranges
- Each range: `start-end` (inclusive)
- Example: `11-22,95-115,998-1012`

**Key rules:**
- An ID is invalid if it's a digit sequence repeated exactly twice
- No leading zeroes are allowed (e.g., `0101` is not a valid ID)
- Sum all invalid IDs found across all ranges

**Example:**

```
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862
```

Step-by-step breakdown:
- `11-22` -> Invalid IDs: `11` (1 twice), `22` (2 twice)
- `95-115` -> Invalid IDs: `99` (9 twice)
- `998-1012` -> Invalid IDs: `1010` (10 twice)
- `1188511880-1188511890` -> Invalid IDs: `1188511885` (118851 twice)
- `222220-222224` -> Invalid IDs: `222222` (222 twice)
- `1698522-1698528` -> No invalid IDs
- `446443-446449` -> Invalid IDs: `446446` (446 twice)
- `38593856-38593862` -> Invalid IDs: `38593859` (3859 twice)

**Expected output:** Sum = `1227775554`

### Idea

1. Parse each range to extract start and end values
2. For each number in the range, check if it's a repeated pattern by testing if the number can be split into two equal halves
3. Verify the two halves are identical (number matches `pattern + pattern`)
4. Sum all numbers that match the invalid ID criteria

## Part 2

Part 2 extends the validation rule: an ID is now **invalid** if it consists of a digit sequence repeated **at least twice** (2 or more times). This includes patterns like `123123` (2 times), `123123123` (3 times), `1212121212` (5 times), etc.

**Modified constraint:**
- IDs with patterns repeated 2, 3, 4, or more times are all invalid
- The pattern length must divide evenly into the total ID length

**Example:**

Using the same ranges as Part 1:
- `11-22` -> Still invalid: `11`, `22`
- `95-115` -> Now includes: `99`, `111` (1 three times)
- `998-1012` -> Now includes: `999` (9 three times), `1010`
- `565653-565659` -> Now includes: `565656` (56 three times)
- `824824821-824824827` -> Now includes: `824824824` (824 three times)
- `2121212118-2121212124` -> Now includes: `2121212121` (21 five times)

**Expected output:** Sum = `4174379265`

**Important edge cases:**
- Single digit repeated (e.g., `1111111` = 1 seven times) is invalid
- The pattern must repeat completely (no partial repetitions)
- Check all possible pattern lengths that divide the number's length

### Idea

1. Parse each range to extract start and end values
2. For each number, try all possible pattern lengths from 1 to `len(number)//2`
3. Check if the number equals the pattern repeated multiple times (at least twice)
4. Mark as invalid if any valid repeating pattern is found, then sum all invalid IDs
