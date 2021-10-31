# High Density Region Estimator (HDRE)


### Hierarchical Density Factorization

```python
hdf = HierarchicalDensityFactorization(num_clusters=16,
                                                                 bins_per_dimension=61,
                                                                 smoothing_parameter=1.,
                                                                 min_leaf_samples=50,
                                                                 alpha=0.5)
```

* **number_of_clusters:** The number of clusters     
* **bins_per_dimension:** The number of histogram bins across each dimensions. This is used for estimating the kernel density function  
* **smoothing_parameter:** Increases the bandwidth of the kernel density estimation 
* **min_leaf_samples:** Prunes clusters than have less than the minimum number of samples
* **alpha:** Discount factor, 0<alpha<1

```python
hdf.optimize(X,maxiter=12,realizations=10,number_of_random_simulations=100,verbose=True)
```

* **X:** Input data -> (rows, columns)
* **maxiter:** maximum number of iterations
* **number_of_realizations:** number of runs                                    
* **number_of_random_simulations:** The number of random simulations per cycle  

```python
assignments = hdf.assign(X)
```
Returns an assignment matrix (observations, clusters) that represents whether a data point is within a hypercube cluster.

* **X:** Input data -> (rows, columns)


### Density Factorization <a name="hdr"></a>

```python
model = kernelml.region_estimator.DensityFactorization(number_of_clusters,bins_per_dimension=41,smoothing_parameter=2.0)
```                                    
                                    
* **number_of_clusters:** The number of clusters     
* **bins_per_dimension:** The number of histogram bins across each dimensions. This is used for estimating the kernel density function  
* **smoothing_parameter:** Increases the bandwidth of the kernel density estimation 

```python
model.optimize(X,y=None,agg_func='mean',
                        ,
                        number_of_random_simulations=500,
                        number_of_realizations=10,
                        )
```

This method runs the density factorization algorithm.

* **X:** Input data -> (rows, columns)
* **y:** target data -> (rows, columns)
* **agg_func:** The aggregate function for the target variable y: 'mean', 'variance', 'max', 'false-positive-cost', 'false-negative-cost', 'count'
* **number_of_realizations:** number of runs                                    
* **number_of_random_simulations:** The number of random simulations per cycle  


```python
assignments = model.get_assignments(X,pad=1.0)
```
Returns an assignment matrix (observations, clusters) that represents whether a data point is within a hypercube cluster.

* **X:** Input data -> (rows, columns)
* **pad:** This pads the variance of each density cluster.

```python
distance = model.get_distances(X,distance='chebyshev',pad=1.0)
```

Computes the distances between the data points and the hypercube centroids.

* **X:** Input data -> (rows, columns)
* **distance:** the distance metric used to assign data to clusters: 'chebyshev', 'euclidian','mae'
* **pad:** This pads the variance of each density cluster.

```python
model.prune_clusters(X,pad=pad,limit=10)
```

Prunes the clusters that have a lower number of data points than the limit. The model can be optimized after pruning.

* **X:** Input data -> (rows, columns)
* **pad:** This pads the variance of each density cluster.
* **limit:** the distance metric used to assign data to clusters: 'chebyshev', 'euclidian','mae'
