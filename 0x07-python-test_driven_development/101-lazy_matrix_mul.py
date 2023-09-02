#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""creates a matrix multiplication function NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """The two matrices multiplied should be returned.

    Args:
        m_a (list of lists of ints/floats): The initial matrix.
        m_b (list of lists of ints/floats): The subsequent matrix.
    """

    return (np.matmul(m_a, m_b))
