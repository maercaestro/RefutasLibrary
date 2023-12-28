import numpy as np


class Refutas:
    """
    Refutas class is an object that apply Refutas Equation to determine the viscosity of a mixture.
    This is important especially in determining the blending viscosity of base oil for lubricant formulation.
    In this python object, we are able to calculate the weight fraction, blending index and finally the 
    viscosity mixture.
    
    flow unit is  m3/hr
    viscosity unit is centistoke(cst)
    """
    
    def __init__(self, flow, viscosity):
        self.flow = flow
        self.viscosity = viscosity

    def weight_fraction(self):
        """Calculate weight fraction based on flow. Flow must be given in m3/hr"""
        flow_values = np.atleast_1d(self.flow)  # Convert to 1D array
        weight = (flow_values * 0.861) / 3600

        if len(flow_values) == 1:  # Single value case
            total_mass = weight
        else:
            total_mass = np.sum(weight)

        weight_fraction = weight / total_mass
        return weight_fraction

    def blending_index(self):
        """Calculate blending index based on viscosity in centistoke."""
        return 14.534 * np.log(np.log(self.viscosity + 0.8)) + 10.975

    def visc_mix(self):
        """Calculate mixkv directly."""
        weight_fraction = self.weight_fraction()
        blending_idx = self.blending_index()
        avg_index = np.sum(blending_idx * weight_fraction)
        mixkv = np.exp(np.exp((avg_index - 10.975) / 14.534)) - 0.8
        return mixkv