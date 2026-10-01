class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[-1]*cols for _ in range(rows)]
        islands = 0
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        

        for i in range(rows):
            for j in range(cols):
                if visited[i][j] > -1: #already seen this square in a search
                    continue
                if grid[i][j] == '0': #water
                    visited[i][j] = 0
                else:
                    islands += 1
                    print(islands)
                    current_island = deque()
                    current_island.append((i,j))
                    visited[i][j] = 1
                    while len(current_island)>0:
                        r,c = current_island.popleft()
                        if grid[r][c] == '0':#water
                            visited[r][c] = 0
                            continue
                        visited[r][c] = islands
                        for d in DIRS:
                            a, b = r+d[0], c+d[1]
                            if a < 0 or b < 0 or a >= rows or b >= cols:
                                continue
                            if visited[a][b] > -1:
                                continue
                            visited[a][b] = 1
                            current_island.append((a, b))
        # print(visited)
        # print(grid)
        return islands
                    




        


        
        