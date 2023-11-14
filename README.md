# PRAC1
 TIPOLOGIA_DATOS

Extrae la información de los inmuebles que se encuentran en alquiler en la provincia de Ciudad Real.

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
Para la realización de la extracción de los datos  se ha utilizado Selenium.
Se trata de una pagina dinámica y por tanto de difícil extraccion.
Se ha tenido que introducir por  el código parámetros en la  cabecera de la peticion
para evitar la detección y el baneo

Se ha realizado una extracción de la información  tanto horizontal como vertical de todos los inmuebles y teniendo en cuenta la  paginación.
Posteriormente se realizara una limpieza y reenombrado de las columnas, ya que la extraccion de los datos no me lo permitia.Toda la informacion obtenida es la deseada para el analisis posterior de los inmuebles.
