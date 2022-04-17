from board import BoardUpdater


class Action:

    def __init__(self, passengers=[], count=0):
        self.passengers = passengers
        self.count = count

    def do(self, state):
        boardupdater = BoardUpdater(state)
        for passenger in self.passengers:
            boardupdater.move_animal(
                passenger=passenger, n=self.count)
        boardupdater.move_boat()
        return boardupdater.get_state()


def main():
    """test action

    state = (0, 0, 0,  # <- LEFT RIVER BANK
             3, 3, 1)  # <- RIGHT RIVER BANK
    """

    state = (0, 0, 0,  # <- LEFT RIVER BANK
             3, 3, 1)  # <- RIGHT RIVER BANK

    # action1 move1chicken
    action1 = Action(passengers=["chicken"], count=1)
    print("\naction1: ", action1.do(state) == (1, 0, 1, 2, 3, 0))

    # action2 move2chickens
    action2 = Action(passengers=["chicken"], count=2)
    print("\naction2: ", action2.do(state) == (2, 0, 1, 1, 3, 0))

    # action3 move1wolf
    action3 = Action(passengers=["wolf"], count=1)
    print("\naction3: ", action3.do(state) == (0, 1, 1, 3, 2, 0))

    # action4 move1each
    action4 = Action(passengers=["chicken", "wolf"], count=1)
    print("\naction4: ", action4.do(state) == (1, 1, 1, 2, 2, 0))

    # action5 move2wolves
    action5 = Action(passengers=["wolf"], count=2)
    print("\naction5: ", action5.do(state) == (0, 2, 1, 3, 1, 0))


if __name__ == "__main__":
    main()
