from django.shortcuts import render, redirect, get_object_or_404
from .models import Scout
from .forms import ScoutForm

def add_scout(request):
    if request.method == 'POST':
        form = ScoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_all_scouts')
    else:
        form = ScoutForm()
    return render(request, 'add_scout.html', {'form': form})

def view_all_scouts(request):
    scouts = Scout.objects.all()
    return render(request, 'view_all_scouts.html', {'scouts': scouts})

def edit_scout(request, scout_id):
    scout = get_object_or_404(Scout, id=scout_id)
    if request.method == 'POST':
        form = ScoutForm(request.POST, instance=scout)
        if form.is_valid():
            form.save()
            return redirect('view_all_scouts')
    else:
        form = ScoutForm(instance=scout)
    return render(request, 'edit_scout.html', {'form': form})

def delete_scout(request, scout_id):
    scout = get_object_or_404(Scout, id=scout_id)
    if request.method == 'POST':
        scout.delete()
        return redirect('view_all_scouts')
    return render(request, 'delete_scout.html', {'scout': scout})
