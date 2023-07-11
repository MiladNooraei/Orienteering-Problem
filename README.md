
# Orienteering Problem

Using two Algorithms (Dynamic Programming, Floyd Warshall) to solve Orienteering Problem
## Introduction
The Orienteering Problem is a type of optimization problem that involves finding the
shortest possible route between a set of locations (often referred to as ”control points”)
while visiting each location only once. The goal is to maximize the total score obtained
by visiting these locations, where each location has a different score associated with it.

The problem is often encountered in the field of operations research, and has many
real-world applications, such as in logistics, transportation planning, and even in recreational
activities like hiking and orienteering.

## Instance format
The first line contains the following data:
- Tmax P
where:
- Tmax = available time budget per path
- P = number of paths (=1)
The remaining lines contain the data of each point. For each point, the line contains the following data:
- x y s
where:
- x = x coordinate
- y = y coordinate
- s = score
*REMARKS*
1. The first point is the starting point.
2. The second point is the ending point.
3. The Euclidean distance is used.

## Description

In this project, Orienteering Problem was solved using 2 Algorithms: 
1. Dynamic Programming
2. Floyd Warshall

    The output in terminal is number of node and shows the path and at last the graph and path is plotted.
