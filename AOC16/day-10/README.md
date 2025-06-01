## Part 1

You're given instructions for a network of bots that compare microchips. Each bot holds up to two microchips and gives the lower and higher value chips to other bots or output bins as instructed. You are asked to find which bot is responsible for comparing two specific values.

**Example:**
```
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
```
In this example, bot 2 is responsible for comparing 5 and 2.

### Idea

We first assign values to bots based on the `value` instructions. Then we process the transfer instructions only when a bot has exactly two chips. When this happens, we simulate it giving away the low and high chips as per the rules. If the bot compares the target chip values, we return its number.

## Part 2

Now, you're asked to compute the product of the values in output bins 0, 1, and 2.

### Idea

We simulate the same process as in Part 1, but this time we continue until all instructions are processed. Once done, we retrieve the chip values from the relevant output bins and multiply them to get the final answer.