__name__ = "Ali Etemadfard, Milad Nooraei" 
__email__ = "alietemadfard@gmail.com, miladnooraiy0@gmail.com"

#Importing libraries
import math
import numpy as np
import matplotlib.pyplot as plt

#Finding node number for output
def find_index_2d(lst, target):
    for i, sublist in enumerate(lst):
        if sublist == target:
            return i

#Finding distance of next node
def distance_node(node, data_array):
    global T_max
    global sum_distance
    global full_data_array
    global path
    global sum_score

    distance_list = []
    current_node = [node[0], node[1]]

    for i in data_array:
        next_node = [i[0], i[1]]
        distance_list += [i[2] / math.dist(current_node, next_node)]

    for i in range(len(data_array)):
        if distance_list[i] == max(distance_list):
            index = i
            break
    
    next_node = data_array[index]
    sum_distance += math.dist(current_node, [next_node[0], next_node[1]])

    if sum_distance > T_max:
        sum_distance -= math.dist(current_node, [next_node[0], next_node[1]])
        return
    
    sum_score += next_node[2]
    path += str(find_index_2d(full_data_array, next_node)) + " "

    new_node = data_array[index]
    data_array.pop(index)
    
    distance_node(new_node, data_array)

#Example instance data
data_array = []
with open("test.txt", "r") as file:
    for line in file:
        values = line.split()
        values = [float(value) for value in values]
        data_array.append(values)

#Initialize
T_max = data_array[0][0]
P = data_array[0][1]
data_array.pop(0)
sum_distance = 0
sum_score = 0
path = "0 "
full_data_array = data_array.copy()

#Action
distance_node(data_array[0], data_array[1:])

#Printing result
print("\n*** Dijkstra ***")
print("Distance: ", sum_distance)
print("Maximum Score: ", sum_score)
path_list_1 = [int(item) for item in path.split()]
print("Optimal Path: \n", path)

print("\n\n######################################################################################################################\n")

#Finding index of node
def find_index_2d(lst, target):
    for i, sublist in enumerate(lst):
        if sublist == target:
            return i

#Floyd algorithm
def floyd_warshall(data_array):
    n = len(data_array)
    distances = np.zeros((n, n))
    next_nodes = np.zeros((n, n), dtype = int)

    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = math.inf

    for i, data in enumerate(data_array):
        x, y, score = data
        for j, other_data in enumerate(data_array):
            if i != j:
                x_other, y_other, _ = other_data
                dist = math.dist((x, y), (x_other, y_other))
                distances[i][j] = dist

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    next_nodes[i][j] = k

    return distances, next_nodes

def get_optimal_path(next_nodes, start, end):
    if next_nodes[start][end] == 0:
        return []

    path = [start]
    while start != end:
        start = next_nodes[start][end]
        path.append(start)
    return path

#Example instance data
data_array = []
with open("test.txt", "r") as file:
    for line in file:
        values = line.split()
        values = [float(value) for value in values]
        data_array.append(values)

#Initialize
T_max = data_array[0][0]
P = data_array[0][1]
data_array.pop(0)
full_data_array = data_array.copy()

#Action
distances, next_nodes = floyd_warshall(data_array)
start_node = 0
current_node = start_node
#Store the path as a list of integers
path = [start_node]

visited = set()
visited.add(current_node)

sum_distance = 0
sum_score = 0

while len(visited) < len(data_array):
    max_distance_ratio = -math.inf
    next_node = None

    for i, data in enumerate(data_array):
        if i not in visited:
            x, y, score = data
            distance_ratio = score / distances[current_node][i]
            if distance_ratio > max_distance_ratio:
                max_distance_ratio = distance_ratio
                next_node = i

    if next_node is None or sum_distance + distances[current_node][next_node] > T_max:
        break

    sum_distance += distances[current_node][next_node]
    sum_score += data_array[next_node][2]
    #Append the next node to the path
    path.append(next_node)
    current_node = next_node
    visited.add(current_node)

# Printing result
print("*** Floyd Warshall ***")
print("Distance: ", sum_distance)
print("Maximum Score: ", sum_score)
print("Optimal Path: ")
path_list_2 = path
print(" ".join(str(find_index_2d(full_data_array, data_array[node])) for node in path))

print("\n\n######################################################################################################################\n")

################################################    PLOTS   #########################################################

nodes = []
with open("test.txt", "r") as file:
    for line in file:
        values = line.split()
        values = [float(value) for value in values]
        nodes.append(values)

nodes.pop(0)
result = [[sublist[0], sublist[1]] for sublist in nodes]
x_axis_numbers, y_axis_numbers = [], []
for i in result:
    x_axis_numbers += [int(i[0])]
    y_axis_numbers += [int(i[1])]

plot_1_x, plot_1_y = [], []
for i in path_list_1:
    plot_1_x += [x_axis_numbers[i]]
    plot_1_y += [y_axis_numbers[i]]

for i in range(len(path_list_1)):
    plt.text(plot_1_x[i], plot_1_y[i], str(path_list_1[i]), ha = "center", va = "bottom", color = "Black")

plt.plot(plot_1_x, plot_1_y, color = "green", linestyle = "dashed", linewidth = 3, marker = "o", markerfacecolor = "blue", markersize = 12)
plt.ylim(1, 8)
plt.xlim(1, 8)
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Orienteering Problem Dynamic Programming Solution")
plt.show()


plot_2_x, plot_2_y = [], []
for i in path_list_2:
    plot_2_x += [x_axis_numbers[i]]
    plot_2_y += [y_axis_numbers[i]]

for i in range(len(path_list_2)):
    plt.text(plot_2_x[i], plot_2_y[i], str(path_list_2[i]), ha = "center", va = "bottom", color = "Black")

plt.plot(plot_2_x, plot_2_y, color = "green", linestyle = "dashed", linewidth = 3, marker = "o", markerfacecolor = "blue", markersize = 12)
plt.ylim(1, 8)
plt.xlim(1, 8)
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Orienteering Problem Floyd Warshall solution")
plt.show()