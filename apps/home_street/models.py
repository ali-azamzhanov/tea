from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title




class Menu(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=500, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Settings(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.key


class Home(models.Model):
    title = models.CharField(max_length=255) 
    subtitle = models.CharField(max_length=255, blank=True)
    
    image = models.ImageField(upload_to="home/")

    button_text = models.CharField(max_length=100, blank=True)
    button_url = models.URLField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    
class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    image_main = models.ImageField(upload_to="about/")
    image_secondary = models.ImageField(upload_to="about/", blank=True)

    button_text = models.CharField(max_length=100, blank=True)
    button_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class AboutExtra(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="about/")

    def __str__(self):
        return self.title
    

class Subject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    image = models.ImageField(upload_to="subjects/")
    
    button_text = models.CharField(max_length=50, default="Подробнее")
    button_url = models.URLField(blank=True)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    

class SubjectSection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    
    
class History(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to="history/", blank=True)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.year} - {self.title}"
    
    
class Review(models.Model):
    name = models.CharField(max_length=100) 
    text = models.TextField()

    rating = models.PositiveSmallIntegerField() 

    created_at = models.DateField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")

    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    year = models.IntegerField(blank=True, null=True)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title or "Image"
    
class HeaderFooterSettings(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название школы")
    logo = models.ImageField(upload_to='settings/logo/', verbose_name="Логотип школы")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="URL Instagram")
    faacebook_url = models.URLField(blank=True, null=True, verbose_name="URL Facebook")
    working_hours = models.CharField(max_length=100, verbose_name="Рабочие часы")
    address = models.CharField(max_length=100, verbose_name="Адрес школы")
    views_counter = models.PositiveIntegerField(default=0, verbose_name="Счетчик просмотров")
    map_iframe = models.TextField(blank=True, verbose_name="Код карты (iframe от Google/Yandex)")
    
    class Meta:
        verbose_name = "Настройки шапки и подвала"
        verbose_name_plural = "Настройки шапки и подвала"
        
    def __str__(self):
        return self.name

    def __str__(self):
        return self.title
    
    
class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    image_main = models.ImageField(upload_to="about/")
    image_secondary = models.ImageField(upload_to="about/", blank=True)

    button_text = models.CharField(max_length=100, blank=True)
    button_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class AboutExtra(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="about/")

    def __str__(self):
        return self.title
    

class Subject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    image = models.ImageField(upload_to="subjects/")
    
    button_text = models.CharField(max_length=50, default="Подробнее")
    button_url = models.URLField(blank=True)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    

class SubjectSection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    
    
class History(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to="history/", blank=True)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.year} - {self.title}"
    
    
class Review(models.Model):
    name = models.CharField(max_length=100) 
    text = models.TextField()

    rating = models.PositiveSmallIntegerField() 

    created_at = models.DateField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")

    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    year = models.IntegerField(blank=True, null=True)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title or "Image"
    
class HeaderFooterSettings(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название школы")
    logo = models.ImageField(upload_to='settings/logo/', verbose_name="Логотип школы")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="URL Instagram")
    faacebook_url = models.URLField(blank=True, null=True, verbose_name="URL Facebook")
    working_hours = models.CharField(max_length=100, verbose_name="Рабочие часы")
    address = models.CharField(max_length=100, verbose_name="Адрес школы")
    views_counter = models.PositiveIntegerField(default=0, verbose_name="Счетчик просмотров")
    map_iframe = models.TextField(blank=True, verbose_name="Код карты (iframe от Google/Yandex)")
    
    class Meta:
        verbose_name = "Настройки шапки и подвала"
        verbose_name_plural = "Настройки шапки и подвала"
        
    def __str__(self):
        return self.name