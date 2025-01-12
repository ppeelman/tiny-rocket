from sqlalchemy import Column, Integer, String, Text
from db.config import Base


class Rocket(Base):
    __tablename__ = 'rockets'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    success_rate_pct = Column(Integer)

    def __init__(self, name=None, description=None, success_rate_pct=None):
        self.name = name
        self.description = description
        self.success_rate_pct = success_rate_pct

    def __repr__(self):
        return f'<Rocket {self.name!r}>'
