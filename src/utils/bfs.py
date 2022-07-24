from constants import Constants as C


class Node:
    def __init__(self, current_x, current_y, agent_direction, action=None, parent=None):
        self.current_x = current_x
        self.current_y = current_y
        self.state = tuple([self.current_x, self.current_y])
        self.action = action
        self.parent = parent
        self.agent_direction = agent_direction

    def successor(self):
        actions = []
        x = self.current_x
        y = self.current_y

        # vector rotation: https://stackoverflow.com/questions/4780119/2d-euclidean-vector-rotations
        temp_direction = self.agent_direction
        temp_direction = [-temp_direction[1], temp_direction[0]]
        actions.append((C.ROTATE_LEFT, ((x, y), temp_direction)))

        temp_direction = self.agent_direction
        temp_direction = [temp_direction[1], -temp_direction[0]]
        actions.append((C.ROTATE_RIGHT, ((x, y), temp_direction)))

        if self.agent_direction == C.RIGHT and x < 9:
            actions.append((C.MOVE, ((x + 1, y), self.agent_direction)))
        elif self.agent_direction == C.LEFT and x > 0:
            actions.append((C.MOVE, ((x - 1, y), self.agent_direction)))
        elif self.agent_direction == C.UP and y < 9:
            actions.append((C.MOVE, ((x, y + 1), self.agent_direction)))
        elif self.agent_direction == C.DOWN and y > 0:
            actions.append((C.MOVE, ((x, y - 1), self.agent_direction)))

        return actions


class BFSSearcher:

    def __init__(self):
        self.fringe = []
        self.explored = []

    def search(self, first_state: tuple, goal: tuple, agent_direction: list):
        self.fringe.append(Node(first_state[0], first_state[1], agent_direction))

        while True:
            if not self.fringe:
                return False
            element: Node = self.fringe.pop(0)

            if element.state == goal:
                # print(self.__state_eq_goal_action(element))
                return self.__state_eq_goal_action(element)

            self.explored.append(element)

            # print('state: ' + str(element.state) + ', direction: ' + str(element.agent_direction))
            # print(element.successor())

            for action, state in element.successor():
                fringe_states = [(node.state, node.agent_direction) for node in self.fringe]
                explored_states = [(node.state, node.agent_direction) for node in self.explored]
                if (state not in fringe_states) and (state not in explored_states):
                    x = Node(state[0][0], state[0][1], state[1], action, element)
                    self.fringe.append(x)

    def __state_eq_goal_action(self, elem: Node):
        path = []
        while elem.parent:
            path.append(elem.action)
            elem = elem.parent
        path.reverse()
        return path
