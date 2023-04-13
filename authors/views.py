from django.shortcuts import render

from django.shortcuts import render


def register_view(request):
    return render(request, 'authors/pages/register_view.html')
