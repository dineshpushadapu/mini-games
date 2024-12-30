import random
import art

def main():
    while True:
        print(art.text2art('GAMES!'))
        game = getGame()
        if game == 1:
            TicTacToe()
        elif game == 2:
            MagicBall()
        elif game == 3:
            RockPaperScissors()
        else:
            continue
        request = input('Do you want to carry on playing y/n? ').upper()
        if request in ['NO', 'N']:
            break

def getGame():
    while True:
        try:
            n = int(input('Welcome to games :), If you want to exit press CTRL + C\nSelect a game :\n- 1 for TicTacToe\n- 2 for Magic 8 Ball\n- 3 for Rock Paper Scissors\nAnswer: '))
            if n in [1, 2, 3]:
                return n
            else:
                print('Please enter a value 1, 2, or 3.')
        except ValueError:
            print('Please enter a valid number.')

def RockPaperScissors():
    print('Welcome to Rock Paper Scissors')
    user = input("'r' for rock, 's' for scissors, 'p' for paper\n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print('You tied!')
    elif is_win(user, computer):
        print('You won!')
    else:
        print('You lost!')

def is_win(player, player2):
    return (player == 'r' and player2 == 's') or (player == 's' and player2 == 'p') or (player == 'p' and player2 == 'r')

def MagicBall():
    answerNumber = random.randint(1, 9)
    responses = {
        1: 'It is certain',
        2: 'It is decidedly so',
        3: 'Yes',
        4: 'Reply hazy try again',
        5: 'Ask again later',
        6: 'Concentrate and ask again',
        7: 'My reply is no',
        8: 'Outlook not so good',
        9: 'Very doubtful'
    }
    print(f'Magic 8 Ball says: {responses[answerNumber]}')

def TicTacToe():
    print('Tic Tac Toe started!')
    board = DefineBoard()
    currentPlayer, nextPlayer = 'X', 'O'
    while True:
        try:
            print(DisplayBoard(board))
            if currentPlayer == 'X':
                position = input(f'{currentPlayer} Role to play? ')
                if CheckSpot(board, position):
                    UpdateBoard(board, currentPlayer, position)
                    if Winner(board, currentPlayer):
                        print(DisplayBoard(board))
                        print(f"{currentPlayer} has won the game.")
                        break
                    if checkFullBoard(board):
                        print(DisplayBoard(board))
                        print('Game Over!')
                        break
                    currentPlayer, nextPlayer = nextPlayer, currentPlayer
                else:
                    print("Spot already taken, try again.")
            else:
                position = getComputerMove(board)
                print(f'Computer chose position {position}')
                UpdateBoard(board, currentPlayer, position)
                if Winner(board, currentPlayer):
                    print(DisplayBoard(board))
                    print(f"{currentPlayer} has won the game.")
                    break
                if checkFullBoard(board):
                    print(DisplayBoard(board))
                    print('Game Over!')
                    break
                currentPlayer, nextPlayer = nextPlayer, currentPlayer
        except (ValueError, KeyError):
            print("Enter a Value between 1 and 9.")

def getComputerMove(board):
    available_moves = [k for k, v in board.items() if v == ' ']
    return random.choice(available_moves)

def DefineBoard():
    return {i: ' ' for i in range(1, 10)}

def UpdateBoard(board, player, position):
    board[int(position)] = player

def CheckSpot(board, position):
    return board[int(position)] == ' '

def Winner(board, player):
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

def checkFullBoard(board):
    return all(value != ' ' for value in board.values())

def DisplayBoard(board):
    return (f'{board[1]}|{board[2]}|{board[3]}   1 2 3\n'
            f'-----\n'
            f'{board[4]}|{board[5]}|{board[6]}   4 5 6\n'
            f'-----\n'
            f'{board[7]}|{board[8]}|{board[9]}   7 8 9')

if __name__ == "__main__":
    main()
