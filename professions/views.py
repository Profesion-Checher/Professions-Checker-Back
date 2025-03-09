from django.shortcuts import get_object_or_404, redirect, render
from .models import Profession

def profession_list(request):
    professions = Profession.objects.all()
    return render(request, 'professions/list.html', {'professions': professions})

def profession_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Profession.objects.create(name=name)
        return redirect('profession_list')
    return render(request, 'professions/create.html')

def profession_delete(request):
    profession = get_object_or_404(Profession, id=id)
    profession.delete()
    return redirect('profession_list')

def profession_update(request):
    profession = get_object_or_404(Profession, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        profession.name = name
        profession.save()
        return redirect('profession_list')
    return render(request, 'professions/update.html', {'profession': profession})