## Part 1

Each elf delivers presents to every house that is a multiple of their number, delivering `10 × elf_number` presents to each  
Find the lowest house number that receives at least as many presents as the given input

**Examples:**  
Elf 1 → houses 1, 2, 3, 4, ... (10 presents each)  
Elf 2 → houses 2, 4, 6, 8, ... (20 presents each)

### Idea
- Use a list to store total presents per house  
- For each elf from 1 to limit, update all multiples of that elf number  
- Return the first house with total presents >= input  

## Part 2

Each elf now only visits the first **50** houses that are multiples of their number  
They deliver `11 × elf_number` presents to each of those houses  
Find the lowest house number that receives at least as many presents as the given input

**Examples:**  
Elf 1 → houses 1, 2, 3, 4, ..., 50 (11 presents each)  
Elf 2 → houses 2, 4, 6, 8, ..., 100 (11 presents each)

### Idea
- Same logic as part 1, but only update the first 50 houses per elf  
- Use `range(elf, elf*50 + 1, elf)` and add `11 × elf_number`  
- Return the first house where total presents >= input  