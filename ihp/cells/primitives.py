"""VLSIR-Compatible Components, Generated with Claude Code"""

import gdsfactory as gf
from gdsfactory.typings import CrossSectionSpec

# Common port layer for schematic-only elements
SCHEM_LAYER = (250, 0)


@gf.cell
def resistor(resistance: float = 1e3, model: str = "rpoly") -> gf.Component:
    c = gf.Component()
    c.add_port(name="p", center=(0, 0), width=0.1, orientation=180, layer=SCHEM_LAYER)
    c.add_port(name="n", center=(1, 0), width=0.1, orientation=0, layer=SCHEM_LAYER)
    c.info["model"] = "resistor"
    c.info["vlsir"] = {
        "model": model,
        "spice_type": "RESISTOR",
        "spice_lib": None,
        "port_order": ["p", "n"],
        "port_map": {},
        "params": {"r": resistance},
    }
    return c


@gf.cell
def capacitor(capacitance: float = 1e-12, model: str = "cpoly") -> gf.Component:
    c = gf.Component()
    c.add_port(name="p", center=(0, 0), width=0.1, orientation=180, layer=SCHEM_LAYER)
    c.add_port(name="n", center=(1, 0), width=0.1, orientation=0, layer=SCHEM_LAYER)
    c.info["model"] = "capacitor"
    c.info["vlsir"] = {
        "model": model,
        "spice_type": "CAPACITOR",
        "spice_lib": None,
        "port_order": ["p", "n"],
        "port_map": {},
        "params": {"c": capacitance},
    }
    return c


@gf.cell
def inductor(inductance: float = 1e-9, model: str = "lind") -> gf.Component:
    c = gf.Component()
    c.add_port(name="p", center=(0, 0), width=0.1, orientation=180, layer=SCHEM_LAYER)
    c.add_port(name="n", center=(1, 0), width=0.1, orientation=0, layer=SCHEM_LAYER)
    c.info["model"] = "inductor"
    c.info["vlsir"] = {
        "model": model,
        "spice_type": "INDUCTOR",
        "spice_lib": None,
        "port_order": ["p", "n"],
        "port_map": {},
        "params": {"l": inductance},
    }
    return c


@gf.cell
def mos(
    w: float = 1e-6,
    length: float = 100e-9,
    nf: int = 1,
    model: str = "nmos",
    spice_lib: str | None = None,
) -> gf.Component:
    c = gf.Component()
    c.add_port(name="D", center=(0, 1), width=0.1, orientation=180, layer=SCHEM_LAYER)
    c.add_port(name="G", center=(-1, 0), width=0.1, orientation=270, layer=SCHEM_LAYER)
    c.add_port(name="S", center=(0, -1), width=0.1, orientation=0, layer=SCHEM_LAYER)
    c.add_port(name="B", center=(1, 0), width=0.1, orientation=90, layer=SCHEM_LAYER)
    c.info["model"] = "mos"
    c.info["vlsir"] = {
        "model": model,
        "spice_type": "MOS",
        "spice_lib": spice_lib,
        "port_order": ["D", "G", "S", "B"],
        "port_map": {},
        "params": {"w": w, "l": length, "nf": nf},
    }
    return c


@gf.cell
def diode(model: str = "diol", area: float = 1e-12, pj: float = 1e-6) -> gf.Component:
    c = gf.Component()
    c.add_port(name="p", center=(0, 0), width=0.1, orientation=180, layer=SCHEM_LAYER)
    c.add_port(name="n", center=(1, 0), width=0.1, orientation=0, layer=SCHEM_LAYER)
    c.info["model"] = "diode"
    c.info["vlsir"] = {
        "model": model,
        "spice_type": "DIODE",
        "spice_lib": None,
        "port_order": ["p", "n"],
        "port_map": {},
        "params": {"area": area, "pj": pj},
    }
    return c


@gf.cell
def bipolar(
    model: str = "npn",
    spice_lib: str | None = None,
    area: float = 1.0,
) -> gf.Component:
    c = gf.Component()
    c.add_port(name="C", center=(0, 1), width=0.1, orientation=90, layer=SCHEM_LAYER)
    c.add_port(name="B", center=(-1, 0), width=0.1, orientation=180, layer=SCHEM_LAYER)
    c.add_port(name="E", center=(0, -1), width=0.1, orientation=270, layer=SCHEM_LAYER)
    c.add_port(
        name="S", center=(1, 0), width=0.1, orientation=0, layer=SCHEM_LAYER
    )  # substrate
    c.info["model"] = "bipolar"
    c.info["vlsir"] = {
        "model": model,
        "spice_type": "BIPOLAR",
        "spice_lib": spice_lib,
        "port_order": ["C", "B", "E", "S"],
        "port_map": {},
        "params": {"area": area},
    }
    return c


@gf.cell
def vsource(dc: float = 0.0, ac: float = 0.0) -> gf.Component:
    """Voltage Source"""
    c = gf.Component()
    c.add_port(name="p", center=(0, 0), width=0.1, orientation=180, layer=SCHEM_LAYER)
    c.add_port(name="n", center=(1, 0), width=0.1, orientation=0, layer=SCHEM_LAYER)
    c.info["model"] = "vsource"
    c.info["vlsir"] = {
        "model": "vsource",
        "spice_type": "VSOURCE",
        "spice_lib": None,
        "port_order": ["p", "n"],
        "port_map": {},
        "params": {"dc": dc, "ac": ac},
    }
    return c


@gf.cell
def isource(dc: float = 0.0, ac: float = 0.0) -> gf.Component:
    """Current Source"""
    c = gf.Component()
    c.add_port(name="p", center=(0, 0), width=0.1, orientation=180, layer=SCHEM_LAYER)
    c.add_port(name="n", center=(1, 0), width=0.1, orientation=0, layer=SCHEM_LAYER)
    c.info["model"] = "isource"
    c.info["vlsir"] = {
        "model": "isource",
        "spice_type": "ISOURCE",
        "spice_lib": None,
        "port_order": ["p", "n"],
        "port_map": {},
        "params": {"dc": dc, "ac": ac},
    }
    return c


@gf.cell
def vcvs(gain: float = 1.0) -> gf.Component:
    """Voltage-controlled voltage source."""
    c = gf.Component()
    c.add_port(
        name="p_out", center=(0, 1), width=0.1, orientation=90, layer=SCHEM_LAYER
    )
    c.add_port(
        name="n_out", center=(0, -1), width=0.1, orientation=270, layer=SCHEM_LAYER
    )
    c.add_port(
        name="p_ctrl", center=(-1, 0), width=0.1, orientation=180, layer=SCHEM_LAYER
    )
    c.add_port(
        name="n_ctrl", center=(1, 0), width=0.1, orientation=0, layer=SCHEM_LAYER
    )
    c.info["model"] = "vcvs"
    c.info["vlsir"] = {
        "model": "vcvs",
        "spice_type": "VCVS",
        "spice_lib": None,
        "port_order": ["p_out", "n_out", "p_ctrl", "n_ctrl"],
        "port_map": {},
        "params": {"gain": gain},
    }
    return c


@gf.cell
def vccs(gm: float = 1e-3) -> gf.Component:
    """Voltage-controlled current source."""
    c = gf.Component()
    c.add_port(
        name="p_out", center=(0, 1), width=0.1, orientation=90, layer=SCHEM_LAYER
    )
    c.add_port(
        name="n_out", center=(0, -1), width=0.1, orientation=270, layer=SCHEM_LAYER
    )
    c.add_port(
        name="p_ctrl", center=(-1, 0), width=0.1, orientation=180, layer=SCHEM_LAYER
    )
    c.add_port(
        name="n_ctrl", center=(1, 0), width=0.1, orientation=0, layer=SCHEM_LAYER
    )
    c.info["model"] = "vccs"
    c.info["vlsir"] = {
        "model": "vccs",
        "spice_type": "VCCS",
        "spice_lib": None,
        "port_order": ["p_out", "n_out", "p_ctrl", "n_ctrl"],
        "port_map": {},
        "params": {"gm": gm},
    }
    return c


@gf.cell
def cccs(gain: float = 1.0) -> gf.Component:
    """Current-controlled current source."""
    c = gf.Component()
    c.add_port(
        name="p_out", center=(0, 1), width=0.1, orientation=90, layer=SCHEM_LAYER
    )
    c.add_port(
        name="n_out", center=(0, -1), width=0.1, orientation=270, layer=SCHEM_LAYER
    )
    c.add_port(
        name="p_ctrl", center=(-1, 0), width=0.1, orientation=180, layer=SCHEM_LAYER
    )
    c.add_port(
        name="n_ctrl", center=(1, 0), width=0.1, orientation=0, layer=SCHEM_LAYER
    )
    c.info["model"] = "cccs"
    c.info["vlsir"] = {
        "model": "cccs",
        "spice_type": "CCCS",
        "spice_lib": None,
        "port_order": ["p_out", "n_out", "p_ctrl", "n_ctrl"],
        "port_map": {},
        "params": {"gain": gain},
    }
    return c


@gf.cell
def ccvs(rm: float = 1e3) -> gf.Component:
    """Current-controlled voltage source."""
    c = gf.Component()
    c.add_port(
        name="p_out", center=(0, 1), width=0.1, orientation=90, layer=SCHEM_LAYER
    )
    c.add_port(
        name="n_out", center=(0, -1), width=0.1, orientation=270, layer=SCHEM_LAYER
    )
    c.add_port(
        name="p_ctrl", center=(-1, 0), width=0.1, orientation=180, layer=SCHEM_LAYER
    )
    c.add_port(
        name="n_ctrl", center=(1, 0), width=0.1, orientation=0, layer=SCHEM_LAYER
    )
    c.info["model"] = "ccvs"
    c.info["vlsir"] = {
        "model": "ccvs",
        "spice_type": "CCVS",
        "spice_lib": None,
        "port_order": ["p_out", "n_out", "p_ctrl", "n_ctrl"],
        "params": {"rm": rm},
    }
    return c


@gf.cell
def tline(z0: float = 50.0, td: float = 1e-9) -> gf.Component:
    """Transmission line."""
    c = gf.Component()
    c.add_port(name="p1", center=(0, 0), width=0.1, orientation=180, layer=SCHEM_LAYER)
    c.add_port(name="n1", center=(0, -1), width=0.1, orientation=180, layer=SCHEM_LAYER)
    c.add_port(name="p2", center=(2, 0), width=0.1, orientation=0, layer=SCHEM_LAYER)
    c.add_port(name="n2", center=(2, -1), width=0.1, orientation=0, layer=SCHEM_LAYER)
    c.info["model"] = "tline"
    c.info["vlsir"] = {
        "model": "tline",
        "spice_type": "TLINE",
        "spice_lib": None,
        "port_order": ["p1", "n1", "p2", "n2"],
        "params": {"z0": z0, "td": td},
    }
    return c


@gf.cell
def subckt(
    model: str,
    ports: list[str],
    spice_lib: str | None = None,
    params: dict | None = None,
) -> gf.Component:
    """Generic subcircuit wrapper."""
    c = gf.Component()

    c.info["model"] = model
    for i, port_name in enumerate(ports):
        c.add_port(
            name=port_name,
            center=(i, 0),
            width=0.1,
            orientation=0 if i % 2 else 180,
            layer=SCHEM_LAYER,
        )
    c.info["vlsir"] = {
        "model": model,
        "spice_type": "SUBCKT",
        "spice_lib": spice_lib,
        "port_order": ports,
        "params": params or {},
    }

    return c


@gf.cell
def tline1(
    length: float = 100,
    width: float = 14,
    signal_cross_section: CrossSectionSpec = "topmetal2_routing",
    ground_cross_section: CrossSectionSpec = "metal3_routing",
    npoints: int = 2,
) -> gf.Component:
    """Returns a straight coplanar transmission line.

    Creates a signal straight and a wider ground straight aligned around it.

    Args:
        length: length of the signal line (um).
        width: signal line width (um).
        signal_cross_section: cross-section for the signal line.
        ground_cross_section: cross-section for the ground line.
        npoints: number of points used to draw the straights.
    """
    c = gf.Component()

    signal = c.add_ref(
        gf.c.straight(
            length=length,
            cross_section=signal_cross_section,
            width=width,
            npoints=npoints,
        )
    )
    c.add_ports(signal.ports)

    ground = c.add_ref(
        gf.c.straight(
            length=length + 6 * width,
            cross_section=ground_cross_section,
            width=7 * width,
            npoints=npoints,
        )
    )
    ground.move((-3 * width, 0))

    return c


@gf.cell
def branch_line_coupler(
    width: float = 10,
    width_coupled: float = 14,
    quarter_wave_length: float = 500,
    connection_length: float = 100,
    signal_cross_section: CrossSectionSpec = "topmetal2_routing",
    ground_cross_section: CrossSectionSpec = "metal3_routing",
) -> gf.Component:
    """Returns a branch line coupler using coplanar transmission lines.

    Creates a four-port rectangular coupler from quarter-wave transmission
    line sections connected at corners.

    Args:
        width: width of the through lines (um).
        width_coupled: width of the coupled (branch) lines (um).
        quarter_wave_length: quarter wavelength at the design frequency (um).
        connection_length: length of the input/output feed lines (um).
        signal_cross_section: cross-section for the signal line.
        ground_cross_section: cross-section for the ground line.
    """
    c = gf.Component()

    signal_layer = gf.get_cross_section(signal_cross_section).layer

    corner = gf.Component()
    corner.add_polygon(
        points=[
            (0, 0),
            (0, width),
            (width - (width_coupled - width), width),
            (width, width_coupled),
            (width, 0),
        ],
        layer=signal_layer,
    )
    corner.add_port(
        name="e1",
        center=(width / 2, 0),
        width=width,
        orientation=270,
        port_type="electrical",
        layer=signal_layer,
    )
    corner.add_port(
        name="e2",
        center=(width, width_coupled / 2),
        width=width_coupled,
        orientation=0,
        port_type="electrical",
        layer=signal_layer,
    )
    corner.add_port(
        name="e3",
        center=(0, width / 2),
        width=width,
        orientation=180,
        port_type="electrical",
        layer=signal_layer,
    )

    # top-left corner
    corner_nw = c.add_ref(corner)

    # top coupled line
    tline_top = c.add_ref(
        tline1(
            length=quarter_wave_length - width,
            signal_cross_section=signal_cross_section,
            ground_cross_section=ground_cross_section,
            width=width_coupled,
        )
    )
    tline_top.connect("e1", corner_nw.ports["e2"])

    # top-right corner
    corner_ne = c.add_ref(corner).mirror(p1=(0, 0), p2=(0, 1))
    corner_ne.connect("e2", tline_top.ports["e2"])

    # left through line
    tline_left = c.add_ref(
        tline1(
            length=quarter_wave_length - width_coupled,
            signal_cross_section=signal_cross_section,
            ground_cross_section=ground_cross_section,
            width=width,
        )
    )
    tline_left.connect("e1", corner_nw.ports["e1"])

    # bottom-left corner
    corner_sw = c.add_ref(corner).mirror(p1=(0, 0), p2=(1, 0))
    corner_sw.connect("e1", tline_left.ports["e2"])

    # bottom coupled line
    tline_bottom = c.add_ref(
        tline1(
            length=quarter_wave_length - width,
            signal_cross_section=signal_cross_section,
            ground_cross_section=ground_cross_section,
            width=width_coupled,
        )
    )
    tline_bottom.connect("e1", corner_sw.ports["e2"])

    # bottom-right corner
    corner_se = (
        c.add_ref(corner).mirror(p1=(0, 0), p2=(1, 0)).mirror(p1=(0, 0), p2=(0, 1))
    )
    corner_se.connect("e2", tline_bottom.ports["e2"])

    # right through line
    tline_right = c.add_ref(
        tline1(
            length=quarter_wave_length - width_coupled,
            signal_cross_section=signal_cross_section,
            ground_cross_section=ground_cross_section,
            width=width,
        )
    )
    tline_right.connect("e1", corner_ne.ports["e1"])

    # input/output feed lines
    for port, name in [
        (corner_nw.ports["e3"], "e1"),
        (corner_ne.ports["e3"], "e2"),
        (corner_se.ports["e3"], "e3"),
        (corner_sw.ports["e3"], "e4"),
    ]:
        feed = c.add_ref(
            tline1(
                length=connection_length,
                signal_cross_section=signal_cross_section,
                ground_cross_section=ground_cross_section,
                width=width,
            )
        )
        feed.connect("e1", port)
        c.add_port(name=name, port=feed.ports["e2"])

    c.move((0, -width))
    return c
