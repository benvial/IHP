"""IHP SG13G2 PDK models."""

from ihp.models.sax import models as sax_models


def get_models() -> dict:
    """Return a dictionary of SAX models for use with the IHP PDK."""
    return dict(sax_models)
