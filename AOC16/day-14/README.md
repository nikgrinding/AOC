## Part 1

To generate keys for a one-time pad, we take the MD5 hash of a salt and a growing integer index. A hash is only considered a valid key if it contains a triplet (three identical characters in a row), and within the next 1000 hashes there is at least one hash that contains the same character repeated five times.

**Examples:**
```
abc39 -> ...eee...
abc816 -> ...eeeee...
```

The first such index where this happens 64 times determines the answer.

### Idea

We precompute the next 1000 hashes in advance and keep sliding this window as we increment the index. For each hash, we check if it has a triple, and if it does, we look forward through the next 1000 hashes to see if any of them contain the same character five times in a row. We stop when we find the 64th key.

## Part 2

In Part 2, we enhance the hashing process by performing **key stretching**, meaning each hash is re-hashed 2016 additional times (for a total of 2017 MD5 hashes). The rest of the key detection logic remains the same.

**Example:**
```
MD5(abc0) = 577571...
MD5(MD5(...)) → repeated 2016 more times → a107ff...
```

The new sequence of stretched hashes produces different keys.

### Idea

The only change is that each hash is generated using 2017 rounds of MD5 hashing. We memoize these results for reuse in both the initial 1000-hash buffer and the forward look-ahead window. The process of identifying triplets and matching quintuples stays the same as in Part 1.