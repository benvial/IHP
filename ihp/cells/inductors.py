"""Inductor components for IHP PDK."""

import math

import gdsfactory as gf
from gdsfactory import Component


def inductor_min_diameter(width: float, space: float, turns: int, grid: float) -> float:
    """Calculate minimum diameter for inductor.

    Args:
        width: Width of the inductor trace in micrometers.
        space: Space between turns in micrometers.
        turns: Number of turns.
        grid: Grid resolution.

    Returns:
        Minimum diameter in micrometers.
    """
    min_d = 2 * turns * (width + space) + 4 * width
    return round(min_d / grid) * grid


@gf.cell
def inductor2(
    width: float = 2.0,
    space: float = 2.1,
    diameter: float = 25.35,
    resistance: float = 0.5777,
    inductance: float = 33.303e-12,
    turns: int = 1,
    block_qrc: bool = True,
) -> Component:
    """Create a 2-turn inductor.

    Args:
        width: Width of the inductor trace in micrometers.
        space: Space between turns in micrometers.
        diameter: Inner diameter in micrometers.
        resistance: Resistance in ohms.
        inductance: Inductance in henries.
        turns: Number of turns (default 1 for inductor2).
        block_qrc: Block QRC layer.

    Returns:
        Component with inductor layout.
    """
    c = Component()

    # Define layers
    TM2 = (134, 0)  # TopMetal2
    IND = (27, 0)  # IND layer
    NoRCX = (148, 0)  # NoRCX layer
    PWellBlock = (46, 21) # PWellBlock layer
    TopMetal2Pin = (134, 2) #TopMetal2pin layer

    # No fill layers
    NoFill_layers = [
        (1, 23),  # ActiveNoFill
        (5, 23),  # GatePolyNoFill
        (8, 23),  # Metal1NoFill
        (10, 23),  # Metal2NoFill
        (30, 23),  # Metal3NoFill
        (50, 23),  # Metal4NoFill
        (67, 23),  # Metal5NoFill
        (126, 23),  # TopMetal1NoFill
        (134, 23),  # TopMetal2NoFill
    ]

    # Grid fixing for manufacturing constraints
    grid = 0.01
    w = round(width / (2 * grid)) * 2 * grid
    s = round(space / grid) * grid
    d = round(diameter / (2 * grid)) * 2 * grid

    # Calculate geometry parameters
    r = d / 2 + s
    octagon_center_y = 3 * r
    pi_over_4 = math.radians(45)

    path_points = []
    path_points.append((+space/2, octagon_center_y - r * math.cos(pi_over_4 / 2)))

    for i in range(-2, 6):
        angle = i * pi_over_4 + pi_over_4 / 2
        r = d / 2 + s
        x = r * math.cos(angle)
        y = r * math.sin(angle) + octagon_center_y

        if -2 <= i < 2:
            path_points.append((x, y))
        else:
            path_points.append((x, y))

    path_points.append((-space/2, octagon_center_y - r * math.cos(pi_over_4 / 2)))

    # Create the path
    path = gf.Path(path_points)
    c << gf.path.extrude(path, layer=TM2, width=w)

    # Adding ports
    length = 2 * r + s

    port1_trace = c << gf.components.rectangle(size=(s, length), layer=TM2)
    port1_trace.move((-s - s/2, 0))
    c.add_port(
        name="P1", center=(-s, s), width=s, orientation=270, layer=TM2
    )

    port2_trace = c << gf.components.rectangle(size=(s, length), layer=TM2)
    port2_trace.move((s - s/2, 0))
    c.add_port(
        name="P2", center=(+s, s), width=s, orientation=270, layer=TM2
    )

    # Add IND layer
    outer_polygon_pts = []
    for i in range(8):
        r_outer =  (d / 2 + length) / (math.cos(pi_over_4/2))
        angle = i * pi_over_4 + pi_over_4 / 2
        x = r_outer * math.cos(angle)
        y = r_outer * math.sin(angle) + octagon_center_y
        outer_polygon_pts.append((x, y))
    c.add_polygon(points=outer_polygon_pts, layer=IND)

    # Add No fill layers
    for layer in NoFill_layers:
        c.add_polygon(points=outer_polygon_pts, layer=layer)

    # Add blocking layer
    if block_qrc:
        c.add_polygon(points=outer_polygon_pts, layer=NoRCX)

    # Add PWell block
    c.add_polygon(points=outer_polygon_pts, layer=PWellBlock)

    # Adding pins
    pin_1_trace = c << gf.components.rectangle(size=(s, s), layer=TopMetal2Pin)
    pin_1_trace.move((s/2, 0))

    pin_2_trace = c << gf.components.rectangle(size=(s, s), layer=TopMetal2Pin)
    pin_2_trace.move((-s-s/2, 0))

    # Add metadata
    c.info["resistance"] = resistance
    c.info["inductance"] = inductance
    c.info["model"] = "inductor2"
    c.info["turns"] = turns
    c.info["width"] = width
    c.info["space"] = space
    c.info["diameter"] = diameter

    return c


@gf.cell
def inductor3(
    width: float = 2.0,
    space: float = 2.1,
    diameter: float = 24.68,
    resistance: float = 1.386,
    inductance: float = 221.5e-12,
    turns: int = 2,
    block_qrc: bool = True,
    substrate_etch: bool = False,
) -> Component:
    """Create a 3-turn inductor.

    Args:
        width: Width of the inductor trace in micrometers.
        space: Space between turns in micrometers.
        diameter: Inner diameter in micrometers.
        resistance: Resistance in ohms.
        inductance: Inductance in henries.
        turns: Number of turns (default 2 for inductor3).
        block_qrc: Block QRC layer.
        substrate_etch: Enable substrate etching.

    Returns:
        Component with inductor layout.
    """
    # Use inductor2 as base with different default parameters
    return inductor2(
        width=width,
        space=space,
        diameter=diameter,
        resistance=resistance,
        inductance=inductance,
        turns=turns,
        block_qrc=block_qrc,
        substrate_etch=substrate_etch,
    )


if __name__ == "__main__":
    from ihp import PDK
    from ihp.cells import fixed

    from gdsfactory.difftest import xor

    PDK.activate()

    # Test the components
    c0 = fixed.inductor2()  # original
    c1 = inductor2()  # New
    # c = gf.grid([c0, c1], spacing=100)
    c = xor(c0, c1)
    c.show()

    # c0 = cells.inductor3()  # original
    # c1 = inductor3()  # New
    # # c = gf.grid([c0, c1], spacing=100)
    # c = xor(c0, c1)
    # c.show()
