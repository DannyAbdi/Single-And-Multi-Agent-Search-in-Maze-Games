from minmax import MinMax


class Expectimax(MinMax):
    """
    Initializes an Expectimax object.

    :param maze: The maze used for navigation and solving.
    """
    def __init__(self, maze):
        super().__init__(maze)

    """
    Performs the Expectimax algorithm to determine the best move the enemy can take.

    :param player_position: The current position of the player agent.
    :param enemy_position: The current position of the enemy agent.
    :param depth: The depth of the Expectimax search tree.
    :param maximising_player: True if maximising player (enemy), False if minimising player (player).
    :return: The best move for the enemy agent.
    """
    def expectimax(self, player_position, enemy_position, depth, maximising_player):
        if depth == 0 or self.game_over():
            # Evaluate the current game state
            return self.evaluate(player_position, enemy_position)

        if maximising_player:
            max_eval = float('-inf')
            valid_moves = self.get_valid_moves(enemy_position)
            for move in valid_moves:
                if self.is_valid_move(move):
                    eval = self.expectimax(player_position, move, depth - 1, False)
                    max_eval = max(max_eval, eval)
            return max_eval
        else:
            total_eval = 0
            valid_moves = self.get_valid_moves(player_position)
            num_moves = len(valid_moves)
            for move in valid_moves:
                if self.is_valid_move(move):
                    eval = self.expectimax(move, enemy_position, depth - 1, True)
                    total_eval += eval
            return total_eval / num_moves