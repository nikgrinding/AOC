## Part 1

You're checking IPv7 addresses to see if they support TLS (transport-layer snooping). An IP supports TLS if:
- It contains at least one ABBA sequence (e.g., `abba`, `xyyx`) **outside** square brackets.
- It does **not** contain any ABBA sequences **inside** square brackets.

An ABBA is a 4-character sequence where:
- The first and fourth characters are the same,
- The second and third characters are the same,
- The first and second characters are different.

**Examples:**
- `abba[mnop]qrst` → supports TLS
- `abcd[bddb]xyyx` → does **not** support TLS (because of `bddb` inside brackets)
- `aaaa[qwer]tyui` → does **not** support TLS (`aaaa` is invalid)
- `ioxxoj[asdfgh]zxcvbn` → supports TLS

### Idea

Separate each address into supernet (outside `[]`) and hypernet (inside `[]`) sequences. Check if any supernet contains an ABBA and make sure none of the hypernet sequences do.

## Part 2

Now you're checking for SSL (super-secret listening). An IP supports SSL if:
- It contains an ABA pattern in a supernet sequence.
- It contains the corresponding BAB pattern (reversed ABA) in a hypernet sequence.

An ABA is a 3-character sequence like `aba` or `xyx`. The corresponding BAB would be `bab` or `yxy`.

**Examples:**
- `aba[bab]xyz` → supports SSL (aba and corresponding bab)
- `xyx[xyx]xyx` → does **not** support SSL
- `aaa[kek]eke` → supports SSL
- `zazbz[bzb]cdb` → supports SSL

### Idea

Find all ABA patterns in supernet sequences and check if any corresponding BAB appears in the hypernet sequences.