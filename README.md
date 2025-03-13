# Sobre el Proyecto de Predicción de Calidad del Aire

A continuación, se presentarán los puntos más relevantes para la investigación que involucra este proyecto: 

En primer lugar, se definió como objetivo general lo siguiente: “Desarrollar una solución interactiva para la predicción de la calidad del aire, por medio de modelos de aprendizaje automático (Machine Learning)”.

Además, se definieron los alcances (lo que contendrá el proyecto) y lo que no contendrá:

**Alcances:**
- Realizar el EDA (análisis exploratorio de datos) para comprender los datos (distribución, features, correlaciones, tendencias, etcétera).
- Hacer el respectivo preprocesamiento de los datos (imputación de outliers (datos anómalos), eliminación de features ("características") innecesarios, etcétera).
- Entrenamiento de datos con múltiples modelos de aprendizaje automático (Machine Learning).
- Evaluación de diversas métricas relevantes (RMSE, MAE, Accuracy, etcétera) para determinar el modelo más efectivo.
- Desarrollo de una solución interactiva: 1. Aplicación web simple en Streamlit (Python), 2. Aplicación móvil en Jetpack Compose (Android).


Lo que no se tendrá en cuenta:
- Políticas ambientales (específicamente, de Colombia)
- Datos en tiempo real: no se utilizarán sensores para la obtención de datos (únicamente datos históricos, contenidos en el dataset)
- Publicación en la Google Play Store: No se publicará la aplicación móvil en la Play Store.

También se realizó la definición del problema, identificando por qué es importante realizar este proyecto, los datos que se tienen a disposición para realizarlo, y los grupos de personas que se verían beneficiados con este diseño; a partir de estas preguntas, se definió esto como problema:

Es sumamente importante la predicción de la calidad del aire; esto puede afectar no solamente a las personas sensibles a la contaminación, sino también a los gobiernos que deseen plantear políticas ambientales. Sin embargo, la predicción del AQI (Air Quality Index) no es tan buena en algunos casos; esto debido a la poca disponibilidad de modelos de aprendizaje automático efectivos para hacer esto. Se busca, pues, desarrollar una solución (por medio del Machine Learning) para una mejor toma de decisiones.

Finalmente, se definieron los requerimientos de negocio/usuario, que sientan las bases para otorgar un producto de calidad y confiabilidad a los clientes; estos fueron los siguientes:

- El modelo debe tener una accuracy (exactitud), por lo menos, mayor al 70 %.
- Las predicciones deben ser fácilmente identificables por el usuario (uso de mapas, recomendaciones según la predicción de la calidad aérea, etcétera).
- Se debe predecir el AQI o clasificar la calidad del aire por categorías (bueno, moderado, malo, etcétera).

