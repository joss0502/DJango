from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/',admin.site.urls),
    path('graficas/', views.grafica_view, name='grafica_view'),
 

    path('graficas/line/', views.grafica_line_view, name='grafica_line'),
    path('graficas/pastel/', views.grafica_pastel_view, name='grafica_pastel'),
    path('graficas/dispersion/', views.grafica_dispersion_view, name='grafica_dispersion'),
    path('graficas/histograma/', views.grafica_histograma_view, name='grafica_histograma'),
    path('graficas/boxplot/', views.grafica_boxplot_view, name='grafica_boxplot'),
]
