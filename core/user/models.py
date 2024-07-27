from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database import Base
import uuid


class User(Base):
    __tablename__="users"
    
    
    id  =   Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    username = Column(String,unique=True,index=True)
    email = Column(String,unique=True,index=True)
    hashed_password = Column(String)
    posts = relationship("post",back_populates="author")