""" "Module for creating a graph representation of BART stations."""

import math
import sys

sys.path.append(".")

from src.graph import Graph
from src.station import Station


class StationMap:
    """Graph representation of BART stations built from CSV data."""

    # Constants
    STATION_DATA_FILE = "data/BART.csv"
    NUM_DATA_FIELDS = 4
    STATION_NAME_FIELD = 0
    LATITUDE_FIELD = 2
    LONGITUDE_FIELD = 3

    NUM_STATIONS = -1  # BART has 100. T has 152. When set to -1, all data is used

    EARTH_RADIUS_IN_MILES = 3963

    def __init__(self) -> None:
        self.graph: Graph[Station] = Graph()
        self._make_graph()

    @staticmethod
    def _distance_in_miles(station1: Station, station2: Station) -> float:
        """
        Calculate the distance between two stations using the great circle formula.
        """
        lat1_rad = math.radians(station1.latitude)
        lat2_rad = math.radians(station2.latitude)

        unit_sphere = (math.sin(lat1_rad) * math.sin(lat2_rad)) + (
            math.cos(lat1_rad)
            * math.cos(lat2_rad)
            * math.cos(math.radians(station2.longitude - station1.longitude))
        )
        clamped_value = max(-1, min(1, unit_sphere))
        return StationMap.EARTH_RADIUS_IN_MILES * math.acos(clamped_value)

    def _read_data_from_file(self) -> list[str]:
        """Read station data from CSV file."""
        with open(self.STATION_DATA_FILE, "r", encoding="utf-8") as file:
            return file.readlines()

    def _make_graph(self) -> None:
        """
        Complete this method to build the graph.

        Done for you:
        1. Read data from the CSV file
        2. Parse each line to create Station objects and add them as nodes

        Steps for students to do:
        3. Add edges connecting each pair of nodes with weight as distance in miles
        4. Use the _distance_in_miles helper method
        5. Since edges are undirected, add only one edge between each pair
        6. Do not add edges between a node and itself

        CSV format: station_name,station_id,longitude,latitude
        """
        lines: list[str] = self._read_data_from_file()
        num_stations = 0

        for line in lines:
            num_stations += 1
            if self.NUM_STATIONS != -1 and num_stations > self.NUM_STATIONS:
                break
            fields: list[str] = line.split(sep=",")
            if len(fields) == self.NUM_DATA_FIELDS:
                station = Station(
                    fields[self.STATION_NAME_FIELD],
                    float(fields[self.LATITUDE_FIELD]),
                    float(fields[self.LONGITUDE_FIELD]),
                )
                self.graph.add_node(station)
            else:
                raise ValueError(f"Unable to parse line: {line}")

        # TODO: Complete this method by adding edges connecting each pair of nodes.
        # The weight of the edge should be the distance in miles between their
        # cities. Use the provided helper method. Because the edges are
        # undirected, you should add only one edge between each pair of nodes.
        # Do not make an edge between a node and itself.
