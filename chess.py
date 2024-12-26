import turtle

def is_valid_move(x, y, visited, n):
    return 0 <= x < n and 0 <= y < n and not visited[y][x]

def generate_legal_moves(x, y, visited, n):
    possible_moves = [
        (x + 1, y + 2), (x + 2, y + 1),
        (x + 2, y - 1), (x + 1, y - 2),
        (x - 1, y - 2), (x - 2, y - 1),
        (x - 2, y + 1), (x - 1, y + 2)
    ]

    legal_moves = [
        move for move in possible_moves
        if is_valid_move(*move, visited, n)
    ]

    return legal_moves

def draw_chessboard():
    square_size = 75
    start_x = -300  # X-coordinate of the starting point
    start_y = 300   # Y-coordinate of the starting point

    board = turtle.Turtle()
    board.speed(0)
    board.penup()
    board.goto(start_x, start_y)
    board.pendown()

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                board.fillcolor("white")
            else:
                board.fillcolor("black")
            board.begin_fill()
            for _ in range(4):
                board.forward(square_size)
                board.right(90)
            board.end_fill()
            board.forward(square_size)
        board.backward(square_size * 8)
        board.right(90)
        board.forward(square_size)
        board.left(90)

    return board

def knight_tour(board_size, start_x, start_y):
    visited = [[False for _ in range(board_size)] for _ in range(board_size)]
    x, y = start_x, start_y
    move_number = 1

    moves = [(x, y)]

    while move_number <= board_size * board_size:
        visited[y][x] = True
        print(f"Move {move_number}: ({x + 1}, {y + 1})")

        # Draw the move on the chessboard
        draw_move(x, y, move_number)

        legal_moves = generate_legal_moves(x, y, visited, board_size)
        if not legal_moves:
            break

        # Warnsdorff's algorithm: Choose the move with the fewest next legal moves
        legal_moves.sort(key=lambda move: len(generate_legal_moves(*move, visited, board_size)))
        x, y = legal_moves[0]
        move_number += 1

        moves.append((x, y))

    if move_number < board_size * board_size:
        print("The knight's tour is not possible.")
    else:
        print("The knight's tour is complete.")

    # Draw lines between consecutive moves
    draw_lines_between_moves(moves)

def draw_move(x, y, move_number):
    board.penup()
    board.goto((x) * square_size - 300 + square_size / 2, (y - 7) * square_size + 300 - square_size / 2)
    board.pendown()
    board.color("red")
    board.write(f"{move_number}", align="center", font=("Arial", 12, "normal"))

def draw_lines_between_moves(moves):
    board.penup()
    board.pendown()
    board.color("blue")
    board.width(2)

    for i in range(len(moves) - 1):
        x1, y1 = moves[i]
        x2, y2 = moves[i + 1]
        board.goto((x1) * square_size - 300 + square_size / 2, (y1 - 7) * square_size + 300 - square_size / 2)
        board.goto((x2) * square_size - 300 + square_size / 2, (y2 - 7) * square_size + 300 - square_size / 2)

# Get user input for the starting position
start_x = int(input("Enter the starting column (1-8): ")) - 1
start_y = int(input("Enter the starting row (1-8): ")) - 1

# Initialize and draw the chessboard
square_size = 75
board = turtle.Turtle()
board.speed(0)
draw_chessboard()

# Perform the knight's tour and draw the moves on the chessboard
knight_tour(board_size=8, start_x=start_x, start_y=start_y)

turtle.done()


