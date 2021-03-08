from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_rental_info),
    path("members/", views.show_member_info),
    path("movies/", views.show_movie_info),
    path("movie/update/<int:id>/", views.update_movie_info),
    path("member/update/<int:id>/", views.update_member_info),
    path("movie/delete/<int:id>/", views.delete_movie),
    path("member/delete/<int:id>/", views.delete_member),
    path("movie/create/", views.create_movie),
    path("member/create/", views.create_member),
    path("rent/", views.rent_movie),
]
