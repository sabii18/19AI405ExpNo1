# Exp No: 1 – Developing AI Agent with PEAS Description

**Name:** SABEESHWARAN. P

**Register Number:** 212225230234

## AIM

To identify the PEAS description for the given AI problem and develop a Vacuum Cleaner AI Agent using Python.

## THEORY

**Vacuum Cleaner Agent:**

A vacuum cleaner agent is an intelligent agent that cleans dirty locations in an environment. In this experiment, the environment consists of two rooms, A and B. The agent starts in room A and can move left or right between the two rooms.

The agent has four actions: move left, move right, suck dirt, and do nothing. When the agent detects dirt in its current location, it removes the dirt using the suck action. If the room is already clean, the agent can move to another room or do nothing.

The agent's performance can be measured based on the cleanliness of the rooms, the number of successful cleaning actions, and the number of movements performed.

## PEAS DESCRIPTION

| Agent Type | Performance | Environment | Actuators | Sensors |
|---|---|---|---|---|
| Vacuum Cleaner Agent | Cleaning dirty rooms and reducing unnecessary movements | Two rooms (A and B), dirt | Move left, move right, suck dirt, do nothing | Current location and dirt status |

## DESIGN STEPS

### STEP 1: Identifying the Input

- Initial location of the agent (Room A).
- Dirt status of the rooms A and B.
- Action selected by the user.

### STEP 2: Identifying the Output

- Display the current location of the agent.
- Display the dirt status of both rooms.
- Print a message when dirt is removed.
- Display an error message for an invalid action.

### STEP 3: Developing the PEAS Description

The PEAS description is developed by identifying the four components of the agent:

- **Performance:** Cleaning the rooms and minimizing unnecessary movements.
- **Environment:** Two rooms, A and B.
- **Actuators:** Movement and cleaning actions.
- **Sensors:** Information about the agent's location and the dirt status of the rooms.

### STEP 4: Implementing the AI Agent

The Vacuum Cleaner Agent is implemented using a Python class. The class contains methods to move between rooms, suck dirt, perform no action, execute the selected action, and display the current status.

The `perform_action()` method selects the appropriate operation based on the given action. The `print_status()` method displays the current location and dirt status.

### STEP 5: Measuring the Performance Parameters

The performance of the agent can be evaluated using the following parameters:

1. **Cleaning performance:** Whether the dirt is removed successfully.
2. **Movement efficiency:** The number of movements required to reach different rooms.
3. **Room cleanliness:** Whether both rooms are clean.
4. **Action accuracy:** Whether the agent performs the correct action based on the selected command.

## PROGRAM:
```python
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
```
## OUTPUT:

<img width="580" height="120" alt="Screenshot 2026-10-22 095806" src="https://github.com/user-attachments/assets/44c4ee28-03b9-4213-9a5b-dfbe8794f283" />


## RESULT

Thus, the PEAS description was identified, and a Vacuum Cleaner AI Agent was developed using Python to perform movement and cleaning actions in a two-room environment. The agent's location and the dirt status of the rooms were displayed after each action.
