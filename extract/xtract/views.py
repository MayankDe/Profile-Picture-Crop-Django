from django.shortcuts import render, redirect
# from xtract.new import crop_part_pdf
from .models import Photo
from .forms import PhotoForm

from django.core.files import File


def home(request):
    return render(request, 'xtract/home.html')



def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PhotoForm()
    return render(request, 'xtract/cropimg.html', {'form': form,'photos':photos})