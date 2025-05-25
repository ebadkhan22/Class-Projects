import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20


def erase(event, canvas, eraser):
    """Erase objects in contact with the eraser"""
    mouse_x, mouse_y = event.x, event.y

    # Calculate where our eraser is
    left_x = mouse_x - ERASER_SIZE // 2
    top_y = mouse_y - ERASER_SIZE // 2
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    # Find items on the canvas and change color to white if within eraser area
    for item in canvas.find_overlapping(left_x, top_y, right_x, bottom_y):
        canvas.itemconfig(item, fill="white")


def main():
    root = tk.Tk()
    root.title("Canvas with Eraser")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    # Draw a grid of cells
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="blue")

    # Create an eraser rectangle
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

    # Move eraser with mouse movement
    canvas.bind("<B1-Motion>", lambda event, canvas= canvas, eraser= eraser: erase(event, canvas, eraser))

    root.mainloop()


if __name__ == '__main__':
    main()
