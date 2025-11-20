from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

# Cargar el dataset
wine = load_wine()
X, y = wine.data, wine.target

# Dividir datos en entrenamiento y prueba (80% - 20%), test y train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear clasificador con profundidad limitada (aqui es donde se puede probar con diferentes
# max_depth=2, incluso none o dentro de pruebas.py )
tree = DecisionTreeClassifier(max_depth=2, random_state=42)
tree.fit(X_train, y_train)

# Exportar reglas
rules = export_text(tree, feature_names=wine.feature_names)
print("\nLas reglas aprendidas con max_depth=2:\n")
print(rules)

#  la prescision 
accuracy = tree.score(X_test, y_test)
print("Precisión en datos de prueba:", accuracy)
