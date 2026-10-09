import unittest
import matplotlib.pyplot as plt
import sys
from pathlib import Path

test_dir = Path(__file__).resolve().parent

src_dir = test_dir.parent.parent / "src"

sys.path.insert(0, str(src_dir))

from scatter import create_plot  # noqa


class TestCreatePlot(unittest.TestCase):

    def tearDown(self):
        """Close figures after each test."""
        plt.close("all")

    def test_plot_created(self):
        fig = create_plot(
            [1, 2, 3],
            [4, 5, 6],
            "Test Plot",
            "X Axis",
            "Y Axis"
        )

        self.assertIsInstance(fig, plt.Figure)


if __name__ == '__main__':
    unittest.main()
