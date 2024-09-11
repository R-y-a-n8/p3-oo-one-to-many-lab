class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {Pet.PET_TYPES}.")
        self.pet_type = pet_type

        if owner and isinstance(owner, Owner):
            self.owner = owner
            owner.add_pet(self)
        elif owner:
            raise Exception("Owner must be an instance of the Owner class.")

        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, Owner):
            self._owner = value
        else:
            raise Exception("Owner must be an instance of the Owner class.")


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
            if pet not in self._pets:
                self._pets.append(pet)
        else:
            raise Exception("Pet must be an instance of the Pet class.")

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)





