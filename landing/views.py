from django.shortcuts import render_to_response


def render_landing(request):
    return render_to_response('index.html')
