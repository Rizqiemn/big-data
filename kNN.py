from sklearn.datasets import load_iris
iris_ku = load_iris()
x = iris_ku.data
y = iris_ku.target

feature_names = iris_ku.feature_names
target_names = iris_ku.target_names

print("feature names: ",feature_names)
print("Target names: ",target_names)

print("\nType of x is: ",type(x))

print("\nFirst 5 rows of x: ",x[:5])

x=iris_ku.data
y=iris_ku.target

from sklearn.model_selection import train_test_split
x_latih, x_tes, y_latih, y_tes = train_test_split(x, y, test_size = 0.4, random_state=1)

print(x_latih.shape)
print(x_tes.shape)

print(y_latih.shape)
print(y_tes.shape)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_latih,y_latih)

y_prediksi = knn.predict(x_tes)

from sklearn import metrics
print("Akurasi model kNN : ",metrics.accuracy_score(y_tes,y_prediksi))

contoh = [[3,5,4,2],[2,3,5,4]]
preds = knn.predict(contoh)
pred_species=[iris_ku.target_names[p] for p in preds]
print("Prediksi : ",pred_species)

from sklearn.externals import joblib
joblib.dump(knn,'iris_knn.pkl')