class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_in_list in people:
        Person(person_in_list["name"], person_in_list["age"])

    for person_in_list in people:
        person = Person.people[person_in_list["name"]]
        if "wife" in person_in_list and person_in_list["wife"]:
            person.wife = Person.people[person_in_list["wife"]]
        if "husband" in person_in_list and person_in_list["husband"]:
            person.husband = Person.people[person_in_list["husband"]]

    return [Person.people[data["name"]] for data in people]
