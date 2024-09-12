# models/aves_model.py
from bson.objectid import ObjectId
from .database import get_database

db = get_database()
aves_collection = db["aves"]

class Ave:
    def __init__(self, identificador, peso, edad, temperatura_corporal, datos_cualitativos, imagen, fecha_registro, apto_para_produccion, id=None):
        self.id = id if id else ObjectId()
        self.identificador = identificador
        self.peso = peso
        self.edad = edad
        self.temperatura_corporal = temperatura_corporal
        self.datos_cualitativos = datos_cualitativos
        self.imagen = imagen
        self.fecha_registro = fecha_registro
        self.apto_para_produccion = apto_para_produccion

    def to_dict(self):
        return {
            "_id": self.id,
            "identificador": self.identificador,
            "peso": self.peso,
            "edad": self.edad,
            "temperatura_corporal": self.temperatura_corporal,
            "datos_cualitativos": self.datos_cualitativos,
            "imagen": self.imagen,
            "fecha_registro": self.fecha_registro,
            "apto_para_produccion": self.apto_para_produccion
        }

    @staticmethod
    def from_dict(data):
        return Ave(
            identificador=data["identificador"],
            peso=data["peso"],
            edad=data["edad"],
            temperatura_corporal=data["temperatura_corporal"],
            datos_cualitativos=data["datos_cualitativos"],
            imagen=data["imagen"],
            fecha_registro=data["fecha_registro"],
            apto_para_produccion=data["apto_para_produccion"],
            id=data["_id"]
        )
