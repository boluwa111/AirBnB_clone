#! /bin/usr/python3

import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects (if the file exists)."""
        try:
            with open(self.__file_path, "r") as file:
                deserialized_objects = json.load(file)

            for key, value in deserialized_objects.items():
                class_name, obj_id = key.split(".")
                class_obj = models[class_name]
                obj = class_obj(**value)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
