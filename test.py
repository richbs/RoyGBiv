import os

from roygbiv import *

roy = Roygbiv(os.path.join(os.path.dirname(__file__), 'test.png'))
assert roy.get_average_hex() == '#468489'
assert roy.get_average_rgb() == (70, 132, 137)
palette_rgb = roy.get_palette_rgb()
palette_hex = roy.get_palette_hex()
assert 1 <= len(palette_rgb) <= 7
assert all(len(color) == 3 and all(0 <= channel <= 255 for channel in color)
           for color in palette_rgb)
assert palette_hex == ['#{:02x}{:02x}{:02x}'.format(*color)
                       for color in palette_rgb]
