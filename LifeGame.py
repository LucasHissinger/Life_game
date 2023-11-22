import pygame, time, sys

size = 50
grille = [[0 for i in range(size)] for j in range(size)]

# change this to modify the grid
grille[9][0] = 1

grille[10][1] = 1
grille[10][2] = 1
grille[10][3] = 1
grille[10][4] = 1
grille[10][5] = 1

grille[9][5] = 1
grille[8][5] = 1

grille[7][4] = 1


def life(grille, size):
  next_grille = [[0 for i in range(size)] for j in range(size)]
  for i in range(size):
    for j in range(size):
      nb = 0
      if i == 0:
        if j == 0:
          nb = around(grille, [0, 1, 1], [1, 0, 1])
        elif j == size-1:
          nb = around(grille, [0, 1, 1], [size-2, size-2, size-1])
        else:
          nb = around(grille, [0, 1, 1, 1, 0], [j+1, j+1, j, j-1, j-1])
      elif i == size-1:
        if j == 0:
          nb = around(grille, [size-2, size-2, size-1], [0, 1, 1])
        elif j == size-1:
          nb = around(grille, [size-1, size-2, size-2],[size-2, size-2, size-1])
        else:
          nb = around(grille, [size-1, size-2, size-2, size-2, size-1], [j+1, j+1, j, j-1, j-1])
      elif j == 0:
        nb = around(grille, [i-1, i-1, i, i+1, i+1], [0, 1, 1, 1, 0])
      elif j == size-1:
        nb = around(grille, [i-1, i-1, i, i+1, i+1], [size-1, size-2, size-2, size-2, size-1])
      else:
        nb = around(grille, [i-1, i, i+1, i+1, i+1, i, i-1, i-1], [j-1, j-1, j-1, j, j+1, j+1, j+1, j])
      if nb == 3 or (grille[i][j] == 1 and nb == 2):
        next_grille[i][j] = 1
      else:
        next_grille[i][j] = 0
  return next_grille


def around(grille, list_i, list_j):
  nb = 0
  for i,j in zip(list_i, list_j):
    if grille[i][j] == 1:
      nb += 1
  return nb

pygame.init()

S_size = width, height = 1000, 800

screen = pygame.display.set_mode(S_size)
running = True

while running:

  screen.fill((255, 255, 255))
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

  for i in range(size):
    for j in range(size):
      if grille[i][j] == 0:
          pygame.draw.rect(screen, (255, 255, 255), (50+int(600/size)*j, 50+int(600/size)*i, int(600/size)-1, int(600/size)-1))
          pygame.draw.rect(screen, (0, 0, 0), (50+int(600/size)*j, 50+int(600/size)*i, int(600/size)-1, int(600/size)-1), 1)  # Ajout de la bordure noire
      elif grille[i][j] == 1:
          pygame.draw.rect(screen, (30, 220, 130), (50+int(600/size)*j, 50+int(600/size)*i, int(600/size)-1, int(600/size)-1))
          pygame.draw.rect(screen, (0, 0, 0), (50+int(600/size)*j, 50+int(600/size)*i, int(600/size)-1, int(600/size)-1), 1)  # Ajout de la bordure noire

  time.sleep(0.1)
  grille = life(grille, size)
  pygame.display.flip()
