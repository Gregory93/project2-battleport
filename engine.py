import pygame
from module3 import *
pygame.init()

navy = (0,0,128)
cobalt = (61,89,171)
navy = (0,0,128)
cobalt = (61,89,171)

class Player_holder:
    def __init__(self, player1, player2):
        self.Player1 = player1
        self.Player2 = player2

        self.Player = self.Player1
    

    def Change_player(self):
        if self.Player == self.Player1:
            self.Player = self.Player2
        else:
            self.Player = self.Player1

    def Draw(self):
        Text_draw(self.Player, 50, 500, 500)

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

    def Menu(self): game.Level = "menu"

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
class Menu_bar:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Width = game.Width
        self.Height = game.Height / 20
        self.Color = cobalt

        self.end_turn = Button(self.Width-300, self.Y, 150, self.Height, self.End_turn, navy, cobalt, "End turn", False, 35)
        self.pause_menu = Button(self.Width-150, self.Y, 150, self.Height, self.Menu, navy, cobalt, "Pause", False, 35)
    
    def End_turn(self):
        for b in (boat, boat2, boat3):
            b.Moves = b.Movement
            b.Attacked = False
        grid.Clear()
        grid.Menu.Clear()
        player_holder.Change_player()
    
    def Menu(self):
        game.Level = "menu2"

    def Draw(self):
        pygame.draw.rect(game.Display, self.Color, [self.X, self.Y, self.Width, self.Height])
        self.end_turn.Draw()
        self.pause_menu.Draw()
        pygame.draw.line(game.Display, (100,100,100), (self.end_turn.X, self.end_turn.Y), (self.end_turn.X, self.Height), 2)
        pygame.draw.line(game.Display, (100,100,100), (self.pause_menu.X, self.pause_menu.Y), (self.pause_menu.X, self.Height), 2)
        pygame.draw.line(game.Display, (100,100,100), (self.X, self.Height), (self.Width, self.Height), 3)

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

class Boat_menu:
    def __init__(self,x,y):
        self.X = x
        self.Y = y
        self.Boat = None
        self.a = None
        self.m = None
        self.s = None
        
    def Add_boat(self, boat):
        self.Boat = boat
        self.a = Button(self.X, self.Y+90, 85, 30, self.Boat.Attack, navy, cobalt, "Attack")
        self.m = Button(self.X+85, self.Y+90, 85, 30, self.Boat.Move, navy, cobalt, "Move")
        self.s = Button(self.X+170, self.Y+90, 85, 30, self.Boat.Stance_change, navy, cobalt, "Stance")
    
    def Clear(self):
        self.Boat = None
        self.a = None
        self.m = None
        self.s = None
    
    def Draw(self):
        if self.Boat != None:
            Text_draw(self.Boat.Name, 40, self.X, self.Y)
            Text_draw("Health: " + str(self.Boat.Health), 25, self.X, self.Y + 40)
            Text_draw("Moves: " + str(self.Boat.Moves), 25, self.X + 100, self.Y + 40)
            Text_draw("Perks: " + str(self.Boat.Perks), 25, self.X, self.Y + 65)
            if self.a != None:
                self.a.Draw()
                if self.m != None:
                    self.m.Draw()
                    if self.s != None:
                        self.s.Draw()


class Boat:
    def __init__(self, x, y, length, player="blue", name="unnamed boat"):
        self.Player = player
        self.X = x
        self.Y = y
        if self.Player == "blue":
            self.Pos = [grid.Tiles[x][y].X, grid.Tiles[x][y].Y]
        else:
            self.Pos = [grid.Tiles[x][y].X, grid.Tiles[x][y - (length - 1)].Y]
        self.Length = length
        self.Stance = "attack"

        self.Movement = 5 - self.Length
        self.Moves = self.Movement
        self.Range_def = self.Length + 1
        self.Range_att = self.Length
        self.Attacked = False

        self.Name = name
        self.Health = self.Length
        self.Perks = None

        self.Menu = grid.Menu
    
    def Tell_tile(self):
        if self.Stance == "defense":
            if self.Player == "blue":
                for x in range(self.X, self.X - self.Length, -1):
                    grid.Tiles[x][self.Y].Color = (100,100,255)
            else:
                for x in range(self.X, self.X + self.Length):
                    grid.Tiles[x][self.Y].Color = (255,100,100)
        else:
            if self.Player == "blue":
                for y in range(self.Y, self.Y + self.Length):
                    grid.Tiles[self.X][y].Color = (100,100,255)
            else:
                for y in range(self.Y, self.Y - self.Length, -1):
                    grid.Tiles[self.X][y].Color = (255,100,100)

    
    def Attack(self):
        if not self.Attacked:
            if self.Stance == "defense":
                if self.Player == "blue":
                    for x in range(self.X - (self.Length - 1), self.X + 1):
                        y = self.Y - self.Range_def
                        for i in range(y, self.Y + self.Range_def + 1):
                            if not(i < 0) and not(i > 19):
                                if i != self.Y:
                                    grid.Tiles[x][i].Click(self.Attack_on, (204,0,0))
                else:
                    for x in range(self.X, self.X + self.Length):
                        y = self.Y - self.Range_def
                        for i in range(y, self.Y + self.Range_def + 1):
                            if not(i < 0) and not(i > 19):
                                if i != self.Y:
                                    grid.Tiles[x][i].Click(self.Attack_on, (204,0,0))

            else:
                if self.Player == "blue":
                    for Y in range(self.Y, self.Y + self.Length):
                        X = self.X
                        y = Y - self.Range_att
                        while y <= Y + self.Range_att:
                            x = X - self.Range_att
                            while x <= X + self.Range_att:
                                if not(self.Y <= y < self.Y + self.Length and x == X):
                                    if x == X or y == Y:
                                        if not(x < 0) and not(x > 19) and not(y < 0) and not(y > 19):
                                            grid.Tiles[x][y].Click(self.Attack_on, (204,0,0))
                                x = x + 1
                            y = y + 1
                else:
                    for Y in range(self.Y - (self.Length - 1), self.Y + 1):
                        X = self.X
                        y = Y - self.Range_att
                        while y <= Y + self.Range_att:
                            x = X - self.Range_att
                            while x <= X + self.Range_att:
                                if not(self.Y <= y < self.Y - self.Length and x == X):
                                    if x == X or y == Y:
                                        if not(x < 0) and not(x > 19) and not(y < 0) and not(y > 19):
                                            grid.Tiles[x][y].Click(self.Attack_on, (204,0,0))
                                x = x + 1
                            y = y + 1

            self.Menu.Clear()
    def Move(self):
        if not self.Moves <= 0:
            x = self.X - (self.Moves)
            y = self.Y - self.Moves
            a = 1
            b = self.Moves

            while y <= self.Y + self.Moves:
                for i in range(0,a):
                    if not(x+b+i < 0) and not(x+b+i > 19) and not(y < 0) and not(y > 19 - self.Length + 1):
                        if not(y == self.Y and x+b+i == self.X):
                            grid.Tiles[x+b+i][y].Click(self.Move_to, (255,255,153), self.Length, self.Stance)
                if y >= self.Y:
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
        self.Attacked = True

    def Move_to(self,x,y):
        if x < self.X: mx = self.X - x
        elif x > self.X: mx = x - self.X
        else: mx = 0

        if y < self.Y: my = self.Y - y
        elif y > self.Y: my = y - self.Y
        else: my = 0

        m = mx + my
        self.Moves = self.Moves - m

        self.X = x
        self.Y = y
        self.Pos[0] = grid.Tiles[x][y].X
        if self.Player == "blue":
            self.Pos[1] = grid.Tiles[x][y].Y
        else:
            self.Pos[1] = grid.Tiles[x][y - (self.Length - 1)].Y

    def Stance_change(self):
        if self.Moves > 0:
            moved = True
            if self.Player == "blue":
                if self.Stance == "attack":
                    if self.X < self.Length - 1:
                        moved = False
                        print("FAILED TO CHANGE STANCE")
                    else:
                        self.Stance = "defense"
                        self.Pos[0] = grid.Tiles[self.X - (self.Length - 1)][self.Y].X
                else:
                    if self.X > 19 + (self.Length - 1):
                        moved = False
                        print("FAILED TO CHANGE STANCE")
                    else:
                        self.Stance = "attack"
                        self.Pos[0] = grid.Tiles[self.X][self.Y].X
            else:
                if self.Stance == "attack":
                    self.Stance = "defense"
                    self.Pos[1] = grid.Tiles[self.X][self.Y].Y
                else:
                    self.Stance = "attack"
                    self.Pos[1] = grid.Tiles[self.X][self.Y - (self.Length - 1)].Y
            if moved: self.Moves -= 1
            grid.Clear()
                





            self.Moves -= 1
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
            self.Menu.Add_boat(self)

        if self.Player == "blue":
                pygame.Surface.blit(game.Display,  pygame.image.load('images\\boats\\' + str(self.Length) + '\\' + self.Stance + '.png'), [self.Pos[0], self.Pos[1]])
        else:
                pygame.Surface.blit(game.Display,  pygame.image.load('images\\boats\\' + str(self.Length) + '\\' + self.Stance + '_red.png'), [self.Pos[0], self.Pos[1]])
        self.Tell_tile()
        
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
    def __init__(self, x, y, width, height, function, color, hovercolor, text, constant=False, textsize=None, textcolor=(255,255,255)):
        self.X = x
        self.Y = y
        self.Width = width
        self.Height = height

        self.Function = function
        self.Color = color
        self.Color_hover = hovercolor
        self.Color_text = textcolor
        self.Text = text
        if textsize != None: self.Text_size = textsize
        else: self.Text_size = int(self.Height / 1.2)

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
                self.Pressing = self.Click()
                if self.Pressing:
                    self.Pressed = True
                    self.Pressing = False
                else:
                    if self.Pressed == True:
                        self.Function()
                        self.Pressed = False

        else:
            pygame.draw.rect(game.Display, self.Color, (self.X, self.Y, self.Width, self.Height))
        Text_draw(self.Text, int(self.Text_size), self.X + 5, self.Y + self.Height / 5, self.Color_text)

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
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            hand.Normal.Add_card(fmj_upgrade.Name, fmj_upgrade.Desc, testf)
                        if event.key == pygame.K_2:
                            hand.Normal.Add_card(advanced_rifling.Name, advanced_rifling.Desc, testf)
                        if event.key == pygame.K_3:
                            hand.Activate()
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
game.loop()

pygame.quit()
quit()
