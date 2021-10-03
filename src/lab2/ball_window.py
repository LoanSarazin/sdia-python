from lab2.utils import get_random_number_generator
import numpy as np
import numpy.linalg as la
from math import gamma


class BallWindow:
    """BallWindow: :math:`X in \mathbb{R}^{n},\, \|X-C\|_{2}\leq r`"""

    def __init__(self, center, radius=1.0):
        """Initialize the BallWindow from the bounds given and from a radius

        Args:
            center (array): Array containing the coordinates of the center.
            radius (float, optional): The radius of the BallWindow. Defaults to 1.
        """

        self.center = center
        self.radius = radius

    def __str__(self):
        """Display the BallWindow in a string

        Returns:
            str: BallWindow center coordinates and radius
        """

        return "BallWindow: center={}, radius={:.2f}".format(
            np.round(self.center, 2), self.radius
        )

    def __len__(self):
        """Return the dimension of the space in which the box is

        Returns:
            int: The  dimension of the box
        """

        return len(self.center)

    def __contains__(self, point):
        """Check if a point is inside the BallWindow.

        Args:
            point (array): The coordinates of a point

        Returns:
            bool: True if the point is the point is inside the box, False otherwise
        """

        assert len(point) == len(self)  # Test if the point has the same dimension
        return la.norm(self.center - point) <= self.radius

    def dimension(self):
        """Return the dimension of the space in which the box is. See __len__

        Returns:
            int: the dimension of the box (number of sides)
        """

        return len(self)

    def volume(self):
        """Return the volume of the BoxWindow

        Returns:
            int: the volume of the box
        """

        n = self.dimension()
        R = self.radius
        return (np.pi ** (n / 2) * R ** (n)) / gamma(1 + n / 2)

    def indicator_function(self, points):
        """Return an array of int (0 or 1), saying if the points given are inside the BoxWindow

        Args:
            points (array): the coordinates of a point, or an array of point

        Returns:
            list of int: the i-th element is 1 if the i-th point given in argument is inside the box, 0 otherwise
        """

        if len(points.shape) == 1:
            return [int(points in self)]
        else:
            return [int(p in self) for p in points]
