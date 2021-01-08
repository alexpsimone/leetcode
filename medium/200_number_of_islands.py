def num_islands_all_in_one_func(grid) -> int:

  num_rows = len(grid)
  num_cols = len(grid[0])
  num_islands = 0
  
  # put all island vertices in the grid in a list of vertices to see  
  unseen_land_vertices = set((x,y) for x in range(num_rows) for y in range(num_cols) if grid[x][y] == '1')
  
  # look until you've visited all land vertices
  while unseen_land_vertices:

    # take an item from the unseen land vertices and use it as a starting point for the BFS
    start_point = unseen_land_vertices.pop()
    seen_vertices = set([start_point])
    to_see = [start_point]

    while to_see:

      # do a BFS from the vertex, looking at any points around it
      x, y = to_see.pop(0)

      for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:

        new_x, new_y = x + dx, y + dy

        # only look at nodes in the grid that are "land", and ones which haven't been looked at before
        if 0 <= new_x < num_rows and 0 <= new_y < num_cols and (new_x, new_y) not in seen_vertices and grid[new_x][new_y] == '1':
          
          to_see.append((new_x, new_y))
          seen_vertices.add((new_x, new_y))
          unseen_land_vertices.remove((new_x, new_y))
    
    # when you run out of vertices to see, you've reached the end of the connected component/island
    num_islands += 1

  return num_islands


def breadth_first_search(grid, num_rows, num_cols, unseen_land_vertices):
  
  start_point = unseen_land_vertices.pop()
  seen_vertices = set([start_point])
  to_see = [start_point]

  while to_see:

    # do a BFS from the vertex, looking at any points around it
    x, y = to_see.pop(0)

    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:

      new_x, new_y = x + dx, y + dy

      # only look at nodes in the grid that are "land", and ones which haven't been looked at before
      if 0 <= new_x < num_rows and 0 <= new_y < num_cols and (new_x, new_y) not in seen_vertices and grid[new_x][new_y] == '1':
        
        to_see.append((new_x, new_y))
        seen_vertices.add((new_x, new_y))
        unseen_land_vertices.remove((new_x, new_y))


def num_islands_w_sub_func(grid) -> int:
  
  num_rows = len(grid)
  num_cols = len(grid[0])
  num_islands = 0

  unseen_land_vertices = set((x,y) for x in range(num_rows) for y in range(num_cols) if grid[x][y] == '1')

  while unseen_land_vertices:

    breadth_first_search(grid, num_rows, num_cols, unseen_land_vertices)
    num_islands += 1

  return num_islands


# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

# grid2 = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]