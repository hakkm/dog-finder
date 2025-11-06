from Dog import Dog
from Util import Util
from elasticsearch import Elasticsearch
from typing import List

class DogRepo:
    def __init__(self, es_client: Elasticsearch, index_name: str = "dog-images"):
        self.es_client = es_client
        self._index_name = index_name
        Util.create_index(es_client, index_name)

    def insert(self, dog: Dog):
        dog.generate_embedding()
        self.es_client.index(index=self._index_name, body=dog.to_dict())


    def bulk_insert(self, dogs: List[Dog]):
        operations = []
        for dog in dogs:
            operations.append({"index": {"_index": self._index_name}})
            operations.append(dog.to_dict())
        self.es_client.bulk(body=operations)

    def search_by_image(self, image_embedding: List[float]):
        knn = {
                  "field": "image_embedding",
                  "query_vector": image_embedding,
                  "k": 2,
                  "num_candidates": 100,
                  "boost": 100
              }


        fields = ["dog_id", "breed", "owner_name","image_path", "image_embedding"]

        try:
            response = self.es_client.search(
                index=self._index_name,
                body={
                    "knn": knn,
                    "_source": fields
                    },
                size=1
                )
            return response
        except Exception as e:
            print(f"Error during search: {e}")
            return {}
