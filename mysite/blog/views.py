from django.shortcuts import render
from  .forms import PostModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

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

def post_model_detail_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    context = {
        "object": obj,
    }
    template = "blog/detail-view.html"
    return render(request, template, context)

def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    template = "blog/update-view.html"
    form = PostModelForm(request.POST or None, instance=obj)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        context = {
            "form": PostModelForm()
        }
    return render(request, template, context)

def post_model_delete_view(request, id=None):
    template = "blog/delete-view.html"
    if request.method == 'POST':
        obj = get_object_or_404(PostModel, id=id)
        obj.delete()

    
    return render(request, template)