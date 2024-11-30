from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from metadonne.models import Film as ModelFilm

@registry.register_document
class SearchFilm(Document):
    titre = fields.TextField()
    summary = fields.TextField()
    date_publication = fields.DateField()
    format_fichier = fields.TextField()
    url = fields.TextField()
    langue = fields.TextField()
    resolution = fields.TextField()
    acteurs = fields.TextField()
    
    class Index:
        name = 'film'

    class Django:
        model = ModelFilm
        queryset = ModelFilm.objects.all() 

    def prepare_titre(self, instance):
        return instance.document.titre if instance.document else None

    def prepare_summary(self, instance):
        return instance.document.summary if instance.document else None

    def prepare_date_publication(self, instance):
        return instance.document.date_publication if instance.document else None

    def prepare_format_fichier(self, instance):
        return instance.document.format_fichier if instance.document else None

    def prepare_url(self, instance):
        return instance.document.url if instance.document else None

    def prepare_langue(self, instance):
        return instance.document.langue_principale.nom if instance.document and instance.document.langue_principale else None

    def prepare_resolution(self, instance):
        return instance.resolution
    def prepare_acteurs(self, instance):
        return " | ".join(instance.acteur.values_list('nom',flat = True))
    
