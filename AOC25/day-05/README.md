# Day 5: Cafeteria

## Part 1

The cafeteria's new inventory management system tracks fresh ingredients using ID ranges. You need to determine which available ingredient IDs are fresh by checking if they fall within any of the specified fresh ID ranges. An ingredient ID is fresh if it appears in at least one range.

**Input format:**

-   First section: Fresh ingredient ID ranges (format: `start-end`, one per line)
-   Blank line separator
-   Second section: Available ingredient IDs to check (one per line)

**Key rules:**

-   Ranges are inclusive (e.g., `3-5` includes 3, 4, and 5)
-   Ranges can overlap
-   An ingredient ID is fresh if it falls into ANY range

**Example:**

```
3-5
10-14
16-20
12-18

1
5
8
11
17
32
```

Step-by-step walkthrough:

-   Ingredient ID `1` -> spoiled (not in any range)
-   Ingredient ID `5` -> fresh (in range 3-5)
-   Ingredient ID `8` -> spoiled (not in any range)
-   Ingredient ID `11` -> fresh (in range 10-14)
-   Ingredient ID `17` -> fresh (in ranges 16-20 and 12-18)
-   Ingredient ID `32` -> spoiled (not in any range)

**Expected output:** `3` fresh ingredients

### Idea

1. Parse the input to extract the fresh ID ranges and the list of available ingredient IDs
2. **Merge overlapping ranges** by sorting ranges and combining those that overlap or are adjacent to optimize checking
3. For each available ingredient ID, check if it falls within any merged range
4. Count how many ingredient IDs are fresh

## Part 2

Instead of checking specific ingredient IDs, you need to count the **total number of ingredient IDs** that the fresh ranges consider to be fresh. The available ingredient IDs list from Part 1 is now irrelevant - you only need to process the ranges themselves.

**Modified task:**

-   Ignore the second section (available ingredient IDs)
-   Count all unique IDs covered by the fresh ranges

**Example:**

Using the same ranges:

```
3-5
10-14
16-20
12-18
```

The fresh IDs are:

-   From `3-5`: 3, 4, 5
-   From `10-14`: 10, 11, 12, 13, 14
-   From `16-20`: 16, 17, 18, 19, 20
-   From `12-18`: 12, 13, 14, 15, 16, 17, 18 (overlaps with 10-14 and 16-20)

After removing duplicates: 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

**Expected output:** `14` total fresh ingredient IDs

**Important edge case:** Overlapping ranges must not be counted multiple times (e.g., ID 17 appears in both `16-20` and `12-18` but only counts once)

### Idea

1. Parse only the fresh ID ranges from the input (ignore the available IDs section)
2. **Merge all overlapping ranges** by sorting and combining ranges that overlap or touch
3. For each merged range, calculate the count of IDs it contains using `end - start + 1`
4. Sum up the counts from all merged ranges to get the total number of fresh IDs
