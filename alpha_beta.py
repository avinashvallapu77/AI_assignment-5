from tic_tac_toe import TicTacToe


def alpha_beta(state, depth, alpha, beta, maximizing_player):
    if state.current_winner == 'X':
        return 10 - depth
    elif state.current_winner == 'O':
        return depth - 10
    elif not state.empty_squares():
        return 0

    if maximizing_player:
        max_eval = -float('inf')
        for move in state.available_moves():
            state.make_move(move, 'X')
            eval = alpha_beta(state, depth+1, alpha, beta, False)
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
            eval = alpha_beta(state, depth+1, alpha, beta, True)
            state.board[move] = ' '
            state.current_winner = None
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


if __name__ == '__main__':
    game = TicTacToe()
    print(alpha_beta(game, 0, -float('inf'), float('inf'), True))
