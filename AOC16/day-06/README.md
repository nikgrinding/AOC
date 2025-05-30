## Part 1

You're intercepting a corrupted message that was sent using a repetition code. The same message was sent repeatedly, but due to noise, each character position may contain different characters across transmissions. To recover the original message, you need to take the most common character at each position.

**Example:**
```
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
```

The most common characters per column form the message: `easter`.

### Idea

Loop through each column and count how often each character appears. For each position, take the most frequent character and add it to the final message.

## Part 2

Instead of using the most common characters, the message is encoded using the *least* common character at each position, due to how the noise is introduced.

**Example:**
From the same input as above, using the least frequent characters gives: `advent`.

### Idea

Same as Part 1, but instead of picking the most frequent character at each column, pick the least frequent one to reconstruct the message.