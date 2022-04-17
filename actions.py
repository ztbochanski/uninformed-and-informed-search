from action import Action


class Actions:
    """define game actions here
    """

    def __init__(self):
        self.available = {
            "action1": Action(passengers=["chicken"], count=1),
            "action2": Action(passengers=["chicken"], count=2),
            "action3": Action(passengers=["wolf"], count=1),
            "action4": Action(passengers=["chicken", "wolf"], count=1),
            "action5": Action(passengers=["wolf"], count=2)
        }


def main():
    """test calling actions
    """
    state = (0, 0, 0,  # <- LEFT RIVER BANK
             3, 3, 1)  # <- RIGHT RIVER BANK
    print(Actions().available["action1"].do(state))


if __name__ == "__main__":
    main()
