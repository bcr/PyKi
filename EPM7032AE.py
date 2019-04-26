from pint import UnitRegistry

ureg = UnitRegistry()

#(-150,-150)
#(-150,-250)

pins = (
    ("INPUT/GCLRn", "I"),
    ("INPUT/OE2/GCLK2", "I"),
    ("VCC", "W"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O/TDI", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("GND", "W"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O/TMS", "B"),
    ("I/O", "B"),
    ("VCC", "W"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("GND", "W"),
    ("VCC", "W"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("GND", "W"),
    ("I/O", "B"),
    ("I/O/TCK", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("VCC", "W"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O/TDO", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("I/O", "B"),
    ("GND", "W"),
    ("INPUT/GCLK1", "I"),
    ("INPUT/OE1n", "I"),
)

count = len(pins)

rows = int(count / 2)

for row in range(rows):
    ypos = -150 - (row * 100)
    print(-150, ypos)
    print(1450, ypos)

print(len(pins))
