from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'lospaises'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    capital = Column(String(200))
    continente = Column(String(10))
    dial = Column(String(50))
    geoname = Column(Integer)
    ITU = Column(String(200))
    lenguajes = Column(String(200))
    independiente = Column(String(60))

    def __repr__(self):
        return "Pais: nombre=%s capital=%s continente=%s dial=%s geoname=%s ITU=%s lenguajes=%s independiente=%s" % (
                          self.nombre,
                          self.capital,
                          self.continente,
                          self.dial,
                          self.geoname,
                          self.ITU,
                          self.lenguajes,
                          self.independiente)


Base.metadata.create_all(engine)

