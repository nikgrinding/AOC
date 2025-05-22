## Part 1

We are given a list of 500 "Aunt Sue" descriptions, each with a few known properties like "cats", "trees", etc. The MFCSAM machine has scanned the gift and tells us the *exact* number of several compounds. We need to find the Aunt Sue whose known properties exactly match the scanned values for all the compounds she has listed.

Each Aunt has only a few known compounds, and missing properties should be ignored. The goal is to find the only Aunt whose known traits fully match the machine's output.

### Idea
Parse the MFCSAM data into a dictionary. Then for each Aunt, compare only the properties she lists with the MFCSAM data and find the one that matches exactly.

## Part 2

Now we update the matching logic:
- For "cats" and "trees", the Aunt must have *more than* the number given by MFCSAM
- For "pomeranians" and "goldfish", the Aunt must have *less than* the number given
- All other properties must still match exactly

The rest of the logic stays the same: find the Aunt who fits the updated conditions.

### Idea
Parse and match as before, but use conditional logic based on the property name:
- Use `>` for cats and trees
- Use `<` for pomeranians and goldfish
- Use `==` for everything else