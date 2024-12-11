from repo import VectorRepository
from My_Vector import MyVector

def test_add_vector():
    repository = VectorRepository()
    v1 = MyVector('v1', 'b', 1, [1, 2, 3])
    v2 = MyVector('v2', 'r', 2, [4, 5, 6])
    v3 = MyVector('v3', 'y', 3, [1, -2, 3])
    repository.add_vector(v1)
    assert v1 in repository.get_vectors()
    repository.add_vector(v2)
    assert v2 in repository.get_vectors()
    repository.add_vector(v3)
    assert v3 in repository.get_vectors()

def test_get_vectors():
    repository = VectorRepository()
    v1 = MyVector('v1', 'b', 1, [1, 2, 3])
    v2 = MyVector('v2', 'r', 2, [4, 5, 6])
    v3 = MyVector('v3', 'y', 3, [1, -2, 3])
    repository.add_vector(v1)
    assert repository.get_vectors() == [v1]
    repository.add_vector(v2)
    assert repository.get_vectors() == [v1, v2]
    repository.add_vector(v3)
    assert repository.get_vectors() == [v1, v2, v3]

def test_get_vector_by_index():
    repository = VectorRepository()
    v1 = MyVector('v1', 'b', 1, [1, 2, 3])
    v2 = MyVector('v2', 'r', 2, [4, 5, 6])
    v3 = MyVector('v3', 'y', 3, [1, -2, 3])
    repository.add_vector(v1)
    repository.add_vector(v2)
    repository.add_vector(v3)
    assert repository.get_vector_by_index(0) == v1
    assert repository.get_vector_by_index(1) == v2
    assert repository.get_vector_by_index(2) == v3

def test_update_vector_by_index():
    repository = VectorRepository()
    v1 = MyVector('v1', 'b', 1, [1, 2, 3])
    v2 = MyVector('v2', 'r', 2, [4, 5, 6])
    v3 = MyVector('v3', 'y', 3, [1, -2, 3])
    repository.add_vector(v1)
    repository.add_vector(v2)
    repository.add_vector(v3)
    repository.update_by_index(0, 'v10', 'm', 2, [-1, -2, -3])
    assert repository.get_vector_by_index(0) == MyVector('v10', 'm', 2, [-1, -2, -3])
    repository.update_by_index(1, '1341', 'b', 1, [-1, -1, -4])
    assert repository.get_vector_by_index(1) == MyVector('1341', 'b', 1, [-1, -1, -4])
    repository.update_by_index(2, 'fafa', 'y', 0, [5, -1, -11])
    assert repository.get_vector_by_index(2) == MyVector('fafa', 'y', 0, [5, -1, -11])

def test_update_vector_by_name():
    repository = VectorRepository()
    v1 = MyVector('v1', 'b', 1, [1, 2, 3])
    v2 = MyVector('v2', 'r', 2, [4, 5, 6])
    v3 = MyVector('v3', 'y', 3, [1, -2, 3])
    repository.add_vector(v1)
    repository.add_vector(v2)
    repository.add_vector(v3)
    repository.update_by_name('v1', 'm', 2, [-1, -2, -3])
    assert repository.get_vector_by_index(0) == MyVector('v1', 'm', 2, [-1, -2, -3])
    repository.update_by_name('v2',  'b', 1, [-1, -1, -4])
    assert repository.get_vector_by_index(1) == MyVector('v2', 'b', 1, [-1, -1, -4])
    repository.update_by_name('v3', 'r', 2, [5, -2, 11])
    assert repository.get_vector_by_index(2) == MyVector('v3', 'r', 2, [5, -2, 11])

def test_delete_vector_by_index():
    repository = VectorRepository()
    v1 = MyVector('v1', 'b', 1, [1, 2, 3])
    v2 = MyVector('v2', 'r', 2, [4, 5, 6])
    v3 = MyVector('v3', 'y', 3, [1, -2, 3])
    repository.add_vector(v1)
    repository.add_vector(v2)
    repository.add_vector(v3)
    repository.delete_by_index(0)
    assert v1 not in repository.get_vectors()
    repository.delete_by_index(0)
    assert v2 not in repository.get_vectors()
    repository.delete_by_index(0)
    assert v3 not in repository.get_vectors()

def test_delete_vector_by_name():
    repository = VectorRepository()
    v1 = MyVector('v1', 'b', 1, [1, 2, 3])
    v2 = MyVector('v2', 'r', 2, [4, 5, 6])
    v3 = MyVector('v3', 'y', 3, [1, -2, 3])
    repository.add_vector(v1)
    repository.add_vector(v2)
    repository.add_vector(v3)
    repository.delete_by_name('v1')
    assert v1 not in repository.get_vectors()
    repository.delete_by_name('v2')
    assert v2 not in repository.get_vectors()
    repository.delete_by_name('v3')
    assert v3 not in repository.get_vectors()

def test_max_sum_greater_than_value():
    repository = VectorRepository()
    v1 = MyVector('v1', 'b', 1, [1, 2, 3])
    v2 = MyVector('v2', 'r', 2, [4, 5, 6])
    v3 = MyVector('v3', 'y', 3, [1, -2, 3])
    repository.add_vector(v1)
    repository.add_vector(v2)
    repository.add_vector(v3)
    assert repository.max_sum_greater_than_value(3) == 15
    assert repository.max_sum_greater_than_value(0) == 15
    assert repository.max_sum_greater_than_value(15) is None

def test_delete_product_greater_than_value():
    repository = VectorRepository()
    v1 = MyVector('v1', 'b', 1, [1, 2, 3])
    v2 = MyVector('v2', 'r', 2, [4, 5, 6])
    v3 = MyVector('v3', 'y', 3, [1, -2, 3])
    repository.add_vector(v1)
    repository.add_vector(v2)
    repository.add_vector(v3)
    repository.delete_product_greater_than_value(6)
    assert v2 not in repository.get_vectors() and v1 in repository.get_vectors()
    repository.delete_product_greater_than_value(5)
    assert v1 not in repository.get_vectors() and v3 in repository.get_vectors()
    repository.delete_product_greater_than_value(-7)
    assert v3 not in repository.get_vectors()

def test_update_by_type():
    repository = VectorRepository()
    v1 = MyVector('v1', 'b', 1, [1, 2, 3])
    v2 = MyVector('v2', 'r', 2, [4, 5, 6])
    v3 = MyVector('v3', 'y', 3, [1, -2, 3])
    repository.add_vector(v1)
    repository.add_vector(v2)
    repository.add_vector(v3)
    repository.update_by_type(1, 'm')
    assert repository.get_vector_by_index(0).get_colour() == 'm'
    repository.update_by_type(2, 'm')
    assert repository.get_vector_by_index(1).get_colour() == 'm'
    repository.update_by_type(3, 'm')
    assert repository.get_vector_by_index(2).get_colour() == 'm'
'''
def test_plot_vectors():
    repository = VectorRepository()
    v1 = MyVector('v1', 'b', 1, [1, 2, 3])
    v2 = MyVector('v2', 'r', 2, [4, 5, 6])
    v3 = MyVector('v3', 'y', 3, [1, -2, 3])
    repository.add_vector(v1)
    repository.add_vector(v2)
    repository.add_vector(v3)
    repository.plot_vectors()

    
#test_plot_vectors()
'''

test_update_by_type()

test_delete_product_greater_than_value()

test_max_sum_greater_than_value()

test_add_vector()
test_get_vectors()
test_get_vector_by_index()
test_update_vector_by_index()
test_update_vector_by_name()
test_delete_vector_by_index()
test_delete_vector_by_name()

