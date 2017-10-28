import edgeDetection
from sklearn.neural_network import MLPClassifier

x = [[0,0],[1,1]]
y = [0,1]

img = edgeDetection.getImageArray('rectangle.png')

print(img)



# scale some inputs
#scaler = StandardScaler()
#scaler.fit(x_train)
#x_train = scaler.transform(x_train)
#x_test = scaler.transform(x_test)


# create an encoder
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)

clf.fit(1,img)

print(clf.predict(1))
