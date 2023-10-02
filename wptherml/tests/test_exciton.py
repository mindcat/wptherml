"""
Unit and regression test for the wpspec package.
"""

# Import package, test suite, and other packages as needed
import wptherml
import numpy as np
import pytest
import sys


""" perform a series of tests that would apply to the simple
    case of a r = 100e-9 m spehere made of glass with ri = 1.5+0j
    in air with ri = 1.0+0j
"""
sf = wptherml.SpectrumFactory()
args = {
'exciton_energy': 1.5,
'aggregate_shape': (2,1,1),
'displacement_vector' : [10000, 0, 0],  
'transition_dipole_moment' : np.array([0, 0, 0.5]),
'refractive_index' : 1.0,
}

exciton_test = sf.spectrum_factory('Frenkel', args)

""" Define a second test instance that will
    provide a simple case to test the dynamics... simple meaning
    no coupling, so the transition_dipole_moment is set to zero
    so that the V terms are 0 and so any localized exciton state
    (i.e. c_vector = [1, 0] or c_vector = [0, 1] will be an eigenstate)
    of the exciton Hamiltonian
"""
dynamics_args = {
'exciton_energy': 1,
'aggregate_shape': (2,1,1),
'displacement_vector' : [1000000, 0, 0],  
'transition_dipole_moment' : np.array([0, 0, 0.0]),
'refractive_index' : 1.0,
}

dynamics_test = sf.spectrum_factory("Frenkel", dynamics_args)

def test_compute_H0_element():

    _H_11 = exciton_test._compute_H0_element(1, 1)
    _H_12 = exciton_test._compute_H0_element(1, 2)

    _expected_H_11 = exciton_test.exciton_energy
    _expected_H_12 = 0.

    assert np.isclose(_H_11, _expected_H_11, 1e-5)
    assert np.isclose(_H_12, _expected_H_12, 1e-5)


def test_compute_dipole_dipole_coupling():

    _V_test = exciton_test._compute_dipole_dipole_coupling(0, 1)

    _V_expected = 0

    assert np.isclose(_V_test, _V_expected)



def test_build_exciton_hamiltonian():
    # test case based on 2x2 system defined in args above
    _H_expected = np.zeros((2,2))
    _H_expected[0,0] = exciton_test.exciton_energy
    _H_expected[1,1] = exciton_test.exciton_energy
    _H_expected[0,1] = 0
    _H_expected[1,0] = 0

    # this line will build the exciton hamiltonian and
    # store it in the attribute .exciton_hamiltonian
    exciton_test.build_exciton_hamiltonian()

    assert np.allclose(_H_expected, exciton_test.exciton_hamiltonian)


def test_rk_exciton():
    ci = 0+1j

    E1 = dynamics_test.exciton_energy
    dynamics_test.build_exciton_hamiltonian()

    dt1 = 0.01

    tf = 1

    c_analytical = np.array([[np.cos(E1) - ci * np.sin(E1)], [0 + 0j]])

    for i in range(1, 101):
        dynamics_test._rk_exciton(dt1)

    assert np.allclose(c_analytical, dynamics_test.c_vector)

def test_rk_density_matrix():
    ci = 0+1j

    E1 = dynamics_test.exciton_energy
    E2 = dynamics_test.exciton_energy
    dynamics_test.build_exciton_hamiltonian()


    dt1 = 0.01

    tf = 1

    D_analytical = np.array([[np.cos(E1-E2) - ci * np.sin(E1-E2), 0 + 0j], [0 + 0j, 0 + 0j]])

    for i in range(1, 101):
        dynamics_test._rk_exciton_density_matrix(dt1)

    assert np.allclose(D_analytical, dynamics_test.density_matrix)


