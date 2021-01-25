from django.urls import include, path
from .import views
from .views import *

urlpatterns=[
    
    path('api/branches/', BranchView.as_view(), name="branch-view"),
    path('api/branches/autocomplete/', BranchViewAuto.as_view(), name="branch-view-auto"),
    path('', home, name='home'),
]

