import pygame
from module3 import *
pygame.init()

navy= (0,0,128)
cobalt = (61,89,171)



class Button1:
    def __init__(self, x, y, width, height, function, color, hovercolor, text, constant=False, textsize=None, textcolor=(0,0,128)):
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
            Text_Draw(self.Text,int(self.Text_size), self.X + 5, self.Y + self.Height / 5, self.Color_text)
        #Text_Draw(text, size, x, y, textcolor=(0,0,128)):

        if self.Constant == True:
            if self.Pressed:
                self.Function()
class Button:
    def __init__(self, x, y, width, function, color, hovercolor, text,Constant, textcolor=(0,0,0)):
        self.X = x
        self.Y = y
        self.Width = width
        #self.Height = height

        self.Function = function
        self.Color = color
        self.Color_hover = hovercolor
        self.Color_text = textcolor
        
        self.Text = text
        self.Constant=Constant
        

        self.Pressed=False
        self.Pressing=False
   
                


    
    
    def Click(self): 
        return pygame.mouse.get_pressed()[0]  ###change boolean on button press
        
      
                
        
    def Hover(self):
        if self.X < pygame.mouse.get_pos()[0] < self.X + self.Width:
            if self.Y < pygame.mouse.get_pos()[1] < self.Y + self.Height: return True
        return False

    def Draw(self):
        if self.Hover():
                pygame.draw.rect(game.Display, self.Color_hover, (self.X, self.Y, self.Width, self.Height))
                if self.Constant:
                    if self.Click():
                        self.Pressing=True
                    else:
                        if self.Pressing:
                            if self.Pressed:
                                self.Pressed=False 
                            else:
                                self.Pressed=True
                            self.Pressing=False
                else:
                 self.Function()

        else:
            pygame.draw.rect(game.Display, self.Color, (self.X, self.Y, self.Width, self.Height))
        Text_draw(self.Text, self.Height, self.X + 5, self.Y + self.Height / 5, self.Color_text)

        if self.Pressed and self.Constant:
            self.Function()
class Instructions_Rules:
    def __init__(self):
        self.Level="Instructions_Rules"
        
        self.buttons_Instructions_Rules=Container(10,100,400,50,0)
        self.buttons_Instructions_Rules.Add_button((0,0,128),(61,89,171),self.B_Instructions,"Instructions",False)
        self.buttons_Instructions_Rules.Add_button((0,0,128),(61,89,171),self.B_Rules,"Rules",False)
        self.buttons_Instructions_Rules.Add_button((0,0,128),(61,89,171),self.B_menu,"Menu",False)
        
    def B_menu(self):game.Level="menu"    
    def B_Rules(self):game.Level="Rules"               
    def B_Instructions(self): game.Level="Instructions"
    def Draw(self):
            self.buttons_Instructions_Rules.Draw()
         
class Instructions:
    def __init__(self):
            self.Level="Instructions"
            self.current=0

            self.L_instructions=[\
            pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Instructions list//generalinstructions.png"),(600,600)),\
            pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Instructions list//shipinstructions.png"),(600,600)),\
            pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Instructions list//cardinstructions1of2.png"),(600,600)),\
            pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Instructions list//cardinstructions2of2.png"),(600,600))]
           
            self.buttons_instructions=Container(10,100,400,50,0)
            self.buttons_instructions.Add_button((0,0,128),(61,89,171),self.General_instructions,"General_instructions", False)
            self.buttons_instructions.Add_button((0,0,128),(61,89,171),self.Ship_instructions,"Ship_instructions", False)
            self.buttons_instructions.Add_button((0,0,128),(61,89,171),self.Card_instructions,"Card_instructions", False)  
            self.buttons_instructions.Add_button((0,0,128),(61,89,171),self.forward_instructions,"Next",False)   
            self.buttons_instructions.Add_button((0,0,128),(61,89,171),self.backward_instructions,"Previous", False)         
            self.buttons_instructions.Add_button((0,0,128),(61,89,171),self.back_instructions,"Back", False)      
    
    def General_instructions(self):self.current=0
         
    def Ship_instructions(self):self.current=1
    def Card_instructions(self):self.current=2
    def back_menu(self): game.Level = "menu"
    def back_instructions(self): game.Level = "Instructions_Rules"
     ######
    def forward_instructions(self):      #### currently hardcoded because it doesn't work with 'len(self.L_rules)'
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
        
        self.Level="Rules"
        self.current1=0
        self.L_Rules=[\
        pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Rules list//generalRules.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Rules list//shipRules.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Rules list//shipstats1of2.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Rules list//shipstats2of2.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Rules list//cardRules1of2.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Rules list//cardRules2of2.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Rules list//cardinformation1of4.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Rules list//cardinformation2of4.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Rules list//cardinformation3of4.png"),(600,600)),\
        pygame.transform.scale(pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//images//Rules list//cardinformation4of4.png"),(600,600)),\
        ]
        
        self.buttons_Rules=Container(10,100,400,50,0)
        self.buttons_Rules.Add_button((0,0,128),(61,89,171),self.General_Rules,"General_Rules",False)
        self.buttons_Rules.Add_button((0,0,128),(61,89,171),self.Ship_Rules,"Ship_Rules",False)
        self.buttons_Rules.Add_button((0,0,128),(61,89,171),self.Card_Rules,"Card_Rules",False)
        self.buttons_Rules.Add_button((0,0,128),(61,89,171),self.forward_Rules,"next",False)
        self.buttons_Rules.Add_button((0,0,128),(61,89,171),self.backward_Rules,"previous",False)
        self.buttons_Rules.Add_button((0,0,128),(61,89,171),self.back_Rules,"Back",False)
        
    

    def forward_Rules(self):      #### currently hardcoded because it doesn't work with 'len(self.L_rules)'
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
    def back_Rules(self): game.Level = "Instructions_Rules"
        
   
        
    def Draw(self):
           self.buttons_Rules.Draw()
           game.Display.blit(self.L_Rules[self.current1],(400,100))
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
        self.button_color_hover = (61,89,171)

        self.Buttons = [
        Button1(self.X+650, self.Y+500, 280, 50, self.Menu, self.button_color, self.button_color_hover, "back to main menu")]
           # def __init__(self, x, y, width, height, function, color, hovercolor, text, constant=False, textsize=None, textcolor=(0,0,128)):
           # #Text_Draw(text, size, x, y, textcolor=(0,0,128)):
    def Menu(self): game.Level = "menu"

    def Draw(self):
        Text_Draw("Highscore", 60, self.X+230, self.Y-150)
        Text_Draw("Name", 40, self.X-50, self.Y-80)
        Text_Draw("Played", 40, self.X+200, self.Y-80)
        Text_Draw("Won", 40, self.X+500, self.Y-80)
        Text_Draw("Lost", 40, self.X+800, self.Y-80)

        Text_Draw("1", 40, self.X-150, self.Y-30)
        Text_Draw("2", 40, self.X-150, self.Y+10)
        Text_Draw("3", 40, self.X-150, self.Y+50)

        Text_Draw(self.name, 40, self.X-50, self.Y-30)
        Text_Draw(self.name2, 40, self.X-50, self.Y+10)
        Text_Draw(self.name3, 40, self.X-50, self.Y+50)
        Text_Draw(self.name4, 40,  self.X-50, self.Y+90)
        Text_Draw(self.name5, 40,  self.X-50, self.Y+130)

        Text_Draw(self.gamesp, 40, self.X+200, self.Y-30)
        Text_Draw(self.gamesp2, 40, self.X+200, self.Y+10)
        Text_Draw(self.gamesp3, 40, self.X+200, self.Y+50)
        Text_Draw(self.gamesp4, 40, self.X+200, self.Y+90)
        Text_Draw(self.gamesp5, 40, self.X+200, self.Y+130)

        Text_Draw(self.gamesw, 40, self.X+500, self.Y-30)
        Text_Draw(self.gamesw2, 40, self.X+500, self.Y+10)
        Text_Draw(self.gamesw3, 40, self.X+500, self.Y+50)
        Text_Draw(self.gamesw4, 40, self.X+500, self.Y+90)
        Text_Draw(self.gamesw5, 40, self.X+500, self.Y+130)

        Text_Draw(self.gamesl, 40, self.X+800, self.Y-30)
        Text_Draw(self.gamesl2, 40, self.X+800, self.Y+10)
        Text_Draw(self.gamesl3, 40, self.X+800, self.Y+50)
        Text_Draw(self.gamesl4, 40, self.X+800, self.Y+90)
        Text_Draw(self.gamesl5, 40, self.X+800, self.Y+130)

        for button in self.Buttons:
            button.Draw()

    def Start(self): game.Level = "start"
    def Menu(self): game.Level = "menu"
    def Load(self): game.Level = "load"
    #def Instructions(self): game.Level = "instructions"
    def Exit(self): game.Level = "exit"

    def Draw(self):
        Text_Draw("1", 40, self.X-200, self.Y+50)
        Text_Draw("2", 40, self.X-200, self.Y+90)
        Text_Draw("3", 40, self.X-200, self.Y+130)

        Text_Draw(self.name, 40, self.X-85, self.Y+50)
        Text_Draw(self.name2, 40, self.X-85, self.Y+90)
        Text_Draw(self.name3, 40, self.X-85, self.Y+130)
        Text_Draw(self.name4, 40,  self.X-85, self.Y+170)
        Text_Draw(self.name5, 40,  self.X-85, self.Y+210)

        Text_Draw(self.gamesp, 40, self.X+120, self.Y+50)
        Text_Draw(self.gamesp2, 40, self.X+120, self.Y+90)
        Text_Draw(self.gamesp3, 40, self.X+120, self.Y+130)
        Text_Draw(self.gamesp4, 40, self.X+120, self.Y+170)
        Text_Draw(self.gamesp5, 40, self.X+120, self.Y+210)

        Text_Draw(self.gamesw, 40, self.X+320, self.Y+50)
        Text_Draw(self.gamesw2, 40, self.X+320, self.Y+90)
        Text_Draw(self.gamesw3, 40, self.X+320, self.Y+130)
        Text_Draw(self.gamesw4, 40, self.X+320, self.Y+170)
        Text_Draw(self.gamesw5, 40, self.X+320, self.Y+210)

        Text_Draw(self.gamesl, 40, self.X+520, self.Y+50)
        Text_Draw(self.gamesl2, 40, self.X+520, self.Y+90)
        Text_Draw(self.gamesl3, 40, self.X+520, self.Y+130)
        Text_Draw(self.gamesl4, 40, self.X+520, self.Y+170)
        Text_Draw(self.gamesl5, 40, self.X+520, self.Y+210)

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
        Button1(self.X+93, self.Y+320, 498, 69, self.Load, self.button_color, self.button_color_hover, "Resume game"),\
        Button1(self.X+93, self.Y+400, 498, 69, self.Instructions_Rules, self.button_color, self.button_color_hover, "Instructions_Rules"),\
        Button1(self.X+93, self.Y+480, 498, 69, self.Highscore, self.button_color, self.button_color_hover, "Highscore"),\
        Button1(self.X+946, self.Y+520, 61, 54, self.Exit, self.button_color, self.button_color_hover, "E")]

    def Start(self): game.Level = "start"
    def Menu(self): game.Level = "menu"
    def Load(self): game.Level = "load"
    def Highscore(self): game.Level = "highscore"
    def Instructions_Rules(self): game.Level="Instructions_Rules"
    def Exit(self): game.Level = "exit"
    def Draw(self):
        for button in self.Buttons:
            button.Draw()


class Menu_bar:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Width = game.Width
        self.Height = game.Height / 20
        self.Color = (61,89,171)

        self.Player_holder = Player_holder(self.X+10, self.Y+8, 35)
        self.end_turn = Button1(self.Width-150, self.Y, 150, self.Height, self.End_turn, (0,0,128), (61,89,171), "End turn", False, 35)
        self.pause_menu = Button1(self.Width-300, self.Y, 150, self.Height, self.Menu, (0,0,128), (61,89,171), "Pause", False, 35)

    def End_turn(self):
        for b in (boat, boat2, boat3):
            b.Moves = b.Movement
            b.Attacked = False
        grid.Clear()
        grid.Menu.Clear()
        self.Player_holder.Change_player()
    
    def Menu(self):
        game.Level = "menu2"

    def Draw(self):
        pygame.Draw.rect(game.Display, self.Color, [self.X, self.Y, self.Width, self.Height])

        self.Player_holder.Draw()
        self.end_turn.Draw()
        self.pause_menu.Draw()
        pygame.Draw.line(game.Display, (100,100,100), (self.end_turn.X, self.end_turn.Y), (self.end_turn.X, self.Height), 2)
        pygame.Draw.line(game.Display, (100,100,100), (self.pause_menu.X, self.pause_menu.Y), (self.pause_menu.X, self.Height), 2)
        pygame.Draw.line(game.Display, (100,100,100), (self.X, self.Height), (self.Width, self.Height), 3)


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
                pygame.Draw.rect(game.Display, (100,100,100), (self.X, self.Y, self.Width, self.Height))
                Text_Draw(str(self.ID), 15, self.X, self.Y-15)
                Text_Draw(self.Name, 15, self.X, self.Y - 40)
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
                pygame.Draw.rect(game.Display, (50,50,50), (self.X, self.Y, self.Width, self.Height))
                Text_Draw(str(self.ID), 15, self.X, self.Y-15)
                Text_Draw(self.Name, 10, self.X, self.Y - 40)
                # pygame.blit(game.Display, pygame.image.load("images\\cards\\" + self.name + "active.png"), [self.X, self.Y])
        else:
            # pygame.blit(game.Display, pygame.image.load("images\\cards\\" + self.name + "inactive.png"), [self.X, self.Y])
            pygame.Draw.rect(game.Display, (255,0,0), (self.X, self.Y, self.Width, self.Height))

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
            Text_Draw(self.Caption, 40, self.X, self.Y-40)

            if self.Boat_class != None:
                Text_Draw("Class: " + str(self.Boat_class), 25, self.Stats_x, self.Stats_y)
                Text_Draw("Moves: " + str(self.Boat_moves), 25, self.Stats_x, self.Stats_y + 25)
                Text_Draw("Def Range: " + str(self.Boat_range_def), 25, self.Stats_x, self.Stats_y + 50)
                Text_Draw("Health: " + str(self.Boat_health), 25, self.Stats_x + 150, self.Stats_y)
                Text_Draw("Perks: " + str(self.Boat_perks), 25, self.Stats_x + 150, self.Stats_y + 25)
                Text_Draw("Att Range: " + str(self.Boat_range_att), 25, self.Stats_x + 150, self.Stats_y + 50)

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
        self.Menu_actions.Add_button((0,0,128), (61,89,171), self.Show_submenu, "Movement")
        self.Menu_actions.Add_button((0,0,128), (61,89,171), self.Attack, "Attack")
        self.Menu_actions_move = Container(self.Menu.Menu_x + self.Menu_actions.Width, self.Menu_actions.Y, 80, 100, 25, 0)
        self.Menu_actions_move.Add_button((0,0,128), (61,89,171), self.Move, "Move")
        self.Menu_actions_move.Add_button((0,0,128), (61,89,171), self.Stance_change, "stance")
    
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
        self.a = Button1(self.X, self.Y+90, 85, 30, self.Boat.Attack, (0,0,128), (61,89,171), "Attack")
        self.m = Button1(self.X+85, self.Y+90, 85, 30, self.Boat.Move, (0,0,128), (61,89,171), "Move")
        self.s = Button1(self.X+170, self.Y+90, 85, 30, self.Boat.Stance_change, (0,0,128), (61,89,171), "Stance")
    
    def Clear(self):
        self.Boat = None
        self.a = None
        self.m = None
        self.s = None
    
    def Draw(self):
        if self.Boat != None:
            Text_Draw(self.Boat.Name, 40, self.X, self.Y)
            Text_Draw("Health: " + str(self.Boat.Health), 25, self.X, self.Y + 40)
            Text_Draw("Moves: " + str(self.Boat.Moves), 25, self.X + 100, self.Y + 40)
            Text_Draw("Perks: " + str(self.Boat.Perks), 25, self.X, self.Y + 65)
            if self.a != None:
                self.a.Draw()
                if self.m != None:
                    self.m.Draw()
                    if self.s != None:
                        self.s.Draw()
        
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
        pygame.Draw.rect(game.Display, self.Color, (self.X, self.Y, self.Size, self.Size))
        pygame.Draw.lines(game.Display, (100,100,100), True, [(self.X,self.Y), (self.X+self.Size,self.Y), (self.X+self.Size,self.Y+self.Size), (self.X,self.Y+self.Size)],2)
        
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
    def __init__(self, x, y, width, buttonheight, space):
        self.X = x
        self.Y = y
        self.Width = width
        self.Buttonheight = buttonheight
        self.Space = space
        self.Buttons = [""] * 25

    def Add_button(self, color, hovercolor, function, text, constant=False, textsize=None, textcolor=(0,0,0)):
        a = 0
        for button in self.Buttons:
            if button == "":
                self.Buttons[a] = Button1(self.X, self.Y+self.Buttonheight*a+self.Space*a, self.Width, self.Buttonheight, function, color, hovercolor, text, constant, textsize, textcolor)
                break   #  def __init__(self, x, y, width, height, function, color, hovercolor, text,Constant, textcolor=(0,0,0)):
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

        self.Width = 1000
        self.Height = 800
        self.Display = pygame.display.set_mode((self.Width, self.Height))
        
        self.Level = "menu"



    def Draw(self): self.Display.fill((0,0,0))
    def tick(self): self.clock.tick(self.FPS)
    def loop(self):
        while not self.Exit:
            if self.Level == "menu":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.Exit = True   
                self.Draw()
                menu.Draw()
                pygame.display.update()
                self.tick()
                
                 

            
            elif self.Level == "Instructions_Rules":
                   for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                         self.Exit = True
                   self.Draw()
                   Instructions_Rules.Draw()
                   pygame.display.update()
                   self.tick() 

            elif self.Level == "Instructions":
                   for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                         self.Exit = True
                   self.Draw()
                   Instructions.Draw()
                   pygame.display.update()
                   self.tick() 

            elif self.Level == "Rules":
                   for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                         self.Exit = True
                   self.Draw()
                   Rules.Draw()
                   pygame.display.update()
                   self.tick() 

            
                
            else: self.Exit = True
        





def Text_Draw(text, size, x, y, textcolor=(0,0,128)):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, textcolor)
    game.Display.blit(screen_text, [x,y])




game = Game()
highscore = Highscore()
menu = Menu()
Instructions_Rules=Instructions_Rules()
Rules=Rules()
Instructions=Instructions()




# boat = pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//MAIN_MENU(2)//7.png")
# boat2 = pygame.image.load("C://Users//erikv//Downloads//project2-battleport-Highscore//project2-battleport-Highscore//HIGHSCORE_MENU(2)//1.png")
game.loop()

pygame.quit()
quit()
