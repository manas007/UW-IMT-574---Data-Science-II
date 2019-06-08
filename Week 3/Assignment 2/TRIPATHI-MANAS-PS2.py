import numpy as np
import pandas as pd
import sklearn.preprocessing as skl
import time as t

start_time = t.time()

# 1.1 Data Input from links.txt file
data = pd.read_csv('links.txt', header = None)
data.columns = ['column','row','value']
unique_cols = np.unique(data[['row','column']])
data_ind = data.set_index(['row','column']).value.unstack(fill_value=0).reindex(columns = unique_cols, index = unique_cols , fill_value = 0 )

# 1.2 Creating the adjacency matrix
adjacency_matrix = np.array(data_ind.values,dtype=float)

#1.3 Modifying the adjacency matrix
        # 1.3.1 Set the diagonals for the adjacency matrix to zero
np.fill_diagonal(adjacency_matrix, 0)
shapeOfMatrix = adjacency_matrix.shape[0]

        #1.3.2 Normalize the columns of the adjacency matrix
adjacency_matrix = skl.normalize(adjacency_matrix, norm = 'l1', axis=0)

#1.4 identifying the dangling nodes
dangling_vector = np.array(adjacency_matrix.sum(axis = 0) == 0).astype(int)


#1.5 Calculating the influence vector
        #1.5.1 Calculate the Article Vector
article_vector = np.ones((1,shapeOfMatrix), dtype=float)
sum = article_vector.sum()
article_vector = article_vector.transpose() / sum

        #1.5.2 Calculating the Initial Start Vector
initial_start_vector = np.ones((shapeOfMatrix,1)) / shapeOfMatrix

alpha = 0.85
epsilon = 0.00001

        #1.5.3 Setting up the influence vector
influence_vector = ((alpha * adjacency_matrix).dot(initial_start_vector))+(((alpha*dangling_vector).dot(initial_start_vector)+(1-alpha))[0])*(article_vector)
previous_influence_vector = initial_start_vector
numberOfIterations = 1

        #1.5.4 Iterate to converge to the leading eigenvector 
while (np.linalg.norm(influence_vector - previous_influence_vector) > epsilon):
        previous_influence_vector = influence_vector
        nfirstpart = alpha * (adjacency_matrix.dot(influence_vector))
        nsecondpart = ((alpha * (dangling_vector.dot(influence_vector)) +  (1- alpha))[0]) * (article_vector)
        influence_vector = nfirstpart + nsecondpart
        numberOfIterations += 1

#1.6 Calculating the EigenFactor
eigenfactor = 100 * (np.dot(adjacency_matrix,influence_vector) / np.sum(np.dot(adjacency_matrix,influence_vector), axis = 0))
eigenfactorasDataFrame = pd.DataFrame({ 'EigenFactor Value' : eigenfactor [:, 0] }).sort_values(by='EigenFactor Value', ascending=False).head(20)
eigenfactorasDataFrame.index.name = 'Journal'
print('a) Answer : EigenFactor Value for top 20 journals is shown below')
print(eigenfactorasDataFrame)
print('b) Answer : Total number of iterations', numberOfIterations)
end_time = t.time()
print('c) Answer : Total time taken to run the code is' , end_time-start_time , 'seconds')

# Reported Scores: 
""" Journal : 4408, EigenFactor Value : 1.447538
Journal : 4801, EigenFactor Value : 1.412038
Journal : 6610, EigenFactor Value : 1.234606
Journal : 2056, EigenFactor Value : 0.679335
Journal : 6919, EigenFactor Value : 0.664692
Journal : 6667, EigenFactor Value : 0.634253
Journal : 4024, EigenFactor Value : 0.576867
Journal : 6523, EigenFactor Value : 0.480609
Journal : 8930, EigenFactor Value : 0.477589
Journal : 6857, EigenFactor Value : 0.439622
Journal : 5966, EigenFactor Value : 0.429627
Journal : 1995, EigenFactor Value : 0.385984
Journal : 1935, EigenFactor Value : 0.385048
Journal : 3480, EigenFactor Value : 0.379524
Journal : 4598, EigenFactor Value : 0.372625
Journal : 2880, EigenFactor Value : 0.330194
Journal : 3314, EigenFactor Value : 0.327306
Journal : 6569, EigenFactor Value : 0.319195
Journal : 5035, EigenFactor Value : 0.316591
Journal : 1212, EigenFactor Value : 0.311212 """