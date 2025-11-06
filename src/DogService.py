from Dog import Dog
from DogRepo import DogRepo
from typing import List


class DogService:
    def __init__(self, dog_repo: DogRepo) -> None:
        self.dog_repo = dog_repo

    def add_dog(self, dog):
        self.dog_repo.insert(dog)

    def add_dogs_bulk(self, dogs: List[Dog]):
        self.dog_repo.bulk_insert(dogs)

    def find_similar_dogs(self, image_path: str):
        image_embedding = Dog.get_embedding(image_path)
        return self.dog_repo.search_by_image(image_embedding)
