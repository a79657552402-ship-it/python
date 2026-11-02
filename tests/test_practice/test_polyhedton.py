import pytest

from tests.practice.polyhedton import BasicShape, Quadrilateral, Shapes


class TestBasicShape:

    @pytest.fixture
    def data(self):
        return BasicShape([(0, 0), (4, 0), (4, 3), (0, 3)])

    def test_line(self):
        assert BasicShape._line((0, 0), (0, 1)) == 1.0

    def test_perimeter(self, data):
        assert data.perimeter == 14.0

    def test_square(self, data):
        assert data.square == 12.0

    def test_add(self, data):
        data.add((1, 0))
        assert data._points == ([(0, 0), (4, 0), (4, 3), (0, 3), (1, 0)])


class TestQuadrilateral:
    @pytest.fixture
    def data_square(self):
        return Quadrilateral([(2, 3), (7, 3), (7, 8), (2, 8)])

    @pytest.fixture
    def data_rectangle(self):
        return Quadrilateral([(2, 3), (7, 3), (7, 8), (2, 8)])

    def test_is_square(self, data_square):
        assert data_square.is_rectangle is True

    def test_is_rectangle(self, data_rectangle):
        assert data_rectangle.is_rectangle is True

    def test_add_rectangle(self, data_rectangle):
        with pytest.raises(AttributeError):
            data_rectangle.add((0,0))

    def test_add_square(self, data_square):
        with pytest.raises(AttributeError):
            data_square.add((0,0))

class TestShapes:
    @pytest.fixture
    def data(self):
        s = Shapes()
        s.add_new(BasicShape([(0, 0), (4, 0), (4, 3), (0, 3)]))  # прямоугольник, S=12, P=14
        s.add_new(Quadrilateral([(2, 3), (7, 3), (7, 8), (2, 8)]))  # квадрат 5×5, S=25, P=20
        return s

    def test_add_new(self, data):
        shape = Quadrilateral([(2, 1), (3, 3), (4, 8), (2, 2)])
        data.add_new(shape)
        assert data._shapes[-1] is shape

    def test_square(self, data):
        assert data.square == 37

    def test_perimeter(self, data):
        assert data.perimeter == 34

    def test_remove_shape(self, data):
        shape = data._shapes[0]
        data.remove_shape(shape)
        assert len(data._shapes) == 1
        assert data._shapes[0]._points == [(2, 3), (7, 3), (7, 8), (2, 8)]