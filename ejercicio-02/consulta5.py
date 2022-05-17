from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

# se importa la clase(s) del
# archivo genera_tablas
from genera_base import Pais

engine = create_engine('sqlite:///basepaises.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


paises = session.query(Pais).filter(or_(Pais.nombre.like("%uador%"), Pais.capital.like("%ito%"))).all()
print(paises)

print("--------------------------------")
