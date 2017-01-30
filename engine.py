import pygame
from module3 import *
pygame.init()

navy = (0,0,128)
cobalt = (61,89,171)
class Highscore:
    def __init__(self):
        self.X = game.Width / 4
        self.Y = game.Height / 10 + 100
        self.Width = game.Width / 2
        self.Level = "highscore"

        self.name= row[0]
        self.name2 = row2[0]  
        self.name3 = row3[0]
        self.name4 = row4[0]
        self.name5 = row5[0]  

        self.gamesp = str(row[1])
        self.gamesp2 = str(row2[1])
        self.gamesp3 = str(row3[1])
        self.gamesp4 = str(row4[1])
        self.gamesp5= str(row5[1])

        self.gamesw = str(row[2])
        self.gamesw2 = str(row2[2])
        self.gamesw3 = str(row3[2])
        self.gamesw4 = str(row4[2])
        self.gamesw5= str(row5[2])

        self.gamesl = str(row[3])
        self.gamesl2 = str(row2[3])
        self.gamesl3 = str(row3[3])
        self.gamesl4 = str(row4[3])
        self.gamesl5= str(row5[3])

        self.button_height = 50
        self.button_color = (224,224,224)
        self.button_color_hover = (160, 160, 160)

        self.Buttons = [
        Button(self.X+650, self.Y+500, 280, 50, self.Menu, self.button_color, self.button_color_hover, "back to main menu")]

    def Start(self): game.Level = "start"
    def Menu(self): game.Level = "menu"
    def Load(self): game.Level = "load"
    def Instructions(self): game.Level = "instructions"
    def Exit(self): game.Level = "exit"

    def Draw(self):
        Text_draw("1", 40, self.X-200, self.Y+50)
        Text_draw("2", 40, self.X-200, self.Y+90)
        Text_draw("3", 40, self.X-200, self.Y+130)

        Text_draw(self.name, 40, self.X-85, self.Y+50)
        Text_draw(self.name2, 40, self.X-85, self.Y+90)
        Text_draw(self.name3, 40, self.X-85, self.Y+130)
        Text_draw(self.name4, 40,  self.X-85, self.Y+170)
        Text_draw(self.name5, 40,  self.X-85, self.Y+210)

        Text_draw(self.gamesp, 40, self.X+120, self.Y+50)
        Text_draw(self.gamesp2, 40, self.X+120, self.Y+90)
        Text_draw(self.gamesp3, 40, self.X+120, self.Y+130)
        Text_draw(self.gamesp4, 40, self.X+120, self.Y+170)
        Text_draw(self.gamesp5, 40, self.X+120, self.Y+210)

        Text_draw(self.gamesw, 40, self.X+320, self.Y+50)
        Text_draw(self.gamesw2, 40, self.X+320, self.Y+90)
        Text_draw(self.gamesw3, 40, self.X+320, self.Y+130)
        Text_draw(self.gamesw4, 40, self.X+320, self.Y+170)
        Text_draw(self.gamesw5, 40, self.X+320, self.Y+210)

        Text_draw(self.gamesl, 40, self.X+520, self.Y+50)
        Text_draw(self.gamesl2, 40, self.X+520, self.Y+90)
        Text_draw(self.gamesl3, 40, self.X+520, self.Y+130)
        Text_draw(self.gamesl4, 40, self.X+520, self.Y+170)
        Text_draw(self.gamesl5, 40, self.X+520, self.Y+210)

        for button in self.Buttons:
            button.Draw()

class Menu:
    def __init__(self):
        self.X = game.Width / 4
        self.Y = game.Height / 10 + 100
        self.Width = game.Width / 2
        self.Level = "menu"

        self.button_height = 50
        self.button_color = (224,224,224)
        self.button_color_hover = (160, 160, 160)

        self.Buttons = [
        Button(self.X+93, self.Y+240, 498, 69, self.Start, self.button_color, self.button_color_hover, "Start game"),\
        Button(self.X+93, self.Y+320, 498, 69, self.Load, self.button_color, self.button_color_hover, "Resume game"),\
        Button(self.X+93, self.Y+400, 498, 69, self.Instructions, self.button_color, self.button_color_hover, "Instructions"),\
        Button(self.X+93, self.Y+480, 498, 69, self.Highscore, self.button_color, self.button_color_hover, "Highscore"),\
        Button(self.X+870, self.Y+520, 63, 54, self.Instructions, self.button_color, self.button_color_hover, "S"),\
        Button(self.X+946, self.Y+520, 61, 54, self.Exit, self.button_color, self.button_color_hover, "E")]

    def Start(self): game.Level = "start"
    def Menu(self): game.Level = "menu"
    def Load(self): game.Level = "load"
    def Highscore(self): game.Level = "highscore"
    def Instructions(self): game.Level = "instructions"
    def Exit(self): game.Level = "exit"

    def Draw(self):
        #text_draw
        for button in self.Buttons:
            button.Draw()

class temp_card_holder:
    def __init__(self, name, id, desc, amount):
        self.Name = name
        self.ID = id
        self.Desc = desc
        self.Amount = amount

class Card:
    def __init__(self, x, y, width, height, name, desc, function, i, deck):
        self.X = x
        self.Y = y
        self.Width = width
        self.Height = height
        self.Name = name
        self.Desc = desc
        self.Function = function
        self.Active = True
        self.Deck = deck
        self.ID = i

        self.Pressed = False
        self.Pressing = False
    
    def Hover(self):
        if self.X < pygame.mouse.get_pos()[0] < self.X + self.Width:
            if self.Y < pygame.mouse.get_pos()[1] < self.Y + self.Height: return True
        return False
    
    def Click(self): return pygame.mouse.get_pressed()[0]

    def Draw(self):
        if self.Active:
            if self.Hover():
                # pygame.blit(game.Display, pygame.image.load("images\\cards\\" + self.name + "hover.png"), [self.X, self.Y])
                pygame.draw.rect(game.Display, (100,100,100), (self.X, self.Y, self.Width, self.Height))
                Text_draw(str(self.ID), 15, self.X, self.Y-15)
                Text_draw(self.Name, 15, self.X, self.Y - 40)
                self.Pressing = self.Click()
                if self.Pressing:
                    self.Pressed = True
                    self.Pressing = False
                else:
                    if self.Pressed:
                        self.Function()
                        self.Deck.Remove_card(self.ID)
                        self.Pressed = False


            else:
                pygame.draw.rect(game.Display, (50,50,50), (self.X, self.Y, self.Width, self.Height))
                Text_draw(str(self.ID), 15, self.X, self.Y-15)
                Text_draw(self.Name, 10, self.X, self.Y - 40)
                # pygame.blit(game.Display, pygame.image.load("images\\cards\\" + self.name + "active.png"), [self.X, self.Y])
        else:
            # pygame.blit(game.Display, pygame.image.load("images\\cards\\" + self.name + "inactive.png"), [self.X, self.Y])
            pygame.draw.rect(game.Display, (255,0,0), (self.X, self.Y, self.Width, self.Height))

class Deck:
    def __init__(self, x, y, player, limit):
        self.X = x
        self.Y = y
        self.Player = player
        self.Limit = limit

        self.Cards = [""] * self.Limit
    
    def Add_card(self, name, desc, function):
        i = 0
        x = self.X
        y = self.Y
        w = 50
        h = 100

        for card in self.Cards:
            if card == "":
                self.Cards[i] = Card(x, y, w, h, name, desc, function, i, self)
                break
            x = x + w + 10
            i += 1

    def Remove_card(self, element):
        del self.Cards[element]
        for i in range(element, self.Limit - 1):
            if self.Cards[i] != "":
                self.Cards[i].ID -= 1
                self.Cards[i].X -= self.Cards[i].Width + 10
        self.Cards.append("")
    
    def Activate(self):
        for card in self.Cards:
            if card == "": break
            else:
                if card.Active: card.Active = False
                else: card.Active = True

    def Draw(self):
        for card in self.Cards:
            if card == "": break
            else: card.Draw()        
        
class Hand:
    def __init__(self, x, y, player):
        self.X = x
        self.Y = y
        self.Player = player

        self.Decks = [Deck(self.X, self.Y, self.Player, 6), Deck(self.X, self.Y, self.Player, 7), Deck(self.X, self.Y, self.Player, 8)]
        self.Normal = self.Decks[0]
        self.Traps = self.Decks[1]
        self.Special = self.Decks[2]
    
    def Activate(self):
        for deck in self.Decks:
            deck.Activate()


    def Draw(self):
        for deck in self.Decks:
            deck.Draw()

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
        self.Menu_x = self.X
        self.Menu_y = self.Y + 100
        self.Stats_x = self.X
        self.Stats_y = self.Y

        self.Caption = None
        self.Boat_class = None
        self.Boat_range_att = None
        self.Boat_range_def = None
        self.Boat_moves = None
        self.Boat_health = None
        self.Boat_perks = None

        self.Menu = None
        self.Show_sub_menu = False
        self.Sub_menu = None
    
    def Add_boat(self, length, attrange, defrange, moves, health, perks):
        self.Boat_class = length
        self.Boat_range_att = attrange
        self.Boat_range_def = defrange
        self.Boat_moves = moves
        self.Boat_health = health
        self.Boat_perks = perks

    def Add_menu(self, caption, menu, submenu=None):
        self.Caption = caption
        self.Menu = menu
        self.Sub_menu = submenu
        self.Show_sub_menu = False

    def Clear(self):
        self.Menu = None
        self.Sub_menu = None
        self.Show_sub_menu = False

        self.Boat_class = None
        self.Boat_range_att = None
        self.Boat_range_def = None
        self.Boat_moves = None
        self.Boat_health = None
        self.Boat_perks = None

    def Draw(self):
        if not self.Menu == None:
            Text_draw(self.Caption, 40, self.X, self.Y-40)

            if self.Boat_class != None:
                Text_draw("Class: " + str(self.Boat_class), 25, self.Stats_x, self.Stats_y)
                Text_draw("Moves: " + str(self.Boat_moves), 25, self.Stats_x, self.Stats_y + 25)
                Text_draw("Def Range: " + str(self.Boat_range_def), 25, self.Stats_x, self.Stats_y + 50)
                Text_draw("Health: " + str(self.Boat_health), 25, self.Stats_x + 150, self.Stats_y)
                Text_draw("Perks: " + str(self.Boat_perks), 25, self.Stats_x + 150, self.Stats_y + 25)
                Text_draw("Att Range: " + str(self.Boat_range_att), 25, self.Stats_x + 150, self.Stats_y + 50)

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
        self.Perks = None

        self.Menu = grid.Menu

        self.Menu_actions = Container(self.Menu.Menu_x, self.Menu.Menu_y, 80, 100, 25, 0)
        self.Menu_actions.Add_button(navy, cobalt, self.Show_submenu, "Movement")
        self.Menu_actions.Add_button(navy, cobalt, self.Attack, "Attack")
        self.Menu_actions_move = Container(self.Menu.Menu_x + self.Menu_actions.Width, self.Menu_actions.Y, 80, 100, 25, 0)
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
    def Show_menu(self):
        self.Menu.Add_menu(self.Name, self.Menu_actions, self.Menu_actions_move)
        self.Menu.Add_boat(self.Length, self.Range_att, self.Range_def, self.Movement, self.Health, self.Perks)
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
        if self.Stance == "attack":
            for boat_tile in range(self.Y, self.Y + self.Length):
                x = self.X - (self.Movement - self.Length + 1)
                y = boat_tile - self.Movement
                a = 1
                b = self.Movement

                while y <= boat_tile + self.Movement:
                    for i in range(0,a):
                        if not(x+b+i < 0) and not(x+b+i > 19) and not(y < 0) and not(y > 19 - self.Length + 1):
                            if not(y == self.Y and x+b+i == self.X + self.Length - 1):
                                grid.Tiles[x+b+i][y].Click(self.Move_to, (255,255,153), self.Length, self.Stance)
                    if y >= boat_tile:
                        b += 1
                        a -= 2
                    else:
                        b -= 1
                        a += 2
                    y += 1

        self.Menu.Clear()

    def Attack_on(self,x,y):
        print("Attacking x" + str(x) + " y" + str(y))
        shot = pygame.mixer.Sound("sounds\\boat_shot.wav")
        shot.play()
        self.Menu.Clear()

    def Move_to(self,x,y):
        if self.Stance == "attack":
            self.X = x - self.Length + 1
            self.Y = y
            self.Pos[0] = grid.Tiles[x][y].X
            self.Pos[1] = grid.Tiles[x][y].Y

    def Stance_change(self):
        if self.Stance == "attack":
            if self.X < self.Length - 1:
                print("stance changing is not allowed here")
            else:
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
        if self.Function_boat != None and self.Hover():
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
        
        for y in range(0, self.Size):
            for x in range(0, self.Size):
                self.Tiles[x][y].Ghost()

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
                self.Display.blit(boat,(0,0))
                menu.Draw()
                pygame.display.update()
                self.tick()
            elif self.Level == "highscore":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.Exit = True
                self.draw()
                self.Display.blit(boat2,(0,0))
                highscore.Draw()
                pygame.display.update()
                self.tick()
            else: self.Exit = True

def Text_draw(text, size, x, y, textcolor=(255,255,255)):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, textcolor)
    game.Display.blit(screen_text, [x,y])

game = Game()
highscore = Highscore()
menu = Menu()
boat = pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//MAIN_MENU(2)//7.png")
boat2 = pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//HIGHSCORE_MENU(2)//1.png")
game.loop()

pygame.quit()
quit()
