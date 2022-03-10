from django.urls import include, path
from . import views
urlpatterns = [

    # path('', views.index,name="index"),
    path('<slug:sender>/<slug:receiver>/', views.gotolink,name="gotolink"),
    path('generatelink/', views.generatelink,name="generatelink"),

]
