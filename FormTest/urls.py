from django.urls import path
from . import views

# URLConf (URLConfiguration)
urlpatterns = [
    path('enterData', views.enter_cartoon_data),
    path('viewData', views.show_cartoon_list)
]