from django.contrib import admin
from main.models import Home, About, Feature, Menu_Category, Menu, Event, Contact

@admin.register(Home)
class Home(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title', )



@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('about_title', 'article',)
    list_display_links = ('about_title', 'article' )



@admin.register(Feature)
class Feature(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title', )




@admin.register(Menu_Category)
class Menu_Category(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title', )



@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = ('title', 'category', 'food_name', 'food_price',)
    list_display_links = ('title', 'category', 'food_name', 'food_price', )


@admin.register(Event)
class Event(admin.ModelAdmin):
    list_display = ('title', 'title_card', 'book_card')
    list_display_links = ('title', 'title_card', 'book_card')
    list_filter = ('book_card',)
    
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('title', 'phone', 'email')
    list_display_links = ('title', 'phone', 'email')
    list_filter = ('adress',)

