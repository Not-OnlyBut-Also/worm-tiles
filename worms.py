#--- Imports ---#
from PIL import Image
from os import listdir
from random import choice

#--- Directories ---#
tile_dir = 'worms/tiles/'
tiles = listdir(tile_dir)
skull_dir = 'worms/skulls/'
skulls = listdir(skull_dir)

#--- Tiles and Grid ---#
tile_size = 90
wing_size = 150
diff = (wing_size - tile_size)//2
possible_cells = range(2, 9, 2)
grid_width = choice(possible_cells)
grid_height = choice(possible_cells)
tile_dict = {}

#--- Image ---#
img_size = (1080, 1080)
bg = (0, 0, 0)
img = Image.new('RGBA', img_size, bg)
diff_x = img_size[0]//tile_size//2 - grid_width//2
diff_y = img_size[1]//tile_size//2 - grid_height//2

#--- Randomly Insert Tiles ---#
for x in range(grid_width):
    for y in range(grid_height):
        tile_choice = choice(tiles)
        tile_dict[(x, y)] = tile_choice
        tile = Image.open(f'{tile_dir}{tile_choice}').convert('RGBA')
        img.alpha_composite(tile, ((x + diff_x) * tile_size - diff, (y + diff_y) * tile_size - diff))

#--- Add Skulls ---#
skull_choice = choice(range(1, 3))
skull = Image.open(f'{skull_dir}skull{skull_choice}.png').convert('RGBA')
if skull_choice == 1:
    x = (-1 + diff_x) * tile_size - diff - diff//2
elif skull_choice == 2:
    x = (grid_width + diff_x) * tile_size - diff + diff//2
y = choice(range(grid_height))
img.alpha_composite(skull, (x, (y + diff_y) * tile_size - diff))

img.show()
img.save('export.png', quality = 100)