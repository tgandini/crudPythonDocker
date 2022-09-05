from curses import can_change_color
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from bbdd import Base


class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    descripcion = Column(String)
    cantidad = Column(Integer)

    def __repr__(self):
        return f"Id: {self.id} || Nombre: {self.nombre} || Descripción: {self.descripcion}"

    def getCantidad(self):
        return self.cantidad

    def __init__(self, nombre, descripcion, cantidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad