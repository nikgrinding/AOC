## Part 1

We are given a JSON document represented as a string. The task is to find all numbers in it (ignoring its structure) and compute their sum. All numbers are outside of quoted strings.

**Examples:**
- `[1,2,3]` -> `6`
- `{"a":2,"b":4}` -> `6`
- `[[[3]]]` -> `3`
- `{"a":{"b":4},"c":-1}` -> `3`

### Idea
We parse the string character by character, collecting digits (including negative signs) to form numbers. Once we finish a number, we convert and add it to the sum.

## Part 2

Now, if any object contains `"red"` as a value, that object and everything inside it should be ignored. This rule does not apply to arrays.

**Examples:**
- `[1,{"c":"red","b":2},3]` -> `4` (middle object is skipped)
- `{"d":"red","e":[1,2,3,4],"f":5}` -> `0` (entire structure skipped)
- `[1,"red",5]` -> `6` (`"red"` in array is fine)

### Idea
We load the input as JSON and then recursively traverse it. If we hit a number, we add it. If it's a list, we sum its elements. If it's a dictionary and has `"red"` as any value, we ignore it. Otherwise, we recursively sum its values.