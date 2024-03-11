"""
Fisier local de urls, fiecare app o sa aiba cate unul.
Dupa ce definim aici endpoints, le importam in fisierul global,
care este mysite/urls.py.

"""
from django.urls import path

from . import views

"""
Intotdeauna vom avea o lista de tipul urlpatterns,
in care vom apela functia 
path("<url relativ>", <view>, <nume view>)
"""
# aceasta variabila ne permite sa ne referim la URL-urile de mai jos cu prefixul polls,
# de exemplu "polls:hello"
app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("hello/<str:name>", views.hello, name="hello"),
    path("<int:question_id>", views.detail, name="detail"),
    path("<int:question_id>/results", views.results, name="results"),
    path("<int:question_id>/vote", views.vote, name="vote")
]