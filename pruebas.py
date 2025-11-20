from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

wine = load_wine()
X, Y = wine.data, wine.target

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# diferentes resultados impresos

for depth in [1, 2, 3, 5, None]:
    print("\n========================")
    print("max_depth =", depth)
    print("==========================")

    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)

    rules = export_text(tree, feature_names=wine.feature_names)
    print(rules)

    print("Precisión:", tree.score(X_test, y_test))
