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

    def move_agent(self, passenger1=None, passenger2=None, n=0):
        board_position = {
            "chicken": 0,
            "wolf": 1,
            "boat": 2
        }

        if passenger1 != None:
            if self.left_bank[2] == self.boat_docked_flag:
                self.left_bank[board_position[passenger1]
                               ] = self.left_bank[board_position[passenger1]] - n
                self.right_bank[board_position[passenger1]
                                ] = self.right_bank[board_position[passenger1]] + n

            elif self.right_bank[2] == self.boat_docked_flag:
                self.left_bank[board_position[passenger1]
                               ] = self.left_bank[board_position[passenger1]] + n
                self.right_bank[board_position[passenger1]
                                ] = self.right_bank[board_position[passenger1]] - n

        if passenger2 != None:
            if self.left_bank[2] == self.boat_docked_flag:
                self.left_bank[board_position[passenger2]
                               ] = self.left_bank[board_position[passenger2]] - n
                self.right_bank[board_position[passenger2]
                                ] = self.right_bank[board_position[passenger2]] + n

            elif self.right_bank[2] == self.boat_docked_flag:
                self.left_bank[board_position[passenger2]
                               ] = self.left_bank[board_position[passenger2]] + n
                self.right_bank[board_position[passenger2]
                                ] = self.right_bank[board_position[passenger2]] - n

        self.move_boat()
        self.update_state(self.left_bank, self.right_bank)

    def move_boat(self):
        if self.left_bank[2] == self.boat_docked_flag:
            self.left_bank[2] = self.left_bank[2] - 1
            self.right_bank[2] = self.right_bank[2] + 1

        elif self.right_bank[2] == self.boat_docked_flag:
            self.left_bank[2] = self.left_bank[2] + 1
            self.right_bank[2] = self.right_bank[2] - 1

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
    boardupdater.move_agent(passenger1="wolf", n=1)
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

    # move 2 wolves
    state = (0, 0, 0,  # <- LEFT RIVER BANK
             3, 3, 1)  # <- RIGHT RIVER BANK
    boardupdater = BoardUpdater(state)
    move2wolves = (0, 2, 1, 3, 1, 0)
    boardupdater.move_agent(passenger1="wolf", n=2)
    state = boardupdater.get_state()
    print("\nmove 2 wolves")
    if state == move2wolves:
        print("passed!")
        print(state, ":result")
        print(move2wolves, ":expected")
    else:
        print("failed!")
        print(state, ":result")
        print(move2wolves, ":expected")

    # move 1 chicken
    state = (0, 0, 0,  # <- LEFT RIVER BANK
             3, 3, 1)  # <- RIGHT RIVER BANK
    boardupdater = BoardUpdater(state)
    move1chicken = (1, 0, 1, 2, 3, 0)
    boardupdater.move_agent(passenger1="chicken", n=1)
    state = boardupdater.get_state()
    print("\nmove 1 chicken")
    if state == move1chicken:
        print("passed!")
        print(state, ":result")
        print(move1chicken, ":expected")
    else:
        print("failed!")
        print(state, ":result")
        print(move1chicken, ":expected")

    # move 2 chickens
    state = (0, 0, 0,  # <- LEFT RIVER BANK
             3, 3, 1)  # <- RIGHT RIVER BANK
    boardupdater = BoardUpdater(state)
    move2chickens = (2, 0, 1, 1, 3, 0)
    boardupdater.move_agent(passenger1="chicken", n=2)
    state = boardupdater.get_state()
    print("\nmove 2 chickens")
    if state == move2chickens:
        print("passed!")
        print(state, ":result")
        print(move2chickens, ":expected")
    else:
        print("failed!")
        print(state, ":result")
        print(move2chickens, ":expected")

    # move 1 wolf, 1 chicken
    state = (0, 0, 0,  # <- LEFT RIVER BANK
             3, 3, 1)  # <- RIGHT RIVER BANK
    boardupdater = BoardUpdater(state)
    move1each = (1, 1, 1, 2, 2, 0)
    boardupdater.move_agent(passenger1="chicken", passenger2="wolf", n=1)
    state = boardupdater.get_state()
    print("\nmove 1 of each")
    if state == move1each:
        print("passed!")
        print(state, ":result")
        print(move1each, ":expected")
    else:
        print("failed!")
        print(state, ":result")
        print(move1each, ":expected")

    # move nothing
    state = (0, 0, 0,  # <- LEFT RIVER BANK
             3, 3, 1)  # <- RIGHT RIVER BANK
    boardupdater = BoardUpdater(state)
    movenone = (0, 0, 1, 3, 3, 0)
    boardupdater.move_agent()
    state = boardupdater.get_state()
    print("\nmove nothing")
    if state == movenone:
        print("passed!")
        print(state, ":result")
        print(movenone, ":expected")
    else:
        print("failed!")
        print(state, ":result")
        print(movenone, ":expected")


if __name__ == "__main__":
    main()
