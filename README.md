# SFEW_dataset

Este repositorio de GitHub hace referencia al TFM del Máster Universitario en Sistemas Inteligentes (UIB) "Reconocimiento automático de emociones en condiciones reales a partir de imágenes y audio".

En este TFM se estudian y desarrollan distintos modelos de reconocimiento automático de emociones "in the wild" basados en deep learning tanto para imágenes, como para audio y se analizará si la combinación de ambas entradas puede contribuir a una mejora de los resultados.

Este repositorio contiene las imágenes del SFEW, que es el dataset "in the wild" analizado así como los notebooks y scripts de python utilizados para reproducir los resultados de las secciones del TFM. Además se incluyen los vectores de features obtenidos de los modelos individuales utilizados para el modelo combinado.

El repositorio está formado por las carpetas data, image, audio y combination.

* data.zip: Esta carpeta contiene las imágenes del dataset SFEW
* Image: En esta carpeta se pueden encontrar los cuadernos de python y scripts de python utilizados para las pruebas de las imágenes: las pruebas hechas con el dataset FACES, la comparación, los entrenamientos y pruebas hechas con el SFEW y el script de python utilizado para calcular las predicciones de los vídeos.
* Audio: Esta carpeta contiene los cuadernos de python con las pruebas realizadas con las 2 configuraciones testeadas:
    * Configuración 1: Modelos entrenados a partir de los datos de los espectrogramas
    * Configuración 2: Modelos entrenados a partir de los espectrogramas convertidos en imágenes
* Prediction_vectors: Contiene los vectores de predicción obtenidos para los modelos del audio y del vídeo seleccionados (VGG16 y VGG16 entrenada con las imágenes de los espectrogramas)         
* Combination: Contiene el cuaderno de python con los tests y resultados de los modelos de combinación        
