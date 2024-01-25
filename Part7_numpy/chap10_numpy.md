# Lambda & Numpy

## 10. Fonction lambda

Vous pouvez appliquer une fonction lambda sur chaque valeur d'un tableau.

```python
a = np.random.randint( 10, size = (10) )
# une promo - 20%
promo = lambda x : x * 0.8
print(promo(a))
"""
array([2.4, 6.4, 3.2, 3.2, 2.4, 6.4, 4.8, 0.8, 4. , 0. ])
"""
```
