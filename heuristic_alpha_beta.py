from tic_tac_toe import TicTacToe


def heuristic(board):
    score = 0

    winning_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for pos in winning_positions:
        line = [board[i] for i in pos]

        if line.count('X') == 2 and line.count(' ') == 1:
            score += 5
        elif line.count('O') == 2 and line.count(' ') == 1:
            score -= 5

    return score


def heuristic_alpha_beta(state, depth, alpha, beta, maximizing):
    if depth == 0 or state.current_winner or not state.empty_squares():
        return heuristic(state.board)

    if maximizing:
        max_eval = -float('inf')
        for move in state.available_moves():
            state.make_move(move, 'X')
            eval = heuristic_alpha_beta(state, depth-1, alpha, beta, False)
            state.board[move] = ' '
            state.current_winner = None
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval

    else:
        min_eval = float('inf')
        for move in state.available_moves():
            state.make_move(move, 'O')
            eval = heuristic_alpha_beta(state, depth-1, alpha, beta, True)
            state.board[move] = ' '
            state.current_winner = None
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
