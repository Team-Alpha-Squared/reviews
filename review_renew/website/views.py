from django.shortcuts import render


def home_view(request):
    """Function that renders Home Page of Review Renew Website."""

    return render(request, 'website/index.html')


def about_view(request):
    """Function that renders About Page of Review Renew Website."""

    return render(request, 'website/about.html')
