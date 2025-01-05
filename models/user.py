#!/usr/bin/python3
""" class User"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import String


class User(BaseModel, Base):
    """class that represents user
    Atrributes:
        __tablename__: name for sql table
        email: user email address.
        passwd: user's password.
        f_name: user's first name
        l_name: user's lastname
        places: user-pace relationship
        reviews: user-review"""

        __tablename__ = "users"
    email = (
        Column(String(128), nullable=False)
        if os.getenv("HBNB_TYPE_STORAGE") == "db"
        else ""
    )

    password = (
        Column(String(128), nullable=False)
        if os.getenv("HBNB_TYPE_STORAGE") == "db"
        else ""
    )

    first_name = (
        Column(String(128), nullable=True)
        if os.getenv("HBNB_TYPE_STORAGE") == "db"
        else ""
    )

    last_name = (
        Column(String(128), nullable=True)
        if os.getenv("HBNB_TYPE_STORAGE") == "db"
        else ""
    )

    places = (
        relationship(
            "Place", cascade="all, delete, delete-orphan", backref="user"
        )
        if os.getenv("HBNB_TYPE_STORAGE") == "db"
        else None
    )

    reviews = (
        relationship(
            "Review", cascade="all, delete, delete-orphan", backref="user"
        )
        if os.getenv("HBNB_TYPE_STORAGE") == "db"
        else None
    )
