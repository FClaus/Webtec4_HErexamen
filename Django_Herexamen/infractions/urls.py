from django.urls import path
from . import views

app_name = 'infractions'

urlpatterns = [
	path('<int:infractions_speed>', views.overtreding, name='index'),
]
