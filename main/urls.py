from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/', views.about, name='about'),
    path('ORVI/', views.ORVI, name='ORVI'),
    path('Antipyretics/', views.Antipyretics, name='Antipyretics'),
    path('Painkillers/', views.Painkillers, name='Painkillers'),
    path('Sore-throat/', views.Throat, name='Throat'),
    path('Nose-remedy/', views.Nose, name='Nose'),
    path('redir/<slug:r_slug>/', views.get_link, name='get_link'),
    path('ORVI/<slug:product_slug>/', views.product_orvi, name='orvi_slug'),
    path('Antipyretics/<slug:product_slug>/', views.product_antipyretics, name='antipyretics_slug'),
    path('Painkillers/<slug:product_slug>/', views.product_painkillers, name='painkillers_slug'),
    path('Sore-throat/<slug:product_slug>/', views.product_throat, name='throat_slug'),
    path('Nose-remedy/<slug:product_slug>/', views.product_nose, name='nose_slug'),
    path('Feedback', views.feedback, name='feedback'),
    path('Ok/', views.message_ok, name='send'),
    path('Feedbacks', views.feedbacks_view, name='feedbacks'),
]
