import pygame
pygame.init()

navy = (0,0,128)
cobalt = (61,89,171)

class Mine:
    def __init__(self, x, y, player):
        self.X = x
        self.Y = y
        self.Player = player
        self.Dead
        
    def Detect(self):
        print("TODO: find a way to detect the boats in the area.")
    
    def Explode(self):
        print("TODO: (when the sprites are made) create the exploding animation 75x75")
        print("TODO: activate the decrease health function of the boats in the area")
    
    def Die(self): self.Dead = True
    def Draw(self):
        if self.Dead:
            print("TODO: (when the sprites are made) create the dead mine sprite (or animation) on the tile. (background)")

class Options:
    def __init__(self,x,y):
        self.X = x
        self.Y = y

        self.Caption = None
        self.Menu = None
        self.Show_sub_menu = False
        self.Sub_menu = None

    def Add_menu(self, caption, menu, submenu=None):
        self.Caption = caption
        self.Menu = menu
        self.Sub_menu = submenu
        self.Show_sub_menu = False

    def Clear(self):
        self.Menu = None
        self.Sub_menu = None
        self.Show_sub_menu = False


    def Draw(self):
        if not self.Menu == None:
            Text_draw(self.Caption, 40, self.X, self.Y-40)
            self.Menu.Draw()
            if not self.Sub_menu == None:
                if self.Show_sub_menu:
                    self.Sub_menu.Draw()


class Boat:
    def __init__(self, x, y, length, name="unnamed boat"):
        self.X = x
        self.Y = y
        self.Length = length
        self.Stance = "defense"
        self.Pos = [grid.Tiles[x][y].X, grid.Tiles[x][y].Y]

        self.Movement = 5 - self.Length
        self.Range_def = self.Length + 1
        self.Range_att = self.Length

        self.Name = name
        self.Health = self.Length

        self.Menu = grid.Menu

        self.Menu_actions = Container(self.Menu.X, self.Menu.Y, 80, 100, 25, 0)
        self.Menu_actions.Add_button(navy, cobalt, self.Show_submenu, "Movement")
        self.Menu_actions.Add_button(navy, cobalt, self.Attack, "Attack")
        self.Menu_actions_move = Container(self.Menu.X + self.Menu_actions.Width, self.Menu_actions.Y, 80, 100, 25, 0)
        self.Menu_actions_move.Add_button(navy, cobalt, self.Move, "Move")
        self.Menu_actions_move.Add_button(navy, cobalt, self.Stance_change, "stance")
    
    def Tell_tile(self):
        if self.Stance == "defense":
            for x in range(self.X, self.X - self.Length + 1):
                grid.Tiles[x][self.Y]
        else:
            for y in range(self.Y, self.Y + self.Length - 1):
                grid.Tiles[self.X][y]
    
    def Show_submenu(self): self.Menu.Show_sub_menu = True
    def Show_menu(self): self.Menu.Add_menu(self.Name, self.Menu_actions, self.Menu_actions_move)
    def Attack(self):
        if self.Stance == "defense":
            for x in range(self.X, self.X + self.Length):
                y = self.Y - self.Range_def
                for i in range(y, self.Y + self.Range_def + 1):
                    if not(i < 0) and not(i > 19):
                        if i != self.Y:
                            grid.Tiles[x][i].Click(self.Attack_on, (204,0,0))
        else:
            for Y in range(self.Y, self.Y + self.Length):
                X = self.X + self.Length - 1
                y = Y - self.Range_att
                while y <= Y + self.Range_att:
                    x = X - self.Range_att
                    while x <= X + self.Range_att:
                        if not(self.Y <= y < self.Y + self.Length and x == X):
                            if x == X or y == Y:
                                grid.Tiles[x][y].Click(self.Attack_on, (204,0,0))
                        x = x + 1
                    y = y + 1
                            
        self.Menu.Clear()
    def Move(self):
        if self.Stance == "defense":
            for boat_tile in range(self.X, self.X + self.Length):
                y = self.Y - self.Movement
                a = boat_tile - self.Movement
                b = self.Movement
                x = 1
                while y <= self.Y + self.Movement:
                    for i in range(0,x):
                        if not(a+b+i < 0) and not(a+b+i > 19) and not(y < 0) and not(y > 19):
                            if not(y == self.Y and a + b + i == self.X + self.Length - 1):
                                grid.Tiles[a+b+i][y].Click(self.Move_to, (255,255,153), self.Length, self.Stance)
                    if y >= self.Y:
                        x -= 2
                        b += 1
                    else:
                        x += 2
                        b -= 1
                    y += 1

        self.Menu.Clear()

    def Attack_on(self,x,y):
        print("Attacking x" + str(x) + " y" + str(y))
        shot = pygame.mixer.Sound("sounds\\boat_shot.wav")
        shot.play()
        self.Menu.Clear()

    def Move_to(self,x,y):
        if self.Stance == "defense":
            self.X = x - self.Length + 1
            self.Y = y
            self.Pos[0] = grid.Tiles[x - self.Length + 1][y].X
            self.Pos[1] = grid.Tiles[x - self.Length + 1][y].Y

    def Stance_change(self):
        if self.Stance == "attack":
            self.Stance = "defense"
            self.Pos[0] = grid.Tiles[self.X][self.Y].X
        else:
            self.Stance = "attack"
            self.Pos[0] = grid.Tiles[self.X + self.Length - 1][self.Y].X
        
        self.Menu.Clear()

    def Hover(self):
        if self.Stance == "defense":
            if self.Pos[0] < pygame.mouse.get_pos()[0] < self.Pos[0] + (self.Length * grid.Tiles[self.X][self.Y].Size):
                if self.Pos[1]< pygame.mouse.get_pos()[1] < self.Pos[1] + grid.Tiles[self.X][self.Y].Size: return True
            return False
        else:
            if self.Pos[0] < pygame.mouse.get_pos()[0] < self.Pos[0] + grid.Tiles[self.X][self.Y].Size:
                if self.Pos[1] < pygame.mouse.get_pos()[1] < self.Pos[1] + (self.Length * grid.Tiles[self.X][self.Y].Size): return True
            return False

    def Draw(self):
        if self.Hover() and pygame.mouse.get_pressed()[0]:
            grid.Clear()
            self.Show_menu()

        if self.Stance == "attack":
            pygame.Surface.blit(game.Display,  pygame.image.load('images\\boats\\' + str(self.Length) + '\\attack.png'), [grid.Tiles[self.X + self.Length - 1][self.Y].X, self.Pos[1]])
        else:
            pygame.Surface.blit(game.Display,  pygame.image.load('images\\boats\\' + str(self.Length) + '\\defense.png'), [self.Pos[0], self.Pos[1]])
        
class Tile:
    def __init__(self, x, y, pos, size, menu):
        self.X = x
        self.Y = y
        self.Pos = pos
        self.Size = size
        self.Color = (0,0,0)

        self.Menu = menu

        self.Boat = None

        self.Function_boat = None
        self.Function = None

    def Clear(self):
        self.Boat = None
        self.Function = None
        self.Color = (0,0,0)
        self.Function_boat = None
    
    def Click(self, function, color, length=None, stance=None):
        self.Color = color
        self.Function = function
        if length != None and stance != None:
            self.Function_boat = [length, stance]
    
    def Hover(self):
        if self.X < pygame.mouse.get_pos()[0] < self.X + self.Size:
            if self.Y < pygame.mouse.get_pos()[1] < self.Y + self.Size: return True
        return False
    def Ghost(self):
        if self.Function_boat[1] == "defense":
            x = self.X - (self.Function_boat[0] - 1) * self.Size
            y = self.Y
        else:
            x = self.X
            y = self.Y
        pygame.Surface.blit(game.Display, pygame.image.load("images\\boats\\" + str(self.Function_boat[0]) + "\\" + str(self.Function_boat[1]) + ".png"), [x,y])

    def Draw(self):
        pygame.draw.rect(game.Display, self.Color, (self.X, self.Y, self.Size, self.Size))
        pygame.draw.lines(game.Display, (100,100,100), True, [(self.X,self.Y), (self.X+self.Size,self.Y), (self.X+self.Size,self.Y+self.Size), (self.X,self.Y+self.Size)],2)
        
        if self.Hover():
            if self.Function_boat != None:
                self.Ghost()
            if pygame.mouse.get_pressed()[0]:
                if self.Function == None:
                    self.Menu.Clear()
                    grid.Clear()
                else:
                    self.Function(self.Pos[0], self.Pos[1])
                    grid.Clear()

class Grid:
    def __init__(self,x,y,size,tilesize, menu):
        self.Tile_size = tilesize
        self.Size = size
        self.X = x
        self.Y = y

        self.Menu = menu
        
        self.Tile_x = self.X
        self.Tile_y = self.Y
        self.Tiles = [''] * self.Size
        for x in range(0, self.Size):
            self.Tiles[x] = [''] * self.Size
            for y in range(0, self.Size):
                self.Tiles[x][y] = Tile(self.Tile_x, self.Tile_y, [x,y], self.Tile_size, self.Menu)
                self.Tile_y = self.Tile_y + self.Tile_size
            self.Tile_x = self.Tile_x + self.Tile_size
            self.Tile_y = self.Y

    def Change_color(self, tile_x, tile_y, color):
        self.Tiles[tile_x][tile_y].Color = color

    def Clear(self):
        for y in range(0, self.Size):
            for x in range(0, self.Size):
                self.Tiles[x][y].Clear()

    def Draw(self):
        for y in range(0, self.Size):
            for x in range(0, self.Size):
                self.Tiles[x][y].Draw()
        self.Menu.Draw()

class Animation:
    def __init__(self, x, y, imagefolder, imageamount, speed, animating=True):
        self.X = x
        self.Y = y
        self.Image_folder = imagefolder
        self.Image_amount = imageamount
        self.Image = 1
        self.Speed = speed
        self.I = 0
        self.Animating = animating
    
    def Draw(self):
        if self.Animating:
            pygame.Surface.blit(game.Display, pygame.image.load(self.Image_folder + "\\" + str(self.Image) + ".png"), [self.X, self.Y])
            if self.I > self.Speed:
                self.Image += 1
                if self.Image == self.Image_amount:
                    self.Image = 1
                self.I = 0
            self.I += 1

class Container:
    def __init__(self, x, y, width, height, buttonheight, space):
        self.X = x
        self.Y = y
        self.Width = width
        self.Height = height
        self.Buttonheight = buttonheight
        self.Space = space
        self.Buttons = [""] * int((self.Height + self.Space) / (self.Buttonheight + self.Space))

    def Add_button(self, color, hovercolor, function, text, textcolor=(255,255,255)):
        a = 0
        for button in self.Buttons:
            if button == "":
                self.Buttons[a] = Button(self.X, self.Y+self.Buttonheight*a+self.Space*a, self.Width, self.Buttonheight, function, color, hovercolor, text, textcolor)
                break
            a += 1
    
    def Draw(self):
        for button in self.Buttons:
            if button == "": break
            else: button.Draw()

class Button:
    def __init__(self, x, y, width, height, function, color, hovercolor, text, constant=False, textcolor=(255,255,255)):
        self.X = x
        self.Y = y
        self.Width = width
        self.Height = height

        self.Function = function
        self.Color = color
        self.Color_hover = hovercolor
        self.Color_text = textcolor
        self.Text = text

        self.Constant = constant

        self.Pressing = False
        self.Pressed = False
    
    def Click(self): return pygame.mouse.get_pressed()[0]

    def Hover(self):
        if self.X < pygame.mouse.get_pos()[0] < self.X + self.Width:
            if self.Y < pygame.mouse.get_pos()[1] < self.Y + self.Height: return True
        return False

    def Draw(self):
        if self.Hover():
            pygame.draw.rect(game.Display, self.Color_hover, (self.X, self.Y, self.Width, self.Height))

            if self.Constant == True:
                if self.Click():
                    self.Pressing = True
                else:
                    if self.Pressing:
                        if self.Pressed:
                            self.Pressed = False
                        else:
                            self.Pressed = True
                        self.Pressing = False
            else:
                if self.Click(): self.Function()

        else:
            pygame.draw.rect(game.Display, self.Color, (self.X, self.Y, self.Width, self.Height))
        Text_draw(self.Text, int(self.Height/1.15), self.X + 5, self.Y + self.Height / 5, self.Color_text)

        if self.Constant == True:
            if self.Pressed:
                self.Function()

class Game:
    def __init__(self):
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.Exit = False

        self.Width = 1360
        self.Height = 768
        self.Display = pygame.display.set_mode((self.Width, self.Height))
        
        self.Level = "menu"

    def draw(self): self.Display.fill((0,0,0))
    def tick(self): self.clock.tick(self.FPS)
    def loop(self):
        while not self.Exit:
            if self.Level == "menu":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.Exit = True
                self.draw()
                grid.Draw()
                boat.Draw()
                pygame.display.update()
                self.tick()
            else: self.Exit = True

def Text_draw(text, size, x, y, textcolor=(255,255,255)):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, textcolor)
    game.Display.blit(screen_text, [x,y])

game = Game()


def function():
    print("hoi")

grid = Grid(50,50,20,25,Options(100 + 20 * 25, 100))
boat = Boat(2,2,2)
boat2 = Boat(5,6,4)
boat3 = Boat(12,10,3)


game.loop()

pygame.quit()
quit()
