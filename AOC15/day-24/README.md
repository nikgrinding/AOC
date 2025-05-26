## Part 1

Santa needs to balance his sleigh by dividing all packages into three groups with equal total weight  
The first group, going in the passenger compartment, must use the fewest packages  
If multiple such groups exist, choose the one with the smallest quantum entanglement (product of weights)

**Examples:**
```
Group 1: 11 9 (QE= 99)
Group 2: 10 8 2
Group 3: 7 5 4 3 1

Group 1: 10 9 1 (QE= 90)
Group 2: 11 7 2
Group 3: 8 5 4 3
```

The best choice is `11 9`, since it has the fewest number of packages even though its QE is higher than `10 9 1`

### Idea

Start by finding all combinations of packages that sum to one-third of the total weight  
Pick the group with the fewest packages and the smallest quantum entanglement  
Return the QE of the best group

## Part 2

Now, Santa needs to divide the packages into four groups of equal weight  
The goal remains the same: choose the smallest group for the passenger compartment with the lowest QE

**Examples:**
```
Group 1: 11 4 (QE=44)
Group 2: 10 5
Group 3: 9 3 2 1
Group 4: 8 7
```

### Idea

Same logic as Part 1, but this time divide into four groups  
Find valid groups summing to one-fourth of the total weight  
Return the QE of the smallest-sized group with the lowest entanglement