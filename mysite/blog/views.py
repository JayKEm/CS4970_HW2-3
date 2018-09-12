from django.shortcuts import render
from  .forms import PostModelForm
from django.http import HttpResponse

from .models import PostModel
# Create your views here.

def post_model_list_view(request):
    qs = PostModel.objects.all()

    template = "blog/list-view.html"
    context = {
        "object_list": qs,
    }
    return render(request, template, context)

def post_model_create_view(request):
    template = "blog/create-view.html"
    form = PostModelForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        context = {
            "form": PostModelForm()
        }
    return render(request, template, context)
