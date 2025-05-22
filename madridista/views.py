from django.shortcuts import render
from berita.models import Kategori, Artikel

def home(request):
    template_name = "halaman/index.html"  # Pastikan path ini benar
    context = {
        'title': 'Madridista'
    }
    return render(request, template_name, context)

def about(request):
    template_name = "about.html"  # Disarankan untuk konsisten foldernya
    context = {
        'title': 'Selamat datang di About'
    }
    return render(request, template_name, context)
