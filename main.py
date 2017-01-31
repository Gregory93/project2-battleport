import os
os.environ['SDL_VIDEO_CENTERED'] = "1"

import pygame
import tkinter
import psycopg2
from tkinter import *
from module3 import *

try: conn = psycopg2.connect("dbname=battleport user=postgres host=localhost password=Mei_Juutje99")
except: print("cannot connect to the database")
cur = conn.cursor()
conn.set_isolation_level(0)

pygame.init()

navy = (0,0,128)
cobalt = (61,89,171)
class Endgame:
    def __init__(self):
        self.X = game.Width / 4
        self.Y = game.Height / 10 + 100
        self.Width = game.Width / 2

        # if winner is player1 
        self.Player1 = "Unnamed"
        self.Player2 = "Unnamed"

        self.Players = Player_attributes()
        
        self.button_height = 50
        self.button_color = (224,224,224)
        self.button_color_hover = (160, 160, 160)

        self.Buttons = [
        Button1(self.X-300, self.Y+522, 100, 57, self.Menu, self.button_color, self.button_color_hover, "main"),\
        Button1(self.X-200, self.Y+400, 100, 57, self.Update_score, self.button_color, self.button_color_hover, "update")]

    def End(self, name):
        if name == game.Player1:
            self.Player1 = game.Player1
            self.Player2 = game.Player2
        elif name == game.Player2:
            self.Player1 = game.Player2
            self.Player2 = game.Player1
        else:
            print("error. input name is not a player")
        self.Update_score()

    def Tryname(self, name):
        cur.execute("select * FROM score WHERE name = '{}'".format(name))
        try:
            cur.fetchall()[0]
        except:
            print("player does not exist yet")
            return False
        print("player exists")
        return True

    def Update_score(self):
        self.Player1 = game.Player1
        self.Player2 = game.Player2
        if not self.Tryname(self.Player1):
            cur.execute ("""INSERT INTO score (name, gp, gw, gl) VALUES(%s, %s, %s, %s)""", (self.Player1, '0', '0', '0'))
        if not self.Tryname(self.Player2):
            cur.execute ("""INSERT INTO score (name, gp, gw, gl) VALUES(%s, %s, %s, %s)""", (self.Player2, '0', '0', '0'))

        cur.execute("UPDATE score SET gp = gp+1, gw = gw+1, gl = gl WHERE name = '{}'".format(self.Player1))
        cur.execute("UPDATE score SET gp = gp+1, gw = gw, gl = gl+1 WHERE name = '{}'".format(self.Player2))

    def Start(self): game.Level = "start"
    def Menu(self): game.Level = "menu"
    def Load(self): game.Level = "load"
    def Instructions(self): game.Level = "instructions"
    def Exit(self): game.Level = "exit"

    def Draw(self):
        self.Player1 = game.Player1
        self.Player2 = game.Player2

        cur.execute("SELECT *, ROUND((CASE gw WHEN 0 THEN 1 ELSE gw END / CASE gl WHEN 0 THEN 1 ELSE gl END::numeric),2) FROM score WHERE name = '{}'".format(self.Player1))
        p1 = cur.fetchall()[0]
        cur.execute("SELECT *, ROUND((CASE gw WHEN 0 THEN 1 ELSE gw END / CASE gl WHEN 0 THEN 1 ELSE gl END::numeric),2) FROM score WHERE name = '{}'".format(self.Player2))
        p2 = cur.fetchall()[0]

        Text_draw("New score:", 40, self.X-100, self.Y+150)
        Text_draw(p1[0], 70, self.X+25, self.Y+50)
        Text_draw(p2[0], 50, self.X+600, self.Y+50)

        Text_draw(str(p1[1]), 40, self.X+25, self.Y+200)
        Text_draw(str(p2[1]), 40, self.X+25, self.Y+275)

        Text_draw(str(p1[2]), 40, self.X+100, self.Y+200)
        Text_draw(str(p2[2]), 40, self.X+100, self.Y+275)

        Text_draw(str(p1[3]), 40, self.X+175, self.Y+200)
        Text_draw(str(p2[3]), 40, self.X+175, self.Y+275)

        Text_draw(str(p1[4]), 40, self.X+250, self.Y+200)
        Text_draw(str(p2[4]), 40, self.X+250, self.Y+275)
        


        #Text_draw(self.ratio, 40, self.X+520, self.Y+50)

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
        Button1(self.X+93, self.Y+240, 498, 69, self.Start, self.button_color, self.button_color_hover, "Start game"),\
        Button1(self.X+93, self.Y+320, 498, 69, self.Load, self.button_color, self.button_color_hover, "Load game"),\
        Button1(self.X+93, self.Y+400, 498, 69, self.Instructions, self.button_color, self.button_color_hover, "Instructions"),\
        Button1(self.X+93, self.Y+480, 498, 69, self.Highscore, self.button_color, self.button_color_hover, "Highscore"),\
        Button1(self.X+870, self.Y+520, 63, 54, self.Instructions, self.button_color, self.button_color_hover, "S"),\
        Button1(self.X+946, self.Y+520, 61, 54, self.Exit, self.button_color, self.button_color_hover, "E")]

    def Start(self):
        game.Get_name_input()
        menubar.Player_holder.Change_player()
        game.Start = True
        game.Level = "game"
    def Menu(self): game.Level = "menu"
    def Load(self): game.Level = "load"
    def Highscore(self): game.Level = "highscore"
    def Instructions(self): game.Level = "instructions_rules"
    def Exit(self): game.Level = "exit"
    def Draw(self):
        #text_draw
        for button in self.Buttons:
            button.Draw()

class Instructions_Rules:
    def __init__(self):
        
        self.buttons_Instructions_Rules=Container(10,100,400,50,0)
        self.buttons_Instructions_Rules.Add_button((0,0,128),(61,89,171),self.B_Instructions,"instructions",False)
        self.buttons_Instructions_Rules.Add_button((0,0,128),(61,89,171),self.B_Rules,"rules",False)
        self.buttons_Instructions_Rules.Add_button((0,0,128),(61,89,171),self.B_menu,"menu",False)
        
    def B_menu(self):game.Level = "menu"
    def B_Rules(self):game.Level = "rules"
    def B_Instructions(self): game.Level = "instructions"
    def Draw(self):
            self.buttons_Instructions_Rules.Draw()
         
class Instructions:
    def __init__(self):
            self.current=0

            self.L_instructions=[\
            pygame.transform.scale(pygame.image.load("images//instructions//generalinstructions.png"),(600,600)),\
            pygame.transform.scale(pygame.image.load("images//instructions//shipinstructions.png"),(600,600)),\
            pygame.transform.scale(pygame.image.load("images//instructions//cardinstructions1of2.png"),(600,600)),\
            pygame.transform.scale(pygame.image.load("images//instructions//cardinstructions2of2.png"),(600,600))]
           
            self.buttons_instructions=Container(10,100,400,50,0)
            self.buttons_instructions.Add_button((0,0,128),(61,89,171),self.General_instructions,"General instructions", False)
            self.buttons_instructions.Add_button((0,0,128),(61,89,171),self.Ship_instructions,"Ship instructions", False)
            self.buttons_instructions.Add_button((0,0,128),(61,89,171),self.Card_instructions,"Card instructions", False)  
            self.buttons_instructions.Add_button((0,0,128),(61,89,171),self.forward_instructions,"Next",False)   
            self.buttons_instructions.Add_button((0,0,128),(61,89,171),self.backward_instructions,"Previous", False)         
            self.buttons_instructions.Add_button((0,0,128),(61,89,171),self.back_instructions,"Back", False)      
    def General_instructions(self):self.current=0
    def Ship_instructions(self):self.current=1
    def Card_instructions(self):self.current=2
    def back_menu(self): game.Level = "menu"
    def back_instructions(self): game.Level = "instructions_rules"
    def forward_instructions(self):
        if self.current<len(self.L_instructions)-1:
            self.current+=1
        elif self.current==len(self.L_instructions)-1:
            self.current=len(self.L_instructions)-1
    def backward_instructions(self):
        if self.current>0:
            self.current-=1
        elif self.current==0:
            self.current=0
            self.current-=1
       
    
    def Draw(self):
           self.buttons_instructions.Draw()
           game.Display.blit(self.L_instructions[self.current],(400,100)) 

class Rules:
    def __init__(self):
        self.current1=0

        self.L_Rules=[\
        pygame.transform.scale(pygame.image.load("images//rules//generalRules.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("images//rules//shipRules.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("images//rules//shipstats1of2.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("images//rules//shipstats2of2.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("images//rules//cardRules1of2.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("images//rules//cardRules2of2.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("images//rules//cardinformation1of4.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("images//rules//cardinformation2of4.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("images//rules//cardinformation3of4.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("images//rules//cardinformation4of4.png"),(600,600)),\
        ]
        
        self.buttons_Rules=Container(10,100,400,50,0)
        self.buttons_Rules.Add_button((0,0,128),(61,89,171),self.General_Rules,"General Rules",False)
        self.buttons_Rules.Add_button((0,0,128),(61,89,171),self.Ship_Rules,"Ship Rules",False)
        self.buttons_Rules.Add_button((0,0,128),(61,89,171),self.Card_Rules,"Card Rules",False)
        self.buttons_Rules.Add_button((0,0,128),(61,89,171),self.forward_Rules,"next",False)
        self.buttons_Rules.Add_button((0,0,128),(61,89,171),self.backward_Rules,"previous",False)
        self.buttons_Rules.Add_button((0,0,128),(61,89,171),self.back_Rules,"Back",False)
        
    

    def forward_Rules(self):
        if self.current1<len(self.L_Rules)-1:
            self.current1+=1
        elif self.current1==len(self.L_Rules)-1:
            self.current1=len(self.L_Rules)-1
    def backward_Rules(self):
        if self.current1>0:
            self.current1-=1
        elif self.current1==0:
            self.current1=0
        
    def General_Rules(self): self.current1=0
    def Ship_Rules(self): self.current1=1
    def Card_Rules(self): self.current1=4
    def back_Rules(self): game.Level = "instructions_rules"
    def Draw(self):
           self.buttons_Rules.Draw()
           game.Display.blit(self.L_Rules[self.current1],(400,100))

class Player:
    def __init__(self, name, color):
        self.Name = name
        self.Color = color
        self.Boat_hand = None

        self.Boats = [\
        Boat(600,300,4,self.Color),\
        Boat(650,300,3,self.Color),\
        Boat(700,300,3,self.Color),\
        Boat(750,300,2,self.Color)]

        self.Ready_button = Button1(700, 400, 100, 40, game.Next, navy, cobalt, "Ready")
        self.Clicked_button = False

    def Start(self):
        if self.Boat_hand != None:
        
            if not(grid.X < pygame.mouse.get_pos()[0] < grid.X + 500 and grid.Y < pygame.mouse.get_pos()[1] < grid.Y + 500): # checking if mouse is in the grid
                self.Boat_hand.Pos[0] = pygame.mouse.get_pos()[0]
                self.Boat_hand.Pos[1] = pygame.mouse.get_pos()[1]
                if not pygame.mouse.get_pressed()[0]:
                    self.Boat_hand = None

    def Draw(self):
        show_button = True
        for boat in self.Boats:
            boat.Draw()
            if not(grid.X <= boat.Pos[0] <= grid.X + 500 and grid.Y <= boat.Pos[1] <= grid.Y + 500):
                show_button = False
        if show_button and self.Clicked_button == False:
            self.Ready_button.Draw()
        

class Player_holder:
    def __init__(self, x, y, textsize):
        self.X = x
        self.Y = y
        self.Text_size = textsize
        self.Player = "Unnamed player"

    def Change_player(self):
        if self.Player == "Unnamed player":
            self.Player = game.Player1

        elif self.Player == game.Player1:
            self.Player = game.Player2
            menubar.Player = "red"
        else:
            self.Player = game.Player1
            menubar.Player = "blue"

    def Draw(self):
        Text_draw(self.Player + "\'s turn", self.Text_size, self.X, self.Y)

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
        self.button_color = (0,0,128)
        self.button_color_hover = (0, 0, 180)

        self.Buttons = [
        Button1(self.X+650, self.Y+500, 280, 50, self.Menu, self.button_color, self.button_color_hover, "back to main menu")]

    def Menu(self): game.Level = "menu"
    def Draw(self):
        Text_draw("Highscore", 60, self.X+230, self.Y-150)
        Text_draw("Name", 40, self.X-50, self.Y-80)
        Text_draw("Played", 40, self.X+200, self.Y-80)
        Text_draw("Won", 40, self.X+500, self.Y-80)
        Text_draw("Lost", 40, self.X+800, self.Y-80)

        Text_draw("1", 40, self.X-150, self.Y-30)
        Text_draw("2", 40, self.X-150, self.Y+10)
        Text_draw("3", 40, self.X-150, self.Y+50)

        Text_draw(self.name, 40, self.X-50, self.Y-30)
        Text_draw(self.name2, 40, self.X-50, self.Y+10)
        Text_draw(self.name3, 40, self.X-50, self.Y+50)
        Text_draw(self.name4, 40,  self.X-50, self.Y+90)
        Text_draw(self.name5, 40,  self.X-50, self.Y+130)

        Text_draw(self.gamesp, 40, self.X+200, self.Y-30)
        Text_draw(self.gamesp2, 40, self.X+200, self.Y+10)
        Text_draw(self.gamesp3, 40, self.X+200, self.Y+50)
        Text_draw(self.gamesp4, 40, self.X+200, self.Y+90)
        Text_draw(self.gamesp5, 40, self.X+200, self.Y+130)

        Text_draw(self.gamesw, 40, self.X+500, self.Y-30)
        Text_draw(self.gamesw2, 40, self.X+500, self.Y+10)
        Text_draw(self.gamesw3, 40, self.X+500, self.Y+50)
        Text_draw(self.gamesw4, 40, self.X+500, self.Y+90)
        Text_draw(self.gamesw5, 40, self.X+500, self.Y+130)

        Text_draw(self.gamesl, 40, self.X+800, self.Y-30)
        Text_draw(self.gamesl2, 40, self.X+800, self.Y+10)
        Text_draw(self.gamesl3, 40, self.X+800, self.Y+50)
        Text_draw(self.gamesl4, 40, self.X+800, self.Y+90)
        Text_draw(self.gamesl5, 40, self.X+800, self.Y+130)

        for button in self.Buttons:
            button.Draw()
class Menu_bar:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Width = game.Width
        self.Height = game.Height / 20
        self.Color = cobalt
        self.Start = True

        self.Player = "blue"

        self.Player_holder = Player_holder(self.X+10, self.Y+8, 35)
        self.end_turn = Button1(self.Width-300, self.Y, 150, self.Height, game.Toggle_blackscreen, navy, cobalt, "End turn", False, 35)
        self.pause_menu = Button1(self.Width-150, self.Y, 150, self.Height, self.Menu, navy, cobalt, "Pause", False, 35)
    
    def Menu(self):
        game.Level = "menu2"

    def Draw(self):
        pygame.draw.rect(game.Display, self.Color, [self.X, self.Y, self.Width, self.Height])

        self.Player_holder.Draw()
        if not self.Start:
            self.end_turn.Draw()
        self.pause_menu.Draw()
        pygame.draw.line(game.Display, (100,100,100), (self.end_turn.X, self.end_turn.Y), (self.end_turn.X, self.Height), 2)
        pygame.draw.line(game.Display, (100,100,100), (self.pause_menu.X, self.pause_menu.Y), (self.pause_menu.X, self.Height), 2)
        pygame.draw.line(game.Display, (100,100,100), (self.X, self.Height), (self.Width, self.Height), 3)

class temp_card_holder:
    def __init__(self, name, id, desc, amount):
        self.Name = name
        self.ID = id
        self.Desc = desc
        self.Amount = amount

class Card:
    def __init__(self, x, y, name, desc, function, id, deck):
        self.X = x
        self.Y = y
        self.Width = 74
        self.Height = 31
        self.Name = name
        self.Desc = desc
        self.Function = function
        self.Active = True

        self.Desc_width = 412
        self.Desc_height = 138

        self.ID = id
        self.Deck = deck

        self.Pressed = False
    
    def Hover(self):
        if self.X < pygame.mouse.get_pos()[0] < self.X + self.Width:
            if self.Y < pygame.mouse.get_pos()[1] < self.Y + self.Height: return True
        return False

    def Draw(self):
        if self.Active:
            if self.Hover():
                # pygame.blit(game.Display, pygame.image.load("images\\cards\\" + self.name + "hover.png"), [self.X, self.Y])
                pygame.draw.rect(game.Display, (100,100,100), (self.X, self.Y, self.Width, self.Height))
                pygame.draw.rect(game.Display, (50,50,50), (self.X + self.Width / 2 - self.Desc_width / 2, self.Y + self.Height + 10, self.Desc_width, self.Desc_height))
                Text_draw(self.Name, 35, self.X + self.Width / 2 - self.Desc_width / 2 + 10, self.Y + self.Height + 20)
                Text_draw(self.Desc, 20, self.X + self.Width / 2 - self.Desc_width / 2 + 10, self.Y + self.Height + 50)

                pressing = pygame.mouse.get_pressed()[0]
                if pressing:
                    self.Pressed = True
                elif self.Pressed:
                    self.Function()
                    self.Deck.Remove_card(self.ID)
                    self.Pressed = False


            else:
                pygame.draw.rect(game.Display, (50,50,50), (self.X, self.Y, self.Width, self.Height))
                # pygame.blit(game.Display, pygame.image.load("images\\cards\\" + self.name + "active.png"), [self.X, self.Y])
        else:
            # pygame.blit(game.Display, pygame.image.load("images\\cards\\" + self.name + "inactive.png"), [self.X, self.Y])
            pygame.draw.rect(game.Display, (25,25,25), (self.X, self.Y, self.Width, self.Height))

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
        w = 74
        h = 31

        for card in self.Cards:
            if card == "":
                self.Cards[i] = Card(x, y, name, desc, function, i, self)
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

class Mines:
    def __init__(self):
        self.Mines = [Mine(12,4), Mine(15,4), Mine(18,4),\
        Mine(1,8), Mine(4,8), Mine(7,8),\
        Mine(12,11), Mine(15,11), Mine(18,11),\
        Mine(1,15), Mine(4,15), Mine(7,15)]

    def Activate(self, mineID, player):
        self.Mines[mineID].Activate(player)
    
    def Light_up(self, mineID="all", showrange=False):
        if mineID == "all":
            for mine in self.Mines:
                mine.Draw(showrange)
        else:
            self.Mines[mineID].Draw(showrange)

class Mine:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.Pos = [grid.Tiles[x][y].X, grid.Tiles[x][y].Y]
        self.Player = None
        self.Active = False
        self.Boats = None

        self.C = 0
        
    def Detect(self):
        if self.Active:
            self.Boats = None
            for y in range(self.Y - 1, self.Y+2):
                for x in range(self.X - 1, self.X + 2):
                    grid.Tiles[x][y].Color = (50,50,50)
                    if grid.Tiles[x][y].Boat != None:
                        if self.Boats == None:
                            self.Boats = [grid.Tiles[x][y].Boat]
                        else:
                            self.Boats.append(grid.Tiles[x][y].Boat)

            if self.Boats != None:
                self.Boats = set(self.Boats)
                for boat in self.Boats:
                    print("Boat detected! (" + boat.Player + ")")
            else:
                print("No boats detected")

            if grid.Tiles[self.X][self.Y].Boat != None:
                if grid.Tiles[self.X][self.Y].Boat.Player != self.Player:
                    self.C += 1
            
            if self.C > 1:
                self.Explode()
                self.C = 0
    
    def Explode(self):
        # TODO: Show exploding animation
        for boat in self.Boats:
            boat.Lose_health(1)
        self.Active = False
        print("BOOM")
    
    def Activate(self, player):
        self.Active = True
        self.Player = player
    def Draw(self, showrange=False):
        # TODO: Show a mine image on the tile
        for y in range(self.Y - 1, self.Y+2):
            for x in range(self.X - 1, self.X + 2):
                if x == self.X and y == self.Y: grid.Tiles[x][y].Color = (100,0,0)
                elif showrange: grid.Tiles[x][y].Color = (35,0,0)

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
        self.a = Button1(self.X, self.Y+90, 85, 30, self.Boat.Attack, navy, cobalt, "Attack")
        self.m = Button1(self.X+85, self.Y+90, 85, 30, self.Boat.Move, navy, cobalt, "Move")
        self.s = Button1(self.X+170, self.Y+90, 85, 30, self.Boat.Stance_change, navy, cobalt, "Stance")
    
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
        # self.X = x
        # self.Y = y
        # if self.Player == "blue":
        #     self.Pos = [grid.Tiles[x][y].X, grid.Tiles[x][y].Y]
        # else:
        #     self.Pos = [grid.Tiles[x][y].X, grid.Tiles[x][y - (length - 1)].Y]
        self.Pos = [x,y]
        
        self.Length = length
        self.Stance = "attack"
        self.Start = True

        self.Damage = 1
        self.Movement = 5 - self.Length
        self.Moves = self.Movement
        self.Range_def = self.Length + 1
        self.Range_att = self.Length
        self.Attacked = False

        self.Name = name
        self.Health = self.Length
        self.Perks = None

        self.Took_damage = False
        self.Count = 0
        self.Placed = False

        self.Menu = grid.Menu
    
    def Tell_tile(self):
        if self.Placed:
            if self.Stance == "defense":
                if self.Player == "blue":
                    for x in range(self.X, self.X - self.Length, -1):
                        grid.Tiles[x][self.Y].Boat = self
                else:
                    for x in range(self.X, self.X + self.Length):
                        grid.Tiles[x][self.Y].Boat = self
            else:
                if self.Player == "blue":
                    for y in range(self.Y, self.Y + self.Length):
                        grid.Tiles[self.X][y].Boat = self
                else:
                    for y in range(self.Y, self.Y - self.Length, -1):
                        grid.Tiles[self.X][y].Boat = self
    
    def Attack(self):
        if not self.Attacked:
            if self.Stance == "defense":
                if self.Player == "blue":
                    for x in range(self.X - (self.Length - 1), self.X + 1):
                        y = self.Y - self.Range_def
                        for i in range(y, self.Y + self.Range_def + 1):
                            if not(i < 0) and not(i > 19):
                                if i != self.Y:
                                    grid.Tiles[x][i].Color = (50,0,0)
                                    if grid.Tiles[x][i].Boat != None and grid.Tiles[x][i].Boat.Player != self.Player:
                                            grid.Tiles[x][y].Click(self.Attack_on, "hit")
                else:
                    for x in range(self.X, self.X + self.Length):
                        y = self.Y - self.Range_def
                        for i in range(y, self.Y + self.Range_def + 1):
                            if not(i < 0) and not(i > 19):
                                if i != self.Y:
                                    grid.Tiles[x][i].Color = (50,0,0)
                                    if grid.Tiles[x][i].Boat != None and grid.Tiles[x][i].Boat.Player != self.Player:
                                            grid.Tiles[x][y].Click(self.Attack_on, "hit")

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
                                            grid.Tiles[x][y].Color = (50,0,0)
                                            if grid.Tiles[x][y].Boat != None:
                                                grid.Tiles[x][y].Click(self.Attack_on, "hit")
                                x = x + 1
                            y = y + 1
                else:
                    for Y in range(self.Y - (self.Length - 1), self.Y + 1):
                        X = self.X
                        y = Y - self.Range_att
                        while y <= Y + self.Range_att:
                            x = X - self.Range_att
                            while x <= X + self.Range_att:
                                if not(self.Y >= y > self.Y - self.Length and x == X):
                                    if x == X or y == Y:
                                        if not(x < 0) and not(x > 19) and not(y < 0) and not(y > 19):
                                            grid.Tiles[x][y].Color = (50,0,0)
                                            if grid.Tiles[x][y].Boat != None:
                                                grid.Tiles[x][y].Click(self.Attack_on, "hit")
                                x = x + 1
                            y = y + 1

            self.Menu.Clear()
    def Move(self):
        if self.Player == "blue":
            if not self.Moves <= 0:
                x = self.X - (self.Moves)
                y = self.Y - self.Moves
                a = 1
                b = self.Moves

                while y <= self.Y + self.Moves:
                    for i in range(0,a):
                        if not(x+b+i < 0) and not(x+b+i > 19) and not(y < 0) and not(y > 19 - self.Length + 1):
                            if not(y == self.Y and x+b+i == self.X):
                                if grid.Tiles[x+b+i][y].Boat == None or grid.Tiles[x+b+i][y].Boat == self:
                                    if self.Player == "blue":
                                        # TODO: RESTRICTION: when boat other than yourself is on the tile under the clickable Tile (check with forloop(y, y+(length-1))
                                        # TODO: RESTRICTION: a boat should not be able to go over other boats 
                                        grid.Tiles[x+b+i][y].Click(self.Move_to, (255,255,153), self)
                                    else:
                                        # TODO: RESTRICTION: when boat other than yourself is on the tile above the clickable Tile (check with forloop(y, y-(length-1))
                                        # TODO: RESTRICTION: a boat should not be able to go over other boats 
                                        grid.Tiles[x+b+i][y].Click(self.Move_to, (255,255,153), self)
                    if y >= self.Y:
                        b += 1
                        a -= 2
                    else:
                        b -= 1
                        a += 2
                    y += 1
        else:
            if not self.Moves <= 0:
                x = self.X - (self.Moves)
                y = self.Y - self.Moves
                a = 1
                b = self.Moves

                while y <= self.Y + self.Moves:
                    for i in range(0,a):
                        if not(x+b+i < 0) and not(x+b+i > 19) and not(y < 0 + (self.Length - 1)) and not(y > 19):
                            if not(y == self.Y and x+b+i == self.X):
                                if grid.Tiles[x+b+i][y].Boat == None or grid.Tiles[x+b+i][y].Boat == self:
                                    if self.Player == "blue":
                                        # RESTRICTION: when boat other than yourself is on the tile under the clickable Tile (check with forloop(y, y+(length-1))
                                        # RESTRICTION: a boat should not be able to go over other boats 
                                        grid.Tiles[x+b+i][y].Click(self.Move_to, (255,255,153), self)
                                    else:
                                        # RESTRICTION: when boat other than yourself is on the tile above the clickable Tile (check with forloop(y, y-(length-1))
                                        # RESTRICTION: a boat should not be able to go over other boats 
                                        grid.Tiles[x+b+i][y].Click(self.Move_to, (255,255,153), self)
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
        grid.Tiles[x][y].Boat.Lose_health(self.Damage)
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
    def Lose_health(self, damage):
        self.Health -= damage
        self.Took_damage = True
        self.Count = 0
    def Hover(self):
        if self.Start:
            if self.Pos[0] < pygame.mouse.get_pos()[0] < self.Pos[0] + grid.Tile_size:
                if self.Pos[1] < pygame.mouse.get_pos()[1] < self.Pos[1] + self.Length * grid.Tile_size: return True
            return False
        else:
            if self.Stance == "defense":
                if self.Pos[0] < pygame.mouse.get_pos()[0] < self.Pos[0] + (self.Length * grid.Tile_size):
                    if self.Pos[1]< pygame.mouse.get_pos()[1] < self.Pos[1] + grid.Tile_size: return True
                return False
            else:
                if self.Pos[0] < pygame.mouse.get_pos()[0] < self.Pos[0] + grid.Tile_size:
                    if self.Pos[1] < pygame.mouse.get_pos()[1] < self.Pos[1] + (self.Length * grid.Tile_size): return True
                return False

    def Draw(self):
        if self.Player == "blue":
            pygame.Surface.blit(game.Display,  pygame.image.load('images\\boats\\' + str(self.Length) + '\\' + self.Stance + '.png'), [self.Pos[0], self.Pos[1]])
        else:
            pygame.Surface.blit(game.Display,  pygame.image.load('images\\boats\\' + str(self.Length) + '\\' + self.Stance + '_red.png'), [self.Pos[0], self.Pos[1]])

        if self.Start:
            if self.Hover() and pygame.mouse.get_pressed()[0]:
                if game.Start_player == 1:
                    player = player1
                elif game.Start_player == 2:
                    player = player2
                
                if player.Color == self.Player:
                    if player.Boat_hand == None and self.Player == player.Color:
                        player.Boat_hand = self
        elif self.Player == menubar.Player:
            if self.Hover() and pygame.mouse.get_pressed()[0]:
                grid.Clear() # TODO: upgrade this to a better version (only use this when a boat is using attack or move)
                self.Menu.Add_boat(self)

            if self.Took_damage:
                y = self.Pos[1] - self.Count * 2
                pygame.Surface.blit(game.Display, pygame.image.load("images\\damage.png"), [self.Pos[0],y])
                if not(self.Count > 15):
                    self.Count += 1
                else:
                    self.Count = 0
                    self.Took_damage = False

        if grid.X <= self.Pos[0] <= grid.X + 500:
            if grid.Y <= self.Pos[1] <= grid.Y + 500:
                if player1.Boat_hand != self and player2.Boat_hand != self:
                    self.Tell_tile()
        
class Tile:
    def __init__(self, x, y, pos, size, menu):
        self.X = x
        self.Y = y
        self.Pos = pos
        self.Size = size
        self.Color = (0,0,0)
        self.Start = True

        self.Menu = menu

        self.Boat = None

        self.Function_boat = None
        self.Function = None
        self.Pressed = False

    def Clear(self):
        self.Boat = None
        self.Function = None
        self.Color = (0,0,0)
        self.Function_boat = None
    
    def Click(self, function, color, boat=None):
        if self.Color != 'hit':
            self.Color = color
        self.Function = function
        self.Function_boat = boat
    
    def Hover(self):
        if self.X < pygame.mouse.get_pos()[0] < self.X + self.Size:
            if self.Y < pygame.mouse.get_pos()[1] < self.Y + self.Size: return True
        return False
    def Ghost(self):
        if self.Function_boat != None and self.Hover():
            if self.Function_boat.Player == "blue":
                if self.Function_boat.Stance == "defense":
                    x = self.X - (self.Function_boat.Length - 1) * self.Size
                    y = self.Y
                else:
                    x = self.X
                    y = self.Y
                pygame.Surface.blit(game.Display, pygame.image.load("images\\boats\\" + str(self.Function_boat.Length) + "\\" + str(self.Function_boat.Stance) + ".png"), [x,y])
            else:
                if self.Function_boat.Stance == "defense":
                    x = self.X - (self.Function_boat.Length - 1) * self.Size
                    y = self.Y - (self.Function_boat.Length - 1) * self.Size
                else:
                    x = self.X
                    y = self.Y - (self.Function_boat.Length - 1) * self.Size
                pygame.Surface.blit(game.Display, pygame.image.load("images\\boats\\" + str(self.Function_boat.Length) + "\\" + str(self.Function_boat.Stance) + "_red.png"), [x,y])


    def Draw(self):
        if self.Color != 'hit':
            pygame.draw.rect(game.Display, self.Color, (self.X, self.Y, self.Size, self.Size))
        pygame.draw.lines(game.Display, (100,100,100), True, [(self.X,self.Y), (self.X+self.Size,self.Y), (self.X+self.Size,self.Y+self.Size), (self.X,self.Y+self.Size)],2)
        if self.Hover():
            if self.Start:

                if game.Start_player == 1:
                    player = player1
                    if player.Boat_hand != None:
                        if grid.Tiles[self.Pos[0]][19].Boat == None:
                            player.Boat_hand.Pos[0] = self.X
                            player.Boat_hand.Pos[1] = grid.Tiles[self.Pos[0]][19 - (player.Boat_hand.Length - 1)].Y
                            
                            if pygame.mouse.get_pressed()[0]:
                                self.Pressed = True
                            elif self.Pressed:
                                player.Boat_hand.X = self.Pos[0]
                                player.Boat_hand.Y = grid.Tiles[self.Pos[0]][19 - (player.Boat_hand.Length - 1)].Pos[1]
                                self.Pressed = False
                                grid.Clear()
                                player.Boat_hand.Placed = True
                                player.Boat_hand = None
                else:
                    player = player2
                    if player.Boat_hand != None:
                        if grid.Tiles[self.Pos[0]][0].Boat == None:
                            player.Boat_hand.Pos[0] = self.X
                            player.Boat_hand.Pos[1] = grid.Tiles[self.Pos[0]][0].Y

                            if pygame.mouse.get_pressed()[0]:
                                self.Pressed = True
                            elif self.Pressed:
                                player.Boat_hand.X = self.Pos[0]
                                player.Boat_hand.Y = grid.Tiles[self.Pos[0]][0 + (player.Boat_hand.Length - 1)].Pos[1]
                                self.Pressed = False
                                grid.Clear()
                                player.Boat_hand.Placed = True
                                player.Boat_hand = None


            else:
                if pygame.mouse.get_pressed()[0]:
                    self.Pressed = True
                elif self.Pressed:
                    if self.Function == None:
                        if self.Boat == None:
                            self.Menu.Clear()
                            grid.Clear()
                    else:
                        self.Function(self.Pos[0], self.Pos[1])
                        grid.Clear()
                    self.Pressed = False

class Grid:
    def __init__(self, x, y, size, tilesize, menu):
        self.Tile_size = tilesize
        self.Size = size
        self.X = x
        self.Y = y
        self.Start = True

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

    def Draw_over(self):
        for y in range(0, self.Size):
            for x in range(0, self.Size):
                self.Tiles[x][y].Ghost()
                if self.Tiles[x][y].Color == 'hit':
                    pygame.Surface.blit(game.Display, pygame.image.load('images\\rood25.png'), [self.Tiles[x][y].X + 1, self.Tiles[x][y].Y + 1])

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


class Button1:
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
class Container:
    def __init__(self, x, y, width, buttonheight, space):
        self.X = x
        self.Y = y
        self.Width = width
        self.Buttonheight = buttonheight
        self.Space = space
        self.Buttons = [""] * 25

    def Add_button(self, color, hovercolor, function, text, constant=False, textsize=None, textcolor=(255,255,255)):
        a = 0
        for button in self.Buttons:
            if button == "":
                self.Buttons[a] = Button1(self.X, self.Y+self.Buttonheight*a+self.Space*a, self.Width, self.Buttonheight, function, color, hovercolor, text, constant, textsize, textcolor)
                break
            a += 1
    
    def Draw(self):
        for button in self.Buttons:
            if button == "": break
            else: button.Draw()
class Game:
    def __init__(self):
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.Exit = False

        self.Width = 1360
        self.Height = 768
        self.Display = pygame.display.set_mode((self.Width, self.Height))

        self.Player1 = "Unnamed"
        self.Player2 = "Unnamed"
        
        self.Level = "menu"
        self.Interval = False

        self.Start = True
        self.Start_player = 1

    def Next(self):
        if self.Start_player == 1:
            self.Start_player += 1
            menubar.Player_holder.Change_player()
            player1.Clicked_button = True
        else:
            self.Toggle_blackscreen()
            self.Start = False
            menubar.Start = False
            for x in range(0,19):
                for y in range(0,19):
                    grid.Tiles[x][y].Start = False
            for boat in player1.Boats:
                boat.Start = False
            for boat in player2.Boats:
                boat.Start = False
            player2.Clicked_button = True
            
    def Toggle_blackscreen(self):
        if self.Interval:
            self.Interval = False
            for b in player1.Boats:
                b.Moves = b.Movement
                b.Attacked = False
            for b in player2.Boats:
                b.Moves = b.Movement
                b.Attacked = False
            grid.Clear()
            grid.Menu.Clear()
        else:
            menubar.Player_holder.Change_player()
            self.Interval_text = menubar.Player_holder.Player + "\'s turn"
            self.Interval_button = Button1(self.Width / 2 - 100, self.Height - 100, 200, 60, self.Toggle_blackscreen, navy, cobalt, "Ready")
            self.Interval = True
            
    def Draw(self): self.Display.fill((0,0,0))
    def Tick(self): self.clock.tick(self.FPS)
    def Get_name_input(self):
        self.GUI = Tk()
        self.Player1 = StringVar()
        self.Player2 = StringVar()
        self.GUI.geometry('200x100+600+300')
        self.GUI.title = ("Choose a name")

        self.Player = Label(self.GUI, text='enter player names:').pack()
        self.Entry = Entry(self.GUI, textvariable=self.Player1).pack()
        self.Entry = Entry(self.GUI, textvariable=self.Player2).pack()
        self.Button = Button(self.GUI, text='Submit', command=self.Get_names, fg='black', bg='gray').pack()
        self.GUI.mainloop()
    
    def Get_names(self):
        self.Player1 = self.Player1.get()
        self.Player2 = self.Player2.get()
        self.GUI.destroy()

    def Loop(self):
        while not self.Exit:

            if self.Level == "menu":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.Exit = True
                self.Draw()
                self.Display.blit(pygame.image.load("images\\backgrounds\\menu.png"),(0,0))
                menu.Draw()
                pygame.display.update()
                self.Tick()

            elif self.Level == "highscore":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.Exit = True
                self.Draw()
                self.Display.blit(pygame.image.load("images\\backgrounds\\highscore.png"),(0,0))
                highscore.Draw()
                pygame.display.update()
                self.Tick()

            elif self.Level == "endgame":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.Exit = True
                self.Draw()
                # self.Display.blit(pygame.image.load("images\\backgrounds\\endgame.png"),(0,0))
                endgame.Draw()
                pygame.display.update()
                self.Tick()

            elif self.Level == "instructions_rules":
                   for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                         self.Exit = True
                   self.Draw()
                   Instructions_Rules.Draw()
                   pygame.display.update()
                   self.Tick() 

            elif self.Level == "instructions":
                   for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                         self.Exit = True
                   self.Draw()
                   Instructions.Draw()
                   pygame.display.update()
                   self.Tick() 

            elif self.Level == "rules":
                   for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                         self.Exit = True
                   self.Draw()
                   Rules.Draw()
                   pygame.display.update()
                   self.Tick()

            elif self.Level == "game":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.Exit = True
                self.Draw()
                if self.Interval:
                    pygame.Surface.blit(self.Display, pygame.image.load('images\\backgrounds\\ready.png'), (0,0))
                    Text_draw(self.Interval_text, 50, self.Width / 2 - 100, self.Height - 150)
                    self.Interval_button.Draw()
                elif self.Start:
                    grid.Draw()
                    mines.Light_up("all", True)
                    grid.Draw_over()
                    menubar.Draw()
                    if self.Start_player == 1:
                        player1.Start()
                    else:
                        player2.Start()
                        player2.Draw()
                    player1.Draw()
                else:
                    grid.Draw()
                    mines.Light_up("all", True)
                    grid.Draw_over()
                    menubar.Draw()
                    player1.Draw()
                    player2.Draw()
                pygame.display.update()
                self.Tick()
            elif self.Level == "debugging":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.Exit = True
                    self.Draw()
                    test_button.Draw()
                    pygame.display.update()
                    self.Tick()

            else: self.Exit = True

def Text_draw(text, size, x, y, textcolor=(255,255,255)):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, textcolor)
    game.Display.blit(screen_text, [x,y])
def Player_attributes():
    players = []
    cur.execute("SELECT COUNT(*) FROM score")
    player_number = cur.fetchall()[0][0]

    for i in range(0, player_number):
        cur.execute("SELECT *, ROUND((CASE gw WHEN 0 THEN 1 ELSE gw END / CASE gl WHEN 0 THEN 1 ELSE gl END::numeric), 2) AS ratio FROM score OFFSET '{}' LIMIT 1".format(i))
        print(i)
        players.append(cur.fetchall()[0])
    return players

game = Game()
def p1wins():
    game.Get_name_input()
    endgame.End(game.Player1)
    game.Level = "endgame"
### INITS
# highscore = Highscore()
test_button = Button1(10,10,100,100,p1wins,navy,cobalt, "endgame")
endgame = Endgame()
menu = Menu()

Instructions_Rules = Instructions_Rules()
Rules = Rules()
Instructions = Instructions()

### GAME INITS
menubar = Menu_bar()
grid = Grid(50,50,20,25,Boat_menu(50, 600))
mines = Mines()
player1 = Player(game.Player1, "blue")
player2 = Player(game.Player2, "red")

game.Loop()