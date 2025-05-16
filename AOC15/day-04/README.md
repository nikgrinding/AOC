## Part 1

Santa wants to give out digital gifts using a fictional cryptocurrency called **AdventCoins**. To "mine" these coins, we need to solve a hash puzzle using the **MD5 algorithm**.

We are given a **secret key**. To successfully mine an AdventCoin, we must find the **smallest positive integer** that, when appended to the secret key and hashed with **MD5**, results in a hexadecimal string that **starts with five zeroes**.

**Examples:**

- Input: `abcdef` → Output: `609043` (because the MD5 hash of `abcdef609043` starts with five zeroes `000001dbbfa...`)
- Input: `pqrstuv` → Output: `1048970`

### Idea

We can use the built-in MD5 hashing algorithm in the `hashlib` library for hashing. Initially, we start with a variable set to `0`, append it to the given input, and check if the hashed value starts with five zeroes. If it does, we return the variable; otherwise, we increment it until we get such a hash.

## Part 2

We are given a **secret key**. To successfully mine an AdventCoin, we must find the **smallest positive integer** that, when appended to the secret key and hashed with **MD5**, results in a hexadecimal string that **starts with six zeroes**.

### Idea

We use the same logic as in the previous part, but here we check if the hash starts with **six** zeroes instead.