# Orienteering Problem

This project solves the Orienteering Problem using a greedy score-to-distance heuristic.

## Introduction
The Orienteering Problem is an optimisation problem where the goal is to select a path
that maximises the total score collected from visiting different locations (control points),
while ensuring the total travel distance does not exceed a given time/distance budget.
Each point has an associated score, and distances are computed using the Euclidean metric.

This problem appears in routing, logistics, tourism planning, and recreational orienteering.

## Instance Format
The first line contains:
- `Tmax  P`
  - `Tmax` = travel budget
  - `P` = number of paths (always 1)

Each remaining line contains:
- `x  y  s`
  - `x` = x-coordinate
  - `y` = y-coordinate
  - `s` = score of the point

**Remarks**
1. The first point is the starting point.
2. Euclidean distance is used.
3. The objective is to collect the maximum score without exceeding `Tmax`.

## Description
This project implements a greedy score/distance heuristic:
- Start from the first point.
- Repeatedly select the unvisited point with the highest score-to-distance ratio.
- Add it to the path if it does not violate the distance budget.
- Continue until no further points can be visited.

The program prints total distance, total score, and the visited node indices.
A plot of the final path is also generated.
