from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Post 
#download import
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf

from .forms import PostForm

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        name = request.POST['name']
        country = request.POST['country']
        duration = request.POST['duration']
        industry = request.POST['industry']
        if form.is_valid():
            print('I work')
            form.save()
            return redirect("template")
    else:
        form = PostForm()
    return render(request, "posts/new.html", {"form": form})

def template(request):

    # rqts = Post.objects.all()
    rqts = Post.objects.get(pk=8)

    return render(request, "posts/template.html", {"rqts": rqts})

#download code
class downloadpdf(View):
    def get(self, request, *args, **kwargs):
        global pdf
        pdf = render_to_pdf('posts/templated.html')
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 't&c_%s.pdf' %('terms')
        content =  'attachment; filename="%s"' %(filename)
        response['Content-Disposition'] = content
        return response