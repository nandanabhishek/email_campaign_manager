from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    is_subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email
    
class Campaign(models.Model):
    subject = models.CharField(max_length=200)
    preview_text = models.CharField(max_length=200)
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateTimeField()