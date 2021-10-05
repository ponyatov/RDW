from RDW import *
import pytest

def test_any(): assert True

def test_R_empty(): assert R == []
def test_D_empty(): assert D == []
def test_W_empty(): assert W == {}

def test_push():
    push(1); push(2); push(3)
    assert D == [1, 2, 3]
def test_pop(): assert pop() == 3
def test_top(): assert top() == 2

def test_dup(): assert dup() == [1, 2, 2]
def test_drop(): assert drop() == [1, 2]
def test_swap(): assert swap() == [2, 1]
def test_over(): assert over() == [2, 1, 2]

def test_nop(): nop(); assert D == [2, 1, 2]
def test_dot(): dot(); assert D == []

def test_init():
    init()
    assert W['nop'] == nop; assert W['halt'] == halt
    assert W['dup'] == dup; assert W['drop'] == drop
    assert W['swap'] == swap; assert W['over'] == over
    assert W['.'] == dot
