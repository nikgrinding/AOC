## Part 1

You're given a small set of assembly-like instructions in a language called "assembunny" that operates on four registers: a, b, c, and d. All registers start at 0. The goal is to execute the instructions and find the value left in register `a` once the program terminates.

**Example:**
```
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
```

This sets `a` to 41, increases it twice to 43, decreases it to 42, then jumps over the last `dec a`, leaving `a` as 42.

### Idea

We simulate the program line by line using a simple instruction pointer. Each instruction is parsed and executed accordingly: `cpy` sets a register, `inc`/`dec` modify a register, and `jnz` conditionally jumps. We keep looping until the pointer moves past the last instruction and then return the value in register `a`.

## Part 2

Now, the same program must be executed, but with register `c` initialized to 1 instead of 0. This represents a changed starting condition that affects how the program executes.

### Idea

We use the same simulation logic from Part 1 but start with `c = 1` in the register map. The change in starting state causes the program to behave differently, leading to a different final value in register `a`.