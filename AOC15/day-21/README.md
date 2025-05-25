## Part 1

You're playing an RPG and need to find the **minimum gold** required to beat the boss. You can buy exactly one weapon, optionally one armor, and up to two rings from the shop. Each item has a cost, damage, and armor stat. The battle is turn-based: you always attack first, and each attack deals damage equal to `your damage - their armor`, but at least 1.

**Example:**

Boss: `Hit Points: 12, Damage: 7, Armor: 2`  
Player: `Hit Points: 8, Damage: 5, Armor: 5`

```
Player deals 5 - 2 = 3 -> Boss HP = 9
Boss deals 7 - 5 = 2 -> Player HP = 6
Player deals 3 -> Boss HP = 6
...
Player wins
```

### Idea
Try all combinations of 1 weapon, 0–1 armor, and 0–2 rings  
For each gear set, simulate a fight  
Track the minimum cost for which the player wins


## Part 2

Now you must find the **maximum gold** you can spend and still lose to the boss using the same rules

**Example:** Same as above, but this time you're looking for setups where you **lose**

### Idea
Try all valid gear combinations  
Simulate the battle like before  
Track the maximum cost among the losing loadouts