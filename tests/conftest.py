import pytest

import numpy as np


@pytest.fixture(scope = 'function')
def dummy_args():
    x = np.linspace(0, 1, 100)
    y_0 = 1

    return x, y_0
