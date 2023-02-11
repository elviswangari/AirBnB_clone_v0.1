#!/usr/bin/python3
"""defines the storage of the instances"""
import json


class FileStorage:
    """represents a file storage system

       Atributes:
       __file_path(str): contains the file in which we'll
                        save the instances
       __objects: contains the dictionary of instantiated objects

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets object with key value of id"""
        fs_cname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(fs_cname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.key()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
