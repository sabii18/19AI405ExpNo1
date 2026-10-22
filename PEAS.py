class VacuumCleanerAgent:
    def __init__(self):
        self.location = "A"  
        self.dirt_status = {"A": False, "B": False}  

    def move_left(self):
        if self.location == "B":
            self.location = "A"

    def move_right(self):
        if self.location == "A":
            self.location = "B"

    def suck_dirt(self):
        if self.dirt_status[self.location]:
            self.dirt_status[self.location] = False
            print(f"Sucked dirt in location {self.location}")

    def do_nothing(self):
        pass

    def perform_action(self, action):
        if action == "left":
            self.move_left()
        elif action == "right":
            self.move_right()
        elif action == "suck":
            self.suck_dirt()
        elif action == "nothing":
            self.do_nothing()
        else:
            print("Invalid action")

    def print_status(self):
        print(f"Location: {self.location}, Dirt Status: {self.dirt_status}")

agent = VacuumCleanerAgent()


agent.perform_action("left")
agent.print_status()
agent.perform_action("suck")
agent.print_status()
agent.perform_action("nothing")
agent.print_status()
