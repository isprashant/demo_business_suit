from django.shortcuts import render, get_object_or_404
from django.apps import apps
from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def get_all_models():
    return [(model.__name__, model._meta.verbose_name_plural) for model in apps.get_app_config('keystone').get_models()]

def model_list(request):
    app_models = apps.get_app_config('keystone').get_models()
    models_info = [(model.__name__, model._meta.verbose_name_plural) for model in app_models]
    return render(request, 'model_list.html', {'models': models_info})

def model_detail(request, model_name):
    model = apps.get_model('keystone', model_name)
    fields = [field.name for field in model._meta.fields]
    objects = model.objects.all()
    models_info = get_all_models()
    return render(request, 'model_detail.html', {
        'model_name': model_name,
        'fields': fields,
        'objects': objects,
        'models': models_info
    })

def model_add(request, model_name):
    model = apps.get_model('keystone', model_name)
    ModelForm = modelform_factory(model, fields='__all__')  # Create form dynamically

    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('model_detail', args=[model_name]))
    else:
        form = ModelForm()

    models_info = get_all_models()
    return render(request, 'model_add.html', {
        'form': form,
        'model_name': model_name,
        'models': models_info
    })