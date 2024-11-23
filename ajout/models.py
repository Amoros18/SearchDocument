from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Utilisateur(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(blank=True,null=True)
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    def __str__(self):
        return self.username
    
class HistoriqueDeRecherche(models.Model):
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    requete = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Langue(models.Model):
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    code_iso = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nom

class TypeDocument(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class Personne(models.Model):
    nom = models.CharField(max_length=255)
    nationnalite = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class Sujet(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class Document(models.Model):
    titre = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    date_publication = models.DateTimeField()
    format_fichier = models.CharField(max_length=50)
    url = models.URLField(unique=True)
    type_document = models.ForeignKey(TypeDocument,null=True, on_delete=models.SET_NULL)
    langue_principale = models.ForeignKey(Langue,null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titre
    
class Musique(models.Model):
    musiciens = models.ManyToManyRel(Personne,'musique')
    genre = models.CharField(max_length=100)
    document_id = models.ForeignKey(Document,on_delete=models.CASCADE)
    duree = models.IntegerField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Film(models.Model):
    acteur = models.ManyToManyField(Personne,related_name='film')
    realisateur = models.ForeignKey(Personne,on_delete=models.SET_NULL,blank=True, null=True, related_name="film_realiser")
    resolution = models.CharField(max_length=50, blank=True, null=True)
    document_id = models.ForeignKey(Document,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ClipMusicale(models.Model):
    musique = models.ForeignKey(Musique, null=True,on_delete=models.SET_NULL)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    document_id = models.ForeignKey(Document,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


