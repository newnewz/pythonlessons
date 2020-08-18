rows, cols = (6,7)
board = [[] for j in range(cols)]

def drawBoard():
    print("---------------------")
    for row in range(rows-1, -1, -1):
        print("[", end = " ")
        for col in range(0, cols):
            if len(board[col]) > row:
                print(board[col][row], end = ' ')
            else:
                print('_', end = ' ')
        print("]")
    


def placePiece(player, col):
    board[col].append(0)
        

def main():
    drawBoard()
    placePiece(1, 2)
    drawBoard()

if __name__ == "__main__":
    main()

        