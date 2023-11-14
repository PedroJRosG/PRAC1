# PRAC1
 TIPOLOGIA_DATOS

ALUMNO: Pedro José Ros Gómez
URL WEB : https://www.enalquiler.com/search?provincia=16
Repositorio: https://github.com/PedroJRosG/PRAC1.git
Datos de salida: https://zenodo.org/uploads/10127244
DOI: md5:8c1a5976fa371add9310f72aa94cae1e 

Extrae la informacion de los inmuebles que se encuentran en arquiler en la provincia de Ciudad Real.

Para ejecutar el script es necesario instalar la siguientes bibliotecas:

pip install pandas
pip install requests
pip install lxml
pip install beautifulsoup4
pip install csv
pip install pandas
pip install json
pip install webdriver

El script se debe ejecutar de la siguiente manera:

python webTrapping_enalquiler.py

Los registros se almacenan en un archivo de tipo CSV (salida.cvs)
Para la realizacion de la extracion de los datos  se ha utilizado Selenium.
Se trata de una pagina dinamica y por tanto de dificil extraccion.
Se ha tenido que introducir en el codigo parametros de cabecera de la peticion
para eviatar la deteccion y el baneo

Se ha realizado una extraccion tanto lineal como vertical con paginacion.
