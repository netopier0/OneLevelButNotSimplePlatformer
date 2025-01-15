# **OT_Game_2024 - Game Design Document**

In this repositary you can find prototype of a game OneLevelButNotSimplePlatformer created in Pygame. 

**Author**: Šimon Szombay

**Chosen theme**: One level, but constantly changing

---
## **1. Introduction**
This is a simple platformer game created as a final project for subject Object Technologies. This game meets requirements of a theme One level, but constantly changing because whole game is composed of 8 levels but movement between these levels is determined by 3x3 sliding puzzle.

### **1.1 Inspiration**
[<ins>**Hopslide**</ins>](https://managore.itch.io/hopslide)

HopSlide consists of two games.

In Hop you can explore a large, blue world. There are some platforms to jump on, springs to launch you into the air, a mysterious map room to investigate and two doors (but they don't seem to go anywhere).

In Slide you can slide some colored blocks around. There are some markings on the blocks (but who cares what those are for). Slide doesn't come with any music so maybe you should leave Hop running in the background.

<p align="center">
  <img src="https://img.itch.zone/aW1hZ2UvMTE2NTEvMzY0NjMucG5n/original/CJOnMc.png" alt="Hopslide">
  <br>
  <em>Figure 1 Preview of Hopslide</em>
</p>

[<ins>**3x3 Sliding Puzzle**</ins>](https://slidingtiles.com/en/puzzle/play/other/25367-3x3-puzzle#3x3)

3x3 Sliding Puzzle is a simple puzzle game where the objective is to slide tiles around in order to create a complete picture. There are 9 slots, 8 puzzle pieces and 1 empty space.

### **1.2 Player Experience**
The goal of the game is for player to visit all levels and press all buttons. Player can move freely around each level and when player want to visit another level player has to move tiles in sliding puzzle.

### **1.3 Development Software**
- **Pygame-CE**: chosen programming language.
- **3D Skicár**: software for drawing sprites for the game

---
## **2. Concept**

### **2.1 Gameplay Overview**
The player controls his character, jumps around each level and tries to press all the buttons. While moving around levels, the player encounters doors which can lead him to different levels based on the current sliding puzzle configuration.

### **2.2 Theme Interpretation**
**"One level, but constantly changing"** - player moves around level and can enter door which may lead him to another level. Which level will the door lead to depends on tiles in 3x3 puzzle, since player can move tiles in puzzle each door can lead to different level depending on 3x3 puzzle. 


### **2.3 Primary Mechanics**
- **Basic Movement**: player jumps and moves around level
- **Doors**: player enters door and may or may not appear in next level
- **Puzzle tiles**: player traverses between levels based on current tile placement

### **2.4 Class design**
- **Game**: class containing the main game logic (game loop)
- **Menu**: class containing start screen
- **Puzzle**: class containing 3x3 sliding Puzzle
- **World**: class containing each level player moves around in
- **Player**: class representing the player, player control, character rendering.

---
## **3. Art**

### **3.1 Theme Interpretation**
The game has simple art design, with aim to minimalism and simplicity. All art was created by me using 3D Skicár. Character is small with only animation being moving feet. Environment is mostly created by small art which is tiled.

<p align="center">
  <img src="https://github.com/netopier0/OneLevelButNotSimplePlatformer/blob/main/assets/character/idle.png" alt="Player">
  <br>
  <em>Figure 2 Preview of player sprite</em>
</p>

### **3.2 Design**
Since I drew all assets myself and I am not an artistic person so my aim was to draw as little as possible. I only created few assets an reused the all throughout the game. Each asset has it destingused used som player won't be confused what object does what.

---
## **4. Game Experience**

### **4.1 UI**
Main screen contains buttons to start and exit the game. Each level contains floor, at least one button, door and multiple objects which help player press the button. Puzzle contains 8 tiles with one level each and one empty space so player can move tiles around.

### **4.2 Controls**
<ins>**Keyboard**</ins>
- **AD**: Player movement
- **W**: Jump
- **S**: Fast fall
- **M**: Open map
- **N**: Close map
- **Escape**: Back to main menu

<ins>**Mouse**</ins> 
- **Left button**: Move tiles on map
