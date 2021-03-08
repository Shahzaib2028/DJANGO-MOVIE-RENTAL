from django.shortcuts import render, redirect
from django.utils import timezone
from . import models
from . import forms

def getMovie(id):
    try:
        movie = models.Movies.objects.get(id=id)
        return movie
    except:
        return None

def getMember(id):
    try:
        member = models.Members.objects.get(id=id)
        return member
    except:
        return None

def show_rental_info(request):
    movies = models.Movies.objects.all()
    return render(request, 'videostore/index.html', {"data":movies})

def show_member_info(request):
    members = models.Members.objects.all()
    return render(request, 'videostore/members.html', {"data":members})

def create_member(request):
    if request.method == "POST":
        form = forms.MemberForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['member_name']
            form.save()
            data = {"strong": f"Member with name {name.title()} created", "simple": "you can now start renting movies"}
            return render(request, 'videostore/created_success.html', {"data":data})
        else:
            return render(request, 'videostore/error.html')
    form = forms.MemberForm()
    return render(request, 'videostore/create_member.html', {"form":form})

def update_member_info(request, id):
    form = forms.MemberForm(request.POST or None, instance=getMember(id))
    if form.is_valid():
          form.save()
          return redirect('/members/')
    return render(request, 'videostore/update_member.html', {"member":getMember(id), "form":form})

def delete_member(request, id):      
    if request.method == "POST":
        member = models.Members.objects.get(id=id)
        member.delete()
        return redirect('/members/')
    return render(request, 'videostore/delete_member.html', {"member":getMember(id)})

def show_movie_info(request):
    movies = models.Movies.objects.all()
    return render(request, 'videostore/movies.html', {"data":movies})

def create_movie(request):
    if request.method == "POST":
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['movie_name']
            form.save()
            data = {"strong": f"Movie with name {name.title()} created", "simple": "this movie can now be rented"}
            return render(request, 'videostore/created_success.html', {"data":data})
        else:
            return render(request, 'videostore/error.html')
    form = forms.MovieForm()
    return render(request, 'videostore/create_movie.html', {"form":form})

def update_movie_info(request, id):
    form = forms.MovieForm(request.POST or None, instance=getMovie(id))
    if form.is_valid():
          form.save()
          return redirect('/movies/')
    return render(request, 'videostore/update_movie.html', {"movie":getMovie(id), "form":form})

def delete_movie(request, id):    
    if request.method == "POST":
        movie = models.Movies.objects.get(id=id)
        movie.delete()
        return redirect('/movies/')
    return render(request, 'videostore/delete_movie.html', {"movie":getMovie(id)})

def rent_movie(request):
    if request.method == "POST":
        form = forms.MovieRentalForm(request.POST)
        if form.is_valid():
            return_date = form.cleaned_data['return_date']
            if return_date >= timezone.now():
                form.save()
                data = {"strong": "Thank You!", "simple": "for renting the movie, have a nice day."}
                return render(request, 'videostore/created_success.html', {"data":data})
            else:
                return render(request, 'videostore/error.html')
        else:
            return render(request, 'videostore/error.html')
    form = forms.MovieRentalForm()
    return render(request, 'videostore/rent_movie.html', {"form":form})

