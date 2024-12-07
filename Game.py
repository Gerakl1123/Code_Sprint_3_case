import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Главный экран")

font = pygame.font.Font(None, 48)

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)
gray = (200, 200, 200)

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, highlight=False):
        color = yellow if highlight else blue
        pygame.draw.rect(screen, color, self.rect)
        text_surface = font.render(self.text, True, white)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

start_button = Button("Начать", width // 2 - 100, height // 2 - 25, 200, 50)

level_buttons = [
    Button(f"Уровень {i + 1}", width // 2 - 100, height // 2 + (i + 1) * 60, 200, 50) for i in range(5)
]

game_started = False
level_1_completed = False  
level_2_completed = False  
level_3_completed = False  
level_4_completed = False

def level_1():
    global level_1_completed
    input_text = ""
    level_1_window_open = True
    while level_1_window_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.strip() == 'print("Hello World!")':
                        level_1_completed = True  
                        level_1_window_open = False  
                    else:
                        input_text = ""  
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  
                else:
                    input_text += event.unicode  

        screen.fill(gray)
        title_surface = font.render('Напишите на Python "Hello World!"', True, black)
        screen.blit(title_surface, (width // 2 - title_surface.get_width() // 2, height // 2 - title_surface.get_height() // 2))

        input_surface = font.render(input_text, True, black)
        screen.blit(input_surface, (width // 2 - input_surface.get_width() // 2, height // 2 + 50))

        pygame.display.flip()

def level_2():
    global level_2_completed
    input_text = ""
    level_2_window_open = True
    while level_2_window_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.strip() == 'input()':
                        level_2_completed = True  
                        level_2_window_open = False  
                    else:
                        input_text = ""  
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  
                else:
                    input_text += event.unicode  

        screen.fill(gray)
        title_surface = font.render("Напишите функцию Python для ввода", True, black)
        screen.blit(title_surface, (width // 2 - title_surface.get_width() // 2, height // 2 - title_surface.get_height() // 2))

        input_surface = font.render(input_text, True, black)
        screen.blit(input_surface, (width // 2 - input_surface.get_width() // 2, height // 2 + 50))
        pygame.display.flip()

def level_3():
    global level_3_completed
    input_text = ""
    level_3_window_open = True
    while level_3_window_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.strip() == 'a = 5':
                        level_3_completed = True  
                        level_3_window_open = False  
                    else:
                        input_text = ""  
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  
                else:
                    input_text += event.unicode  

        screen.fill(gray)
        title_surface = font.render("Присвойте переменной a значение 5", True, black)
        screen.blit(title_surface, (width // 2 - title_surface.get_width() // 2, height // 2 - title_surface.get_height() // 2))

        input_surface = font.render(input_text, True, black)
        screen.blit(input_surface, (width // 2 - input_surface.get_width() // 2, height // 2 + 50))

        pygame.display.flip()

def level_4():
    global level_4_completed
    input_text = ""
    level_4_window_open = True
    while level_4_window_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.strip() == 'while True:':
                        level_4_completed = True  
                        level_4_window_open = False  
                    else:
                        input_text = ""  
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  
                else:
                    input_text += event.unicode  

        screen.fill(gray)
        title_surface = font.render("Создай бесконечный цикл while", True, black)
        screen.blit(title_surface, (width // 2 - title_surface.get_width() // 2, height // 2 - title_surface.get_height() // 2))

        input_surface = font.render(input_text, True, black)
        screen.blit(input_surface, (width // 2 - input_surface.get_width() // 2, height // 2 + 50))

        pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                if start_button.is_clicked(event.pos):
                    game_started = True  
                elif game_started:
                    for i, button in enumerate(level_buttons):
                        if button.is_clicked(event.pos):
                            if i == 0:
                                level_1()  
                            elif i == 1:
                                level_2()  
                            elif i == 2:
                                level_3()  
                            elif i == 3:
                                level_4()

    if not game_started:
        screen.fill(white)
        start_button.draw(screen)
    else:
        screen.fill(gray)
        title_surface = font.render("Выберите уровень:", True, black)
        screen.blit(title_surface, (width // 2 - title_surface.get_width() // 2, height // 2 - title_surface.get_height() // 2 - 100))

        for i, button in enumerate(level_buttons):
            highlight = ((i == 0 and level_1_completed) or (i == 1 and level_2_completed) or
                          (i == 2 and level_3_completed) or (i == 3 and level_4_completed))
            button.draw(screen, highlight)

    pygame.display.flip()

