# --- Part Two ---

The lanternfish use your information to find a safe moment to swim in and turn off the malfunctioning robot! Just as they start preparing a festival in your honor, reports start coming in that a second warehouse's robot is also malfunctioning.

This warehouse's layout is surprisingly similar to the one you just helped with. However, there is one key difference: everything except the robot is **twice as wide**! The robot's list of movements doesn't change.

To get the wider warehouse's map, start with your original map and, for each tile, make the following transformations:

- If the tile is `#`, the new map contains `##`.
- If the tile is `O`, the new map contains `[]`.
- If the tile is `.`, the new map contains `..`.
- If the tile is `@`, the new map contains `@.`.

This transformation produces a new warehouse map that is twice as wide, with wide boxes represented by `[]`. (The robot does not change size.)

For example, the larger version of the previous warehouse would look like this:

```
####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################
```

Because the boxes are now twice as wide but the robot remains the same size and speed, the robot can now push **two boxes at once** if they are aligned horizontally or vertically. 

Consider this situation:

```
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
```


The robot's movements are: `<vv<<^^<<^^`. After resizing the warehouse and simulating the robot's movements, the robot pushes the boxes as follows:

### Initial State (resized map):

```
Initial state:
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############

Move <:
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############

Move ^:
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############
```

This warehouse uses **GPS coordinates** to locate the boxes. For the larger boxes (`[]`), distances are measured from the **edge of the map** to the **closest edge of the box**. 

For example, consider the following box in the map:

```
##########
##...[]...
##........
```

- The box is **1 unit from the top edge**.
- The box is **5 units from the left edge**.

In this example, the GPS coordinate is `100 * 1 + 5 = 105`.

In the scaled-up version of the larger example from above, after the robot has finished all of its moves, the warehouse would look like this:

```
####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
```

The sum of these boxes' GPS coordinates is **9021**.

Predict the motion of the robot and boxes in this new, scaled-up warehouse. What is the sum of all boxes' final GPS coordinates?