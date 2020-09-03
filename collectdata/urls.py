
from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    
    path('',views.home,name='home'),
    path('login/', views.login_request, name="login"),
    path("details/", views.Details, name="details"),
    path('add_form/',views.add_form,name='add_form'),
    path("logout/", views.logout_request, name="logout"),
    path("distance/", views.get_distance, name="distance"),
    path("boostangel_post", views.post_boostangel, name="boostangel"),
    path("ir_support", views.Ir_support, name="Ir_support"),
    path("boost_angke_details", views.boost_angke_details, name="boost_angke_details"),
    path("conditions", views.Conditions, name="conditions"),
    path("bracketed", views.bracketed, name="bracketed"),
    path("gasgiant", views.gasgiant, name="gasgiant"),
    path("bracket_c", views.bracket_c, name="bracket_c"),
    path("opposition", views.opposition, name="opposition"),
    path("sextiles", views.sextile, name="sextiles"),
    path("trines", views.trine, name="trines"),
    path("bracketedC", views.bracketedC, name="bracketedC"),
    path("multiple_squares", views.multiple_square, name="multiple_squares"),
    path("moons", views.moons, name="moons"),



    
]
