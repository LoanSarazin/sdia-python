from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """[summary]"""

    def __init__(self, boundsArg):
        """Initialize the BoxWindow from the bounds given in the array

        Args:
            boundsArg (array): array of bounds containing the coordinates of each bound
        """

        self.bounds = np.array(boundsArg)

    def __str__(self):
        """Display the BoxWindow in a string

        Returns:
            string: BoxWindows points coordinates
        """

        description = "BoxWindow: "
        for i in range(len(self.bounds)):
            description = description + str(list(self.bounds[i])) + " x "
        return description[:-3]

    def __len__(self):
        """Return the dimension of the space in which the box is

        Returns:
            int: the dimension of the box (number of sides)
        """

        return self.bounds.shape[0]

    def __contains__(self, point):
        """Check if a point is inside the BoxWindow.

        Args:
            point (array): The coordinates of a point

        Returns:
            bool: True if the point is the point is inside the box, False otherwise
        """

        # assert len(point) == len(self)  ##Test if the point has the same dimension
        a = self.bounds[:, 0]
        b = self.bounds[:, 1]
        return np.all(np.logical_and(a <= point, point <= b))

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

        a = self.bounds[:, 0]
        b = self.bounds[:, 1]
        return np.prod(abs(b - a))

    def indicator_function(self, points):
        """Return an array of int (0 or 1), saying if the points given are inside the BoxWindow

        Args:
            points (array): the coordinates of a point, or an array of point

        Returns:
            list of int: the i-th element is 1 if the i-th point given in argument is inside the box, 0 otherwise
        """

        if points.size <= 2:
            return [int(points in self)]
        else:
            return [int(p in self) for p in points]

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """

        rng = get_random_number_generator(rng)
        return


class UnitBoxWindow(BoxWindow):
    def __init__(self, center=0, dimension=2):
        """Create a BoxWindow centered, for a dimension given.

        The box is cented by default in 0, and is created in 2 dimensions.

        Args:
            center (int, optional): The center of the box. Defaults to 0.
            dimension (int, optional): The dimension of the box. Defaults to 2.

        Returns:

        """
        bounds = np.zeros((dimension, 2))
        bounds[:, 0], bounds[:, 1] = center - 0.5, center + 0.5
        # super(BoxWindow, self).__init__(bounds)
