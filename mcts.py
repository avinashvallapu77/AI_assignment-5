import random

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

    def uct(self):
        if self.visits == 0:
            return float('inf')

        return (self.wins / self.visits) + math.sqrt(
            2 * math.log(self.parent.visits) / self.visits
        )


class MCTS:
    def __init__(self, iterations=1000):
        self.iterations = iterations

    def search(self, initial_state):
        root = Node(initial_state)

        for _ in range(self.iterations):
            node = root
            state = initial_state

            while node.children:
                node = max(node.children, key=lambda n: n.uct())

            if state.empty_squares():
                move = random.choice(state.available_moves())
                state.make_move(move, 'X')
                child = Node(state, node)
                node.children.append(child)
                node = child

            winner = self.simulate_random_game(state)
              while node is not None:
                node.visits += 1
                if winner == 'X':
                    node.wins += 1
                node = node.parent

        return max(root.children, key=lambda n: n.visits)

    def simulate_random_game(self, state):
        current = 'O'

        while state.empty_squares():
            move = random.choice(state.available_moves())
            state.make_move(move, current)
            current = 'X' if current == 'O' else 'O'

        return state.current_winner
if __name__ == '__main__':
    game = TicTacToe()
    ai = MCTS()
    best = ai.search(game)
    print(best.visits)
