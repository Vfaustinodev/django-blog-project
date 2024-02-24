from django.contrib import admin
from blog.models import Tag, Category, Page

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug', #tags visiveis
    list_display_links = 'name', # tags que vão ser link
    search_fields = 'id', 'name', 'slug', #Campos que podem ser buscados
    list_per_page = 10 #Quantidade de tags por pagina
    ordering = '-id', # Ordenado pelo Id decrescente
    prepopulated_fields = { #Vai capturar de forma automatica a tag digitada e passa pelo metódo slugify
        "slug": ('name',),
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug', #tags visiveis
    list_display_links = 'name', # tags que vão ser link
    search_fields = 'id', 'name', 'slug', #Campos que podem ser buscados
    list_per_page = 10 #Quantidade de tags por pagina
    ordering = '-id', # Ordenado pelo Id decrescente
    prepopulated_fields = { #Vai capturar de forma automatica a tag digitada e passa pelo metódo slugify
        "slug": ('name',),
    }
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published', #tags visiveis
    list_display_links = 'title', # tags que vão ser link
    search_fields = 'id', 'slug', 'title', 'content' #Campos que podem ser buscados
    list_per_page = 50 #Quantidade de tags por pagina
    list_filter = 'is_published',
    list_editable = 'is_published',
    ordering = '-id', # Ordenado pelo Id decrescente
    prepopulated_fields = { #Vai capturar de forma automatica a tag digitada e passa pelo metódo slugify
        "slug": ('title',),
    }