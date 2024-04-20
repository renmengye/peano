import turtle
import tempfile
import os
from PIL import Image

def peano_curve(axiom, rules, angle, iterations, length):
    def apply_rules(char):
        if char in rules:
            return rules[char]
        return char

    def draw_curve(instructions, length):
        for cmd in instructions:
            if cmd == 'F':
                t.forward(length)
                save_frame()
            elif cmd == '+':
                t.left(angle)
            elif cmd == '-':
                t.right(angle)

    def save_frame():
        frame_path = os.path.join(tempfile.gettempdir(), f"frame_{len(frames)}.eps")
        t.getscreen().getcanvas().postscript(file=frame_path)
        # frames.append(Image.open(frame_path))
        frames.append(frame_path)

    instructions = axiom
    frames = []

    for _ in range(iterations):
        instructions = ''.join(apply_rules(c) for c in instructions)


    # Calculate the starting position and line length
    # total_length = length * (3 ** (iterations - 1))
    total_length = length
    for it in range(iterations):
        total_length = total_length * 2 + 1
    # Set up the canvas size
    canvas_size = total_length + 23
    turtle.setup(canvas_size, canvas_size)
    start_x = -total_length/2 + 5
    start_y = -total_length/2 + 15
    print(start_x, start_y)

    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    draw_curve(instructions, length)

    # Save the frames as a GIF
    gif_path = "peano_curve.gif"
    images = [Image.open(frame) for frame in frames]
    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=50, loop=0)
    # frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=50, loop=0)

    # Clean up temporary files
    for frame in frames:
        os.remove(frame)

    turtle.done()

# L-system for Peano curve
axiom = 'X'
rules = {
    'X': '+YF-XFX-FY+',
    'Y': '-XF+YFY+FX-'
}
angle = 90
iterations = 5
length = 5

peano_curve(axiom, rules, angle, iterations, length)