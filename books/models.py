from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
    