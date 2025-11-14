> [!CAUTION]
> This repository is for viewing only. Do not work on the assignment using this repository -- the actual course assignments will be provided to you via Pawtograder.

# Homework 9

## Learning Outcomes

- Minimum Spanning Trees and Union-Find
- The Model-View-Controller paradigm
- Iterator
- Working with an existing codebase

This assignment involves animating the construction of a minimum spanning tree to connect public transportation stations using train tracks.

The learning outcomes are:

- building minimum spanning trees with Kruskal's Algorithm
- implementing the Iterator interface
- detecting and reporting risky concurrency (modifying something while iterating over it)
- analyzing dataset choices with regards to ethics, privacy, and social bias

## A note about BART

We love BART and public transportation, which is why it is the theme of this assignment. But, as we are doing an assignment about "efficient" BART tracks, we must also acknowledge the racist history of those BART tracks when they were built in Oakland.

Here are two articles about the location of the West Oakland BART, which was chosen to disrupt vibrant Black communities: [OaklandVoices](https://oaklandvoices.us/2024/08/05/talk-of-the-town-imagine-west-oakland-before-bart-post-office/#:~:text=In%20the%201950s%20and%201960s%2C%20the%20various,the%20Acorn%20towers%20and%20other%20housing%20projects.) and [TheMetropole](https://themetropole.blog/2024/09/12/bart-disconnects-the-san-francisco-bay-area/#:~:text=BART's%20plans%20especially%20impacted%20West,around%20to%20reap%20these%20benefits.)

As you can see, it is important for us to consider multiple stakeholders when deciding where to build public infrastructure. Please feel free to contribute to this discussion further on our course messaging board.

## Setup

As always, you should commit often (at least once per milestone below) and regularly push to github.

The `main()` function is in `main.py`. When you run the program, you should see this visualization of the station locations:

<img width="796" height="824" alt="Blue dots in locations of stations" src="https://github.com/user-attachments/assets/9d230ad3-2c07-4fa2-b56a-8ce3f0b0af88" />


## Milestone 1: Build and Display Graph for BART (Oakland's public transportation)

Complete the method `_make_graph(self)` in `StationMap` (in `station_map.py`). The implementation steps are written as comments in the file. It reads in stations from a file and builds a graph with a node for every station. Note that there is a constant `NUM_STATIONS` that you can modify, which may be helpful for debugging.

Complete this method by adding edges connecting each pair of nodes. The weight of the edge should be the distance in miles between their stations. Use the provided helper method, `_distance_in_miles()`. Because the edges are undirected, you should add only one edge between each pair of nodes. Do not make an edge between a node and itself.

After completing the milestone, you should see this when you run the program (from `main.py`) with a value of 5 for `NUM_STATIONS` in `StationMap`:

<img width="795" height="828" alt="Blue dots with green lines" src="https://github.com/user-attachments/assets/7f942a03-6e8a-45fd-a752-a6e325b49974" />


## Milestone 2: Build and Display the Minimum Spanning Tree for BART

This milestone is about the iterator, which is in the `class KruskalIterator` in `graph.py`:

Specifically, you will need to replace the stub implementation of the `class KruskalIterator` with an implementation that provides the edges selected by Kruskal's Algorithm. The necessary data structures are specified in the constructor.

You will also need to implement `find` and `union` in the `Node` class above (in `graph.py`).

In `KruskalIterator`, we suggest pre-computing the first edge in the constructor, and storing it in an instance variable so it is available (or null) when `__next__()` is called. Similarly, before returning the value in `__next__()`, compute and store the next edge.

You should raise a `RuntimeError` if, after the iterator is created, (1) the outer graph is modified and (2) `__next__()` is called.

Once you have completed this part, when you run the program from `main.py`, the MST of the graph will be displayed. Here is what a graph of 5 stations should look like:

<img width="796" height="822" alt="Map of five stations with four edges highlighted" src="https://github.com/user-attachments/assets/6744f346-aa39-43af-a4ca-86e34a8e360b" />


The output should be: The minimum spanning tree has 4 edges and is 70 miles long. It is possible you will get a value slightly different from 70 miles due to rounding.

For the final test of your code, set `NUM_STATIONS` in `StationMap` to -1. Record the output sentence in `Summary.md`.

You may want to modify the value of the constant `PAUSE_BETWEEN_EDGE_HIGHLIGHTING_MS` in `main.py` to make the updates faster or slower.

## Milestone 3: Display the Minimum Spanning Tree for the T (Boston's public transportation)

For this milestone, you will need to find the places in the codebase to properly display a minimum spanning tree for Boston's public transportation (the T).
- Just as the data for BART is in `data/BART.csv`, the data for the T is in `data/T.csv`. It was scraped from [wikipedia.org](https://en.wikipedia.org/wiki/List_of_MBTA_subway_stations).
- In order to make the display show the correct range of coordinates, you will need to change `MAX_LATITUDE`, `MIN_LATITUDE`, `MAX_LONGITUDE`, and `MIN_LONGITUDE` in `map_graphics.py`.

## Optional Milestones

If you want, you can:

- add other "stations"
- improve the GUI
- load information cities or transit locations from other parts of the world (which would require changing at least the constants `MIN_LATITUDE` and `MAX_LATITUDE` in `MapGraphics`)
- add [path compression](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) to the union-find implementation

Optional milestones should be made in a separate branch. One place you can learn about git branching is through the first two lessons in the Introduction Sequence at [Learn Git Branching](https://learngitbranching.js.org/):

1. Introduction to Git Commits
2. Branching in Git

