# Day 1: Historian Hysteria

## Problem Statement

The Chief Historian is missing, and a group of Senior Historians is searching for him. They have discovered two lists of historically significant locations in his office, but the lists are not identical. To reconcile these lists, you need to calculate the total "distance" between the two lists.

### Task

To determine the total distance:
1. Pair up numbers from the two lists:
   - Pair the smallest number in the left list with the smallest in the right list.
   - Continue pairing the next smallest numbers in each list until all numbers are paired.
2. Calculate the "distance" for each pair as the absolute difference between the two numbers.
3. Sum up all the distances to find the total distance.

For example, given the lists:
```
3   4
4   3
2   5
1   3
3   9
3   3
```
The pairs and distances would be:

- Pair (1, 3): Distance = 2
- Pair (2, 3): Distance = 1
- Pair (3, 3): Distance = 0
- Pair (3, 4): Distance = 1
- Pair (3, 5): Distance = 2
- Pair (4, 9): Distance = 5

**Total Distance**: 2 + 1 + 0 + 1 + 2 + 5 = 11.

Your task is to write a program to calculate the total distance for given lists of numbers.

---