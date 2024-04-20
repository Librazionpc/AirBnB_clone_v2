#!/usr/bin/python3
"""Scripts that deals with the database storage"""
import os
from models.base_model import Base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """The clsss for database storage"""
    
    __engine = None
    __session = None
    
    def __init__(self):
        """Initializes the DBStorage object"""
        MySQL_user = os.environ.get("HBNB_MYSQL_USER")
        MySQL_password = os.environ.get("HBNB_MYSQL_PWD")
        MySQL_host = os.environ.get("HBNB_MYSQL_HOST","localhost")
        MySQL_database = os.environ.get("HBNB_MYSQL_DB")
        
        connection_url = f"mysql+mysqldb://{MySQL_user}:{MySQL_password}@{MySQL_host}/{MySQL_database}"
        
        if os.environ.get("HBNB_ENV") == "test":
                self.drop_all_tables()

        self.__engine = create_engine(connection_url, pool_pre_ping=True)
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
            
            
    def all(self, cls=None):
        """Query object from the database session"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        objects = {}
        classes = {'User': User, 'State': State, 'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}
        if cls == None:
            for class_name, class_obj in classes.items():
                for obj in self.__session.query(class_obj).all():                  
                    objects[f"{class_name}.{obj.id}"] = obj
        elif cls.__name__ in classes:
            class_obj = classes[cls.__name__]
            for obj in self.__session.query(class_obj).all():
                objects[f"{cls.__name__}.{obj.id}"] = obj
        else:
            raise ValueError("Invalid class name provided.")
        return objects
    
    def new(self, obj):
        """Add the object to the database session"""
        
        self.__session.add(obj)
    
    def save(self):
        """Commit all changes to the database session"""
        self.__session.commit()
        
        
    def delete(self, obj=None):
        """Deletes obj from the current database"""
        
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables fomr databse"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        
    def drop_all_tables(self):
        """Function that drops all tables from the database"""
        metadata = MetaData()
        metadata.reflect(bind=self.__engine)
        metadata.drop_all(self.__engine)
    
    def close(self):
        self.__session.remove()