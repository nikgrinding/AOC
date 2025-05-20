## Part 1

Santa needs a new password by incrementing the old one until it meets a new set of rules. A valid password must be exactly eight lowercase letters and follow these rules: 
- It must include one increasing straight of at least three letters, like `abc` or `xyz` 
- It must not contain the letters `i`, `o`, or `l` 
- It must contain at least two different non-overlapping pairs of the same letter, like `aa` and `bb`

Starting from the given input password, we keep incrementing the string (like counting, rolling over from 'z' to 'a') until we find the next valid one.

**Example**

Input:
```
abcdefgh
```

Output:
```
abcdffaa
```

### Idea
We build rules using regex to check for forbidden characters, increasing triples, and two different pairs. We increment the password like a base-26 counter and keep checking until we find a match.

## Part 2

Santa’s password expires again, and now we must find the **next** valid password after the one we found in Part 1.

### Idea
We reuse the same validation logic and call the generator again starting from the next string after the previous password.