# Day 14: Reindeer Olympics

## Part 1

Each reindeer has a defined flying speed, a maximum flying duration, and a mandatory rest period. During a race, a reindeer repeats a cycle of flying and then resting. For example, if a reindeer can fly at 14 km/s for 10 seconds and must rest for 127 seconds, it repeats this pattern continuously.

Given a total race duration of 2503 seconds, we need to determine how far each reindeer has traveled by the end of the race. The reindeer that has traveled the farthest wins.

**Example:**
- Comet can fly 14 km/s for 10 seconds, then rest for 127 seconds  
- Dancer can fly 16 km/s for 11 seconds, then rest for 162 seconds  
After 1000 seconds:
- Comet travels 1120 km  
- Dancer travels 1056 km  
So, Comet is the winner for this race duration.

### Idea
For each reindeer, we calculate how many complete fly-rest cycles fit into the total race time. Each full cycle contributes a fixed distance based on speed and fly duration. We then add any distance covered in the final partial cycle (if the remaining time allows for additional flying). The maximum among all reindeers’ distances is the answer.

## Part 2

Now, instead of determining the winner by total distance alone, we track performance per second. At the end of every second, the reindeer(s) who are currently leading in distance are awarded one point. If there is a tie, each of the leading reindeer gets one point.

After 2503 seconds, the reindeer with the highest total score wins.

**Example:**
After 1000 seconds:
- Dancer has 689 points  
- Comet has 312 points  
So, Dancer wins based on points.

### Idea
We simulate each second of the race. For every second, we compute how far each reindeer has traveled using their speed, fly duration, and rest period. Then we identify the reindeer(s) with the greatest distance at that moment and award them one point. We keep a running tally of scores and return the maximum at the end.