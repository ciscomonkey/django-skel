from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from skel import __version__


@login_required
def default(request):
    return render(request, 'index.html', context={'version': __version__})
