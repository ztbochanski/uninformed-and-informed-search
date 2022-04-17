class BoardUpdater:
    """
    state = (0, 0, 0,  # <- LEFT RIVER BANK
            3, 3, 1)  # <- RIGHT RIVER BANK
    """

    def __init__(self, state, boat_docked_flag=1):
        self.state = state
        self.boat_docked_flag = boat_docked_flag
        s = list(state)
        self.left_bank = s[:3]
        self.right_bank = s[3:]

    def get_state(self):
        return self.state

    def move_animal(self, passenger=None, n=0):
        board_position = {
            "chicken": 0,
            "wolf": 1
        }

        if passenger != None:
            if self.left_bank[2] == self.boat_docked_flag:
                self.left_bank[board_position[passenger]
                               ] = self.left_bank[board_position[passenger]] - n
                self.right_bank[board_position[passenger]
                                ] = self.right_bank[board_position[passenger]] + n

            elif self.right_bank[2] == self.boat_docked_flag:
                self.left_bank[board_position[passenger]
                               ] = self.left_bank[board_position[passenger]] + n
                self.right_bank[board_position[passenger]
                                ] = self.right_bank[board_position[passenger]] - n
        self.update_state(self.left_bank, self.right_bank)

    def move_boat(self):
        if self.left_bank[2] == self.boat_docked_flag:
            self.left_bank[2] = self.left_bank[2] - 1
            self.right_bank[2] = self.right_bank[2] + 1

        elif self.right_bank[2] == self.boat_docked_flag:
            self.left_bank[2] = self.left_bank[2] + 1
            self.right_bank[2] = self.right_bank[2] - 1
        self.update_state(self.left_bank, self.right_bank)

    def update_state(self, left_bank, right_bank):
        updated_state = []
        for count in left_bank:
            updated_state.append(count)
        for count in right_bank:
            updated_state.append(count)
        self.state = tuple(updated_state)


def main():
    """test boardupdater

    Methods:
        move_<character>

    Args:
        state: set type

    Returns:
        state: set type
    """

    # move 1 wolf
    state = (0, 0, 0,  # <- LEFT RIVER BANK
             3, 3, 1)  # <- RIGHT RIVER BANK
    boardupdater = BoardUpdater(state)
    move1wolf = (0, 1, 1, 3, 2, 0)
    boardupdater.move_animal(passenger="wolf", n=1)
    boardupdater.move_boat()
    state = boardupdater.get_state()
    print("\nmove 1 wolf")
    if state == move1wolf:
        print("passed!")
        print(state, ":result")
        print(move1wolf, ":expected")
    else:
        print("failed!")
        print(state, ":result")
        print(move1wolf, ":expected")


if __name__ == "__main__":
    main()
