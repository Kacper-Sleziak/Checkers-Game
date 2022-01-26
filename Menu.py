import pygame

# Do poprawy --- kod ze starych lat ... przepraszam ...
class Menu():

    def __init__(self, width, height, screen):
        super().__init__()
        self.width = width
        self.height = height
        self.screen = screen

    def menuDisplay(self):

        def message_display(text, rozmiar, x, y, R, G, B):
            largeText = pygame.font.Font('freesansbold.ttf', rozmiar)
            TextSurf, TextRect = text_objects(text, largeText, R, G, B)
            TextRect.center = ((x), (y))
            self.screen.blit(TextSurf, TextRect)

        def text_objects(text, font, R, G, B):
            textSurface = font.render(text, True, (R, G, B))
            return textSurface, textSurface.get_rect()

        kolor_ekranu = (255, 255, 255)

        running = True


        while running:
          for event in pygame.event.get():
              pygame.display.update()
              self.screen.fill(kolor_ekranu)
              message_display("Multi-player", 30, self.width / 2, self.height / 2, 80, 80, 80)
              message_display("Hot-seat", 30, self.width / 2, self.height / 2 - 100, 80, 80, 80)
              if event.type == pygame.QUIT:
                  pygame.quit()
                  quit()
              if event.type == pygame.MOUSEMOTION:
                  pos = pygame.mouse.get_pos()
                  if pos[0] > self.width / 2 - 50 and pos[0] < self.width / 2 + 50 and pos[1] > self.height / 2 - 20 and pos[
                      1] < self.height / 2 + 20:
                      self.screen.fill(kolor_ekranu)
                      message_display("Multi-player", 50, self.width / 2, self.height / 2, 80, 80, 80)
                      message_display("Hot-seat", 30, self.width / 2, self.height / 2 - 100, 80, 80, 80)
                  if pos[0] > self.width / 2 - 50 and pos[0] < self.width / 2 + 50 and pos[1] > self.height / 2 - 120 and pos[
                      1] < self.height / 2 - 80:
                      self.screen.fill(kolor_ekranu)
                      message_display("Multi-player", 30, self.width / 2, self.height / 2, 80, 80, 80)
                      message_display("Hot-seat", 50, self.width / 2, self.height / 2 - 100, 80, 80, 80)
              if event.type == pygame.MOUSEBUTTONUP:
                  pos = pygame.mouse.get_pos()
                  if pos[0] > self.width / 2 - 50 and pos[0] < self.width / 2 + 50 and pos[1] > self.height / 2 - 20 and pos[
                      1] < self.height / 2 + 20:
                      running = False
                      # display waiting wor game
                      return "Multi-player"


                  if pos[0] > self.width / 2 - 50 and pos[0] < self.width / 2 + 50 and pos[1] > self.height / 2 - 120 and pos[
                      1] < self.height / 2 - 80:
                      running = False
                      return "Hot-seat"
