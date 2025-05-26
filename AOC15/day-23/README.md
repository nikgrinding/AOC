## Part 1

You're given a tiny assembly-like language with two registers: `a` and `b`, both starting at 0. The instructions are:
- `hlf r`: sets register `r` to half its current value
- `tpl r`: triples register `r`
- `inc r`: increments register `r` by 1
- `jmp offset`: jumps to a new instruction relative to the current one
- `jie r, offset`: jumps if register `r` is even
- `jio r, offset`: jumps if register `r` is 1

The program halts when the instruction pointer goes outside the list. You need to run the program and report the final value of register `b`.

**Examples:**

```
inc a
jio a, +2
tpl a
inc a
```

This sets `a = 1`, jumps over `tpl`, and then `inc` runs again, resulting in `a = 2`

### Idea
Simulate the instruction set using a dictionary for registers and an index for the instruction pointer  
Follow each instruction's logic and update the pointer as needed  
Return the final value in register `b`

## Part 2

Now, register `a` starts at 1 instead of 0  
Everything else remains the same, and you still need to report the final value in `b`

**Examples:** Same program, but initial value of `a` is 1 instead of 0

### Idea
Use the same simulator but initialize `a = 1` instead of 0  
Logic and structure remain unchanged