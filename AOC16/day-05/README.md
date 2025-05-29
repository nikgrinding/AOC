## Part 1

You’re given a Door ID and need to generate an 8-character password. You compute the MD5 hash of the Door ID followed by an increasing index (starting at 0). If the hash starts with five zeroes (`00000`), the sixth character of the hash becomes the next character in the password.

**Example:**
```
Door ID: abc
First valid hash: md5("abc3231929") -> ...000001..., so password starts with '1'
Next valid: md5("abc5017308") -> ...000008..., so next char is '8'
Continue until 8 characters are found
```

### Idea

Keep hashing the Door ID with increasing numbers until the hash starts with `"00000"`. When it does, take the 6th character and add it to the password. Repeat until the password has 8 characters.

## Part 2

The Door ID and hash rule are the same, but now the 6th character tells the *position* (0–7) and the 7th character is the value to put there. Each position is filled only once.

**Example:**
```
Door ID: abc
md5("abc3231929") -> ...0000015..., so put '5' at position 1: _5______
md5("abc5357525") -> ...000004e..., so put 'e' at position 4: _5__e___
```

### Idea

As before, generate hashes that start with `"00000"`. If the 6th character is a valid index (0–7) and that position is still empty, insert the 7th character there. Continue until all 8 positions are filled.