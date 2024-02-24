from django.db import models
from utils.rands import slugify_new

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None, #Torna unica a Slug, não poderá ter tags iguais
        null=True, blank=True, max_length=255,
    )

    #Sobreescrevendo metódo Save
    def save(self, *args, **kwargs):
        #Sem slug, gera nova slug
        if not self.slug:
            self.slug = slugify_new(self.name, 6)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None, #Torna unica a Slug, não poderá ter tags iguais
        null=True, blank=True, max_length=255,
    )

    #Sobreescrevendo metódo Save
    def save(self, *args, **kwargs):
        #Sem slug, gera nova slug
        if not self.slug:
            self.slug = slugify_new(self.name, 6)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name

class Page(models.Model):
    title = models.CharField(max_length=65,)
    slug = models.SlugField(
        unique=True, default=None, #Torna unica a Slug, não poderá ter tags iguais
        null=True, blank=True, max_length=255,
    )
    is_published = models.BooleanField(
        default=False,
        help_text=''' Este campo precisará estar marcado
                      para a página ser exibida publicamente.''',
        )
    content = models.TextField()

    def save(self, *args, **kwargs):
        #Sem slug, gera nova slug
        if not self.slug:
            self.slug = slugify_new(self.title, 6)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title