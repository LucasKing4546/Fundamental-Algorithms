from My_Point import *
from Point_Repository import *
import math

def test_add_point():
    p1 = MyPoint(2., 3, 'red')
    p2 = MyPoint(3, 4, 'blue')
    p3 = MyPoint(5, 6, 'green')
    repository = PointRepository()
    repository.add(p1)
    assert repository.get_all_points() == [p1]
    repository.add(p2)
    assert repository.get_all_points() == [p1, p2]
    repository.add(p3)
    assert repository.get_all_points() == [p1, p2, p3]

def test_get_all_points():
    repository = PointRepository()
    p1 = MyPoint(2, 3, 'red')
    p2 = MyPoint(3, 4, 'blue')
    p3 = MyPoint(5, 6, 'green')
    assert repository.get_all_points() == []
    repository.add(p1)
    repository.add(p2)
    assert repository.get_all_points() == [p1, p2]
    repository.add(p3)
    assert repository.get_all_points() == [p1, p2, p3]

def test_get_point_by_index():
    repository = PointRepository()
    p1 = MyPoint(2, 3, 'red')
    p2 = MyPoint(3, 4, 'blue')
    p3 = MyPoint(5, 6, 'green')
    repository.add(p1)
    repository.add(p2)
    repository.add(p3)
    assert repository.get_point_by_index(0) == p1
    assert repository.get_point_by_index(1) == p2
    assert repository.get_point_by_index(2) == p3


def test_get_point_by_color():
    repository = PointRepository()
    p1 = MyPoint(2, 3, 'red')
    p2 = MyPoint(3, 4, 'blue')
    p3 = MyPoint(5, 6, 'green')
    repository.add(p1)
    repository.add(p2)
    repository.add(p3)
    assert repository.get_point_by_color('red') == [p1]
    assert repository.get_point_by_color('blue') == [p2]
    assert repository.get_point_by_color('green') == [p3]

def test_get_point_in_square():
    repository = PointRepository()
    p1 = MyPoint(2, 3, 'red')
    p2 = MyPoint(3, 4, 'blue')
    p3 = MyPoint(5, 6, 'green')
    repository.add(p1)
    repository.add(p2)
    repository.add(p3)
    origin = MyPoint(0, 6, 'blue')
    assert repository.get_points_in_square(origin, 6) == [p1, p2, p3]
    assert repository.get_points_in_square(origin, 4) == [p1, p2]
    assert repository.get_points_in_square(origin, 1) == []

def test_minimum_distance():
    repository = PointRepository()
    p1 = MyPoint(2, 3, 'red')
    p2 = MyPoint(3, 4, 'blue')
    p3 = MyPoint(5, 6, 'green')
    repository.add(p1)
    repository.add(p2)
    repository.add(p3)
    assert repository.minimum_distance() == math.sqrt(2)
    p4 = MyPoint(2, 2, 'blue')
    repository.add(p4)
    assert repository.minimum_distance() == 1
    p5 = MyPoint(2, 2.1, 'red')
    repository.add(p5)
    assert repository.minimum_distance() == 0.10000000000000009

def test_update():
    repository = PointRepository()
    p1 = MyPoint(2.0, 3.0, 'red')
    p2 = MyPoint(3, 4, 'blue')
    p3 = MyPoint(5, 6, 'green')
    repository.add(p1)
    repository.update(0, 1, 1, 'blue')
    assert p1.get_x() == 1 and p1.get_y() == 1 and p1.get_color() == 'blue'
    repository.add(p2)
    repository.update(1, 2, 2, 'green')
    assert p2.get_x() == 2 and p2.get_y() == 2 and p2.get_color() == 'green'
    repository.add(p3)
    repository.update(2, 3, 3.5, 'red')
    assert p3.get_x() == 3 and p3.get_y() == 3.5 and p3.get_color() == 'red'

def test_delete():
    repository = PointRepository()
    p1 = MyPoint(2, 3, 'red')
    p2 = MyPoint(3, 4, 'blue')
    p3 = MyPoint(5, 6, 'green')
    repository.add(p1)
    repository.add(p2)
    repository.add(p3)
    size = len(repository.get_all_points())
    repository.delete(0)
    assert len(repository.get_all_points()) == size - 1
    repository.delete(1)
    assert len(repository.get_all_points()) == size - 2
    repository.delete(0)
    assert len(repository.get_all_points()) == size - 3


def test_delete_square():
    repository = PointRepository()
    p1 = MyPoint(2, 3, 'red')
    p2 = MyPoint(3, 4, 'blue')
    p3 = MyPoint(5, 6, 'green')
    repository.add(p1)
    repository.add(p2)
    repository.add(p3)
    origin = MyPoint(0, 3, 'blue')
    repository.delete_square(origin, 3)
    assert repository.get_points_in_square(origin, 3) == []
    repository.delete_square(origin, 4)
    assert repository.get_points_in_square(origin, 4) == []
    repository.delete_square(origin, 6)
    assert repository.get_points_in_square(origin, 6) == []

def test_get_number_of_points_by_color():
    repository = PointRepository()
    p1 = MyPoint(2, 3, 'red')
    p2 = MyPoint(3, 4, 'blue')
    p3 = MyPoint(5, 6, 'green')
    repository.add(p1)
    repository.add(p2)
    repository.add(p3)
    assert repository.get_number_of_points_by_color('red') == 1
    assert repository.get_number_of_points_by_color('blue') == 1
    assert repository.get_number_of_points_by_color('green') == 1

def test_shift_all_points_on_y_axis():
    repository = PointRepository()
    p1 = MyPoint(2, 3, 'red')
    p2 = MyPoint(3, 4, 'blue')
    p3 = MyPoint(5, 6, 'green')
    repository.add(p1)
    repository.add(p2)
    repository.add(p3)
    repository.shift_all_points_on_y_axis()
    assert p1.get_x() == 0
    assert p2.get_x() == 0
    assert p3.get_x() == 0

def test_delete_points_within_distance():
    repository = PointRepository()
    p1 = MyPoint(2, 3, 'red')
    p2 = MyPoint(3, 4, 'blue')
    p3 = MyPoint(5, 6, 'green')
    repository.add(p1)
    repository.add(p2)
    repository.add(p3)
    repository.delete_points_within_distance(0, 0, 4)
    assert repository.get_all_points() == [p2, p3]
    repository.delete_points_within_distance(0, 0, 6)
    assert repository.get_all_points() == [p3]
    repository.delete_points_within_distance(0, 0, 8)
    assert repository.get_all_points() == []

test_delete()
test_update()
test_add_point()
test_minimum_distance()
test_get_all_points()
test_get_point_by_color()
test_get_point_in_square()
test_get_number_of_points_by_color()
test_shift_all_points_on_y_axis()
test_delete_points_within_distance()
test_get_point_by_index()
