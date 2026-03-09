import pygame
import sys

# Pygame başlatılır
pygame.init()

# Renk tanımları
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Tahta boyutu
BOARD_SIZE = 8
SQUARE_SIZE = 80

# Ekran boyutu
width, height = SQUARE_SIZE * BOARD_SIZE, SQUARE_SIZE * BOARD_SIZE
screen = pygame.display.set_mode((width, height))

# Oyun başlığı
pygame.display.set_caption("Chess")

# Tahtanın başlangıç düzeni
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Taşların başlangıç pozisyonlarını oluşturma
def draw_pieces():
    # Burada taşları basit daireler olarak gösteriyoruz.
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if row == 1:  # Siyah piyonlar
                pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 30)
            elif row == 6:  # Beyaz piyonlar
                pygame.draw.circle(screen, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 30)

# Ana oyun döngüsü
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board()   # Tahtayı çiz
        draw_pieces()  # Taşları çiz

        pygame.display.flip()  # Ekranı güncelle

if __name__ == "__main__":
    main()
