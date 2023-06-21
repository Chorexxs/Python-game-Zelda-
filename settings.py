# game setup
WIDTH = 1280
HEIGTH = 720
FPS = 60
TILEZISE = 64
HITBOX_OFFSET = {"player": -26, "object": -40, "grass": -10, "invisible": 0}

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = "C:/Users/Usuario/Documents/Python/Python game (Zelda)/Graphics/font/joystix.ttf"
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = "#71ddee"
UI_BG_COLOR = "#222222"
UI_BORDER_COLOR = "#111111"
TEXT_COLOR = "#EEEEEE"

# UI colors
HEALTH_COLOR = "red"
ENERGY_COLOR = "blue"
UI_BORDER_COLOR_ACTIVE = "gold"

# upgrade menu
TEXT_COLOR_SELECTED = "#111111"
BAR_COLOR = "#EEEEEE"
BAR_COLOR_SELECTED = "#111111"
UPGRADE_BG_COLOR_SELECTED = "#EEEEEE"

# weapons
weapon_data = {
    'sword': {'cooldown': 25, 'damage': 15, 'graphic': 'c:/Users/Usuario/Documents/Python/Python game (zelda)/Graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 75, 'damage': 30, 'graphic': 'c:/Users/Usuario/Documents/Python/Python game (zelda)/Graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 50, 'damage': 20, 'graphic': 'c:/Users/Usuario/Documents/Python/Python game (zelda)/Graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 10, 'damage': 8, 'graphic': 'c:/Users/Usuario/Documents/Python/Python game (zelda)/Graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 20, 'damage': 10, 'graphic': 'c:/Users/Usuario/Documents/Python/Python game (zelda)/Graphics/weapons/sai/full.png'}}

# magic
magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic': 'c:/Users/Usuario/Documents/Python/Python game (zelda)/Graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic': 'c:/Users/Usuario/Documents/Python/Python game (zelda)/Graphics/particles/heal/heal.png'}}

# enemy
monster_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': 'c:/Users/Usuario/Documents/Python/Python game (zelda)/Audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw',  'attack_sound': 'c:/Users/Usuario/Documents/Python/Python game (zelda)/Audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 'attack_sound': 'c:/Users/Usuario/Documents/Python/Python game (zelda)/Audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack', 'attack_sound': 'c:/Users/Usuario/Documents/Python/Python game (zelda)/Audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}
