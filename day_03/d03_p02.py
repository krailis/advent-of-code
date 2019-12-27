from itertools import groupby


def get_point_steps(wire):
    """Returns the points of the wire."""
    x, y, points = 0, 0, [(0, 0)]
    for (direction, steps) in wire:
        if direction == 'L':
            points.extend([(x1, y) for x1 in range(x, x - steps, -1)])
            x -= steps
        elif direction == 'R':
            points.extend([(x1, y) for x1 in range(x, x + steps)])
            x += steps
        elif direction == 'U':
            points.extend([(x, y1) for y1 in range(y, y + steps)])
            y += steps
        elif direction == 'D':
            points.extend([(x, y1) for y1 in range(y, y - steps, -1)])
            y -= steps
    point_steps, step_count = {}, 0
    for point in [x[0] for x in groupby(points)]:
        if point not in point_steps.keys():
            point_steps[point] = step_count
        step_count += 1
    return point_steps


# Read input from file
with open('d03.txt') as f:
    lines = f.read().splitlines()
    wire_1 = list(map(lambda x: (x[0], int(x[1:])), lines[0].strip().split(',')))
    wire_2 = list(map(lambda x: (x[0], int(x[1:])), lines[1].strip().split(',')))

# Taking (0, 0) as starting points find coordinates
point_steps_1 = get_point_steps(wire_1)
points_1 = set(point_steps_1.keys())
points_1.remove((0, 0))
point_steps_2 = get_point_steps(wire_2)
points_2 = set(point_steps_2.keys())
points_2.remove((0, 0))
common_points = list(points_1.intersection(points_2))
distances = [point_steps_1[p] + point_steps_2[p] for p in common_points]
print(min(distances))
