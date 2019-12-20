from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie


def mov(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = MovieForm()
    return render(request,'index.html', {'form': form})


def show(request):
    movies = Movie.objects.all()
    return render(request,"show.html", {'movies': movies})


def edit(request, id):
    movie = Movie.objects.get(id=id)
    return render(request,'edit.html', {'movie': movie})


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST, instance = movie)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'movie': movie})


def destroy(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect("/show")
