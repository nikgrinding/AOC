# Day 3: Lobby

## Part 1

The lobby elevators are offline, and you need to power an escalator using batteries. Each battery bank is a sequence of digits (1-9), and you must select exactly **two batteries** from each bank to create a joltage value. The joltage is the number formed by concatenating the two selected digits in order (you cannot rearrange them).

-   **Input format:** Each line represents a battery bank with digits 1-9
-   **Goal:** Find the maximum possible joltage from each bank by selecting two batteries
-   **Constraint:** Batteries must be selected in their original order (no rearranging)

**Example:**

```
987654321111111
811111111111119
234234234234278
818181911112111
```

-   `987654321111111` -> Select first two batteries (9 and 8) -> **98** jolts
-   `811111111111119` -> Select batteries at positions 0 and 14 (8 and 9) -> **89** jolts
-   `234234234234278` -> Select last two batteries (7 and 8) -> **78** jolts
-   `818181911112111` -> Select batteries at positions 6 and 13 (9 and 2) -> **92** jolts

**Total output joltage:** 98 + 89 + 78 + 92 = **357**

### Idea

1. For each battery bank, find the maximum digit (this will be the first digit)
2. Find the second maximum digit that comes after the maximum digit or at the end
3. Concatenate these two digits to form the maximum two-digit joltage
4. Sum all maximum joltage values across all banks

This greedy approach works because selecting the largest digit first and the largest remaining digit second guarantees the maximum two-digit number.

## Part 2

Now the escalator needs more power - you must select exactly **twelve batteries** from each bank instead of two. The joltage is still the number formed by concatenating the selected digits in order, but now it will be a 12-digit number.

-   **Modified constraint:** Select exactly 12 batteries from each bank (instead of 2)
-   **Goal:** Maximize the 12-digit joltage number from each bank
-   **Strategy:** To maximize, select the largest digits and exclude the smallest ones

**Example:** Using the same input as Part 1:

```
987654321111111
811111111111119
234234234234278
818181911112111
```

-   `987654321111111` (15 digits) -> Turn on all except 3 smallest `1`s -> **987654321111**
-   `811111111111119` (15 digits) -> Turn on all except 3 smallest `1`s -> **811111111119**
-   `234234234234278` (15 digits) -> Exclude one `2`, one `3`, and one `2` -> **434234234278**
-   `818181911112111` (15 digits) -> Exclude 3 smallest `1`s -> **888911112111**

**Total output joltage:** 987654321111 + 811111111119 + 434234234278 + 888911112111 = **3121910778619**

**Edge case:** Each bank must have at least 12 batteries to select from.

### Idea

1. Use a monotonic stack to build the maximum 12-digit number efficiently
2. For each digit in the bank:
    - Remove smaller digits from the stack if we still have room to exclude digits (total - 12 removals allowed)
    - Add the current digit to the stack
3. Take the first 12 digits from the stack as the maximum joltage
4. Sum all maximum joltage values across all banks

This algorithm maintains a decreasing stack, removing smaller digits when a larger digit is found, ensuring the largest possible number while maintaining the original order.
