from django.db import models





class text(models.Model):
	c = models.TextField()

class pics(models.Model):
	photo = models.ImageField(upload_to='images/')
	title = models.TextField(blank=True)
	username = models.TextField(blank=True)
class password(models.Model):
	usern = models.TextField(blank=True)
	password_text = models.TextField(blank=True)
