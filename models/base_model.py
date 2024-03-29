#!/usr/bin/python3
"""
Module for the BaseModel class.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for ky, val in kwargs.items():
                if ky == "__class__":
                    continue
                elif ky == "created_at" or ky == "updated_at":
                    setattr(self, ky, datetime.strptime(val, t_format))
                else:
                    setattr(self, ky, val)

        models.storage.new(self)

    def save(self):
        """

        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """

        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """

        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
    mdl = BaseModel()
    mdl.name = "My_First_Model"
    mdl.my_number = 89
    print(mdl.id)
    print(mdl)
    print(type(mdl.created_at))
    print("--")
    mdl_json = mdl.to_dict()
    print(mdl_json)
    print("JSON of my_model:")
    for key in mdl_json.keys():
        print("\t{}: ({}) - {}".format(ky, type(mdl_json[ky]), mdl_json[ky]))

    print("--")
    my_new_model = BaseModel(**mdl_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(mdl is my_new_model)
