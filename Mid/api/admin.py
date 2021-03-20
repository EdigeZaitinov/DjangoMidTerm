from django.contrib import admin
from api.models import Book,BookJournalBase,Journal

@admin.register(Book) #первый способ
class BookAdmin(admin.ModelAdmin):
    list_display=('name','price','description','created_at','num_pages','janre',)
    list_display_links=('name',)
    list_filter=('price',)
    search_fields=('name',)

@admin.register(Journal) #первый способ
class JournalAdmin(admin.ModelAdmin):
    list_display=('name','price','description','created_at','type','publisher',)
    list_display_links=('name',)
    list_filter=('price',)
    search_fields=('name',)

