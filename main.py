from maze import *
from player import *
from button import *
from playerController import *
from dfs import *
from bfs import *
from dijkstra import *

pygame.init()
player = Player(TILE_SIZE, TILE_SIZE)

maze = Maze(small_maze)

player_controller = PlayerController(player, maze)
easy_button = Button(easy_button, 150, 500, small_maze, player_controller)
normal_button = Button(normal_button, 300, 500, medium_maze, player_controller)
hard_button = Button(hard_button, 426, 500, large_maze, player_controller)
dfs_solver = DFS()
bfs_solver = BFS()
dijkstra_solver = Dijkstra(maze)
player_controller.set_dfs_solver(dfs_solver)
player_controller.set_bfs_solver(bfs_solver)
player_controller.set_dijkstra_solver(dijkstra_solver)

run = True
while run:
    timer.tick(FPS)
    maze.draw()
    player.draw()
    easy_button.draw()
    normal_button.draw()
    hard_button.draw()

    # player_controller.move_to_goal_dfs()
    # player_controller.move_to_goal_bfs()
    player_controller.move_to_goal_dijkstra()

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
