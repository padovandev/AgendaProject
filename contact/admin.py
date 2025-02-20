from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin (admin.ModelAdmin):
    # Exibindo a listagem de valores no Display Admin
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email',

    # Ordenando as informações por valores especificos
    ordering = 'id',

    # Filtros de listagem para valores 
    list_filter = 'created_date', 

    # Barra de pesquisa de Valores
    search_fields = 'created_date', 'email', 'first_name', 'last_name', 'phone',

    # Quantidade de Contatos exibindo por pagina
    list_per_page = 15
    
    # Maximo de contatos exibidos por pagina
    list_max_show_all = 200

    # valores que são editáveis
    # list_editable = 'first_name', 'last_name', 

    list_display_links = 'first_name', 