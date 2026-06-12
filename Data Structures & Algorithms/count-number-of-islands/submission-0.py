class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        q = deque()
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    q.append((r, c))
                    visited.add((r, c))
                    while q:
                        row, col = q.popleft()
                        directions = [(1,0), (-1,0), (0,1), (0,-1)]

                        for dr, dc in directions:
                            checkR , checkC = row + dr, col + dc

                            if (
                                checkR in range(rows) and
                                checkC in range(cols) and
                                grid[checkR][checkC] == "1" and
                                (checkR, checkC) not in visited
                            ):
                                visited.add((checkR, checkC))
                                q.append((checkR, checkC))


        return islands
                    
                                


                        