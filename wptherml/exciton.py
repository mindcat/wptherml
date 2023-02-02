import numpy as np
from .spectrum_driver import SpectrumDriver


class ExcitonDriver(SpectrumDriver):
    """ A class for computing the dynamics and spectra of a system modelled by the Frenkel Exciton Hamiltonian

    Attributes
    ----------
    radius : float
        the radius of the sphere


    Returns
    -------
    None

    Examples
    --------
    >>> fill_in_with_actual_example!
    """

    def __init__(self, args):
        self.parse_input(args)
        print("Exciton Energy is  ", self.exciton_energy)
        # allocate the exciton Hamiltonian
        self.exciton_hamiltonian = np.zeros((self.number_of_monomers, self.number_of_monomers))


    def parse_input(self, args):
        if "exciton_energy" in args:
            self.exciton_energy = args["exciton_energy"] 
        else:
            self.exciton_energy = 0.5
        if "number_of_monomers" in args:
            self.number_of_monomers = args["number_of_monomers"]
        else:
            self.number_of_monomers = 2
        if "displacement_between_monomers" in args:
            self.displacement_between_monomers = args['displacement_between_monomers']
        else:
            self.displacement_between_monomers = np.array([1, 0, 0])

        if "transition_dipole_moment" in args:
            self.transition_dipole_moment = args["transition_dipole_moment"]
        else:
            self.transition_dipole_moment = np.array([0, 0, 1])
        if "refractive_index" in args:
                self.refractive_index = args["refractive_index"]
        else:
            self.refractive_index = 1

        self.coords = np.zeros((3, self.number_of_monomers))

        for i in range(self.number_of_monomers):
            self.coords[:,i] = self.displacement_between_monomers * i
    
    def _compute_H0_element(self, n, m):
        """ Add proper docstring! 
        
        
        """
        return self.exciton_energy * (n == m)

    def _compute_dipole_dipole_coupling(self, n, m):
        """ Method to compute the dipole-dipole potential between excitons located on site n and site m
        
        Arguments
        ---------
        n : int
            the index of site n offset by +1 relative to the python index
        m : int
            the index of site m offset by +1 relative to the python index

        Attributes
        ----------
        coords : 3 x number_of_monomers numpy array of floats
            the cartesian coordinates of each monomer

        transition_dipole_moment : 1x3 numpy array of floats
            the transition dipole moment associated with the excitons

        Returns
        -------
        V_nm : float
             the dipole-dipole potential between exciton on site n and m
        """ 
        # offset the indices for python
        _n = n - 1
        _m = m - 1

        # calculate separation vector between site m and site n
        _r_vec = self.coords[:, _m] - self.coords[:, _n]

        # self.transition_dipole_moment is the transition dipole moment!
        V_nm = (1 / (self.refractive_index ** 2 * np.sqrt(np.dot(_r_vec, _r_vec)) ** 3 )) * (np.dot(self.transition_dipole_moment, self.transition_dipole_moment) - 3 * ((np.dot(self.transition_dipole_moment, _r_vec) * np.dot(_r_vec, self.transition_dipole_moment)) / (np.sqrt(np.dot(_r_vec, _r_vec)) ** 2))) 

        return V_nm

    def build_exciton_hamiltonian(self):
        """ Method to build the Frenkel Exciton Hamiltonian
        
        Attribute
        ---------
        exciton_hamiltonian : number_of_monomers x number_of_monomers numpy array of floats
            the exciton Hamiltonian, initialized by init and to-be-filled with appropriate values 
            by this function 

        Notes
        -----
        
        """
        _N = self.number_of_monomers # <== _N is just easier to type!

        # nested loop to build Hamiltonian
        for _n in range(_N):
            for _m in range(_N):
                # <== call _compute_H0_element and store value -> H0
                # <== call _compute_dipole_dipole_coupling and store value -> V
                # <== assign H0 + V to appropriate element of self.exciton_hamiltonian
                pass

        pass
        

    def compute_spectrum(self):
        """Will prepare the Frenkel Exciton Hamiltonian and use to compute an absorption spectrum 

        Attributes
        ---------
        TBD


        Returns
        -------
        TBD

        """
        pass

    def compute_exciton_wavefunction_site_basis(self):
        """
        Will compute the single-exciton wavefunctions (approximated as Gaussians) for each site.  
        
        ***Note:***  This is probably not the best model... better model might be a Slater function, but 
        we can fix that later. Also right now the width is somewhat arbitrary.  In reality, the exciton
        has a Bohr radius that will determine the width.  We will update this later as well! 

        Arguments
        ---------
        n : int
            the site index offset from python index by +1

        Attributes
        ----------
        x : 1 x _len numpy array of floats
            the spatial grid that we will evaluate the exciton wavefunction on

        phi : _len x number_of_monomer numpy array of floats
            the single-exciton wavefunctions for each cite

        """
        # get distance between sites
        _dx = self.coords[0, 1] - self.coords[0, 0]
        
        # full-width at half-max based on distance between sites
        _fwhm = _dx / 2

        # width parameter of the Gaussian
        _c = _fwhm / 2.35482

        # normalization of Gaussian
        _a = 1 / (_c * np.sqrt(2 * np.pi))

        # create grid of x values spanning all sites in the system
        # get largest site index
        _N_max = self.number_of_monomers - 1
        # get x-value associated with largest site index 
        _x_max = self.coords[0,_N_max]
        # create the x-grid from 0 to _x_max
        _len = 500
        self.x = np.linspace(-_dx, _x_max, _len)

        self.phi = np.zeros((_len, self.number_of_monomers ))

        for n in range(self.number_of_monomers):
            _x_n = self.coords[0, n]
            self.phi[:, n] = _a * np.exp(- (self.x - _x_n) ** 2 / (2 * _c ** 2 ) )




