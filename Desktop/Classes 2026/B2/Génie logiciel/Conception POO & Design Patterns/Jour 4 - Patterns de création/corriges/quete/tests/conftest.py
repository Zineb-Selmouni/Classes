import pytest

try:
    from pyquest.config import Configuration
except ImportError:  # config.py pas encore écrit
    Configuration = None


@pytest.fixture(autouse=True)
def configuration_neuve():
    """Le Singleton garde son état d'un test à l'autre : on le remet à zéro."""
    if Configuration is not None and hasattr(Configuration, "reinitialiser"):
        Configuration.reinitialiser()
    yield
