# Vectorisation

## 12. Vectorisation

Pour effectuer des opérations sur un polynôme par exemple vous devez utiliser la vectorisation Numpy qui est plus rapide.

```python

import numpy as np

a = np.arange(100)

# compréhension de liste
%timeit [x**2 + 2*x + 1 for x in a ]

# Vectorisation
%timeit a**2 + 2*a + 1

```

Notez que la vectorisation marche avec tous les opérateurs arithmétiques classiques que vous connaissez.

Numpy travaille avec des tableaux dont les données sont stockées dans des zones contigues de mémoire. De plus tous les éléments stockés ont la même dimension.
