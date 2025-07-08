import pygame
import os

base_path = os.path.dirname(__file__)

class Game():
    def __init__(self, width, height):
        self.size = width, height
        self.score = [0,0]
        self.players = ("X","O")
        self.board = [[None,None,None],
                      [None,None,None],
                      [None,None,None]]
        self.turn = 0
        self.circle = os.path.join(base_path, "images", "circle.png")
        self.cross = os.path.join(base_path, "images", "cross.png")
    
    def bg_init(self, display):
        display.fill((40,40,40))
        bg = pygame.image.load(os.path.join(base_path, "images", "board.png"))
        display.blit(bg, (0,0))
        return

    def draw(self, display, but_list):
        for but in but_list:
            but.draw(display)

    def change_turn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0
    def draw_player(self, pos, display, game):
        if self.players[self.turn] == "X":
            #draw cross
            btn = pos[1]
            btn.player = self.players[self.turn]
            btn.draw(display, self.cross, pos[0])
            game.board[btn.pos[0]][btn.pos[1]] = self.players[self.turn]
            for i, but in enumerate(but_list):
                if but == btn:
                    but_list.pop(i)
                    break
            return btn.pos, btn.player
        else:
            #draw circle
            btn = pos[1]
            btn.player = self.players[self.turn]
            btn.draw(display, self.circle, pos[0])
            game.board[btn.pos[0]][btn.pos[1]] = self.players[self.turn]
            for i, but in enumerate(but_list):
                if but == btn:
                    but_list.pop(i)
                    break
            return btn.pos, btn.player
    
    def check_score(self, pos, player):
        # V_check
        def h_check(board, pos, player):
            for line in board:
                line_check = True
                for item in line:
                    if item != player:
                        line_check = False
                        pass
                if line_check:
                    return True
            return False
        # H_check
        def v_check(board, pos, player):
            for y in range(len(board)):
                line_check = True
                for x in range(len(board[y])):
                    if board[x][y] != player:
                        line_check = False
                if line_check:
                    return True
            return False

        # D_check
        def d_check(board, pos, player):
            down = True
            up = True
            # down
            for i in range(len(board)):
                if board[i][i] != player:
                    down = False
                    break
            
            # up
            for i in range(len(board)):
                y = len(board) -1
                if board[i][y-i] != player:
                    up = False
                    break
            return up or down
        
        return v_check(self.board, pos, player) or h_check(self.board, pos, player) or d_check(self.board, pos, player)

    def display_win(self, display, player):
        font = pygame.font.Font(os.path.join(base_path, "fonts", "FreeSansBold.ttf"), 50)
        player = font.render(f"{player}'s",True,(255,255,255),None)
        wins = font.render(f"win",True,(255,255,255),None)
        player_rect = player.get_rect()
        player_rect.center = (350, 100)
        wins_rect = wins.get_rect()
        wins_rect.center = (350,150)

        display.blit(player, player_rect)
        display.blit(wins, wins_rect)


        font = pygame.font.Font(os.path.join(base_path, "fonts", "FreeSansBold.ttf"), 20)
        q = font.render(f"Press ESC to quit",True,(255,255,255),(20,20,20))
        q_rect = q.get_rect()
        q_rect.center = (350, 350)

        display.blit(q, q_rect)
    
    def display_draw(self):
        font = pygame.font.Font(os.path.join(base_path, "fonts", "FreeSansBold.ttf"), 50)
        draw = font.render(f"It's a draw",True,(255,255,255),None)
        draw_rect = draw.get_rect()
        draw_rect.center = (350, 100)

        display.blit(draw, draw_rect)

        font = pygame.font.Font(os.path.join(base_path, "fonts", "FreeSansBold.ttf"), 20)
        q = font.render(f"Press ESC to quit",True,(255,255,255),(20,20,20))
        q_rect = q.get_rect()
        q_rect.center = (350, 350)

        display.blit(q, q_rect)

class Button():
    def __init__(self, coords,width,height):
        super().__init__()
        self.b_size = (width/ 3, height/ 3)
        self.coords = coords[0]
        self.rect = pygame.Rect(coords[0][0]+3, coords[0][1] + 3, self.b_size[0] - 3, self.b_size[1] - 3)
        self.player = None
        self.pos = coords[1]
    
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    return self.coords, self
                
    def draw(self, display, img=None, pos=None):
        pygame.draw.rect(display,(20,20,20), self.rect)
        if self.player != None:
            player = pygame.image.load(img)
            display.blit(player, pos)
            return


def init_buttons(width,height):
    # coordinate list containing two tuples one for the display coordinates and the other for the gameboard coordinates
    coords = [((0,0),(0,0)),((700 / 3, 0),(0,1)),((700 / 3 * 2, 0),(0,2)),
              ((0,700 / 3),(1,0)),((700 / 3, 700 / 3),(1,1)),((700 / 3 * 2, 700 / 3),(1,2)),
              ((0,700 / 3 * 2),(2,0)),((700 / 3, 700 / 3* 2),(2,1)),((700 / 3 * 2, 700 / 3* 2),(2,2))]
    
    but_list = []

    for coord in coords:
        but_list.append(Button(coord, width, height))
    
    return but_list


width, height = 700,700

game = Game(width, height)

pygame.init()

display = pygame.display.set_mode((700,700))

but_list = init_buttons(width, height)

init = False

stop = False

running = True
while running:
    if not init:
        game.bg_init(display)
        init = True

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False
    if len(but_list) == 0 and not stop:
        game.display_draw()
    for but in but_list:
        game.draw(display, but_list)
        if not stop:
            pos = but.update(events)
        if pos != None:
            current_pos = game.draw_player(pos, display, game)
            if game.check_score(current_pos[0], current_pos[1]):
                game.display_win(display, current_pos[1])
                if current_pos[1] == "X":
                    game.score[0] += 1
                else:
                    game.score[1] += 1
                #game.display_score()
                stop = True
            if not stop:
                game.change_turn()



    pygame.display.update()

pygame.quit()