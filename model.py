import json
class Person(object):
    """
    Class used to represent an Person
    """
    def __init__(self, id_person: int, name: str = 'Name', last_name: str = "LastName"):
        """ Person constructor object.
        :param id_person: id of person.
        :type id_person: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :returns: Person object
        :rtype: object
        """
        self._id_person = id_person
        self._name = name
        self._last_name = last_name

    @property
    def id_person(self) -> int:
        """ Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._id_person

    @id_person.setter
    def id_person(self, id_person: int):
        """ The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._id_person = id_person

    @property
    def name(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._name = name

    @property
    def last_name(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the person.
        :param last_name: last name of person.
        :type: str
        """
        self._last_name = last_name

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2})'.format(self.id_person, self.name, self.last_name)
    @classmethod
    def get_all(cls):
            result = list()
            with open('users.json') as json_file:
                data = json.load(json_file)
                for p in data:
                    person = Person(p['id_person'],p['name'], p['last_name'])
                    result.append(person)
            return result
    @classmethod
    def save_person(cls,Person):
        person = {
                "id_person":Person.id_person,
                "name": Person.name,
                "last_name": Person.last_name
            }
        with open("users.json") as archivo:
            datos = json.load(archivo)
            datos.append(person)
        with open('users.json', 'w') as f:
            json.dump(datos, f, indent=4)

    @classmethod
    def delete_person(cls,id_person):
        with open("users.json") as archivo:
            datos = json.load(archivo)
            for person in datos:
                if(person['id_person'] == id_person):
                    datos.remove(person)
        with open('users.json', 'w') as f:
            json.dump(datos, f, indent=4)
    @classmethod
    def edit_person(cls,id_person,new_name,new_last_name):
        with open("users.json") as archivo:
            datos = json.load(archivo)
            for person in datos:
                if(person['id_person'] == id_person):
                    person['name'] = new_name
                    person['last_name'] = new_last_name
        with open('users.json', 'w') as f:
            json.dump(datos, f, indent=4)

    @classmethod
    def find_person(cls,id_person):
        person_found = []
        with open("users.json") as archivo:
            datos = json.load(archivo)
            for person in datos:
                if(person['id_person'] == id_person):
                    person_found = person
        return person_found


#if __name__ == '__main__':
    #edwin = Person(id_person=73577376, name="Edwin", last_name="Puertas")
    #save_person(edwin)
    #edit_person(73577376,'ivan','editado')
    


    