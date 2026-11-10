import pytest
from scripts.vectors import Vector


def test_equals():
    v1 = Vector("test", 1 , 2 ,3)
    v2 = Vector("test", 4, 5, 6)
    v3 = Vector("test" , 4 , 5 , 6)
    v4 = Vector("" , 4 , 5 , 6)
    test_object = (1,2)

    bool1 = (v1 == v2)
    bool2 = (v2 == v3)
    bool3 = (v2 == v4)
    bool4 = (v1 == test_object)

    assert bool1 == False
    assert bool2 == True
    assert bool3 == False
    assert bool4 == False

def test_neg():
    v1 = Vector("test", 1 , 2 ,3)
    neg_v1 = Vector("test", -1 , -2 , -3)

    assert neg_v1 == -v1

def test_vec_addition():
    v1 = Vector("test", 1 , 2 ,3)
    v2 = Vector("test", 4, 5, 6)
    v3 = Vector("" , 4 , 5 , 6)

    test_add = v1 + v2
    test_logic = v1 + v3

    assert test_add.vector[0,0] == 5
    assert test_add.vector[0,1] == 7
    assert test_add.vector[0,2] == 9

    assert test_logic == None

def test_vec_subtraction():

    v1 = Vector("test", 1 , 2 ,3)
    v2 = Vector("test", 4, 5, 6)
    v3 = Vector("" , 4 , 5 , 6)

    test_add = v1 - v2
    test_logic = v1 - v3

    assert test_add.vector[0,0] == -3
    assert test_add.vector[0,1] == -3
    assert test_add.vector[0,2] == -3

    assert test_logic == None

def test_vec_cross():
    i = Vector("test", 1,0,0)
    j = Vector("test", 0,1,0)
    k = Vector("test", 0,0,1)

    test1 = i * j
    test2 = j * k
    test3 = i * k

    assert test1 == k
    assert test2 == i
    assert test3 == -j

def test_dot():
    v1 = Vector("test", 1 , 2 ,3)
    v2 = Vector("test", 4, 5, 6)

    dot = v1.dot(v2)

    assert dot == 32