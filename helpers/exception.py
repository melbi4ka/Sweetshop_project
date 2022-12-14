from django.shortcuts import render


def handler404(request, *args, **kwargs):
    response = render(request, 'not-found.html')
    response.status_code = 404
    return response
