import pygame
pygame.init()

class Animation:
    def __init__(self, imagesfile, amount, speed, x, y):
        self.Images = imagesfile
        self.Amount = amount
        self.Speed = speed
        self.Image = 1
        self.I = 0

        self.X = x
        self.Y = y

    def Draw(self):
        pygame.Surface.blit(game.Display, pygame.image.load(self.Images + "\\" + str(self.Image) + ".png"), [self.X, self.Y])
        if self.I > self.Speed:
            self.Image += 1
            if self.Image == 7:
                self.Image = 1
            self.I = 0
        self.I += 1

class Menu:
    def __init__(self):
        self.X = game.Width / 4
        self.Y = game.Height / 10 + 100
        self.Width = game.Width / 2
        self.Head = "BATTLEPORT:"
        self.Subhead = "Rotterdam edition"

        self.Button_height = 50
        self.Button_color = (0,0,128)
        self.Button_color_hover = (0, 0, 180)

        self.Buttons = [\
        Button(self.X, self.Y, game.Width*0.75, self.Y + self.Button_height, self.Button_color, self.Button_color_hover, self.Start, self.Text_draw, "Start game"),\
        Button(self.X, self.Y+self.Button_height*1.5, game.Width*0.75, self.Y+self.Button_height*2.5, self.Button_color, self.Button_color_hover, self.Load, self.Text_draw, "Load game"),\
        Button(self.X, self.Y+self.Button_height*3, game.Width*0.75, self.Y+self.Button_height*4, self.Button_color, self.Button_color_hover, self.Instructions, self.Text_draw, "Instructions"),\
        Button(self.X, self.Y+self.Button_height*4.5, game.Width*0.75, self.Y+self.Button_height*5.5, self.Button_color, self.Button_color_hover, self.Exit, self.Text_draw, "Exit")]

    def Start(self): game.Level = "start"
    def Load(self): game.Level = "load"
    def Instructions(self): game.Level = "instructions"
    def Exit(self): game.Level = "exit"

    def Text_draw(self, text, textcolor, size, x, y):
        self.font = pygame.font.SysFont(None, size)
        self.screen_text = self.font.render(text, True, textcolor)
        game.Display.blit(self.screen_text, [x,y])

    def Draw(self):
        self.Text_draw(self.Head, (20,20,20), 74, self.X, self.Y-125)
        self.Text_draw(self.Subhead, (40,40,40), 35, self.X + 150, self.Y - 75)
        for button in self.Buttons:
            button.Draw()

class Button:
    def __init__(self, x, y, x2, y2, color, colorhover, function, textfunction=None, text=None, textsize=40, textcolor=(255,255,255)):
        self.X = x
        self.Y = y
        self.X2 = x2
        self.Y2 = y2
        self.Color = color
        self.Color_hover = colorhover
        self.Click_function = function

        self.Text = text
        if self.Text != None:
            self.Text_size = textsize
            self.Text_color = textcolor
            self.Text_function = textfunction

    def Hover(self):
        if pygame.mouse.get_pos()[0] > self.X\
        and pygame.mouse.get_pos()[0] < self.X2\
        and pygame.mouse.get_pos()[1] > self.Y\
        and pygame.mouse.get_pos()[1] < self.Y2:
            return True
        else:
            return False

    def Click(self): return pygame.mouse.get_pressed()[0]
    def Clicked(self): self.Click_function()
    
    def Draw(self):
        if self.Hover():
            if self.Click(): self.Clicked()
            else:
                pygame.draw.rect(game.Display, self.Color_hover, (self.X, self.Y, self.X2 - self.X, self.Y2 - self.Y))
        else:
            pygame.draw.rect(game.Display, self.Color, (self.X, self.Y, self.X2 - self.X, self.Y2 - self.Y))
        if self.Text != None:
            self.Text_function(self.Text, self.Text_color, self.Text_size, self.X * 1.05, (self.Y + self.Y2) / 2 - self.Text_size / 4)

class Game:
    def __init__(self):
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.Exit = False

        self.Width = 800
        self.Height = 600
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
                    boat.Draw()
                    menu.Draw()
                    pygame.display.update()
                    self.tick()
            else: self.Exit = True

game = Game()
menu = Menu()
boat = Animation("D:\\VS\\Saves\\Battleport\\images\\Boat_shooting", 6, 1.5, -50, -30)

game.loop()
pygame.quit()
quit()
