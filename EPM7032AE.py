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
    print("X {pin[0]} {pinno} -150 {ypos} 100 R 50 50 1 1 {pin[1]}".format(pin = pins[row], ypos = ypos, pinno=row + 1))
    print("X {pin[0]} {pinno} 1450 {ypos} 100 L 50 50 1 1 {pin[1]}".format(pin = pins[count - row - 1], ypos = ypos, pinno=count - row))

print(len(pins))
