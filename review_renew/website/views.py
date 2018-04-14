from django.shortcuts import render


def home_view(request):
    """Function that renders Home Page of Review Renew Website."""

    return render(request, 'website/index.html')
