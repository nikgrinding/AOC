# Day 11: Reactor

## Part 1
- The problem describes a directed graph where each device sends data only through its listed outputs.
- We must count all possible distinct paths from the device labeled `you` to the device labeled `out`.

### Input Format
- Each line contains `source: targets`, where:
  - `source` is a device name.
  - `targets` is a space-separated list of device names receiving output from `source`.

### Example
Input:
```
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
```

Sample paths:
- you -> bbb -> ddd -> ggg -> out
- you -> bbb -> eee -> out
- you -> ccc -> ddd -> ggg -> out
- you -> ccc -> eee -> out
- you -> ccc -> fff -> out

**Expected Output:** 5

### Idea
1. Parse input into a graph mapping each device to its output list.
2. Use DFS from `you`, counting paths that eventually reach `out`.
3. Cache the results to avoid recomputation.
4. Sum all valid path counts.

## Part 2
- Similar to Part 1, but only count paths that visit both `dac` and `fft`.
- Starting device is now `svr`.

### Rules
- A path is valid only if it visits both `dac` and `fft`.
- Order does not matter.

### Example
Input:
```
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
```

Only 2 of the possible paths contain both `dac` and `fft`.

**Expected Output:** 2

### Idea
1. Build the adjacency list of the graph as before.
2. Use DFS but track two flags: `has_dac` and `has_fft`.
3. Only count paths reaching `out` with both flags true.
4. Memoize the state of each node being visited to avoid recomputation.