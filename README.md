# arbol-decision Alexia Montelongo R.

Practica de arboles de decision usando el data-set wine, que el objetivo era entrenar un modelo de arbol de decisionque esta incluido en scikit - learn


## Opinion de los resultados - resultados obtenidos

1. Cuando el max_depth=1 el arbol se vuelve mas simple y con la        precision más baja

2. A partir de max_depth=3 el arbol se comporta con reglas mas finas y la precision en notablemente mejor

3. max_depth=5 y none, generan un arbol parecido que el 3, sin ninguna mejora

Entonces el dataset, a partir de la profundidad del tres no necesita mas, pues ya se capturo todo lo relevante.

La conclusion es que el arbol si esta encontrando patrones reales en los datos, pero no necesita crecer de manera indefinida para que sea un buen modelo.

## ¿Base adecuada?
¿La base de conocimiento cumple con los requerimientos para utilizarse en un modelo de árbol de decisiones?

Considero que si por que las variables usadas son numericas, las clases ya se encuentras bien definidas y separadas. Y como se dijo en la conclusion, sin altos niveles de profundidad en el arbol se logro una alta precision.

## Caracteristicas
Las caracteristicas serian las que se usaron en el dataset
 - color_intensity
 - proline
 - alcohol
 - ash 
 - y las demas variables quimicas

## Clases
 Las clases son las que representan los tipo de vinos

 1. clase 0
 2. clase 1
 3. clase 2




