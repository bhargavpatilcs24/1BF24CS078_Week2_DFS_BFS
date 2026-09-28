from collections import deque
GOAL_STATE = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)
START_STATE = (
    (0, 1, 3),
    (8, 2, 4),
    (7, 6, 5)
)

def get_blank_position(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c


def get_neighbors(state):
    r, c = get_blank_position(state)
    neighbors = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        new_r, new_c = r + dr, c + dc
        
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            state_list = [list(row) for row in state]
            state_list[r][c], state_list[new_r][new_c] = state_list[new_r][new_c], state_list[r][c]
            neighbors.append(tuple(tuple(row) for row in state_list))
            
    return neighbors


def solve_bfs(start_state, goal_state):
    if start_state[1][1] == 0:
        raise ValueError("Initial state blank tile (0) must NOT be at center (1, 1).")
    
    if goal_state[1][1] != 0:
        raise ValueError("Goal state blank tile (0) must be at center (1, 1).")

    queue = deque([(start_state, [start_state])])
    visited = {start_state}

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


def solve_dfs(start_state, goal_state, max_depth=20):
    if start_state[1][1] == 0:
        raise ValueError("Initial state blank tile (0) must NOT be at center (1, 1).")

    if goal_state[1][1] != 0:
        raise ValueError("Goal state blank tile (0) must be at center (1, 1).")

    stack = [(start_state, [start_state], 0)]
    visited = set()

    while stack:
        current_state, path, depth = stack.pop()

        if current_state == goal_state:
            return path

        if current_state not in visited:
            visited.add(current_state)

            if depth < max_depth:
                for neighbor in get_neighbors(current_state):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor], depth + 1))

    return None


def print_board(state):
    """Helper function to format and display a 3x3 board state."""
    for row in state:
        print(" ".join(str(tile) if tile != 0 else "_" for tile in row))
    print()


if __name__ == "__main__":
    print("Initial State (Blank at Top-Left [0,0]):")
    print_board(START_STATE)

    print("Goal State (Blank at Center [1,1]):")
    print_board(GOAL_STATE)

    bfs_solution = solve_bfs(START_STATE, GOAL_STATE)
    if bfs_solution:
        print(f"--- BFS Solution Found in {len(bfs_solution) - 1} moves ---")
        for step, state in enumerate(bfs_solution):
            print(f"Step {step}:")
            print_board(state)
    else:
        print("BFS: No solution found.")

    dfs_solution = solve_dfs(START_STATE, GOAL_STATE, max_depth=15)
    if dfs_solution:
        print(f"--- DFS Solution Found in {len(dfs_solution) - 1} moves ---")
        for step, state in enumerate(dfs_solution):
            print(f"Step {step}:")
            print_board(state)
    else:
        print("DFS: No solution found within max depth limit.")