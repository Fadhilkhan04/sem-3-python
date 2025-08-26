import random
import itertools

class Player:
    
    def __init__(self, player_id):
        self.player_id = player_id
        self.d_roll_his = []
        self.pos_his = [1]
        self.pos_his_2d = [(0, 0)]
        self.win_status = 0

    def display(self):
        print(f"PLAYER NUMBER : {self.player_id}")
        print("PLAYER DICE ROLL HISTORY :", self.d_roll_his)
        print("NO OF TIMES THIS PLAYER ROLLED THE DICE:", len(self.d_roll_his))
        print("POSITION HISTORY(VALUE) :", self.pos_his)
        print("POSITION HISTORY(GRID) :", self.pos_his_2d)
        print("WIN STATUS :", self.win_status)
        print("\n")

    def play(self, roll, value_to_coord, total_score):
        current_pos = self.pos_his[-1] + roll
        if current_pos <= total_score:
            self.pos_his.append(current_pos)
            self.pos_his_2d.append(value_to_coord[current_pos])
        return current_pos

    def kill(self):
        self.pos_his.append(1)
        self.pos_his_2d.append((0, 0))


def create_grid(rows):
    grid = []
    value_to_coord = {}
    val = 1
    for i in range(rows):
        row = [val + j for j in range(rows)]
        if i % 2 == 1:
            row.reverse()
        grid.append(row)
        for j in range(rows):
            value_to_coord[row[j]] = (i, j)
        val += rows
    return grid, value_to_coord


def display_grid(grid):
    for row in grid:
        print(row)


def display_all_players(players):
    for player in players:
        player.display()


def roll_dice():
    return random.randint(1, 6)


def main():
    no_of_players = int(input("Enter the number of players: "))
    rows = int(input("Enter the size of the board (n x n): "))
    total_score = rows * rows

    grid, value_to_coord = create_grid(rows)
    display_grid(grid)

    players = [Player(i+1) for i in range(no_of_players)]

    for turn in itertools.cycle(range(no_of_players)):
        current_player = players[turn]
        print(f"\nPlayer {current_player.player_id} rolls a die")

        roll = roll_dice()
        current_player.d_roll_his.append(roll)
        current_pos = current_player.play(roll, value_to_coord, total_score)

        if current_pos == total_score:
            current_player.win_status = 1
            print(f"\nPLAYER {current_player.player_id} WINS!!!")
            break

        for other in players:
            if other != current_player and current_pos == other.pos_his[-1]:
                print(f"PLAYER {current_player.player_id} kills PLAYER {other.player_id}")
                other.kill()

    print("\nFinal Player Info:")
    display_all_players(players)


if __name__ == "__main__":
    main()
