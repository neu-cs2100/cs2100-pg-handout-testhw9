import tkinter as tk
import time
from typing import Optional, Any
from graph import Node, Edge, Graph
from station import Station


class TextWithBackgroundColor:
    """Helper class to display text with background color"""
    TEXT_PADDING = 5
    RECTANGLE_HEIGHT = 15

    def __init__(self, canvas: tk.Canvas, x: int, y: int, text: str) -> None:
        self.canvas = canvas
        self.x = x
        self.y = y
        self.text = text
        self.text_id: Optional[int] = None
        self.bg_id: Optional[int] = None

    def show(self) -> None:
        if self.text_id is None:
            # Create background rectangle
            text_width = len(self.text) * 6  # Approximate text width
            self.bg_id = self.canvas.create_rectangle(
                self.x, self.y - self.RECTANGLE_HEIGHT//2,
                self.x + text_width + self.TEXT_PADDING, 
                self.y + self.RECTANGLE_HEIGHT//2,
                fill="yellow", outline=""
            )
            # Create text
            self.text_id = self.canvas.create_text(
                self.x + self.TEXT_PADDING//2, self.y,
                text=self.text, anchor="w", fill="black"
            )

    def hide(self) -> None:
        if self.text_id is not None:
            self.canvas.delete(self.text_id)
            self.canvas.delete(str(self.bg_id))
            self.text_id = None
            self.bg_id = None


class MapGraphics:
    # Constants
    MAX_LATITUDE = 38.1
    MIN_LATITUDE = 37.3
    MAX_LONGITUDE = -121.7
    MIN_LONGITUDE = -122.5
    PIXELS_PER_DEGREE = 1000
    CANVAS_HEIGHT = int(float(MAX_LATITUDE - MIN_LATITUDE) * PIXELS_PER_DEGREE)
    CANVAS_WIDTH = int(float(MAX_LONGITUDE - MIN_LONGITUDE) * PIXELS_PER_DEGREE)
    SCENE_WIDTH = CANVAS_WIDTH
    SCENE_HEIGHT = CANVAS_HEIGHT
    NODE_COLOR = "blue"
    EDGE_COLOR = "lightgreen"
    NODE_HIGHLIGHT_COLOR = "purple"
    EDGE_HIGHLIGHT_COLOR = "purple"
    HOVER_BACKGROUND_COLOR = "yellow"
    NODE_RADIUS = 2
    MIN_DISTANCE_FOR_LINE = 0

    _instance = None
    _initialized = False

    def __init__(self) -> None:
        if MapGraphics._instance is not None:
            raise Exception("This class is a singleton!")
        
        self.root: Optional[tk.Tk] = None
        self.canvas: Optional[tk.Canvas] = None
        MapGraphics._instance = self
        self.start()

    @staticmethod
    def get_instance() -> 'Optional[MapGraphics]':
        """Gets the singleton instance of this class."""
        if not MapGraphics._initialized:
            MapGraphics()
            time.sleep(0.001)  # equivalent to Thread.yield()
        return MapGraphics._instance

    def start(self) -> None:
        """Start the GUI application"""
        self.root = tk.Tk()
        self.root.title("Stations")
        self.root.geometry(f"{self.SCENE_WIDTH}x{self.SCENE_HEIGHT}")
        
        # Create canvas
        self.canvas = tk.Canvas(
            self.root, 
            width=self.CANVAS_WIDTH, 
            height=self.CANVAS_HEIGHT,
            bg="white"
        )
        self.canvas.pack()
        
        MapGraphics._initialized = True

    def draw_node(self, node: Node, radius: Optional[int] = None, color: Optional[str] = None) -> None:
        """Draw a node on the canvas"""
        if radius is None:
            radius = self.NODE_RADIUS
        if color is None:
            color = self.NODE_COLOR
            
        x = self.get_x(node.data)
        if x < 0:
            print(f"Could not display {node.data}")
            return
            
        y = self.get_y(node.data)
        
        def draw() -> None:
            if self.canvas is not None:
                circle_id = self.canvas.create_oval(
                    x - radius, y - radius, x + radius, y + radius,
                    fill=color, outline=color
                )
                # self.add_hover(circle_id, x, y, node.data.name)
        
        if self.root is not None:
            self.root.after(0, draw)

    def add_hover(self, item_id: int, x: int, y: int, text: str) -> None:
        """Add hover functionality to a canvas item"""
        if self.canvas is not None:
            hover_text = TextWithBackgroundColor(self.canvas, x, y, text)
            
            def on_enter(event: Any) -> None:
                hover_text.show()
                
            def on_leave(event: Any) -> None:
                hover_text.hide()
                
            self.canvas.tag_bind(item_id, "<Enter>", on_enter)
            self.canvas.tag_bind(item_id, "<Leave>", on_leave)

    def draw_edge(self, edge: Edge, color: Optional[str] = None, enable_hover: bool = False) -> None:
        """Draw an edge on the canvas"""
        if color is None:
            color = self.EDGE_COLOR
            
        station1 = edge.node1.data
        station2 = edge.node2.data
        
        x1, y1 = self.get_x(station1), self.get_y(station1)
        x2, y2 = self.get_x(station2), self.get_y(station2)
        
        def draw() -> None:
            if self.canvas is not None:
                line_id = self.canvas.create_line(x1, y1, x2, y2, fill=color, width=1)
                
                if enable_hover:
                    mid_x = (x1 + x2) // 2
                    mid_y = (y1 + y2) // 2
                    hover_text = f"{station1.name} - {station2.name} ({edge.weight})"
                    self.add_hover(line_id, mid_x, mid_y, hover_text)
            
        if self.root is not None:
            self.root.after(0, draw)

    def draw_graph(self, graph: Graph) -> None:
        """
        Displays all nodes in the graph and all edges with a weight of at
        least MIN_DISTANCE_FOR_LINE.
        """
        # Draw edges first (so they appear behind nodes)
        for edge in graph.edges:
            if edge.weight >= self.MIN_DISTANCE_FOR_LINE:
                self.draw_edge(edge)
        
        # Draw nodes
        for node in graph.nodes:
            self.draw_node(node)
    
    def make_visible(self) -> None:
        if self.root is not None:
            self.root.mainloop()

    def highlight_node(self, node: Node, color: Optional[str] = None) -> None:
        """Highlight a node with a specific color"""
        if color is None:
            color = self.NODE_HIGHLIGHT_COLOR
        self.draw_node(node, self.NODE_RADIUS, color)

    def highlight_edge(self, edge: Edge, color: Optional[str] = None) -> None:
        """Highlight an edge and add hover text"""
        if color is None:
            color = self.EDGE_HIGHLIGHT_COLOR
        self.draw_edge(edge, color, True)

    def get_x(self, station: Station) -> int:
        """Get X coordinate for a station"""
        return self.long_to_x(station.longitude)

    def get_y(self, station: Station) -> int:
        """Get Y coordinate for a station"""
        return self.lat_to_y(station.latitude)

    def long_to_x(self, longitude: float) -> int:
        """Convert longitude to X coordinate"""
        return int((longitude - self.MIN_LONGITUDE) * self.PIXELS_PER_DEGREE)

    def lat_to_y(self, latitude: float) -> int:
        """Convert latitude to Y coordinate"""
        return self.SCENE_HEIGHT - int((latitude - self.MIN_LATITUDE) * self.PIXELS_PER_DEGREE)

