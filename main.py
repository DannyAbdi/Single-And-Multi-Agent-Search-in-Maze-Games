from maze import *
from player import *
from button import *
from playerController import *
from dfs import *
from bfs import *
from dijkstra import *
from aStar import *
from enemy import *
from minmax import *

pygame.init()
maze = Maze(small_maze)
player = Player(TILE_SIZE, TILE_SIZE)
enemy1 = Enemy(maze)
depth = 3

player_controller = PlayerController(player, maze)
easy_button = Button(easy_button, 150, 10, small_maze, player_controller)
normal_button = Button(normal_button, 300, 10, medium_maze, player_controller)
hard_button = Button(hard_button, 426, 10, large_maze, player_controller)
dfs_solver = DFS()
bfs_solver = BFS()
dijkstra_solver = Dijkstra(maze)
aStar_solver = AStar(maze)
minmax_solver = MinMax(maze)
player_controller.set_dfs_solver(dfs_solver)
player_controller.set_bfs_solver(bfs_solver)
player_controller.set_dijkstra_solver(dijkstra_solver)
player_controller.set_astar_solver(aStar_solver)
# best_move = minmax_solver.minmax(player_position, enemy_position, depth, True)

run = True
while run:
    timer.tick(FPS)
    maze.draw()
    player.draw(screen)
    enemy1.draw(screen)
    easy_button.draw()
    normal_button.draw()
    hard_button.draw()

    # player_controller.move_to_goal_dfs()
    player_controller.move_to_goal_bfs()
    # player_controller.move_to_goal_dijkstra()
    # player_controller.move_to_goal_astar()

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
                enemy1.reset_position()

    pygame.display.flip()
pygame.quit()
