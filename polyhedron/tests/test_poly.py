from pytest import approx
from math import sqrt
from noshadow.polyedr import Polyedr


class TestPoly:

    def test_square(self):
        poly = Polyedr("data/square.geom")
        _, xy_sum = poly.calculate_good_edge_lengths()
        assert xy_sum == 4

    def test_square_inclined(self):
        poly = Polyedr("data/square_inclined.geom")
        _, xy_sum = poly.calculate_good_edge_lengths()
        assert xy_sum == approx(3.7320508075688776)

    def test_square_2_times_inclined(self):
        poly = Polyedr("data/square-2-times-inclined.geom")
        _, xy_sum = poly.calculate_good_edge_lengths()
        assert xy_sum == approx(3.739267310835703)

    def test_cube(self):
        poly = Polyedr("data/cube.geom")
        _, xy_sum = poly.calculate_good_edge_lengths()
        assert xy_sum == 16

    def test_ccc_out_of_range(self):
        poly = Polyedr("data/ccc.geom")
        _, xy_sum = poly.calculate_good_edge_lengths()
        assert xy_sum == 0

    def test_box_out_of_range(self):
        poly = Polyedr("data/box.geom")
        _, xy_sum = poly.calculate_good_edge_lengths()
        assert xy_sum == 0

    def test_box_out_of_range(self):
        poly = Polyedr("data/box.geom")
        _, xy_sum = poly.calculate_good_edge_lengths()
        assert xy_sum == 0
