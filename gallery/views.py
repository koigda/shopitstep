from django.shortcuts import render, redirect

from .forms import GalleryImageForm
from .models import GalleryImage

# Create your views here.

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery/index.html', {'images': images})

def uploads(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = GalleryImageForm()
    return render(request, 'gallery/uploads.html', {'form': form})
