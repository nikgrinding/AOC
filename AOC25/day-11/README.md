# Day 11: Reactor

## Part 1

The factory's reactor communicates with devices through a network of electrical connections. Each device has outputs that connect to other devices, forming a **directed graph**. The task is to find all possible paths data can take from the starting device `you` to the output device `out`.

### Input Format

-   Each line contains a device name followed by a colon and space-separated list of connected devices
-   Format: `device_name: output1 output2 output3`
-   Data flows only in the direction specified (from device to its outputs, never backwards)

### Key Rules

-   Start at the device labeled `you`
-   End at the device labeled `out`
-   Data flows only forward through output connections
-   Count all distinct paths from start to end

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

**Step-by-step walkthrough:**

Graph structure:

-   `you` connects to `bbb` and `ccc`
-   `bbb` connects to `ddd` and `eee`
-   `ccc` connects to `ddd`, `eee`, and `fff`

All paths from `you` to `out`:

1. `you` -> `bbb` -> `ddd` -> `ggg` -> `out`
2. `you` -> `bbb` -> `eee` -> `out`
3. `you` -> `ccc` -> `ddd` -> `ggg` -> `out`
4. `you` -> `ccc` -> `eee` -> `out`
5. `you` -> `ccc` -> `fff` -> `out`

**Expected output:** 5

### Idea

1. Parse the input to build a directed graph (adjacency list) where each device maps to its list of outputs
2. Use depth-first search (DFS) with memoization starting from `you`
3. Base case: when reaching `out`, return 1 path; otherwise recursively count paths through all neighbors
4. Sum the path counts from all outgoing connections and cache results to avoid recomputation

## Part 2

Part 2 requires finding paths from a different starting point (`svr` instead of `you`) with an additional constraint: **all counted paths must pass through both `dac` and `fft` devices** (in any order). This filters the valid paths to only those visiting both required intermediate nodes.

### Additional Rules

-   Start at the device labeled `svr` (server rack)
-   End at the device labeled `out` (same as Part 1)
-   Only count paths that visit **both** `dac` (digital-to-analog converter) and `fft` (fast Fourier transform)
-   The order of visiting `dac` and `fft` doesn't matter

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

**Explanation:**

Total paths from `svr` to `out` (8 paths):

1. `svr,aaa,fft,ccc,ddd,hub,fff,ggg,out` - has `fft` but no `dac` ✗
2. `svr,aaa,fft,ccc,ddd,hub,fff,hhh,out` - has `fft` but no `dac` ✗
3. `svr,aaa,fft,ccc,eee,dac,fff,ggg,out` - has both `fft` and `dac` ✓
4. `svr,aaa,fft,ccc,eee,dac,fff,hhh,out` - has both `fft` and `dac` ✓
5. `svr,bbb,tty,ccc,ddd,hub,fff,ggg,out` - has neither ✗
6. `svr,bbb,tty,ccc,ddd,hub,fff,hhh,out` - has neither ✗
7. `svr,bbb,tty,ccc,eee,dac,fff,ggg,out` - has `dac` but no `fft` ✗
8. `svr,bbb,tty,ccc,eee,dac,fff,hhh,out` - has `dac` but no `fft` ✗

**Expected output:** 2

### Important Edge Cases

-   Paths may visit `dac` before `fft` or `fft` before `dac` (both are valid)
-   A path visiting only one of the two required devices should not be counted
-   Multiple paths may converge at the same device after visiting the required nodes

### Idea

1. Parse the input to build the directed graph (same as Part 1)
2. Use DFS with state tracking: track current node and two boolean flags (`has_dac`, `has_fft`)
3. Update flags when visiting `dac` or `fft`; at `out`, return 1 only if both flags are true
4. Memoize results based on `(node, has_dac, has_fft)` tuple to avoid redundant computation
