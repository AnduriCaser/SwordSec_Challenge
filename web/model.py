from sqlalchemy import Column, Integer, String
from db import Base


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(300))
    last_name = Column(String(300))
    email = Column(String(300))
    gender = Column(String(300))
    ip_address = Column(String(300))
    user_name = Column(String(300))
    agent = Column(String(300))
    country = Column(String(300))

    def __init__(self, first_name=None, last_name=None, email=None, gender=None, ip_address=None, user_name=None, agent=None, country=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.ip_address = ip_address
        self.user_name = user_name
        self.agent = agent
        self.country = country

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
