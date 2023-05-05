#!/usr/bin/python3


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


class DBStorage:
    """ database storage engine
    Attributes:
        __engine: sqlalchemy engine
        __session: sqlalchemy session
    """

    __engine = None
    __session = None
    hbnb_user = os.getenv('HBNB_MYSQL_USER')
    hbnb_pwd = os.getenv('HBNB_MYSQL_PWD')
    hbnb_host = os.getenv('HBNB_MYSQL_HOST')
    hbnb_db = os.getenv('HBNB_MYSQL_DB')
    hbnb_env = os.getenv('HBNB_ENV')

    def __init__(self):
        """ creates the engine, fetches variables from env 
        db_flavor(mysql, postgress)+db_connector://user:password@host/db_nameselfself__engineself__engineself__engineself__engine
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(self.hbnb_user, self.hbnb_pwd, self.hbnb_host, self.hbnb_db), pool_pre_ping=True)

        try:
            if self.hbnb_env == "test":
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

    def all(self, cls=None):
        """query on the current database session (self.__session) all objects

        Return:
            Dict queried like filestorage
        """

        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        return {"{}.{}".format(type(obj).__name__, obj.id):\
                obj for obj in objs}

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session1 """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session  = Session()

    def close(self):
        """ Closes the session"""
        if self.__session:
            self.__session.close()
