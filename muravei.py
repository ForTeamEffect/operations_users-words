from collections import deque


def sum_of_digits(n):
    return sum(map(int, str(n)))


def can_enter(x, y):
    return sum_of_digits(x) + sum_of_digits(y) <= 25


def find_cells(start_x, start_y):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set([(start_x, start_y)])
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and can_enter(nx, ny):
                visited.add((nx, ny))
                queue.append((nx, ny))
    return len(visited)


# Начальная позиция муравья
start_position = (1000, 1000)
result = find_cells(*start_position)

print(f"Количество доступных для посещения клеток: {result}")
