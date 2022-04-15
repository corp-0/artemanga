from enum import StrEnum


class CiudadChile(StrEnum):
    PUENTE_ALTO = 'Puente Alto'
    MAIPU = 'Maipú'
    SANTIAGO = 'Santiago'
    FLORIDA = 'La Florida'
    TEMUCO = 'Temuco'
    ANTOFAGASTA = 'Antofagasta'
    VINA_DEL_MAR = 'Vina del Mar'
    SAN_BERNARDO = 'San Bernardo'
    VALPARAISO = 'Valparaíso'
    CONDES = 'Las Condes'
    PENALOLEN = 'Peñalolén'
    RANCAGUA = 'Rancagua'
    ARICA = 'Arica'
    CONCEPCION = 'Concepción'
    QUILICURA = 'Quilicura'
    NUNOA = 'ÑUÑOA'
    TALCA = 'Talca'
    PUDAHUEL = 'Pudahuel'
    SERENA = 'La Serena'
    IQUIQUE = 'Iquique'
    PINTANA = 'La Pintana'
    PUERTO_MONTT = 'Puerto Montt'
    CHILLAN = 'Chillán'
    BOSQUE = 'El Bosque'
    CALAMA = 'Calama'
    RECOLETA = 'Recoleta'
    COPIAPO = 'Copiapó'
    VALDIVIA = 'Valdivia'
    QUILPUE = 'Quilpué'
    TALCAHUANO = 'Talcahuano'
    OSORNO = 'Osorno'
    RENCA= 'Renca'
    ANGELES = 'Los Ángeles'
    PROVIDENCIA = 'Providencia'
    ESTACION_CENTRAL = 'Estación Central'
    CERRO_NAVIA = 'Cerro Navia'
    PAZ = 'San Pedro de la Paz'


CIUDAD_CHILE_CHOICE = [[CiudadDes.upper()] for CiudadDes in CiudadChile]
