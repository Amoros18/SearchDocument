from django.shortcuts import render
# from .document import SearchDocument
from .musique import SearchMusique 
from .film import SearchFilm
from .clipmusical import SearchClipMusical
from metadonne.models import Document as ModelDocument

# Create your views here.
def search(request):
    document = ModelDocument.objects.all()
    musiques =ModelDocument.objects.all()
    # document_ = SearchDocument(document)
    # document_.save()
    query = request.GET.get('q')
    if query:
        musiques = SearchMusique.search().query("multi_match", query=query, fields=['titre','genre', 'summary','langue','url','duree'])
        films = SearchFilm.search().query("multi_match", query=query, fields=['titre','genre', 'summary','langue','url','duree'])
        clipMusicaux = SearchClipMusical.search().query("multi_match", query=query, fields=['titre','genre', 'summary','langue','url','duree'])
    else:
        musiques = SearchMusique.search()
        films = SearchFilm.search()
        clipMusicaux = SearchClipMusical.search()

    tous_contenus = []
    for musique in musiques:
        tous_contenus.append({"type": "Musique", **musique})

    for film in films:
        tous_contenus.append({"type": "Film", **film})

    for clip in clipMusicaux:
        tous_contenus.append({"type": "Clip Musical", **clip})

    # print(tous_contenus)
    return render(request, 'search/index2.html', {'documents': tous_contenus, 'q' :query, 'musiques':musiques, 'films': films, 'clipMusicaux': clipMusicaux})