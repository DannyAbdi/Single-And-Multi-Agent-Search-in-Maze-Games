from maze import *
from player import *
from button import *
from playerController import *
from dfs import *
from bfs import *

pygame.init()
player = Player(TILE_SIZE, TILE_SIZE)

maze = Maze(small_maze)

player_controller = PlayerController(player, maze)
easy_button = Button(easy_button, 150, 500, small_maze, player_controller)  # not in correct position
normal_button = Button(normal_button, 300, 500, medium_maze, player_controller)  # not in correct position
hard_button = Button(hard_button, 426, 500, large_maze, player_controller)  # not in correct position
dfs_solver = DFS()
bfs_solver = BFS()
player_controller.set_dfs_solver(dfs_solver)
player_controller.set_bfs_solver(bfs_solver)

run = True
while run:
    timer.tick(FPS)
    maze.draw()
    player.draw()
    easy_button.draw()
    normal_button.draw()
    hard_button.draw()

    player_controller.move_to_goal_dfs()  # comment this line out to test bfs
    # player_controller.move_to_goal_bfs() # uncomment this line out to test bfs

    direction = pygame.key.get_pressed()
    player_controller.move_player(direction)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            easy_button.handle_mouse_click(mouse_pos, maze)
            normal_button.handle_mouse_click(mouse_pos, maze)
            hard_button.handle_mouse_click(mouse_pos, maze)

            if easy_button.is_clicked or normal_button.is_clicked or hard_button.is_clicked:
                player_controller.reset_player_position()

    pygame.display.flip()
pygame.quit()
