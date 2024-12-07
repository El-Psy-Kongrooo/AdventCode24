# --- Day 7: Bridge Repair ---

The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and stole all the operators from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).

For example:
```plaintext
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
```

Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

### Example Walkthrough:
- **190: 10 19**
  - Has only one position that accepts an operator: between 10 and 19. 
  - Choosing `+` gives 29, but choosing `*` gives the test value: `10 * 19 = 190`. ✅
- **3267: 81 40 27**
  - Has two positions for operators. 
  - Possible configurations: `(81 + 40) * 27`, `81 + (40 * 27)`, `(81 * 40) + 27`, and `81 * (40 + 27)`. 
  - Two configurations match: `81 + (40 * 27) = 3267` and `(81 * 40) + 27 = 3267`. ✅
- **292: 11 6 16 20**
  - Multiple positions for operators. 
  - The configuration `11 + (6 * 16) + 20` matches: `11 + 96 + 20 = 292`. ✅
- **Other Equations**
  - None of the other equations can be solved with valid operator combinations.

### Calibration Result:
The engineers just need the total calibration result, which is the sum of the test values from the equations that could possibly be true. 

From the above example, the valid test values are:
- 190
- 3267
- 292

Their sum is:

**190 + 3267 + 292 = 3749**

### Task:
Determine which equations could possibly be true. What is their total calibration result?
