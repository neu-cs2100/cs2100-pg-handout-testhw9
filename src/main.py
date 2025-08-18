import time
from station_map import StationMap
from map_graphics import MapGraphics


PAUSE_BETWEEN_EDGE_HIGHLIGHTING_MS = 500  # milliseconds


def main() -> None:
    """Main execution method that runs the controller logic"""
    try:
        # Create and draw the graph of the stations.
        map_graphics = MapGraphics.get_instance()
        map = StationMap()
        graph = map.graph
        map_graphics.draw_graph(graph)
        
        # Calculate and display the minimum spanning tree.
        iterator = graph.get_kruskal_iterator()
        num_edges = 0
        total_distance = 0
        
        for edge in iterator:
            map_graphics.highlight_edge(edge)
            num_edges += 1
            total_distance += edge.weight
        
        map_graphics.make_visible()

        print(f"The minimum spanning tree has {num_edges} edges and is {total_distance} miles long.")
        
    except KeyboardInterrupt:
        # Handle interruption gracefully
        print("Process interrupted by user.")
    except IOError as e:
        print(f"There was problem reading the input: {e}")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        raise


if __name__ == "__main__":
    main()
