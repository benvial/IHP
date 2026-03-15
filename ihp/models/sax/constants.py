"""
IHP SG13G2 process constants for SAX frequency-domain models.

Values are extracted from the IHP SG13G2 PDK SPICE model libraries
and technology parameters.

References:
    IHP SG13G2 PDK: https://github.com/IHP-GmbH/IHP-Open-PDK
"""

# ---------------------------------------------------------------------------
# Simulation defaults
# ---------------------------------------------------------------------------
DEFAULT_FREQUENCY: float = 5e9  # Hz
Z0_DEFAULT: float = 50.0  # Ω — default reference impedance

# ---------------------------------------------------------------------------
# Resistor sheet resistances (Ω/square, nominal corner)
# Source: cornerRES.lib
# ---------------------------------------------------------------------------
RSH_RSIL: float = 7.0  # Silicided polysilicon
RSH_RPPD: float = 260.0  # P+ polysilicon (unsalicided)
RSH_RHIGH: float = 1360.0  # High-resistance polysilicon
