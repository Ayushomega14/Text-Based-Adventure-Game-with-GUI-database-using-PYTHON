import mysql.connector
import tkinter as tk
from tkinter import ttk
import random

# Initialize the MySQL database connection
conn = mysql.connector.connect(
    host="Localhost",
    user="root",
    password="your_password",
    database="game_database"
)
cursor = conn.cursor()

# Create the GUI window
window = tk.Tk()
window.title("Text-Based Adventure Game")
window.configure(bg='#d9d9d9')  # Set background color to light gray

# Initialize player's data
player = {"name": "", "health": 100}
inventory = []

# Initialize room data
current_room = 0

# This is a Function to fetch character names from the database
def fetch_characters():
    cursor.execute("SELECT name FROM Characters")
    character_names = cursor.fetchall()
    character_listbox.delete(0, tk.END)
    for name in character_names:
        character_listbox.insert(tk.END, name[0])

# This is a Function to fetch monsters from the database
def fetch_monsters():
    cursor.execute("SELECT name, health, description FROM Monsters")
    monsters = cursor.fetchall()
    return [{"name": monster[0], "health": monster[1], "description": monster[2]} for monster in monsters]

# This is a Function to display selected character's inventory
def display_inventory():
    selected_character = character_listbox.get(tk.ACTIVE)
    cursor.execute("SELECT name FROM InventoryItems WHERE owner_id = (SELECT character_id FROM Characters WHERE name = %s)", (selected_character,))
    inventory_items = cursor.fetchall()
    inventory_text.config(state=tk.NORMAL)
    inventory_text.delete("1.0", tk.END)
    for item in inventory_items:
        inventory_text.insert(tk.END, item[0] + "\n")
    inventory_text.config(state=tk.DISABLED)

# This is a Function to simulate a monster encounter
def encounter_monster():
    monster = random.choice(fetch_monsters())
    message_label.config(text=f"A wild {monster['name']} appears!")
    fight_button.config(state=tk.NORMAL, command=lambda: fight_monster(monster))

# This is a Function to simulate a fight with a monster
def fight_monster(monster):
    player_damage = random.randint(10, 20)
    monster_damage = random.randint(5, 15)

    player["health"] -= monster_damage
    monster["health"] -= player_damage

    update_health_bar()

    if player["health"] <= 0:
        message_label.config(text="You were defeated by the monster. Game over!")
        fight_button.config(state=tk.DISABLED)
    elif monster["health"] <= 0:
        message_label.config(text=f"You defeated the {monster['name']}!")
        inventory.append(monster['name'])
        fetch_characters()
        generate_random_room()
        fight_button.config(state=tk.DISABLED)
    else:
        message_label.config(text=f"You attack the {monster['name']} and deal {player_damage} damage. "
                                  f"The {monster['name']} has {monster['health']} health left.")
        window.after(1000, lambda: fight_monster(monster))

# This is a Function to generate a random room description
def generate_random_room():
    global current_room
    current_room = random.randint(0, len(rooms) - 1)
    room_description.config(text=rooms[current_room]["description"])
    encounter_monster_button.config(state=tk.NORMAL)

# This is a Function to handle character name entry and start the game
def start_game():
    player_name = name_entry.get()
    player["name"] = player_name
    fetch_characters()
    window.after(2000, generate_random_room)

# This is a Function to update the health bar
def update_health_bar():
    health_var.set(player["health"])

# This is a Function to restore health using health items
def restore_health():
    # Retrieve a health-restoring item from the database
    cursor.execute("SELECT name, healing_power FROM HealthItems WHERE owner_id = (SELECT character_id FROM Characters WHERE name = %s) ORDER BY RAND() LIMIT 1", (player["name"],))
    health_item = cursor.fetchone()

    if health_item:
        health_power = health_item[1]
        player["health"] += health_power

        # Ensure player health does not exceed the maximum (100)
        if player["health"] > 100:
            player["health"] = 100

        update_health_bar()
        message_label.config(text=f"You used {health_item[0]} to restore {health_power} health.")
    else:
        message_label.config(text="No health-restoring items available.")

# Create GUI elements
# Entry widget for entering player name
name_entry_label = tk.Label(window, text="Enter Your Character's Name:", bg='#d9d9d9', fg='black')  # Set label color
name_entry_label.pack()
name_entry = tk.Entry(window, width=20)
name_entry.pack()

set_name_button = tk.Button(window, text="Set Name", command=start_game, bg='yellow')  # Set button color
set_name_button.pack()

character_label = tk.Label(window, text="Characters:", bg='#d9d9d9', fg='black')  # Set label color
character_label.pack()
character_listbox = tk.Listbox(window)
character_listbox.pack()
fetch_characters()

inventory_label = tk.Label(window, text="Inventory:", bg='#d9d9d9', fg='black')  # Set label color
inventory_label.pack()
inventory_text = tk.Text(window, height=5, width=30, state=tk.DISABLED, bg='white')
inventory_text.pack()

show_inventory_button = tk.Button(window, text="Show Inventory", command=display_inventory, bg='yellow')  # Set button color
show_inventory_button.pack()

message_label = tk.Label(window, text="", bg='#d9d9d9', fg='black')  # Set label color
message_label.pack()

fight_button = tk.Button(window, text="Fight", state=tk.DISABLED, bg='yellow')  # Set button color
fight_button.pack()

room_description = tk.Label(window, text="", bg='#d9d9d9', fg='black')  # Set label color
room_description.pack()

encounter_monster_button = tk.Button(window, text="Explore Room", state=tk.DISABLED, command=encounter_monster, bg='yellow')  # Set button color
encounter_monster_button.pack()

# Health bar
health_label = tk.Label(window, text="Health:", bg='#d9d9d9', fg='black')  # Set label color
health_label.pack()
health_var = tk.IntVar()
health_bar = ttk.Progressbar(window, variable=health_var, length=200, mode='determinate')
health_bar.pack()

# Restore Health button
restore_health_button = tk.Button(window, text="Restore Health", command=restore_health, bg='green', fg='white')  # Set button color
restore_health_button.pack()

# Define a list of rooms with descriptions
rooms = [
    {"description": "You are in a dark cave. It smells musty."},
    {"description": "You are in a lush forest. Birds are chirping."},
    {"description": "You find yourself in a dusty old library. Books are scattered everywhere."},
    {"description": "You are on a sandy beach. Waves crash against the shore."},
]

# Start the GUI main loop
window.mainloop()

# Close the database connection when the GUI is closed
conn.close()
