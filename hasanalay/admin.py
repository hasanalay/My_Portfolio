from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Portfolio, Contact

# Home Page
admin.site.register(Home)

# About Page
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    
# Skills Page
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SkillsInline]
    
# Portfolio Page
admin.site.register(Portfolio)

# Contact Page
admin.site.register(Contact)

