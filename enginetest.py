import pygame
pygame.init()


gameDisplay=pygame.display.set_mode((1000,800))#defining gamedisplay
White=(255,255,255) # defining white

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
                if self.Image == 7:
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
    def __init__(self, x, y, width, height, function, color, hovercolor, text,Constant, textcolor=(0,0,0)):
        self.X = x
        self.Y = y
        self.Width = width
        self.Height = height

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

def Text_draw(text, size, x, y, textcolor=(255,255,255)):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, textcolor)
    game.Display.blit(screen_text, [x,y])

class Game:
    def __init__(self):
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.Exit = False

        self.Width = 1000
        self.Height = 800
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
                buttons.Draw()        ###### draws the container 
                pygame.display.update()
                self.tick()
                
                 
##### add buttons here (play, load , settings , etc)
            
            elif self.Level == "Instruction":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                      self.Exit = True
                self.draw()
                buttons_instructions.Draw()
                pygame.display.update()
                self.tick() 
                
                
                
            elif self.Level == "Rules":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                      self.Exit = True
                self.draw()
                buttons_rules.Draw()
                pygame.display.update()
                self.tick()
              
                
               
                              
            
           
            else: self.Exit = True
        
game = Game()


#def __init__(self, x, y, width, height, function, color, hovercolor, text,Constant, textcolor=(0,0,0)):
buttons=Container(10,100,400,500,50,0)
buttons_instructions=Container(10,100,400,700,50,0)
buttons_rules=Container(10,100,400,700,50,0)


###### instructions/rules

## image array test out



L_instructions=[""] *100
L_instructions[0]=pygame.image.load("C://Users//erikv//Downloads//project2-battleport-master//project2-battleport-master//images//Boat_shooting//testtext.png")
L_instructions[1]=pygame.image.load("2.png")

newL_instructions=[]

for i in L_instructions:
    
    L_instructions[0]=pygame.transform.scale(L_instructions[0],(600,600))
    newL_instructions.append(L_instructions[0])

L_rules=[""]*100
L_rules[0]=pygame.image.load("C://Users//erikv//Downloads//project2-battleport-master//project2-battleport-master//images//Boat_shooting//testtext.png")

newL_rules=[]
for i in L_rules:
    L_rules[0]=pygame.transform.scale(L_rules[0],(600,600))



def Rules():       #### instruction menu init
    game.Level=("Rules")

def rules_menu():
    game.Level=("rules_menu")
    if General_rules():
        pass
    if Ship_rules():
        pass
    if Card_rules():
        pass
    
def General_rules():
    pygame.draw.rect(gameDisplay,(0,0,0),(buttons_rules.Width+50,500,500,500))

def Ship_rules():
    pygame.draw.rect(gameDisplay,(200,0,0),(buttons_rules.Width+50,500,500,500))

def Card_rules():
    pygame.draw.rect(gameDisplay,(200,0,0),(buttons_rules.Width+50,500,500,500))
    







    

#### add all images for rules here in array , then use array to determine which image to show on screen



def Instruction():      ### instruction menu init
    game.Level=("Instruction")



def instruction_menu():
    game.Level=("instruction_menu")
    if General_instructions():
        pass
    if Ship_instructions():
        pass
    if Card_instructions():
        pass
        
def General_instructions():  
      pygame.draw.rect(gameDisplay,(200,0,0),(buttons_instructions.Width+50,100,600,500))

def Ship_instructions():
    pygame.draw.rect(gameDisplay,(200,0,0),(buttons_instructions.Width+50,100,600,500))


def Card_instructions():      
   
    gameDisplay.blit(newL_instructions[0],(400,100))
    
    
#### back
def back_menu():
    game.Level="menu"
def back_instructions():
    game.Level=("Instruction")

def back_rules():
    game.Level="Rules"

### buttons main menu
buttons.Add_button((255,255,255),(200,200,200),Rules,"Rules",(0,0,0))
buttons.Add_button((255,255,255),(200,200,200),Instruction,"Instructions",(0,0,0))

### buttons instruction menu
buttons_instructions.Add_button((255,255,255),(200,200,200),General_instructions,"General_instructions",(0,0,255))
buttons_instructions.Add_button((255,255,255),(200,200,200),Ship_instructions,"Ship_instructions",(0,0,0))
buttons_instructions.Add_button((255,255,255),(200,200,200),Card_instructions,"Card_instructions",(0,0,0))
buttons_instructions.Add_button((255,255,255),(200,200,200),back_instructions,"back_instructions",(0,0,0))
### buttons rules menu 
buttons_rules.Add_button((255,255,255),(200,200,200),General_rules,"General_rules",(0,0,0))
buttons_rules.Add_button((255,255,255),(200,200,200),Ship_rules,"Ship_rules",(0,0,0))
buttons_rules.Add_button((255,255,255),(200,200,200),Card_rules,"Card_rules",(0,0,0))
buttons_rules.Add_button((255,255,255),(200,200,200),Rules,"back_rules",(0,0,0))
 
#### 1/20 text about instructions


##### end instructions/rules
game.loop()

pygame.quit()
quit()




