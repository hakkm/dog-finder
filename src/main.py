from PIL import Image
import json
from pathlib import Path
from DogRepo import DogRepo
from DogService import DogService
from Dog import Dog
from Util import Util

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # parent of src
# show the lost dog image
def show_dog(image_path: str):
    img = Image.open(image_path)
    img.show()

def get_dogs_data():
    data = '''
    {
      "dogs": [
        {"dog_id": "Bella", "image_path": "", "breed": "German Shepherd", "owner_name": "Tokyo Blue"},
        {"dog_id": "Buddy", "image_path": "", "breed": "Labrador Retriever", "owner_name": "Berlin Red"},
        {"dog_id": "Bigu", "image_path": "", "breed": "Beagle", "owner_name": "Lisbon Yellow"},
        {"dog_id": "Charlie", "image_path": "", "breed": "Golden Retriever", "owner_name": "Paris Green"},
        {"dog_id": "Luigi", "image_path": "", "breed": "Jack Russel/Rat Terrier", "owner_name": "Ully"},
        {"dog_id": "Luna", "image_path": "", "breed": "Poodle", "owner_name": "Wellington Brown"},
        {"dog_id": "Max", "image_path": "", "breed": "Bulldog", "owner_name": "Canberra Purple"},
        {"dog_id": "Milo", "image_path": "", "breed": "Rottweiler", "owner_name": "Hanoi Orange"},
        {"dog_id": "Oscar", "image_path": "", "breed": "Dachshund", "owner_name": "Kabul Black"},
        {"dog_id": "Ruby", "image_path": "", "breed": "Boxer", "owner_name": "Ottawa Pink"},
        {"dog_id": "Zoe", "image_path": "", "breed": "Siberian Husky", "owner_name": "Cairo White"}
      ]
    }
    '''

    dogs_data = json.loads(data)
    return dogs_data

def register_all_dogs(srv):

    dogs_data = get_dogs_data()

    image_dogs = PROJECT_ROOT / "data" / "dogs"
    for dog_info in dogs_data["dogs"]:
        filename = f"{dog_info['dog_id']}.png"
        full_path = image_dogs / filename
        dog = Dog(dog_info["dog_id"], str(full_path) , dog_info["breed"], dog_info["owner_name"])
        srv.add_dog(dog)

    return dogs_data

def view_all_dogs():
# visualize new dogs
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import math

    dogs_data = get_dogs_data()

    num_dogs = len(dogs_data["dogs"])

    cols = int(math.sqrt(num_dogs))
    rows = int(math.ceil(num_dogs / cols))

    # Set the figure size
    plt.figure(figsize=(5, 5))

    # Loop para exibir as imagens dos cães
    for i, dog_info in enumerate(dogs_data["dogs"]):
        filename = PROJECT_ROOT / "data" / "dogs" / f"{dog_info['dog_id']}.png"
        img = mpimg.imread(str(filename))

        plt.subplot(rows, cols, i+1)  # (número de linhas, número de colunas, índice do subplot)
        plt.imshow(img)
        plt.axis('off')

    plt.show()

def find_lost_dog(srv, image_path: str):
    result = srv.find_similar_dogs(image_path)
    filename = result['hits']['hits'][0]['_source']['image_path']
    show_dog(filename)

    # Print credentials
    print(result['hits']['hits'][0]['_source']['dog_id'])
    print(result['hits']['hits'][0]['_source']['breed'])
    print(result['hits']['hits'][0]['_source']['owner_name'])

    

def main():
    conn = Util.get_connection()
    # Util.delete_index('dog-images')
    Util.create_index(conn, 'dog-images')
    repo = DogRepo(conn, index_name='dog-images')
    srv = DogService(repo)
    
    lost_dog_image = PROJECT_ROOT / "data" / "lost-dogs" / "lost_dog1.png"

    register_all_dogs(srv)
    # view_all_dogs()
    # show_dog(str(lost_dog_image))
    find_lost_dog(srv, str(lost_dog_image))
    # dog = Dog("TestDog", str(lost_dog_image) , "Unknown", "Unknown Owner")
    # dog.generate_embedding()
    # print(dog.image_embedding)



main()
