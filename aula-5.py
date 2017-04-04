#WRITING OUR FIRST CLASSIFIER 


import random

#step 6 - medindo a distancia
from scipy.spatial import distance
def euc(a,b):
	return distance.euclidean(a,b)

#step 7 - implementando o algoritmo mais proximo
#troca da linha comentada -- random
#implementar closest file 

#step2
#implement a class
class ScrappyKNN():
	def fit(self, X_train, y_train):
		self.X_train = X_train
		self.y_train = y_train
	def predict(self, X_test):
		predictions = []
		for row in X_test: 
			label = self.closest(row)
			#label = random.choice(self.y_train)
			predictions.append(label)
		return predictions
	def closest(self, row):
		best_dist = euc(row, self.X_train[0])
		best_index = 0
		for i in range(1, len(self.X_train)):
			dist = euc(row, self.X_train[i])
			if dist < best_dist:
				best_dist = dist
				best_index = i
		return self.y_train[best_index]

#step3
#understand interface

#step4
#Intro to k-NN

#import a dataset
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

#definer classfier

#from sklearn import tree
#my_classifier = tree.DecisionTreeClassifier()
#from sklearn.neighbors import KNeighborsClassifier
my_classifier = ScrappyKNN()


#independente do classificador, a interface e similar
my_classifier.fit(X_train, y_train)

predicitions =  my_classifier.predict(X_test)
# print predicitions

from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predicitions)

