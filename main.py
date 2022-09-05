from bbdd import engine
from Models.Producto import Producto
from sqlalchemy.orm import Session

def crearProducto(nombre,descripcion,cantidad):
    try:
        if cantidad <1:
            raise ValueError('La cantidad debe ser mayor a 0')
        
        producto= Producto(nombre,descripcion,cantidad)
        with Session(engine) as session:
            session.add(producto)
            session.commit()
            session.refresh(producto)
            return producto
    except Exception as e:
        print("Ha ocurrido un error: "+str(e))

def findProductoByName(nombreProducto):
    try:
        with Session(engine) as session:
            lista= session.query(Producto).filter(Producto.nombre.contains (nombreProducto)).all()
            for producto in lista:
                print (producto)
    except Exception as e:
        print("Ha ocurrido un error: "+str(e))    