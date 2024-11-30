from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Genre(models.Model):
    nom =models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Langue(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    code_iso = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pays(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

class TypeDocument(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Personne(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    nationnalite = models.ManyToManyField(Pays,related_name='personne')
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Sujet(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



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


class Musique(models.Model):
    musiciens = models.ManyToManyRel(Personne,'musique')
    genre = models.ManyToManyField(Genre ,'musique_genre')
    document = models.ForeignKey(Document,on_delete=models.CASCADE)
    duree = models.IntegerField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Film(models.Model):
    acteur = models.ManyToManyField(Personne,related_name='film')
    realisateur = models.ForeignKey(Personne,on_delete=models.SET_NULL,blank=True, null=True, related_name="film_realiser")
    resolution = models.CharField(max_length=50, blank=True, null=True)
    document = models.ForeignKey(Document,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ClipMusicale(models.Model):
    musique = models.ForeignKey(Musique, null=True,on_delete=models.SET_NULL)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    document = models.ForeignKey(Document,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


