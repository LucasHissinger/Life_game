
# Life Game Graphical

My python implementation of the famous game of life in a 50x50 grid


## What is "The game of life"

The "Game of Life" is a simple, yet fascinating, cellular automaton created by mathematician John Conway. It's not a traditional game with players, but a simulation where you set up an initial pattern of cells on a grid and watch how they evolve over time based on a set of rules.

Here are the basic rules of the Game of Life:

- Birth: A dead cell with exactly three live neighbors becomes a live cell. In other words, if a cell is empty (dead) and it has exactly three neighboring cells that are alive, a new cell is "born" in that location.

- Survival: A live cell with two or three live neighbors survives. If a cell is already alive and it has either two or three neighbors that are also alive, it continues to live.

- Death: In all other cases, a cell dies. If a cell is alive and has fewer than two live neighbors (underpopulation) or more than three live neighbors (overpopulation), it dies due to loneliness or overcrowding.

These rules are applied simultaneously to all cells on the grid in each generation (iteration), and the pattern evolves over time. 


## Run Locally

Clone the project

```bash
  git clone https://github.com/LucasHissinger/Life_game.git
```

Go to the project directory

```bash
  cd Life_game
```

Install dependencies

```bash
  pip install pygame
```

Start the project

```bash
  python LifeGame.py
```

## Change the starting set

By default there is 9 alive cells in this 50x50 grid. If you wanna change it, change this part of the program :

```python
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
```

(while waiting for a feature allowing you to modify the base set directly on the grid)


## Screenshots

![Capture](https://github.com/LucasHissinger/Life_game/assets/91745215/bd62378b-df11-457e-94e8-3b4b8da0cc38)

![1](https://github.com/LucasHissinger/Life_game/assets/91745215/5105ee3d-728d-4472-b072-7817f7519194)

## Documentation
If you wanna learn more about the game of life i recommand you this video and of course the wikipedia webpage

[Wikipedia](https://fr.wikipedia.org/wiki/Jeu_de_la_vie)

[ScienceEtonnante](https://www.youtube.com/watch?v=S-W0NX97DB0&ab_channel=ScienceEtonnante)


## Feedback

If you have any feedback, please reach out to me at lucas.hissinger@epitech.eu

