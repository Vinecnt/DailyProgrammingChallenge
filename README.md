# DailyProgrammingChallenge
4-27-2017: Intermediate
- Task: From a given int, find the next largest int 
- Tools Use: Arrays slicing, recursion
- Status: failing on int greater than 4 digits
- Notes: Use functional programming when involving numeric functions


8-23-2017: Intermediate - Pyramid Sliding
https://www.reddit.com/r/dailyprogrammer/comments/6vi9ro/170823_challenge_328_intermediate_pyramid_sliding/
- Task: Similar to Project Euler 67, find the quickest path(shortest sum path) down a pyramid of numbers.
- Tools: Numpy, file reader, recursion, depth-first search
- Status: DFS quite ineffcient method, yet to have implement the efficient version
- Notes:
  - Effecient Method: remove the largest number from the bottom row, sum upward to make a new row, repeat until one number left, which is       your shortest sum
  - The reasoning is that with n nodes on the bottom of the pyramid, there would be n-1 parents for that bottom row. Therefore, there would exist a parent with two child nodes that includes some node and the other node being the largest node. The shortest path would never take that largest node, so we discard. Now that there are n-1 child nodes and n-1 parents, we can sum upward, and repeat until 1 node is left which would represent the sum of the shortest path
