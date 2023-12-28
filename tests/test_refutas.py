import unittest
import numpy as np
from refutaslib.refutaseq import Refutas  # Replace 'your_module_name' with the actual name of your module

class TestRefutas(unittest.TestCase):
    def test_weight_fraction(self):
        # Example values for testing
        flow = 100
        viscosity = 1.0
        refutas_instance = Refutas(flow=flow, viscosity=viscosity)

        # Calculate the weight fraction
        result = refutas_instance.weight_fraction()

        # Expected result (adjust as needed)
        expected_result = np.array([0.000239])

        # Check the result with a tolerance of 1e-6 (6 decimal places)
        np.testing.assert_allclose(result, expected_result, rtol=1e-7)

    def test_blending_index(self):
        # Test the blending_index method
        refutas_instance = Refutas(flow=100, viscosity=1.0)  # Adjust the values as needed
        result = refutas_instance.blending_index()
        expected_result = 14.534 * np.log(np.log(1.0 + 0.8)) + 10.975
        self.assertAlmostEqual(result, expected_result)

    def test_visc_mix(self):
        # Test the visc_mix method
        refutas_instance = Refutas(flow=100, viscosity=1.0)  # Adjust the values as needed
        result = refutas_instance.visc_mix()
        # You might not know the exact expected result, but you can check if the result is a valid number
        self.assertTrue(np.isfinite(result))

if __name__ == '__main__':
    unittest.main()




