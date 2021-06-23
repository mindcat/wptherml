"""
Unit tests for the Materials class
"""

# Import package, test suite, and other packages as needed
import wpspecdev
import numpy as np
import pytest
import sys

material_test = wpspecdev.Materials()

    
def test_material_sio2():
    """ tests material_sio2 method using tabulated n and k at lambda=636 nm """
    
    expected_n = 1.45693 
    expected_k = 0.00000 
  
    # create test multilayer that has 3 layers and wavelength array centered at 636 nm 
    material_test._create_test_multilayer(central_wavelength=636e-9)
    # define central layer as SiO2
    material_test.material_SiO2(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1]) 

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)


def test_material_tio2():
    """ tests material_tio2 method using tabulated n and k at lambda=664 nm """
    expected_n = 2.377021563
    expected_k = 6.79E-10

    # create test multilayer that has 3 layers and wavelength array centered at 664 nm 
    material_test._create_test_multilayer(central_wavelength=664e-9)
    # define central layer as TiO2
    material_test.material_TiO2(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)

def test_material_ta2o5():
    """ tests material_Ta2O5 method using tabulated n and k at lambda=667 nm: 
        6.6782e-07 2.1137e+00 1.0506e-03 """
    expected_n = 2.1137e+00
    expected_k = 1.0506e-03

    # create test multilayer that has 3 layers and wavelength array centered at 647 nm 
    material_test._create_test_multilayer(central_wavelength=6.6782e-07)
    # define central layer as Ta2O5
    material_test.material_Ta2O5(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)

def test_material_tin():
    """ tests material_TiN method using tabulated n and k at lambda=1106 nm 
        1.106906906906907e-06 2.175019337515494 5.175973473259225 """

    expected_n = 2.175019337515494
    expected_k = 5.175973473259225

    # create test multilayer that has 3 layers and wavelength array centered at 664 nm 
    material_test._create_test_multilayer(central_wavelength=1.106906906906907e-06)
    # define central layer as TiN
    material_test.material_TiN(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)

def test_material_Al():
    """ tests material_Al method using tabulated n and k at lambda=206.64 nm 
        2.06640E-07	1.26770E-01	2.35630E+00 """

    expected_n = 1.26770E-01
    expected_k = 2.35630E+00

    # create test multilayer that has 3 layers and wavelength array centered at 206.64 nm 
    material_test._create_test_multilayer(central_wavelength=2.06640E-07)
    # define central layer as Al

    material_test.material_Al(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])
    
    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)


def test_material_W():
    """ tests material_W method using tabulated n and k at lambda=3640.00 nm 
        3.64000E-06	1.8774806 15.8871860 """

    expected_n = 1.8774806
    expected_k = 15.8871860

    # create test multilayer that has 3 layers and wavelength array centered at 3640 nm 
    material_test._create_test_multilayer(central_wavelength=3.64000E-06)

    # define central layer as W
    material_test.material_W(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)


def test_material_AlN():
    """ tests material_AlN method using tabulated n and k at lambda=2774.69 nm 
        2.77469E-06	2.01126	0.00015 """

    expected_n = 2.01126
    expected_k = 0.00015 


    # create test multilayer that has 3 layers and wavelength array centered at 2774.69 nm 
    material_test._create_test_multilayer(central_wavelength=2.77469E-06)

    # define central layer as AlN
    material_test.material_AlN(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)


def test_material_HfO2():
    """ tests material_HfO2 method using tabulated n and k at lambda=1082.00 nm 
        1.082000E-06 1.880787E+00 0.000000E+00 """

    expected_n = 1.880586
    expected_k = 0.000000 

    # create test multilayer that has 3 layers and wavelength array centered at 1082.0 nm 
    material_test._create_test_multilayer(central_wavelength=1.082000E-06)
    
    # define central layer as HfO2
    material_test.material_HfO2(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)

def test_material_Pt():
    """ tests material_Pt method using tabulated n and k at lambda=610 nm 
        6.1096e-06 5.4685e+00 2.4477e+01 """

    expected_n = 5.4685e+00
    expected_k = 2.4477e+01 
    # create test multilayer that has 3 layers and wavelength array centered at 664 nm 
    material_test._create_test_multilayer(central_wavelength= 6.1096e-06)
    # define central layer as Pt
    material_test.material_Pt(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)

def test_material_Pb():
    """ tests material_Pb method using tabulated n and k at lambda=605nm 
       0.0000605	0.7928	0.6622		 """

    expected_n = 0.7928
    expected_k = 0.6622	
    # create test multilayer that has 3 layers and wavelength array centered at 664 nm 
    material_test._create_test_multilayer(central_wavelength= 0.0000605)
    # define central layer as Pb
    material_test.material_Pb(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)

def test_material_Re():
    """ tests material_Re method using tabulated n and k at lambda=1106 nm 
       0.00066	3.525691261	2.530539094			 """

    expected_n = 3.525691261
    expected_k = 2.530539094
    # create test multilayer that has 3 layers and wavelength array centered at 664 nm 
    material_test._create_test_multilayer(central_wavelength= 0.00066)
    # define central layer as Re
    material_test.material_Re(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)

def test_material_Rh():
    """ tests material_Rh method using tabulated n and k at lambda=564 nm 
       5.636E-07	2	5.11			 """

    expected_n = 2
    expected_k = 5.11
    # create test multilayer that has 3 layers and wavelength array centered at 664 nm 
    material_test._create_test_multilayer(central_wavelength= 5.636E-07)
    # define central layer as Rh
    material_test.material_Rh(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)

def test_material_Ru():
    """ tests material_Ru method using tabulated n and k at lambda=539 nm 
       5.391E-08	0.782	0.73		 """

    expected_n = 0.782
    expected_k = 0.73
    # create test multilayer that has 3 layers and wavelength array centered at 664 nm 
    material_test._create_test_multilayer(central_wavelength= 5.391E-08)
    # define central layer as Ru
    material_test.material_Ru(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)

def test_material_Si():
    """ tests material_Si method using tabulated n and k at lambda=85 nm 
       0.00000085	3.636	3.46E-03			 """

    expected_n = 3.636
    expected_k = 3.46E-03
    # create test multilayer that has 3 layers and wavelength array centered at 664 nm 
    material_test._create_test_multilayer(central_wavelength= 0.00000085)
    # define central layer as Si
    material_test.material_Si(1)

    result_n = np.real(material_test._refractive_index_array[1,1])
    result_k = np.imag(material_test._refractive_index_array[1,1])

    assert np.isclose(result_n, expected_n, 1e-3)
    assert np.isclose(result_k, expected_k, 1e-3)

