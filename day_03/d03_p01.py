def get_point_ranges(wire):
    """Returns the points of the wire."""
    x, y, points = 0, 0, []
    for (direction, steps) in wire:
        if direction == 'L':
            points.extend([(x1, y) for x1 in range(x - steps, x + 1)])
            x -= steps
        elif direction == 'R':
            points.extend([(x1, y) for x1 in range(x, x + steps + 1)])
            x += steps
        elif direction == 'U':
            points.extend([(x, y1) for y1 in range(y, y + steps + 1)])
            y += steps
        elif direction == 'D':
            points.extend([(x, y1) for y1 in range(y - steps, y + 1)])
            y -= steps
    return set(points)


def manhattan_distance(point_1, point_2=(0, 0)):
    """Return the Manhattan distance of the points."""
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


# Read input from file
with open('d03.txt') as f:
    lines = f.read().splitlines()
    wire_1 = list(map(lambda x: (x[0], int(x[1:])), lines[0].strip().split(',')))
    wire_2 = list(map(lambda x: (x[0], int(x[1:])), lines[1].strip().split(',')))

# Taking (0, 0) as starting points find coordinates
points_1 = get_point_ranges(wire_1)
points_1.remove((0, 0))
points_2 = get_point_ranges(wire_2)
points_2.remove((0, 0))
common_points = list(points_1.intersection(points_2))
manhattan_distances = list(map(manhattan_distance, common_points))
print(min(manhattan_distances))
