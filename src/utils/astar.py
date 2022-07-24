from operator import itemgetter
import copy
import tractor
from world import World

from constants import Constants as C


class Node:
    def __init__(self, x, y, agent_direction, action=None, parent=None):  # inicjalizacja węzła
        self.x = x
        self.y = y
        self.state = tuple([self.x, self.y])
        self.agent_direction = agent_direction
        self.parent = parent
        self.action = action

    def get_parent(self):
        return self.parent

    def get_direction(self):
        return self.agent_direction

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_action(self):
        return self.action

    def __repr__(self):
        return " <Node x:%s y:%s state:%s agent_dir:%s parent:%s action:%s> " % (
        self.x, self.y, self.state, self.agent_direction, self.parent, self.action)

    def successor(self):
        action_list = []
        x = self.x
        y = self.y

        # vector rotation: https://stackoverflow.com/questions/4780119/2d-euclidean-vector-rotations
        temp_direction = self.agent_direction
        temp_direction = [-temp_direction[1], temp_direction[0]]
        action_list.append((C.ROTATE_LEFT, ((x, y), temp_direction)))

        temp_direction = self.agent_direction
        temp_direction = [temp_direction[1], -temp_direction[0]]
        action_list.append((C.ROTATE_RIGHT, ((x, y), temp_direction)))

        temp_direction = self.agent_direction
        temp_direction = [-temp_direction[0], -temp_direction[1]]
        action_list.append((C.TURN_AROUND, ((x, y), temp_direction)))

        if self.agent_direction == C.RIGHT and x < 9:
            action_list.append((C.MOVE, ((x + 1, y), self.agent_direction)))
        elif self.agent_direction == C.LEFT and x > 0:
            action_list.append((C.MOVE, ((x - 1, y), self.agent_direction)))
        elif self.agent_direction == C.UP and y < 9:
            action_list.append((C.MOVE, ((x, y + 1), self.agent_direction)))
        elif self.agent_direction == C.DOWN and y > 0:
            action_list.append((C.MOVE, ((x, y - 1), self.agent_direction)))

        return action_list


def h_cost(goal: tuple, node: Node):  # oblicznie heurystyki
    return abs(node.x - goal[0]) + abs(node.y - goal[1])


def g_cost(node: Node, world_map: World):  # funkcja kosztu : ile kosztuje przejechanie przez dane pole
    cost = 0
    while node.get_parent() is not None:
        cost += world_map.get_tile_cost(node.x, node.y) + 1
        node = node.get_parent()
    return cost


def f_cost(goal: tuple, node: Node, world_map: World):  # funkcja zwracająca sumę funkcji kosztu oraz heurestyki
    return g_cost(node, world_map) + h_cost(goal, node)


def print_moves(node: Node):  # zwraca listę ruchów jakie należy wykonać by dotrzeć do punktu docelowego
    moves_list = []
    while node.parent is not None:
        moves_list.append(node.action)
        node = node.parent
    return moves_list[::-1]


def is_goal_reached(element: Node, goal: tuple):
    return (element.x, element.y) == goal


def a_star_search(state: tuple, goal: tuple, agent_direction: list, world_map: World):
    fringe = []
    explored = []

    starting_node = Node(state[0], state[1], agent_direction, None, None)

    fringe.append((starting_node, 0))

    while fringe:

        element = fringe.pop(0)

        if is_goal_reached(element[0], goal):
            return print_moves(element[0])

        explored.append(element)

        for (action, elem_state) in element[0].successor():

            fringe_tuple = []
            fringe_tuple_prio = []
            explored_tuple = []

            for (node, cost) in fringe:
                fringe_tuple.append(((node.get_x(), node.get_y()), node.get_direction()))

                fringe_tuple_prio.append((((node.get_x(), node.get_y()), node.get_direction()), cost))

            for (node, cost) in explored:
                explored_tuple.append(((node.get_x(), node.get_y()), node.get_direction()))

            new_node = Node(elem_state[0][0], elem_state[0][1], elem_state[1], action, element[0])
            p = f_cost(goal, new_node, world_map)

            if elem_state not in fringe_tuple and elem_state not in explored_tuple:
                fringe.append((new_node, p))
                fringe = sorted(fringe, key=itemgetter(1))

            elif elem_state in fringe_tuple:
                i = 0
                for (state_prio, r) in fringe_tuple_prio:
                    if str(state_prio) == str(elem_state):
                        if r > p:
                            fringe.insert(i, (new_node, p))
                            fringe.pop(i + 1)
                            fringe = sorted(fringe, key=itemgetter(1))
                            break
                    i += 1
