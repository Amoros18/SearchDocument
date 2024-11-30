from django.shortcuts import render
from django.http import HttpResponse
from .models import Langue as ModelLangue
from .models import Genre as ModelGenre
from .models import Pays as ModelPays
from .models import TypeDocument as ModelTypeDocument
from .models import Personne as ModelPersonne
from .models import Sujet as ModelSujet
from .models import Document as ModelDocument
from .models import Musique as ModelMusique
from .models import Film as ModelFilm
from .models import ClipMusicale as ModelClipMusical
from django.template import loader
from owlready2 import *


# Create your views here.
def index1(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    langues = ModelLangue.objects.all()
    genres = ModelGenre.objects.all()
    payss = ModelPays.objects.all()
    typeDocuments = ModelTypeDocument.objects.all()
    sujets = ModelSujet.objects.all()
    personnes = ModelPersonne.objects.all()
    documents = ModelDocument.objects.all()
    musiques = ModelMusique.objects.all()
    films = ModelFilm.objects.all()
    clipMusicaux = ModelClipMusical.objects.all()

    onto = get_ontology(os.getcwd() + "\\ontologie.rdf").load()

    with onto:
        class Langue(Thing): pass
        class Genre(Thing): pass
        class Pays(Thing): pass
        class TypeDocument(Thing): pass
        class Sujet(Thing): pass
        class Personne(Thing): pass
        class Document(Thing): pass
        class Audio(Document): pass
        class Musique(Audio): pass
        class Video(Thing): pass
        class Film(Video): pass
        class ClipMusical(Video): pass


##########################################################################
##
############           Ajout des langues
##
############################################################################
        for langue in  langues:
            instance = Langue("Langue%d" %langue.id)
            # Ajouter les propriétés
            instance.nom = langue.nom
            instance.code_iso = langue.code_iso
            instance.description = langue.description

##########################################################################
##
############           Ajout des genre
##
############################################################################
        for genre in genres:
            instance = Genre("Genre%d" %genre.id)
            instance.nom = genre.nom
            instance.description = genre.description

##########################################################################
##
############           Ajout des pays
##
############################################################################
        for pays in payss:
            instance = Pays("Pays%d" %pays.id)
            instance.nom = pays.nom
            instance.description = pays.description

##########################################################################
##
############           Ajout des type de document
##
############################################################################
        for typeDocument in typeDocuments:
            instance = TypeDocument("DocumentType%d" %typeDocument.id)
            instance.nom = typeDocument.nom
            instance.description = typeDocument.description

##########################################################################
##
############           Ajout des sujet
##
############################################################################
        for sujet in sujets:
            instance = Sujet("Sujet%d" %sujet.id)
            instance.nom = sujet.nom
            instance.description = sujet.description

##########################################################################
##
############           Ajout des personnes
##
############################################################################
        for personne in personnes:
            instance = Personne("Personne%d" %personne.id)
            instance.nom = personne.nom
            instance.biographie = personne.bio
            pays_ids = personne.nationnalite.values_list('id', flat=True)
            formatted_pays = [f"Pays{id}" for id in pays_ids]

            for nom in formatted_pays:
                # Récupérer le pays par son nom s'il existe dans l'ontologie
                pays = onto.search_one(iri=f"*{nom}")
                if pays:
                    instance.aPourNationalite.append(pays)  # Ajouter à la propriété

##########################################################################
##
############           Ajout des documents
##
############################################################################

        for document in documents:
            instance = Document("Document%d" %document.id)
            instance.titre = document.titre
            instance.summary = document.summary
            instance.date_publication = document.date_publication
            instance.format_fichier = document.format_fichier
            instance.url = document.url

            id = document.type_document.id
            formatted_type_document = "DocumentType"+str(id)
            #print(formatted_type_document)
            type_documenent = onto.search_one(iri=f"*{formatted_type_document}")
            #print(type_documenent)
            if type_documenent:
                instance.aPourType.append(type_documenent)  # Ajouter à la propriété

            langue_principale = onto.search_one(iri=f"*Langue{document.langue_principale.id}")
            print(f"*Langue{document.langue_principale}")
            if langue_principale:
                instance.languePrincipale.append(langue_principale)  # Ajouter à la propriété
##########################################################################
##
############           Ajout des Musique
##
############################################################################
        for musique in musiques:
            instance = Musique("Musique%d" %musique.id)
            instance.duree = musique.duree
            id = musique.document.id
            formatted_document_id = "Document"+str(id)
            # print(formatted_document_id)
            document = onto.search_one(iri=f"*{formatted_document_id}")
            # print(document)
            if document: 
                instance.estUneParticuliarite = document  # Ajouter à la propriété
            genre_ids = musique.genre.values_list('id', flat=True)
            formatted_genre = [f"Genre{id}" for id in genre_ids]
            for nom in formatted_genre:
                # Récupérer le pays par son nom s'il existe dans l'ontologie
                genre = onto.search_one(iri=f"*{nom}")
                if genre:
                    instance.aPourGenre.append(genre)  # Ajouter à la propriété

##########################################################################
##
############           Ajout des Films
##
############################################################################
        for film in films:
            instance = Film("Film%d" %film.id)
            instance.resolution = film.resolution
            document_id = film.document.id
            # print(document_id)
            document = onto.search_one(iri = "*Document"+str(document_id))
            if (document):
                instance.estUneParticuliarite = document
            acteur_ids = film.acteur.values_list('id',flat=True)
            for acteur_id in acteur_ids:
                print(acteur_id)
                acteur = onto.search_one(iri = '*Personne'+str(acteur_id))
                if(acteur):
                    instance.aPourActeur.append(acteur)
            realisateur_id = film.realisateur.id
            realisateur = onto.search_one(iri = "*Personne"+str(realisateur_id))
            if(realisateur):
                instance.aPourRealisateur = realisateur

##########################################################################
##
############           Ajout des Clip Musicaux
##
############################################################################
        for clipMusical in clipMusicaux:
            instance = ClipMusical("ClipMusical%d" %clipMusical.id)
            instance.resolution = clipMusical.resolution
            document_id = clipMusical.document.id
            # print(document_id)
            document = onto.search_one(iri = "*Document"+str(document_id))
            if (document):
                instance.estUneParticuliarite = document
            musique_id = clipMusical.musique.id
            musique = onto.search_one(iri = "*Musique"+str(musique_id))
            if(musique):
                instance.estLeClipDe = musique

##########################################################################
##
############           Sauvegarde de l'ontologie
##
############################################################################

    onto.save(file="ajout_langues_ontologie.rdf")

    template = loader.get_template("metadonne/index.html")
    context = {
        "langues": langues,
    }
    return HttpResponse(template.render(context, request))


def test(Request):
    personne = ModelPersonne.objects.get(id=1)
    nationnalites = personne.nationnalite.all()

    return HttpResponse(nationnalites[1].id)
