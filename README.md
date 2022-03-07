# Phantoms

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

Phantoms is my small platformer game made with pygame. The game uses tile-based physics, along with side-scrolling and parallax animations.

![Screenshot 2022-03-02 130256](https://user-images.githubusercontent.com/72703981/156440654-28aedc0b-9f68-44f9-bf5f-1e040c115e6a.png)


## Quick Start

```
cd Phantoms
python main.py
```

## Requirements


* Pygame

```bash
pip install pygame
```

## Usage

Controls:
* Left arrow key to go left
* Right arrow key to go right
* Up arrow key to jump
* G to throw grenade
* press ESC to escape the game

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 

Please make sure to update tests as appropriate.

## Todo

- Add function to track a tile's current position on a stage current_event 

- Add logic to measure distance of tiles, where the measured distance would be the distance in the tile id's number and letter in alphabet for what units belong to a given tile

- Allow for enemys to take turns in attack

- Allow only valid movements on a level stage

- Change repr functions to be Python expressions

- Add str data model methods

- Add new enemy class objects and attributes
