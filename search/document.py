from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from metadonne.models import Document as ModelDocument

@registry.register_document
class SearchDocument(Document):
    class Index:
        name = 'document'
    # settings = {
    #     'number_of_shards': 1,
    #     'number_of_replicas': 0
    # }
    class Django:
         model = ModelDocument
         fields = [
             'titre',
             'url',
             'summary',
         ]
         