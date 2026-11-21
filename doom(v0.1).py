
# MINI-DOOM v0.2.1
# IDLE-compatible version

WORLD = [
    "#######",
    "#.....#",
    "#..#..#",
    "#.....#",
    "#.#...#",
    "#.....#",
    "#######"
]

X = 2
Y = 3
ROTATION = 0

DIRECTIONS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

def is_wall(x, y):
    if y < 0 or y >= len(WORLD):
        return True

    if x < 0 or x >= len(WORLD[y]):
        return True

    return WORLD[y][x] == "#"


def render():
    left_rotation = (ROTATION - 1) % 4
    right_rotation = (ROTATION + 1) % 4

    left_dx, left_dy = DIRECTIONS[left_rotation]
    right_dx, right_dy = DIRECTIONS[right_rotation]

    left = "1" if is_wall(X + left_dx, Y + left_dy) else "0"
    right = "1" if is_wall(X + right_dx, Y + right_dy) else "0"

    screen = left + "8" + right

    print("\n" * 3)
    print("====================")
    print("     MINI-DOOM")
    print("====================")
    print("Screen:", screen)
    print("Position:", X, Y)
    print("Direction:", ["NORTH", "EAST", "SOUTH", "WEST"][ROTATION])


def move(amount):
    global X, Y

    dx, dy = DIRECTIONS[ROTATION]

    new_x = X + dx * amount
    new_y = Y + dy * amount

    if not is_wall(new_x, new_y):
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

        try:
            command = input("\nCommand: ").lower().strip()
        except (EOFError, OSError):
            print("Input unavailable. Exiting MINI-DOOM.")
            break

        if command == "w":
            move(1)
        elif command == "s":
            move(-1)
        elif command == "a":
            ROTATION = (ROTATION - 1) % 4
        elif command == "d":
            ROTATION = (ROTATION + 1) % 4
        elif command == "q":
            print("Exiting MINI-DOOM...")
            break


if __name__ == "__main__":
    main()
