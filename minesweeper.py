import random

bombs_left = 0

def fill_board_with_numbers_of_nearby_bombs(board_get, x, y):
    for rows in range(x):
        for cols in range(y):
            nearby_bombs = 0
            if board_get[rows][cols] != -1:
                #########1#####################
                if rows == 0 and cols == 0:
                    if board_get[rows][cols + 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows + 1][cols + 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows + 1][cols] == -1:
                        nearby_bombs += 1
                ###########2###############################
                if rows == 0 and cols == y - 1:
                    if board_get[rows - 1][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows - 1][cols] == -1:
                        nearby_bombs += 1
                ######3#####################################
                if rows == x - 1 and cols == y - 1:
                    if board_get[rows - 1][cols] == -1:
                        nearby_bombs += 1
                    if board_get[rows - 1][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows][cols - 1] == -1:
                        nearby_bombs += 1
                ####4####################################
                if rows == x - 1 and cols == 0:
                    if board_get[rows - 1][cols] == -1:
                        nearby_bombs += 1
                    if board_get[rows - 1][cols + 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows][cols + 1] == -1:
                        nearby_bombs += 1
                ##################5######################
                if rows > 0 and rows < x - 1 and cols > 0 and cols < y - 1:
                    if board_get[rows - 1][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows - 1][cols] == -1:
                        nearby_bombs += 1
                    if board_get[rows - 1][cols + 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows][cols + 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows + 1][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows + 1][cols] == -1:
                        nearby_bombs += 1
                    if board_get[rows + 1][cols + 1] == -1:
                        nearby_bombs += 1
                #######6##############################
                if rows == 0 and cols > 0 and cols < y - 1:
                    if board_get[rows][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows][cols + 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows + 1][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows + 1][cols] == -1:
                        nearby_bombs += 1
                    if board_get[rows + 1][cols + 1] == -1:
                        nearby_bombs += 1
                #############7########################
                if rows > 0 and rows < x - 1 and cols == y - 1:
                    if board_get[rows - 1][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows - 1][cols] == -1:
                        nearby_bombs += 1
                    if board_get[rows][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows + 1][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows + 1][cols] == -1:
                        nearby_bombs += 1
                #############8############################
                if rows == x - 1 and cols > 0 and cols < y - 1:
                    if board_get[rows - 1][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows - 1][cols] == -1:
                        nearby_bombs += 1
                    if board_get[rows - 1][cols + 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows][cols - 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows][cols + 1] == -1:
                        nearby_bombs += 1
                ############9##############################
                if rows > 0 and rows < x - 1 and y == 0:
                    if board_get[rows - 1][cols] == -1:
                        nearby_bombs += 1
                    if board_get[rows - 1][cols + 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows][cols + 1] == -1:
                        nearby_bombs += 1
                    if board_get[rows + 1][cols] == -1:
                        nearby_bombs += 1
                    if board_get[rows + 1][cols + 1] == -1:
                        nearby_bombs += 1
                board_get[rows][cols] = nearby_bombs
    return board_get

def generate_board(x = 16, y = 16):
    global bombs_left
    board = []
    for rows in range(x):
        board.append([])
        for cols in range(y): #0 means no bomb in nearby 1 - 1 etc. -1 means it is a bomb
            if random.randint(0, 100) > 12:
                board[rows].append(0)
            else:
                board[rows].append(-1)
                bombs_left += 1
    return fill_board_with_numbers_of_nearby_bombs(board, x, y)

def gen_empty_tab(x = 16, y = 16):
    board = []
    for rows in range(x):
        board.append([])
        for cols in range(y):
            board[rows].append(0)
    return board

def show_map(tab, board, allmode = False, x = 16, y = 16):
    for rows in range(x):
        for cols in range(y):
            if allmode:
                tab[rows][cols] = 1
            if tab[rows][cols] == 1:
                if board[rows][cols] == -1:
                    print("*", end = " ")
                else:
                    print(board[rows][cols], end = " ")
            elif tab[rows][cols] == 2:
                print("^", end = " ") #flag
            else:
                print("-", end = " ")
        print("")

def main_loop(board, x, y):
    global bombs_left
    sim_board = gen_empty_tab(x, y)
    while True:
        if bombs_left == 0:
            print("Wygrana!")
            break

        print("Pozostało {} bomb.".format(bombs_left))
        what_to_do = int(input("Co zrobic? [0]Oznacz, [1]Pokaz "))
        
        choice = str(input("Wybierz pole... "))
        choice = choice.lower()
        tmp = ord(choice[0]) - ord('a')
        if len(choice) == 3:
            tmp_num = int(choice[1]) * 10 + int(choice[2])
        else:
            tmp_num = int(choice[1])

        if what_to_do == 0:
            if board[tmp][tmp_num] == -1:
                bombs_left -= 1
                sim_board[tmp][tmp_num] = 2 #flagged
            show_map(sim_board, board, False, x, y)
        if what_to_do == 1:    
            if board[tmp][tmp_num] == -1:
                sim_board[tmp][tmp_num] = 1
                print("Przegrana!")
                show_map(sim_board, board, True)
                break
            else:
                sim_board[tmp][tmp_num] = 1 #marked as read
                show_map(sim_board, board, False, x, y)
            
main_loop(generate_board(8, 8), 8, 8)