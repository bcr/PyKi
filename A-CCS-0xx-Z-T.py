from pint import UnitRegistry

ureg = UnitRegistry()

def generate_pins(total_pins):
    # http://www.assmann-wsw.com/fileadmin/datasheets/ASS_0981_CO.pdf

    pitch = 2.54 * ureg.mm

    pin_maps = {
        20: { "jump_points" : [3, 8, 13, 18], "pin1_side" : "outside" },
        44: { "jump_points" : [6, 17, 28, 39], "pin1_side" : "inside" },
        }

    jump_points = pin_maps[total_pins]["jump_points"]
    current_state = pin_maps[total_pins]["pin1_side"]

    coordinate_x = 0
    coordinate_y = 0

    direction_adjustments = {
        "top" :    { "inside": (-1, -1), "outside": ( 0,  1), "next": "left"   },
        "left" :   { "inside": (-1,  1), "outside": ( 1,  0), "next": "bottom" },
        "bottom" : { "inside": ( 1,  1), "outside": ( 0, -1), "next": "right"  },
        "right" :  { "inside": ( 1, -1), "outside": (-1,  0), "next": "top"    },
    }

    current_pin = 1

    current_direction_adjustments = direction_adjustments["top"]
    current_jump_point = jump_points.pop(0)

    while current_pin <= total_pins:
        yield (current_pin, coordinate_x * pitch, coordinate_y * pitch)

        if current_pin == current_jump_point:
            current_state = "inside"

            current_direction_adjustments = direction_adjustments[current_direction_adjustments["next"]]
            current_jump_point = jump_points.pop(0) if (len(jump_points) > 0) else total_pins + 1

        current_position_adjustment = current_direction_adjustments[current_state]
        current_state = "inside" if current_state == "outside" else "outside"

        coordinate_x += current_position_adjustment[0]
        coordinate_y += current_position_adjustment[1]
        current_pin += 1

for pin in generate_pins(44):
    # (pad 1 thru_hole circle (at -1.27 -5.08) (size 1.524 1.524) (drill 1) (layers *.Cu *.Mask))

    print("  (pad {pin[0]} thru_hole circle (at {xpos} {ypos}) (size 1.524 1.524) (drill 1) (layers *.Cu *.Mask))".format(pin = pin, xpos = pin[1].to(ureg.millimeter).magnitude, ypos = pin[2].to(ureg.millimeter).magnitude))
