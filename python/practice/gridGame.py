import random
import itertools

class person:

    def __init__(self,player_id,d_roll_his,pos_his,pos_his_2d,win_status):

        self.player_id = player_id
        self.d_roll_his = d_roll_his
        self.pos_his = pos_his
        self.pos_his_2d = pos_his_2d
        self.win_status = win_status

    def display(self):

        print("PLAYER NUMBER : " ,self.player_id)
        print("PLAYER DICE ROLL HISTORY : " ,self.d_roll_his)
        print("NO OF TIMES THIS PLAYER ROLLED THE DICE : ",len(self.d_roll_his))
        print("POSITION HISTORY(VALUE) : ",self.pos_his)
        print("POSITION HISTORY(GRID) : ",self.pos_his_2d)
        print("WIN STATUS : ",self.win_status)
        print("\n")
       



no_of_players = int(input("enter the number of players :"))

start = 1
flag = 0
players = []  # list of instances
my_players = []  # list of players 

# entered the initial value for all the players

for i in range(no_of_players):
    p = person(start,[],[1],[(0,0)],0)
    players.append(p)
    my_players.append(flag)
    start += 1
    flag += 1

# to display the players information
def display_info():
    for p in players:
        p.display()
    
display_info()


# created a grid structure 

def grid_construction(rows) :

    start = 1
    global grid
    grid = []
    for i in range(rows):
        row = []
        for j in range(rows):
            row.append(start)
            start += 1

        if i % 2 == 1:  #reversing odd rows to give the zigzag structure
            row.reverse()

        grid.append(row)

    for row in grid:
        print(row)


rows = int(input("enter the size of the board (nxn) :"))
total_score = rows*rows  #total score basically the victory point
grid_construction(rows)


# generate random number

def gen_random():
    num = random.randint(1, 6)
    return num


#gameplay movesss

for item in itertools.cycle(my_players):
    print("player ",item+1," rolls a die")

    rand_num = gen_random()
    players[item].d_roll_his.append(rand_num)
    current_pos = players[item].pos_his[-1] + rand_num

    # to check if the value dont exceed the final cell

    if current_pos <= total_score:
        players[item].pos_his.append(current_pos)
        pos = next((i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == current_pos)
        players[item].pos_his_2d.append(pos)

    # to check the killings

    for x in my_players:

        if item != x and current_pos == players[x].pos_his[-1]:
            print(f"player {item+1} kills {x+1}")
            players[x].pos_his.append(0)
            players[x].pos_his_2d.append((0,0))

    # to check a winner 

    if current_pos == total_score:
        players[item].win_status = 1
        print(f"PLAYER {item+1} WINSSS")
        break

display_info()