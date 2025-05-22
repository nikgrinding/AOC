## Part 1

We are given a list of ingredients, each with five properties: capacity, durability, flavor, texture, and calories. We have exactly 100 teaspoons to distribute among all the ingredients, using whole numbers only. For each possible distribution that sums to 100, we compute the total score by:
- Multiplying the amount of each ingredient with its respective properties
- Summing each property across all ingredients
- Setting any negative totals to 0
- Multiplying all property totals (except calories) to get the cookie's score

We want to find the highest possible score across all valid distributions.

**Example:**
Input:
```
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8  
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3  
```

Output:
```
62842880
```

### Idea
Try all combinations of ingredient amounts that add up to 100. For each, compute property totals and multiply them to get the score, ignoring calories. Keep track of the maximum score found.


## Part 2

Now we add a constraint: the total calories in the cookie must be exactly 500. The rest of the logic remains the same. Only consider distributions where the calorie total is exactly 500, and among them, find the highest score using the same process.

**Example:**
Input:
```
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8  
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3 
``` 

Output:
```
57600000
```

### Idea
Filter out any combinations that do not result in exactly 500 calories, and calculate the score only for the valid ones. Track the highest score among those.