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
