## Part 1

You are a wizard fighting a boss. You start with 50 hit points and 500 mana. The boss has hit points and damage stats given in the input. Each turn, you or the boss take actions alternately. You always go first.

On your turn, you must cast one spell from these options:
- Magic Missile: costs 53 mana, instantly does 4 damage
- Drain: costs 73 mana, does 2 damage and heals you for 2 hit points
- Shield: costs 113 mana, lasts 6 turns, increases armor by 7 while active
- Poison: costs 173 mana, lasts 6 turns, deals 3 damage to boss each turn
- Recharge: costs 229 mana, lasts 5 turns, gives 101 mana each turn

Effects apply at the start of each turn (both player and boss), then their timers decrease by 1.
You cannot cast a spell that would start an effect which is already active.
The boss attacks normally on its turn, dealing damage reduced by your armor (minimum 1).

You want to find the least amount of mana you can spend and still win the fight.

**Example:**

Player HP: 10, mana: 250; Boss HP: 13, damage: 8

```
Player casts Poison
Boss turn: Poison deals 3 damage; boss attacks for 8 damage
Player casts Magic Missile dealing 4 damage
Poison eventually kills the boss
```

### Idea
Use depth-first search to try all spell sequences. Track active effects and apply them each turn. Prune paths that exceed current minimal mana spent.

## Part 2

Same as Part 1, but at the start of each player turn you lose 1 hit point. If your HP drops to 0 or below, you lose immediately.

Find the least mana to win under these harder conditions.

**Example:** Same as Part 1 but player loses 1 HP each turn before casting spells.

### Idea
Same DFS approach but deduct 1 HP at start of player turn before applying effects and casting spells.