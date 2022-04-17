from action import Action


class Actions:
    """define game actions here
    """

    def __init__(self):
        self.actions = {
            "action1": Action(passengers=["chicken"], count=1),
            "action2": Action(passengers=["chicken"], count=2),
            "action3": Action(passengers=["wolf"], count=1),
            "action4": Action(passengers=["chicken", "wolf"], count=1),
            "action5": Action(passengers=["wolf"], count=2)
        }
