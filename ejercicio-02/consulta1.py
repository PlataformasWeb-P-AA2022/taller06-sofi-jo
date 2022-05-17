from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

# se importa la clase(s) del
# archivo genera_tablas
from genera_base import Pais

engine = create_engine('sqlite:///basepaises.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Uso de in_

paises = session.query(Pais).filter(Pais.continente.in_(['SA', 'NA'])).order_by(Pais.nombre).all()

print(paises)

print("--------------------------------")

