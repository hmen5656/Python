import pygame
from blobsclass import blob
WIDTH=800
HEIGHT=500
RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('huseyin men')
clock = pygame.time.Clock()

class BlueBlob(blob):
    pass

def draw_environment(blobs):
    game_display.fill(WHITE)
    for blob in blobs:
        pygame.draw.circle(game_display,blob.color,[blob.x,blob.y],blob.size)
        blob.move()
        blob.check_baunds()
    pygame.display.update()
def main():
    blobs = [BlueBlob(RED,WIDTH,HEIGHT) for i in range(10)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(blobs)
        clock.tick(60)
if __name__ == '__main__':
    main()
