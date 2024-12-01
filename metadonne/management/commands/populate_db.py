from django.core.management.base import BaseCommand
from random import choice, randint, sample  # Assurez-vous que random est importé
from faker import Faker
from metadonne.models import Genre, Langue, Pays, TypeDocument, Personne, Sujet, Document, Musique, Film, ClipMusicale
from user.models import Utilisateur
from django.contrib.auth.hashers import make_password, check_password

fake = Faker()

class Command(BaseCommand):
    help = 'Remplir la base de données avec des données fictives.'
    users = [
                Utilisateur.objects.create(username="Amoros",email = "example@gmail.com",password =make_password("Amoros") )
            ]

    def handle(self, *args, **kwargs):
        # Créer des genres
        genres = [
            Genre.objects.create(nom='Rap', description=fake.text(max_nb_chars=255)),
            Genre.objects.create(nom='Bikusssi', description=fake.text(max_nb_chars=255)),
            Genre.objects.create(nom='Rock', description=fake.text(max_nb_chars=255)),
            Genre.objects.create(nom='Pop', description=fake.text(max_nb_chars=255)),
            Genre.objects.create(nom='Jazz', description=fake.text(max_nb_chars=255)),
            Genre.objects.create(nom='Classique', description=fake.text(max_nb_chars=255)),
        ]

        # Créer des langues
        langues = [
            Langue.objects.create(nom='Français', description=fake.text(max_nb_chars=255), code_iso='FR'),
            Langue.objects.create(nom='Anglais', description=fake.text(max_nb_chars=255), code_iso='EN'),
            Langue.objects.create(nom='Espagnol', description=fake.text(max_nb_chars=255), code_iso='ES'),
            Langue.objects.create(nom='Russe', description=fake.text(max_nb_chars=255), code_iso='RU'),
            Langue.objects.create(nom='Chinois', description=fake.text(max_nb_chars=255), code_iso='CH'),
            Langue.objects.create(nom='Allemand', description=fake.text(max_nb_chars=255), code_iso='AL'),
        ]

        # Créer des pays
        pays_list = [
            Pays.objects.create(nom='Cameroun', description=fake.text(max_nb_chars=255)),
            Pays.objects.create(nom='Tchad', description=fake.text(max_nb_chars=255)),
            Pays.objects.create(nom='France', description=fake.text(max_nb_chars=255)),
            Pays.objects.create(nom='États-Unis', description=fake.text(max_nb_chars=255)),
            Pays.objects.create(nom='Espagne', description=fake.text(max_nb_chars=255)),
        ]

        # Créer des types de documents
        types_document = [
            TypeDocument.objects.create(nom='Article', description=fake.text(max_nb_chars=255)),
            TypeDocument.objects.create(nom='Livre', description=fake.text(max_nb_chars=255)),
            TypeDocument.objects.create(nom='Vidéo', description=fake.text(max_nb_chars=255)),
        ]

        # Créer des personnes
        personnes = []
        for _ in range(40):
            personne = Personne.objects.create(
                nom=fake.name(),
                bio=fake.text()
            )
            nationalites = sample(pays_list, k=randint(1, len(pays_list)))  # Sélectionner aléatoirement des nationalités
            personne.nationnalite.set(nationalites)  # Utiliser set() pour établir la relation
            personnes.append(personne)

        # Créer des sujets
        sujets = [
            Sujet.objects.create(nom=fake.word(), description=fake.text(max_nb_chars=255)) for _ in range(10)
        ]

        # Créer des documents
        documents = [
            Document.objects.create(
                titre=fake.sentence(),
                summary=fake.text(max_nb_chars=500),
                date_publication=fake.date_time_this_decade(),
                format_fichier='PDF',
                url=fake.url(),
                type_document=choice(types_document),
                langue_principale=choice(langues),
            ) for _ in range(100)
        ]

        # Créer des musiques
        for _ in range(40):
            musique = Musique.objects.create(
                document=choice(documents),
                duree=randint(180, 300)
            )
            musique.musiciens.set(sample(personnes, k=randint(1, len(personnes))))  
            musique.genre.set(sample(genres, k=randint(1, len(genres))))
            
        # Créer des films
        for _ in range(30):
            film = Film.objects.create(
                document=choice(documents)
            )
            film.acteur.set(sample(personnes, k=randint(1, len(personnes))))
            film.realisateur = choice(personnes)

        # Créer des clips musicaux
        for _ in range(30):
            ClipMusicale.objects.create(
                musique=choice(Musique.objects.all()),
                document=choice(documents),
                resolution='1080p'
            )

        self.stdout.write(self.style.SUCCESS('Base de données remplie avec succès !'))