from django.db import models

class dashboard(models.Model):
    dashboard = models.ImageField() #upload_to=hashdash_pictures
    dash_name = models.CharField(max_length=50)
    tags = models.CharField(max_length=20)
    description = models.TextField(max_length=250)

class dashCode(models.Model):
    dash_name = models.CharField(max_length=50)
    yaml = models.TextField()

class creator(models.Model):
    username = models.CharField(max_length=30)
    
    class SocialMedia(models.TextChoices):
        HACOMMUNITY = 'HC', ('Home Assistant Community')
        REDDIT = 'RD', ('Reddit')
        TWITTER = 'TW', ('Twitter')
        FACEBOOK = 'FB', ('Facebook')
        TIKTOK = 'TT', ('Tik-Tok')
    
    social_media = models.CharField(choices=SocialMedia.choices, default=None, max_length=50)