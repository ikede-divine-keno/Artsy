#!/usr/bin/python3
""" holds class User"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5

DEFAULT_LENGTH = 128

class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    email = Column(String(DEFAULT_LENGTH), nullable=False)
    password = Column(String(DEFAULT_LENGTH), nullable=False)
    first_name = Column(String(DEFAULT_LENGTH), nullable=False)
    last_name = Column(String(DEFAULT_LENGTH), nullable=True)
    occupation = Column(String(DEFAULT_LENGTH), nullable=True)
    posts = relationship("Post", backref="user")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
