from presentor.models import Presentation
from django.shortcuts import render, get_object_or_404


def show(request):
    return render(request, 'presentor/show.html')


def fetchshow(request, id):
    slideshow = get_object_or_404(Presentation, pk=id)
    slidenumber = 1
    slidesdict = {}
    slidesdict[1] = []
    slides = slideshow.slides.strip()
    slides = slides.splitlines()
    for slide in slides:
        if not slide:
            slidenumber += 1
            slidesdict[slidenumber] = []
        else:
            slidesdict[slidenumber].append(slide)
    return render(request, 'presentor/slides.html', {'slides': slidesdict,
                  'title': slideshow.title, 'id': slideshow.id})


def control(request, id):
    slideshows = Presentation.objects.all()
    return render(request, 'presentor/control.html',
                  {'slideshows': slideshows})


def student(request):
    return render(request, 'presentor/student.html')


def play(request):
    return render(request, 'presentor/play.html')


def listslideshows(request):
    slideshows = Presentation.objects.values()
    showslist = []
    for slideshow in slideshows:
        showslist.append({"id": slideshow['id'], "title": slideshow['title']})
    return render(request, 'presentor/listslideshows.html',
                  {"showslist": showslist})
