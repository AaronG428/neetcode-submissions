

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = [[0]*cols for _ in range(rows)]

        max_area = 0
        
        DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if seen[r][c]:
                    continue
                else:
                    seen[r][c] = 1
                    if grid[r][c] == 0:
                        continue
                    current_island = deque()
                    area = 0
                    current_island.append((r,c))
                    while len(current_island) > 0:
                        (a, b) = current_island.popleft()
                        area += 1
                        for d in DIRS:
                            r1, c1 = a+d[0], b+d[1]
                            if r1 < 0 or c1 < 0 or r1 >= rows or c1 >= cols or seen[r1][c1]:
                                continue
                            seen[r1][c1] = 1
                            if grid[r1][c1] == 1:
                                current_island.append((r1, c1))
                    if area > max_area:
                        max_area = area
        return max_area