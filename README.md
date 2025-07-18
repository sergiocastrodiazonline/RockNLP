# RockNLP
Aplicación que predice la probabilidad de que una letra de una canción sea del género Rock &amp; Roll o bien de otro distinto.

# ¿Porque hacerla?

Porque los fundamentos de NLP son necesarios para entender una gran parte de lo que es la inteligencia artificial y como ayuda a las empresas a traducir y a tratar textos de forma más automatizada.

# ¿Que se aprendió al hacerla?

Al hacerla en clase aprendimos los fundamentos básicos de NLP (Procesamiento de Lenguaje natural) y como usando dichos fundamentos o conceptos se puede crear un ejemplo que permita utilizarlos como viene siendo esta aplicación, además aprendimos conceptos de probabilidad y de modelos de IA de Machine Learning como viene siendo el perceptrón multicapa que utiliza esta aplicación.

# ¿Como funciona?

<img width="1325" height="780" alt="image" src="https://github.com/user-attachments/assets/791eaa23-46ea-47d6-88a5-70f8e3747789" />

Cuando cargamos la aplicación en un servidor web (en este caso Flask) usará el modelo exportado a través del cuaderno de Colab mediante Pickle o Joblib, este modelo se encargará de realizar la predicción cuando le pasemos nuevas letras a través del campo de texto. Luego usando Punkt de la biblioteca NLTK para Python, permite a través de técnicas como la lematización, el stemming y otras de procesar las letras y limpiarlas para que el modelo pueda realizar la predicción, finalmente predicciendo una probabilidad para cada opción de que sea Rock o No Rock.

# Ejemplos

Blitzkrieg Pop - Ramones

<img width="982" height="307" alt="image" src="https://github.com/user-attachments/assets/71a2790d-fe3c-41c6-a803-e57b4c3f075f" />

Anothers Bites to Dust - Queen

<img width="950" height="295" alt="image" src="https://github.com/user-attachments/assets/8342e0c2-79d4-496b-86a5-2e0f1db3e4a3" />

Lazy Song - Bruno Mars

<img width="741" height="280" alt="image" src="https://github.com/user-attachments/assets/64c7c879-10a4-4a9c-b7b7-62ea133519df" />

# Posibles mejoras

- Utilizar una red neuronal en lugar de un modelo de NLP básico

- Utilizar otro tipo de técnicas de NLP (por ejemplo la detección por ritmo o por voz).

- Mejorar la calidad del dataset ya que los resultados también dependen de los datos.
