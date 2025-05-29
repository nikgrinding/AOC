## Part 1

You’re given a list of encrypted room names with sector IDs and checksums. A room is *real* if the checksum matches the five most common letters in the name, sorted first by frequency (descending) and then alphabetically.

**Examples:**
```
aaaaa-bbb-z-y-x-123[abxyz] -> real
a-b-c-d-e-f-g-h-987[abcde] -> real
not-a-real-room-404[oarel] -> real
totally-real-room-200[decoy] -> not real
```

The task is to sum the sector IDs of the real rooms.

### Idea

Parse the name and checksum, count the letter frequencies (ignoring dashes), and sort them by count and then alphabetically. Compare the result with the checksum and add the sector ID to the total if it’s valid.

## Part 2

Now that decoy rooms are filtered out, decrypt the real room names using a Caesar cipher where each letter is shifted forward by the sector ID. Dashes become spaces. Identify the room that contains the phrase `"north"`.

**Example:**
```
qzmt-zixmtkozy-ivhz-343 -> very encrypted name
```

### Idea

Shift each character in the encrypted name by sector ID positions forward in the alphabet, wrapping around from z to a. After decryption, search for the room name containing `"north"` and return its sector ID.