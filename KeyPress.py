import pygame

def init():
    pygame.init()
    window = pygame.display.set_mode((400,400))

def getKey(keyName):
    answer = False
    for event in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        answer = True
    pygame.display.update()

    return answer

def main():
    print(getKey('a'))

if __name__ == '__main__':
    init()
    while True:
        main()