# Refutas Equation Library
A small library for calculating viscosity of a mixture. This is applicable for oil and gas industry utilizing
Refutas Equation.

### Installation
```
pip install RefutasLibrary
```

### Get started
This library is better use to handle a dataframe containing an array of flow and viscosity.
With this information provided, it can calculate the weight fraction and viscosity of the final mixture.
The weight fraction used the assumption of density of 0.861.

The flow is using the unit of m3/hr
The viscosity is using the unit of centistoke (cst)

```Python
from refutaslib.refutaseq import Refutas

# calling the object
mix = Refutas(flow,viscosity)

# use the object to calculate weight fraction and viscosity of mixture
weight_fractions = mix.weight_fraction()
visc_mix = mix.visc_mix()
```