from django.contrib import admin
from . import models

class Members_Admin(admin.ModelAdmin):
    list_display = ['__str__', 'member_address', 'member_join_date']

class Movies_Admin(admin.ModelAdmin):
    list_display = ['__str__', 'movie_year', 'movie_genere', 'price']

class Movie_Rental_Admin(admin.ModelAdmin):
    list_display = ['member_id', 'movie_id', 'rent_date', 'return_date']

admin.site.register(models.Movies, Movies_Admin)
admin.site.register(models.Members, Members_Admin)
admin.site.register(models.Movie_Rental, Movie_Rental_Admin)