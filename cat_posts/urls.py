from django.urls import path
from .views import CatList, CatDetail

urlpatterns = [
    path('', CatList.as_view(), name='cat_list'),
    path('<int:pk>', CatDetail.as_view(), name='cat_detail'),
    #cat images not showing, Do I need a path here?
]
