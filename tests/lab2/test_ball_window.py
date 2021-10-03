import numpy as np
import pytest

from lab2.ball_window import BallWindow

# ==========================
# ==== BallWindow tests ====
# ==========================


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "center, radius, expected",
    [
        (np.array([1, 1]), 1.0, "BallWindow: center=[1 1], radius=1.00"),
        (
            np.array([0, 1, 2, 3.1]),
            4.129,
            "BallWindow: center=[0 1 2 3.1], radius=4.13",
        ),
        (
            np.array([1.2345, 6.7891011],),
            2.22,
            "BallWindow: center=[1.23 6.79], radius=2.22",
        ),
    ],
)
def test_ball_string_representation(center, radius, expected):
    assert str(BallWindow(center, radius)) == expected


@pytest.mark.parametrize(
    "ball_window, expected",
    [
        (BallWindow(np.array([1, 2, 6, 8, 9, 9516198])), 6),
        (BallWindow(np.array([3.14, 2.78, 1.67])), 3),
    ],
)
def test_len(ball_window, expected):
    assert len(ball_window) == expected


@pytest.mark.parametrize(
    "ball_window, expected",
    [
        (BallWindow(np.array([1, 3])), np.pi),
        (BallWindow(np.array([])), 1),
        (BallWindow(np.array([1, 2, 3, 4]), 2), np.pi ** 2 * 8),
    ],
)
def test_volume(ball_window, expected):
    vol = ball_window.volume()
    assert round(vol, 10) == round(expected, 10)


@pytest.fixture
def ball_3d_1():
    return BallWindow(np.array([1, 1, 1]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([1, 1, 1]), True),
        (np.array([0, 1, 5]), False),
        (np.array([1, 0.9, 0.8]), True),
    ],
)
def test_ball3d_contains(ball_3d_1, point, expected):
    contain = point in ball_3d_1
    assert contain == expected
