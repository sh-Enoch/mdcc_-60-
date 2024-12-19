from django.db import models

# Create your models here.
"""Create a model to store all our recipes."""

class Recipes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cooking_time = models.IntegerField(help_text="How long does it take?")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    