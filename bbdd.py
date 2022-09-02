from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


db_login = "admin"
db_password = "admin"
db_ip ="localhost" 
db_port= "5432"
db_name= "CrudProductos"

# engine = create_engine('postgresql://admin:admin@{}:5432/CrudProductos'.format(db_ip))

engine = create_engine(
    f"postgresql+psycopg2://{db_login}:{db_password}@{db_ip}:{db_port}/{db_name}")

Base = declarative_base()
from Models import Producto
Base.metadata.create_all(engine)