## Part 1

Santa brought little Bobby Tables a bitwise logic circuit kit! Each wire can carry a **16-bit unsigned signal** (0–65535), and the kit comes with a list of wiring instructions using logic gates like `AND`, `OR`, `NOT`, `LSHIFT`, and `RSHIFT`.

Your job is to simulate the circuit based on these instructions and determine the signal carried by wire `a`.

- Wires are labeled with lowercase identifiers (`x`, `y`, `a`, `b`, etc.).
- Each wire gets its signal from:
  - A **constant value**
  - Another **wire**
  - A **bitwise logic gate** with one or two inputs

| Instruction | Description                         | Example                      |
|-------------|-------------------------------------|------------------------------|
| `AND`       | Bitwise AND between two inputs      | `x AND y -> z`               |
| `OR`        | Bitwise OR between two inputs       | `x OR y -> z`                |
| `LSHIFT`    | Left shift a signal by N bits       | `x LSHIFT 2 -> y`            |
| `RSHIFT`    | Right shift a signal by N bits      | `x RSHIFT 2 -> y`            |
| `NOT`       | Bitwise NOT (1-input operation)     | `NOT x -> y`                 |

Other valid formats:
- `123 -> x` assigns a constant to a wire
- `x -> y` copies the value from `x` to `y`

**Example**

Input:
```
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
```

Output:
```
d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
```

### Idea

- Use a dictionary `vars` to store resolved wire values
- Read all instructions into a list
- Process instructions in a loop:
   - If the inputs for an instruction are ready (constants or known wires), compute and assign the output
   - If not, move the instruction to the end of the list for retrying later
- Repeat until all instructions are resolved
- The final signal on wire `a` is your answer

## Part 2

Now you are asked to take the signal you obtained for wire `a` from **Part 1**, **override wire `b`** with that value and reset the remaining circuit. You have to find the **new signal on wire `a`**.

### Idea

- Reload the original list of instructions
- **Remove or ignore** any instruction that assigns a value to wire `b`
- Add a new instruction: `<value of a from Part 1> -> b`
- Re-run the same logic simulation as in Part 1