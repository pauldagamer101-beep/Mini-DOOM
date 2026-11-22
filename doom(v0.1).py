
# MINI-DOOM v0.3.1
# MAP 01: THE CONNECTOR
# Fixed room rendering and hallway movement

import tkinter as tk

# NORTH-facing screen lookup table
SCREEN_TABLE = {
    (1, 1): r"1111/||\1111",
    (2, 1): r"1111/||\1111",
    (3, 1): r"1111/||\1111",

    (1, 2): r"1111/||\####",
    (2, 2): r"####/||\####",
    (3, 2): r"####/||\1111",

    (1, 3): r"1111/||\####",
    (2, 3): r"####/||\####",
    (3, 3): r"####/||\1111"
}

# Player position
X = 2
Y = 2
ROTATION = 0

DIRECTIONS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

DIRECTION_NAMES = ["NORTH", "EAST", "SOUTH", "WEST"]
ARROWS = ["^", ">", "v", "<"]

# Shotgun
GUN = "/||\\"
SHOOTING = False
RELOADING = False


# Full map:
# Room 1 = x 1-3
# Hallway = x 4-8
# Room 2 = x 9-11

MAP = [
    "#############",
    "#...#####...#",
    "#...........#",
    "#...#####...#",
    "#############"
]


def is_walkable(x, y):

    # Room 1
    if 1 <= x <= 3 and 1 <= y <= 3:
        return True

    # Five-tile hallway
    if 4 <= x <= 8 and y == 2:
        return True

    # Room 2
    if 9 <= x <= 11 and 1 <= y <= 3:
        return True

    return False


def get_screen_code():

    # Hallway view
    if 4 <= X <= 8:
        if ROTATION == 1 or ROTATION == 3:
            return r"##11/||\11##"
        return r"####/||\####"

    # Convert world position to room-local position
    if X <= 3:
        local_x = X
    else:
        local_x = X - 8

    local_y = Y

    # Original rotation transformation
    if ROTATION == 0:
        tx, ty = local_x, local_y
    elif ROTATION == 1:
        tx, ty = local_y, 4 - local_x
    elif ROTATION == 2:
        tx, ty = 4 - local_x, 4 - local_y
    else:
        tx, ty = 4 - local_y, local_x

    return SCREEN_TABLE[(tx, ty)]


def move(amount):

    global X, Y

    dx, dy = DIRECTIONS[ROTATION]

    new_x = X + dx * amount
    new_y = Y + dy * amount

    if is_walkable(new_x, new_y):
        X = new_x
        Y = new_y


def finish_shooting():

    global GUN, SHOOTING, RELOADING

    GUN = "/00/"
    SHOOTING = False
    RELOADING = True

    render()
    window.after(1000, finish_reloading)


def finish_reloading():

    global GUN, RELOADING

    GUN = "/||\\"
    RELOADING = False

    render()


def shoot():

    global GUN, SHOOTING

    if SHOOTING or RELOADING:
        return

    GUN = "/**\\"
    SHOOTING = True

    render()
    window.after(1000, finish_shooting)


def render():

    screen = get_screen_code()
    left, right = screen.split("/||\\")
    screen = left + GUN + right

    screen_label.config(text="Screen: " + screen)

    position_label.config(
        text=f"Position: {X}, {Y}"
    )

    direction_label.config(
        text="Direction: " + DIRECTION_NAMES[ROTATION]
    )

    # Draw full top-down map
    map_text = ""

    for row in range(5):

        line = ""

        for col in range(13):

            if row == Y and col == X:
                line += ARROWS[ROTATION]
            else:
                line += MAP[row][col]

        map_text += line + "\n"

    map_label.config(text=map_text)

    if SHOOTING:
        status_label.config(text="SHOTGUN: FIRING!")
    elif RELOADING:
        status_label.config(text="SHOTGUN: RELOADING...")
    else:
        status_label.config(text="SHOTGUN: READY")


def key_pressed(event):

    global ROTATION

    command = event.keysym.lower()

    if command == "w":
        move(1)

    elif command == "s":
        move(-1)

    elif command == "a":
        ROTATION = (ROTATION - 1) % 4

    elif command == "d":
        ROTATION = (ROTATION + 1) % 4

    elif command == "space":
        shoot()
        return

    elif command == "q":
        window.destroy()
        return

    render()


# Window setup
window = tk.Tk()
window.title("MINI-DOOM v0.3.1")
window.geometry("650x500")
window.configure(bg="#202020")

title = tk.Label(
    window,
    text="MINI-DOOM",
    font=("Consolas", 24, "bold"),
    fg="white",
    bg="#202020"
)
title.pack(pady=15)

screen_label = tk.Label(
    window,
    font=("Consolas", 17),
    fg="white",
    bg="#202020"
)
screen_label.pack(pady=8)

position_label = tk.Label(
    window,
    font=("Consolas", 13),
    fg="white",
    bg="#202020"
)
position_label.pack()

direction_label = tk.Label(
    window,
    font=("Consolas", 13),
    fg="white",
    bg="#202020"
)
direction_label.pack()

map_label = tk.Label(
    window,
    font=("Consolas", 18),
    fg="white",
    bg="#202020",
    justify="left"
)
map_label.pack(pady=15)

status_label = tk.Label(
    window,
    font=("Consolas", 13, "bold"),
    fg="#55dd55",
    bg="#202020"
)
status_label.pack(pady=5)

controls = tk.Label(
    window,
    text="W: Forward   S: Backward\n"
         "A: Turn Left   D: Turn Right\n"
         "SPACE: Shoot   Q: Quit",
    font=("Consolas", 11),
    fg="#aaaaaa",
    bg="#202020"
)
controls.pack(pady=10)

window.bind("<KeyPress>", key_pressed)

render()
window.focus_force()
window.mainloop()
