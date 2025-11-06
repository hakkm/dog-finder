from elasticsearch import Elasticsearch

class Util:
    @staticmethod
    def get_index_name():
        return "dog-images"

    @staticmethod
    def get_connection():
        es_user = 'elastic'
        es_pass = 'qkZNijnV'
        es = Elasticsearch(
            # Corrected URL: http instead of https
            "http://localhost:9200", 
            basic_auth=(es_user, es_pass),
        )
        es.info() # should return cluster info
        return es

    @staticmethod
    def create_index(es: Elasticsearch,index_name: str):
        index = {
                "settings": {
                    "index.refresh_interval": "5s",
                    "number_of_shards": 1
                    }
                , "mappings": {
                    "properties": {
                        "image_embedding": {
                            "type": "dense_vector",
                            "dims": 512,
                            "index": True,
                            "similarity": "cosine"
                            },
                        "dog_id": {
                            "type": "keyword"
                            },
                        "breed": {
                            "type" : "keyword"
                            },
                        "image_path" : {
                            "type" : "keyword"
                            },
                        "owner_name" : {
                            "type" : "keyword"
                            }
                        }
                    }
                }
        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name, body=index)
            print(f"Index '{index_name}' created.")
        else:
            print(f"Index '{index_name}' already exists.")

    @staticmethod
    def delete_index(index_name: str):
        es = Util.get_connection()
        if es.indices.exists(index=index_name):
            es.indices.delete(index=index_name)
            print(f"Index '{index_name}' deleted.")
        else:
            print(f"Index '{index_name}' does not exist.")


if __name__ == "__main__":
    conn = Util.get_connection()
