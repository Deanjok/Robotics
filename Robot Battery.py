import tkinter as tk

# Configuration
MAP_WIDTH = 400
MAP_HEIGHT = 400
GRID_SIZE = 40  # Size of each grid cell
ROVER_COLOR = "blue"
MAP_COLOR = "lightgray"

# Example Data: List of obstacles or path coordinates (x, y)
obstacles = [(1, 1), (2, 3), (3, 1), (4, 4)]
rover_pos = [0, 0]  # Initial rover grid coordinates [col, row]


def draw_map(canvas):
    # Draw Grid Background
    for x in range(0, MAP_WIDTH, GRID_SIZE):
        for y in range(0, MAP_HEIGHT, GRID_SIZE):
            canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, outline="white", fill=MAP_COLOR)

    # Draw Obstacles from list
    for obs_x, obs_y in obstacles:
        x1 = obs_x * GRID_SIZE
        y1 = obs_y * GRID_SIZE
        canvas.create_rectangle(x1, y1, x1 + GRID_SIZE, y1 + GRID_SIZE, fill="red", outline="black")


def update_rover(canvas, rover_item, grid_x, grid_y):
    # Convert grid coordinates to pixel coordinates
    x1 = grid_x * GRID_SIZE + 5  # +5 for padding
    y1 = grid_y * GRID_SIZE + 5
    x2 = x1 + GRID_SIZE - 10
    y2 = y1 + GRID_SIZE - 10

    # Move the existing rover rectangle to new coordinates
    canvas.coords(rover_item, x1, y1, x2, y2)


# Setup Window
root = tk.Tk()
root.title("Rover Map Display")

canvas = tk.Canvas(root, width=MAP_WIDTH, height=MAP_HEIGHT, bg="black")
canvas.pack()

# Draw static map elements
draw_map(canvas)

# Create Rover (returns an ID to reference it later)
# Initial draw at (0,0)
rover_id = canvas.create_rectangle(5, 5, GRID_SIZE - 5, GRID_SIZE - 5, fill=ROVER_COLOR, outline="white")


# Example: Move rover to a new coordinate from your list after 2 seconds
def move_rover_example():
    new_pos = [3, 2]  # Target coordinate from your list
    update_rover(canvas, rover_id, new_pos[0], new_pos[1])
    root.title(f"Rover at: {new_pos}")


root.after(2000, move_rover_example)

root.mainloop()   