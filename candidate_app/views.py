from django.shortcuts import render, get_object_or_404, redirect
from .models import Candidatedirectory
from .forms import CandidateForm

def list_candidates(request):
    candidates = Candidatedirectory.objects.all()
    return render(request, 'list_candidates.html', {'candidates': candidates})

def view_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidatedirectory, id=candidate_id)
    return render(request, 'view_candidate.html', {'candidate': candidate})

def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_candidates')
    else:
        form = CandidateForm()
    return render(request, 'add_candidate.html', {'form': form})

def edit_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidatedirectory, id=candidate_id)
    if request.method == 'POST':
        form = CandidateForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('list_candidates')
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'edit_candidate.html', {'form': form, 'candidate': candidate})

def delete_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidatedirectory, id=candidate_id)
    candidate.delete()
    return redirect('list_candidates')