# --- Day 17: Chronospatial Computer ---

The Historians push the button on their strange device, but this time, you all just feel like you're falling.

"Situation critical", the device announces in a familiar voice. "Bootstrapping process failed. Initializing debugger...."

The small handheld device suddenly unfolds into an entire computer! The Historians look around nervously before one of them tosses it to you.

This seems to be a **3-bit computer**: its program is a list of 3-bit numbers (0 through 7), like `0,1,2,3`. The computer also has **three registers** named **A**, **B**, and **C**, but these registers aren't limited to 3 bits and can instead hold any integer.

The computer knows **eight instructions**, each identified by a 3-bit number (called the instruction's **opcode**). Each instruction also reads the 3-bit number after it as an input; this is called its **operand**.

A number called the **instruction pointer** identifies the position in the program from which the next opcode will be read; it starts at 0, pointing at the first 3-bit number in the program. Except for jump instructions, the instruction pointer increases by 2 after each instruction is processed (to move past the instruction's opcode and its operand). If the computer tries to read an opcode past the end of the program, it instead halts.

So, the program `0,1,2,3` would run the instruction whose opcode is **0** and pass it the operand **1**, then run the instruction having opcode **2** and pass it the operand **3**, then halt.

---

## **Combo Operands**

There are two types of operands; each instruction specifies the type of its operand. 

- The value of a **literal operand** is the operand itself.  
  Example: The value of the literal operand **7** is the number **7**.  
- The value of a **combo operand** can be found as follows:  

| Combo Operand | Value Representation          |
|---------------|--------------------------------|
| 0 through 3   | Literal values 0 through 3    |
| 4             | Value of register A           |
| 5             | Value of register B           |
| 6             | Value of register C           |
| 7             | Reserved (will not appear)    |

---

## **The Eight Instructions**

The eight instructions are as follows:

1. **adv** (opcode 0): Performs division.  
   - **Numerator**: The value in register A.  
   - **Denominator**: `2` raised to the power of the combo operand.  
   - The result is truncated to an integer and written back to **register A**.  
   Example: An operand of **2** divides A by **4** (2^2).

2. **bxl** (opcode 1): Calculates the **bitwise XOR** of register **B** and the instruction's **literal operand**, then stores the result in register **B**.

3. **bst** (opcode 2): Calculates the value of its combo operand modulo 8 (keeping the lowest 3 bits), then writes that value to **register B**.

4. **jnz** (opcode 3):  
   - If **A** is 0: Do nothing.  
   - If **A** is not 0: Jump to the value of the **literal operand** (sets the instruction pointer).

5. **bxc** (opcode 4): Calculates the **bitwise XOR** of register **B** and **register C**, then stores the result in **register B**.  
   _(This instruction reads an operand but ignores it.)_

6. **out** (opcode 5): Calculates the value of its combo operand modulo 8, then **outputs** that value.  
   _(If a program outputs multiple values, they are separated by commas.)_

7. **bdv** (opcode 6): Works like **adv** but stores the result in register **B**.  
   _(Numerator still comes from register A.)_

8. **cdv** (opcode 7): Works like **adv** but stores the result in register **C**.  
   _(Numerator still comes from register A.)_

---

## **Examples of Instruction Operation**

- If **register C** contains `9`, the program `2,6` would set **register B** to `1`.
- If **register A** contains `10`, the program `5,0,5,1,5,4` would output `0,1,2`.
- If **register A** contains `2024`, the program `0,1,5,4,3,0` would output `4,2,5,6,7,7,7,7,3,1,0` and leave `0` in register A.
- If **register B** contains `29`, the program `1,7` would set **register B** to `26`.
- If **register B** contains `2024` and **register C** contains `43690`, the program `4,0` would set **register B** to `44354`.

---

## **Input Example**

Given the debugger output:

```plaintext
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
```


Your first task is to determine what the program is trying to output. To do this, initialize the registers to the given values, then run the given program, collecting any output produced by out instructions. (Always join the values produced by out instructions with commas.) After the above program halts, its final output will be **4,6,3,5,6,3,5,2,1,0**

Using the information provided by the debugger, initialize the registers to the given values, then run the program. Once it halts, what do you get if you use commas to join the values it output into a single string?