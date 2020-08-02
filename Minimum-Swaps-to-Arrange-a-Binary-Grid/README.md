[Problem statement](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/)

Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

 

**Example 1:**

<div>
<img src="example.jpg" width="500"/>
</div>

Input: grid = `[[0,0,1],[1,1,0],[1,0,0]]`<br> Output: 3<br>


**Example 2:**

Input: grid = `[[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]`<br> Output:
-1<br> Explanation: All rows are similar, swaps have no effect on the
grid.<br>


**Example 3:**


Input: grid = `[[1,0,0],[1,1,0],[1,1,1]]`<br> Output: 0
 

**Constraints:**

`n == grid.length`<br> `n == grid[i].length`<br> `1 <= n <= 200`<br>
`grid[i][j] is 0 or 1`<br>