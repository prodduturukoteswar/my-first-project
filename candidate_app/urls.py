from django.urls import path
from .views import list_candidates, view_candidate, add_candidate, edit_candidate, delete_candidate

urlpatterns = [
    path('', list_candidates, name='list_candidates'),
    path('<int:candidate_id>/', view_candidate, name='view_candidate'),
    path('add/', add_candidate, name='add_candidate'),
    path('<int:candidate_id>/edit/', edit_candidate, name='edit_candidate'),
    path('<int:candidate_id>/delete/', delete_candidate, name='delete_candidate'),
]
