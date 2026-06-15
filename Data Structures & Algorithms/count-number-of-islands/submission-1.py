class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        q = deque()
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        for r in range(rows):
            for c in range (cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    q.append((r,c))
                    visited.add((r,c))
                    while q:
                        currRow, currCol = q.popleft()

                        ## curr row is within bounds
                        ## curr col is within bounds
                        ## curr row col is 1
                        ## neighboirs not invisited 

                        for dr, dc in directions:
                            newRow = currRow + dr
                            newCol = currCol + dc

                            if (
                                0 <= newRow < rows and
                                0 <= newCol < cols and
                                grid[newRow][newCol] == "1" and
                                (newRow, newCol) not in visited
                            ):
                                                            
                                visited.add((newRow, newCol))
                                q.append((newRow,newCol))

        return islands


                        
              
                        
                        



                    
                                


                        