# Text-Based Adventure Game with GUI & Database (Python)

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview
This Python project is a captivating **text-based adventure game** that skillfully blends the power of **Python, Tkinter, and MySQL** to deliver an engaging gaming experience. The game features:

- Character creation and customization
- Exploration of different locations
- Combat mechanics with enemies
- Inventory and item management
- Save/load game progress using a **MySQL database**

This game offers both players and developers a taste of **interactive storytelling** with a graphical user interface (GUI) powered by Tkinter.

---

## Project Structure
```plaintext
.
├── assets/                  # Contains game-related images and icons
├── database/                # MySQL database schema and scripts
│   ├── game_database.sql
│   └── db_connector.py
├── game/
│   ├── main.py              # Main game entry point
│   ├── character.py         # Character creation and attributes
│   ├── inventory.py         # Inventory management system
│   ├── combat.py            # Combat mechanics
│   ├── locations.py         # Exploration system
│   ├── gui.py               # Tkinter-based GUI implementation
│   ├── save_load.py         # Save and load functionality
├── README.md                # Project documentation
├── requirements.txt         # List of required dependencies
└── LICENSE                  # Project License
```

---

## Features
✅ **Character Creation** – Players can create and customize their character.

✅ **Interactive GUI** – The game is fully interactive with a user-friendly Tkinter interface.

✅ **Exploration** – Navigate through different locations and uncover secrets.

✅ **Combat System** – Engage in battles with enemies using turn-based mechanics.

✅ **Inventory Management** – Collect, use, and trade items during the game.

✅ **Database Integration** – Save and load game progress using MySQL.

✅ **Storytelling Elements** – Dynamic dialogues and quest-based gameplay.

---

## Technologies Used
- **Python** – Core programming language
- **Tkinter** – GUI framework for game interface
- **MySQL** – Database for storing game progress and player data
- **Pillow** – For handling images in the game

---

## Installation
To run the project locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Text-Based-Adventure-Game.git
   ```
2. Navigate into the project directory:
   ```sh
   cd Text-Based-Adventure-Game
   ```
3. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

---

## Database Setup
1. Install MySQL and create a new database:
   ```sql
   CREATE DATABASE adventure_game;
   ```
2. Import the schema from `database/game_database.sql`:
   ```sh
   mysql -u your_username -p adventure_game < database/game_database.sql
   ```
3. Update `db_connector.py` with your MySQL credentials.

---

## Usage
Run the game by executing:
```sh
python game/main.py
```

---

## Screenshots

### Initial GUI screenshot
![Image](https://github.com/user-attachments/assets/64c80893-8696-4c4c-bdc8-cf4aea5f3384)

### Game Fight
![Image](https://github.com/user-attachments/assets/1187dfe4-8165-47a8-862d-87c49c441f31)
![Image](https://github.com/user-attachments/assets/99f3d858-fb85-4294-9120-3973a50dddfe)

### End Battle / Dead Scenario
![Image](https://github.com/user-attachments/assets/6af1a906-12a0-4e59-9679-f7b058d54025)
=======

---

## Contributing
Contributions are welcome! If you’d like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new feature branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```sh
   git commit -m 'Add new feature'
   ```
4. Push to the branch:
   ```sh
   git push origin feature-branch
   ```
5. Create a new Pull Request.

---

## License
This project is licensed under the **MIT License**. See the LICENSE file for more details.

---

## Contact
For any questions or suggestions, please contact:

	•	Ayush Raj
	•	Email: ar5787@srmist.edu.in
	•	GitHub: Ayushomega14

