# --- Part Two ---

### Problem Summary:
We are tasked with handling corrupted memory that contains both `mul()` instructions and new instructions, `do()` and `don't()`, which control whether the `mul()` instructions are enabled or disabled.

- **`do()`**: Enables future `mul()` instructions.
- **`don't()`**: Disables future `mul()` instructions.
- At the start of the program, `mul()` instructions are enabled by default.
  
### Example Input:
```plaintext
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
```

This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2x4 + 8x5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?