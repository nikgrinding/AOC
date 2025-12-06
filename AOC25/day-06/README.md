# Day 6: Trash Compactor

## Part 1

The cephalopod math worksheet contains problems arranged horizontally in columns. Each problem consists of numbers arranged **vertically** in a column, with an operator (`+` or `*`) at the bottom. Problems are separated by full columns of spaces, and the alignment of numbers can be ignored.

**Input format:**
- Numbers are arranged vertically in columns
- Each column represents a separate problem
- The bottom row contains the operator (`+` or `*`)
- Columns with only spaces separate different problems

**Rules:**
- Read each problem **top to bottom** in each column
- Apply the operator at the bottom to all numbers in that column
- Calculate the grand total by adding all individual problem answers

**Example:**
```
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
```

Step-by-step walkthrough:
1. First problem (column 1): `123 * 45 * 6 = 33210`
2. Second problem (column 2): `328 + 64 + 98 = 490`
3. Third problem (column 3): `51 * 387 * 215 = 4243455`
4. Fourth problem (column 4): `64 + 23 + 314 = 401`

**Expected output:** `33210 + 490 + 4243455 + 401 = 4277556`

### Idea
1. Parse the input by transposing rows into columns, identifying each problem by detecting space-only columns as separators
2. For each problem column, extract all digits and the operator symbol
3. Apply the operator (addition or multiplication) to all numbers in sequence
4. Sum all individual problem results to get the grand total

## Part 2

Part 2 reveals that **cephalopod math is written right-to-left**. Each number is given in its own column with the most significant digit at the top and least significant at the bottom. Problems are still separated by space-only columns.

**Additional rules:**
- Read the worksheet **right-to-left** instead of left-to-right
- Each column now represents a **digit position** of numbers, not a separate problem
- Numbers are formed vertically: top digit is most significant, bottom is least significant
- The operator at the bottom still indicates which operation to perform

**Example:**
Using the same input:
```
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
```

Reading right-to-left:
1. Rightmost problem: `4 + 431 + 623 = 1058` (reading columns vertically: 4, 3-2-1-4, 3-6-2-3)
2. Second from right: `175 * 581 * 32 = 3253600`
3. Third from right: `8 + 248 + 369 = 625`
4. Leftmost problem: `356 * 24 * 1 = 8544`

**Expected output:** `1058 + 3253600 + 625 + 8544 = 3263827`

**Important edge cases:**
- Handle empty/space characters properly when reading digits vertically
- Numbers can have different lengths (different number of digits)
- Process columns from right to left, but read digits top to bottom within each number

### Idea
1. Reverse the column order to process right-to-left, then identify problem groups by space-only column separators
2. For each problem, read numbers vertically (top to bottom) to form complete numbers, treating spaces as empty positions
3. Apply the operator to all numbers in the problem
4. Sum all problem results to get the grand total
