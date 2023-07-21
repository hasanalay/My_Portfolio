from django.db import models

# Home Page
class Home(models.Model):
    name = models.CharField(max_length=20)
    greeting_1 = models.CharField(max_length=20)
    greeting_2 = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='pictures/')
    #save time when modified
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
# About Page
class About(models.Model):
    heading = models.CharField(max_length=20)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_picture = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.career
    
class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_media = models.CharField(max_length=20)
    link = models.URLField(max_length=200)    
        
# Skills Page
class Category(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        
    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)
    
# Porfolio Page
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200) 
    
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Portfolio {self.id}'
    
class Contact(models.Model):
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        
    def __str__(self):
        return self.email