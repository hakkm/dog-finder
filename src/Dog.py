from sentence_transformers import SentenceTransformer
from PIL import Image

class Dog:
    model = SentenceTransformer('clip-ViT-B-32')

    def __init__(self, dog_id, image_path, breed, owner_name):
        self.dog_id = dog_id
        self.image_path = image_path
        self.breed = breed
        self.image_embedding = None
        self.owner_name = owner_name

    @staticmethod
    def get_embedding(image_path: str):
        tmp_image = Image.open(image_path)
        return Dog.model.encode(tmp_image)

    def generate_embedding(self):
        self.image_embedding = Dog.get_embedding(self.image_path)

    def to_dict(self):
        return {
            'dog_id': self.dog_id,
            'image_path': self.image_path,
            'breed': self.breed,
            'image_embedding': self.image_embedding,
            'owner_name': self.owner_name
        }
