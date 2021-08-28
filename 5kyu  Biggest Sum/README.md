https://www.codewars.com/kata/5741df13077bdf57af00109c

Description:
You have to find maximum sum of numbers from top left corner of a matrix to bottom right corner.
You can only go down or right.

Input data
    Matrix will be square M x M, 4 ≤ M ≤ 60
    Matrix will have only positive integers N.
    10 ≤ N ≤ 200

Example

matrix = [[20, 20, 10, 10],
          [10, 20, 10, 10],
          [10, 20, 20, 20],
          [10, 10, 10, 20]]

Solution
``` S: start E: end matrix = [[S, ↓, -, -], [-, ↓, -, -], [-, →, →, ↓], [-, -, -, E]]
matrix = [[20, 20, , ], [, 20, , ], [, 20, 20, 20], [, , , 20]]

Top Left Corner, Right, Down, Down, Right, Right, Bottom Right Corner

20 + 20 + 20 + 20 + 20 + 20 + 20 = 140