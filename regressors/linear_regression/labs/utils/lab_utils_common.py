"""
lab_utils_common.py
Functions common to all optional labs, Course 1, Week 2.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

plt.style.use('utils/deeplearning.mplstyle')
dlblue = '#0096ff'
dlorange = '#FF9300'
dldarkred = '#C00000'
dlmagenta = '#FF40FF'
dlpurple = '#7030A0'
dlcolors = [dlblue, dlorange, dldarkred, dlmagenta, dlpurple]
dlc = {
    'dlblue': '#0096ff',
    'dlorange': '#FF9300',
    'dldarkred': '#C00000',
    'dlmagenta': '#FF40FF',
    'dlpurple': '#7030A0'
}


# Regression Routines

def compute_cost_matrix(X: np.ndarray, y: np.ndarray, w: np.ndarray, b: float, verbose: bool = False) -> float:
    """
    Compute the cost for linear regression.

    Parameters
    ----------
    X : np.ndarray
        Data, m examples with n features.
    y : np.ndarray
        Target values.
    w : np.ndarray
        Model parameters.
    b : float
        Model parameter.
    verbose : bool, optional
        If true, print out intermediate value f_wb. Default is False.

    Returns
    -------
    float
        The cost.
    """
    m = X.shape[0]

    # Calculate f_wb for all examples.
    f_wb = X @ w + b

    # Calculate cost.
    total_cost = (1/(2*m)) * np.sum((f_wb-y)**2)

    if verbose:
        print('f_wb:')
        print(f_wb)

    return total_cost


def compute_gradient_matrix(X: np.ndarray, y: np.ndarray, w: np.ndarray, b: float) -> Tuple[float, np.ndarray]:
    """
    Compute the gradient for linear regression.

    Parameters
    ----------
    X : np.ndarray
        Data, m examples with n features.
    y : np.ndarray
        Target values.
    w : np.ndarray
        Model parameters.
    b : float
        Model parameter.

    Returns
    -------
    Tuple[float, np.ndarray]
        The gradient of the cost w.r.t. the parameters w and the parameter b.
    """
    m, n = X.shape
    f_wb = X @ w + b
    e = f_wb - y
    dj_dw = (1/m) * (X.T @ e)
    dj_db = (1/m) * np.sum(e)

    return dj_db, dj_dw


def compute_cost(X: np.ndarray, y: np.ndarray, w: np.ndarray, b: float) -> float:
    """
    Compute cost.

    Parameters
    ----------
    X : np.ndarray
        Data, m examples with n features.
    y : np.ndarray
        Target values.
    w : np.ndarray
        Model parameters.
    b : float
        Model parameter.

    Returns
    -------
    float
        The cost.
    """
    m = X.shape[0]
    cost = 0.0
    for i in range(m):
        f_wb_i = np.dot(X[i], w) + b
        cost = cost + (f_wb_i - y[i])**2
    cost = cost/(2*m)
    return cost 


def compute_gradient(X: np.ndarray, y: np.ndarray, w: np.ndarray, b: float) -> Tuple[float, np.ndarray]:
    """
    Compute the gradient for linear regression.

    Parameters
    ----------
    X : np.ndarray
        Data, m examples with n features.
    y : np.ndarray
        Target values.
    w : np.ndarray
        Model parameters.
    b : float
        Model parameter.

    Returns
    -------
    Tuple[float, np.ndarray]
        The gradient of the cost w.r.t. the parameters w and the parameter b.
    """
    m, n = X.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.

    for i in range(m):
        err = (np.dot(X[i], w) + b) - y[i]
        for j in range(n):
            dj_dw[j] = dj_dw[j] + err * X[i,j]
        dj_db = dj_db + err
    dj_dw = dj_dw/m
    dj_db = dj_db/m

    return dj_db, dj_dw