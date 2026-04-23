# 🌊 Ocean Grabber

A 2D arcade game built in Python and Pygame as the Grade 11 Computer Science culminating project. Play as a scuba diver collecting ocean plastic before it reaches the marine life — all while dodging bombs that get faster as your score increases.

🎥 **Demo:** [Watch on YouTube](https://www.youtube.com/shorts/AUJsslGQf4c)  
🐙 **Repo:** [github.com/rayhasgor07/Ocean-Grabber](https://github.com/rayhasgor07/Ocean-Grabber)

---

## Gameplay

You control a scuba diver with a net. Plastic trash falls from above — catch it before it crosses the fish line or the ocean gets polluted and the game ends. 3 bombs patrol the screen horizontally, and touching one ends the game immediately. The longer you survive, the faster everything gets.

---

## Features

### 🤿 Player
- Animated scuba diver with 3 directional sprites (idle, left, right)
- Movement via arrow keys or WASD
- Bounded to the upper half of the ocean — can't cross the fish line

### 🗑️ Falling Plastic
- 5 types of plastic randomly selected each spawn — water bottle, jug, coke can, sprite can, coffee cup
- Fall speed scales with score — the better you do, the harder it gets
- Splash sound when plastic enters the water

### 💣 Bombs
- 3 bombs patrol horizontally across the screen
- Speed increases with score — same scaling as the plastic
- Bomb collision resets positions and triggers game over
- Bombs auto-reposition if they collide with each other

### 💥 Collision Detection
- Net-to-plastic collision for scoring
- Player-to-bomb collision for game over
- Plastic-crossing-fish-line for game over

### 🎵 Audio
- Splash sound on plastic entry
- Touch sound on successful catch
- Bomb explosion sound on hit
- End game sound when plastic reaches the fish
- Click sound on menu buttons
- Swim sound on player movement

### 📋 Menu System
- Main menu with Start, Help, and Quit
- Help screen with full instructions and keyboard diagram
- Back button available in-game and on the help screen
- Clean state machine: `STATE_MENU`, `STATE_GAME`, `STATE_HELP`, `STATE_QUIT`

---

## Controls

| Action | Key |
|--------|-----|
| Move | Arrow Keys / WASD |
| Back to Menu | Click the Back button |

---

## How to Run

1. Install Python and Pygame:
```bash
pip install pygame
```
2. Navigate to the `Zummative` folder
3. Run the game:
```bash
python game.py
```

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python |
| Game Engine | Pygame |
| Audio | Pygame Mixer |

---

## Recognition

🏆 Perfect score (100%) — Grade 11 Computer Science Culminating Project

---

## Screenshots

> Watch the demo: [YouTube Short](https://www.youtube.com/shorts/AUJsslGQf4c)

---

## About the Developer

Built by **Rayyan Hasan Goraya** — Computational Mathematics student at the University of Waterloo, working at the intersection of game development, software engineering, and data analytics.

🌐 [Portfolio](https://rayhasgor.web.app) · 💼 [LinkedIn](https://linkedin.com/in/rayyanhasangoraya) · 🐙 [GitHub](https://github.com/rayhasgor07)

---

© 2026 Rayyan Hasan Goraya. All rights reserved.
