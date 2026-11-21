
# MINI-DOOM v0.2.2
# 3x3 Coordinate Renderer
# Python IDLE compatible

# NORTH-facing screen lookup table
SCREEN_TABLE = {
    (1, 1): "181",
    (2, 1): "181",
    (3, 1): "181",

    (1, 2): "180",
    (2, 2): "080",
    (3, 2): "081",

    (1, 3): "180",
    (2, 3): "080",
    (3, 3): "081"
}

# Player starting position
X = 2
Y = 2

# 0 = NORTH
# 1 = EAST
# 2 = SOUTH
# 3 = WEST
ROTATION = 0

DIRECTIONS = [
    (0, -1),  # NORTH
    (1, 0),   # EAST
    (0, 1),   # SOUTH
    (-1, 0)   # WEST
]

DIRECTION_NAMES = [
    "NORTH",
    "EAST",
    "SOUTH",
    "WEST"
]

ARROWS = ["^", ">", "v", "<"]


def get_screen_code():
    # Rotate the lookup table based on facing direction

    if ROTATION == 0:
        tx, ty = X, Y

    elif ROTATION == 1:
        tx, ty = Y, 4 - X

    elif ROTATION == 2:
        tx, ty = 4 - X, 4 - Y

    else:
        tx, ty = 4 - Y, X

    return SCREEN_TABLE[(tx, ty)]


def render():
    print("\n" * 2)
    print("========================")
    print("       MINI-DOOM")
    print("========================")

    print("Screen:", get_screen_code())
    print("Position:", X, Y)
    print("Direction:", DIRECTION_NAMES[ROTATION])

    print("\nMAP:")

    for row in range(1, 4):
        line = ""

        for col in range(1, 4):
            if X == col and Y == row:
                line += "[" + ARROWS[ROTATION] + "]"
            else:
                line += " . "

        print(line)

    print("========================")


def move(amount):
    global X, Y

    dx, dy = DIRECTIONS[ROTATION]

    new_x = X + dx * amount
    new_y = Y + dy * amount

    # Keep player inside the 3x3 grid
    if 1 <= new_x <= 3 and 1 <= new_y <= 3:
        X = new_x
        Y = new_y


def main():
    global ROTATION

    while True:
        render()

        print("\nW = Forward")
        print("S = Backward")
        print("A = Turn left")
        print("D = Turn right")
        print("Q = Quit")

        command = input("\nCommand: ").lower().strip()

        if command == "w":
            move(1)

        elif command == "s":
            move(-1)

        elif command == "a":
            ROTATION = (ROTATION - 1) % 4

        elif command == "d":
            ROTATION = (ROTATION + 1) % 4

        elif command == "q":
            print("Closing MINI-DOOM...")
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
