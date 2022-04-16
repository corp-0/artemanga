from django.db import models


class RegionChile(models.TextChoices):
    tarapaca = '1', 'región de tarapacá'
    antofagasta = '2', 'región de antofagasta'
    atacama = '3', 'región de atacama'
    coquimbo = '4', 'región de coquimbo'
    valparaiso = '5', 'región de valparaíso'
    ohiggins = '6', 'región del libertador general bernardo o’higgins'
    maule = '7', 'región del maule'
    biobio = '8', 'región del biobío'
    araucania = '9', 'región de la araucanía'
    lagos = '10', 'región de los lagos'
    ibanez = '11', 'región aysén del general carlos ibáñez del campo'
    magallanes = '12', 'región de magallanes y de la antártica chilena'
    metropolitana = '13', 'región metropolitana de santiago'
    rios = '14', 'región de los ríos'
    arica_y_parinacota = '15', 'región de arica y parinacota'
    nuble = '16', 'región de ñuble'
