# Dino Runner

https://github.com/user-attachments/assets/d4055236-9b24-4a0b-a808-58afd11eeff1

#### Description:
Dino Runner is a classic endless runner game built using Pygame. In this game, you control a dinosaur navigating through an endless desert landscape, avoiding obstacles such as cacti while trying to achieve the highest possible score.

### Features:
- **Scrolling Background**: Multiple layers of background images scroll at different speeds, creating a parallax effect.
- **Dynamic Difficulty**: The speed of the game increases based on the player's score, making it progressively harder.
- **Cactus Obstacles**: Cacti spawn at random intervals and must be avoided to keep playing.
- **Jumping Mechanics**: The dinosaur can jump to avoid obstacles, with physics-based jump mechanics.
- **Game States**: Includes start, pause, and game over states with appropriate screen messages.
- **Animation**: The dinosaur has multiple animations for different actions such as jumping and running.

### Controls:
- **SPACE**: Jump
- **DOWN Arrow**: Duck
- **ESCAPE**: Pause game
- **ENTER**: Resume game or restart after game over

### Setup:
1. Ensure you have Python and Pygame installed.

```
pip install pygame-ce
```

2. Clone or download this repository.

```
git clone https://github.com/Abhishrent/Dino-Runner-Remastered.git
```

3. Place your sprite images in the appropriate directory structure (already done although):
   - `sprites/player/doux.png`
   - `sprites/world/sky.png`
   - `sprites/world/bg1.png`, `bg2.png`, `bg3.png`, `bg4.png`, `bg5.png`
   - `sprites/world/cactus.png`, `cactus_small.png`
   - `sprites/world/floor.png`

4. Run the `main.py` file to start the game.

```
python main.py
```

### Dependencies:
- Python 3.x
- Pygame


