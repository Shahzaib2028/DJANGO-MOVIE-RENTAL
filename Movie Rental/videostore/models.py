from django.db import models

class Members(models.Model):
    member_name = models.CharField(max_length=100)
    member_address = models.CharField(max_length=100)
    member_join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member_name


class Movies(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_year = models.IntegerField()
    movie_genere = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.movie_name


class Movie_Rental(models.Model):
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    rent_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()