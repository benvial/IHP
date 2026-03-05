"""Tests for IHP SAX models."""

import jax.numpy as jnp
import sax

from ihp.models.sax import models
from ihp.models.sax.resistors import resistor, rhigh, rppd, rsil


# -- helpers ---------------------------------------------------------------

F = jnp.linspace(1e9, 20e9, 101)
F_SINGLE = jnp.array([5e9])

TWO_PORT_KEYS = {("o1", "o1"), ("o1", "o2"), ("o2", "o1"), ("o2", "o2")}


def _check_two_port(result):
    """Shared sanity checks: keys, reciprocity, passivity, finiteness."""
    assert set(result.keys()) == TWO_PORT_KEYS

    # reciprocity
    assert jnp.allclose(result[("o1", "o2")], result[("o2", "o1")], atol=1e-9)

    # passivity: |S11|^2 + |S21|^2 <= 1
    power = jnp.abs(result[("o1", "o1")]) ** 2 + jnp.abs(result[("o2", "o1")]) ** 2
    assert jnp.all(power <= 1.0 + 1e-6)

    # no NaN/Inf
    for v in result.values():
        assert jnp.all(jnp.isfinite(v))


# -- resistor (generic) ----------------------------------------------------


class TestResistor:
    def test_basics(self):
        _check_two_port(resistor(f=F, resistance=100.0))

    def test_50ohm_in_50ohm_system(self):
        """S11 = Z/(Z+2*Z0) = 50/150 = 1/3."""
        s = resistor(f=F_SINGLE, resistance=50.0, z0=50.0)
        assert abs(float(jnp.abs(s[("o1", "o1")])[0]) - 1 / 3) < 1e-6

    def test_zero_resistance(self):
        """Short circuit: full transmission."""
        s = resistor(f=F_SINGLE, resistance=0.0)
        assert abs(float(jnp.abs(s[("o1", "o2")])[0]) - 1.0) < 1e-6

    def test_output_length(self):
        s = resistor(f=F, resistance=100.0)
        assert len(s[("o1", "o1")]) == len(F)


# -- rsil ------------------------------------------------------------------


class TestRsil:
    def test_basics(self):
        _check_two_port(rsil(f=F, width=1.0, length=10.0))

    def test_one_square_is_7_ohm(self):
        """1-square rsil: R=7, so S11 = 7/107."""
        s = rsil(f=F_SINGLE, width=1.0, length=1.0)
        expected = 7.0 / (7.0 + 2 * 50.0)
        assert abs(float(jnp.abs(s[("o1", "o1")])[0]) - expected) < 1e-6

    def test_longer_means_more_reflection(self):
        s1 = rsil(f=F_SINGLE, width=1.0, length=1.0)
        s2 = rsil(f=F_SINGLE, width=1.0, length=2.0)
        assert float(jnp.abs(s2[("o1", "o1")])[0]) > float(jnp.abs(s1[("o1", "o1")])[0])


# -- rppd ------------------------------------------------------------------


class TestRppd:
    def test_basics(self):
        _check_two_port(rppd(f=F, width=1.0, length=10.0))

    def test_higher_rsh_than_rsil(self):
        s_lo = rsil(f=F_SINGLE, width=1.0, length=1.0)
        s_hi = rppd(f=F_SINGLE, width=1.0, length=1.0)
        assert float(jnp.abs(s_hi[("o1", "o1")])[0]) > float(
            jnp.abs(s_lo[("o1", "o1")])[0]
        )


# -- rhigh -----------------------------------------------------------------


class TestRhigh:
    def test_basics(self):
        _check_two_port(rhigh(f=F, width=0.5, length=10.0))

    def test_highest_rsh(self):
        s_mid = rppd(f=F_SINGLE, width=1.0, length=1.0)
        s_hi = rhigh(f=F_SINGLE, width=1.0, length=1.0)
        assert float(jnp.abs(s_hi[("o1", "o1")])[0]) > float(
            jnp.abs(s_mid[("o1", "o1")])[0]
        )


# -- models dict -----------------------------------------------------------


class TestModelsDict:
    def test_expected_keys(self):
        assert set(models.keys()) == {"resistor", "rsil", "rppd", "rhigh"}

    def test_all_run_with_defaults(self):
        for name, fn in models.items():
            result = fn()
            assert isinstance(result, dict) and len(result) == 4, name
