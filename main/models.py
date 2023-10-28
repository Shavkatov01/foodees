from django.db import models



class Home(models.Model):
    banner = models.ImageField(upload_to='banner/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=25, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'


class About(models.Model):
    left_image = models.ImageField(upload_to='about/left_image/%Y/%m/%d', blank=True)
    about_title = models.CharField(max_length=255, blank=True)
    descriptions = models.TextField(blank=True)
    article = models.CharField(max_length=255, blank=True)
    article_author = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.about_title
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


class Feature(models.Model):
    icons = models.ImageField(upload_to='Feature/icons/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=25, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)



    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'



class Menu_Category(models.Model):
    icons = models.ImageField(upload_to='Menu_Category/icons/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=255, blank=True)



    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Menu(models.Model):
    icons = models.ImageField(upload_to='Menu/icons/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=25, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Menu_Category, on_delete=models.CASCADE, blank=True)
    food_name = models.CharField(max_length=255, blank=True)
    food_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    food_image = models.ImageField(upload_to='Menu/food_image/%Y/%m/%d', blank=True )



    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menues'


class Event(models.Model):
    icons = models.ImageField(upload_to='Events/icons/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    title_card  = models.CharField(max_length=255, blank=True)
    book_card = models.DateTimeField(auto_now_add=True)
    description_card = models.TextField(blank=True)


    def __str__(self) -> str:
        return self.title_card
    

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

class Contact(models.Model):
    icons = models.ImageField(upload_to='Events/icons/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    adress  = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    site = models.URLField(blank=True)
    site_name = models.CharField(max_length=255, blank=True)
    ceremony = models.CharField(max_length=255, blank=True)
    ceremony_2  = models.CharField(max_length=255, blank=True)
    ceremony_3 = models.CharField(max_length=255, blank=True)
    ceremont_4 = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.adress
    

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'