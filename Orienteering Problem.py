import math
import numpy as np
import matplotlib.pyplot as plt


# Read instance file
def read_instance(filename):
    """
    Reads an Orienteering Problem instance.

    File format:
        Line 1: T_max  P
        Next lines: x  y  score

    Returns:
        T_max (float)
        P (float)
        nodes (list of [x, y, score])
    """
    data = []
    with open(filename, "r") as file:
        for line in file:
            vals = [float(v) for v in line.split()]
            data.append(vals)

    T_max = data[0][0]
    P = data[0][1]
    nodes = data[1:]
    return T_max, P, nodes


# Euclidean distance + matrix
def euclidean(p, q):
    return math.dist((p[0], p[1]), (q[0], q[1]))


def build_distance_matrix(nodes):
    """Create an NxN matrix of pairwise Euclidean distances."""
    n = len(nodes)
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist[i][j] = euclidean(nodes[i], nodes[j])
    return dist


# Greedy score/distance heuristic
def greedy_orienteering(T_max, nodes, distances):
    """
    Simple greedy Orienteering heuristic:

    Start at node 0.
    At each step, choose the unvisited node with the highest score/distance ratio.
    Stop when moving to the next node would exceed T_max.

    Returns:
        path          – visited node indices in order
        total_dist    – total travelled distance
        total_score   – sum of scores collected
    """
    n = len(nodes)
    current = 0

    visited = {current}
    path = [current]

    total_dist = 0.0
    total_score = nodes[current][2]

    while True:
        best_ratio = -math.inf
        best_node = None
        best_d = None

        # try all possible next nodes
        for j in range(n):
            if j in visited:
                continue
            d = distances[current][j]
            if d == 0:
                continue

            ratio = nodes[j][2] / d
            if ratio > best_ratio:
                best_ratio = ratio
                best_node = j
                best_d = d

        # no candidates left
        if best_node is None:
            break

        # check budget
        if total_dist + best_d > T_max:
            break

        # move to next node
        total_dist += best_d
        total_score += nodes[best_node][2]

        path.append(best_node)
        visited.add(best_node)
        current = best_node

    return path, total_dist, total_score


# Load data and run algorithm
FILENAME = "test.txt"

T_max, P, nodes = read_instance(FILENAME)
dist_matrix = build_distance_matrix(nodes)

path, dist_used, score_collected = greedy_orienteering(T_max, nodes, dist_matrix)

# Results
print("\n*** Greedy score/distance heuristic ***")
print("Distance:", dist_used)
print("Total Score:", score_collected)
print("Path (indices):", " ".join(map(str, path)))
print("\n" + "#" * 80 + "\n")

# Plot the path
xs = [p[0] for p in nodes]
ys = [p[1] for p in nodes]

path_x = [xs[i] for i in path]
path_y = [ys[i] for i in path]

# Label nodes in order
for i, idx in enumerate(path):
    plt.text(path_x[i], path_y[i], str(idx), ha="center", va="bottom", color="black")

plt.plot(path_x, path_y, linestyle="dashed", linewidth=2, marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Orienteering – Greedy Score/Distance Heuristic")
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.gca().set_aspect("equal", adjustable="box")
plt.show()

