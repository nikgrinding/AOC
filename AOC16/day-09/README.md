## Part 1

You're given a file that uses a custom compression format. A marker in the form `(AxB)` means to repeat the next A characters B times. The marker itself is not included in the output, and markers inside repeated segments are ignored.

**Examples:**
- `ADVENT` → length 6
- `A(1x5)BC` → `ABBBBBC` → length 7
- `(3x3)XYZ` → `XYZXYZXYZ` → length 9
- `A(2x2)BCD(2x2)EFG` → `ABCBCDEFEFG` → length 11
- `(6x1)(1x3)A` → `(1x3)A` → length 6
- `X(8x2)(3x3)ABCY` → `X(3x3)ABC(3x3)ABCY` → length 18

### Idea

We simulate reading the string one character at a time. When we hit a marker, we parse its parameters, skip the correct number of characters, and add the length contribution from the repeated section directly. We don't recursively evaluate nested markers.

## Part 2

In version two of the format, markers inside repeated data are also decompressed recursively, allowing deeper compression and requiring a more advanced approach.

**Examples:**
- `(3x3)XYZ` → `XYZXYZXYZ` → length 9
- `X(8x2)(3x3)ABCY` → `XABCABCABCABCABCABCY` → length 20
- `(27x12)(20x12)(13x14)(7x10)(1x12)A` → length 241920
- `(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN` → length 445

### Idea

Instead of building the entire decompressed string, we recursively calculate its length. When we hit a marker, we extract the substring it refers to and calculate its decompressed length recursively, multiplying by the repeat count. This avoids memory issues and works for very large inputs.