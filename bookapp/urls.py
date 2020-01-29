from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [

     # login,register & logout urls
    path('',views.homepage,name='home'),
    path('login',views.login_page,name='login'),
    path('register',views.register_page,name='register'),
    path('logout',views.logout_page,name='logout'),
    path('Profile',views.profile,name='profile'),
    path('delete',views.delete,name='delete'),
    path('password-reset',views.password_reset,name='password_reset'),


    # book categories url
    path('book_list',views.book_list, name='book_list'),
    
    # book list urls
    path('personal',views.pd, name='pd'),
    path('nonfiction',views.nf,name='nonfic'),
    path('mystry',views.mystery,name='mystery'),
    path('love',views.romance,name='romance'),
    path('bio',views.biography,name='biography'),

    # book data urls
    path('p_d/<int:pk>/',views.p_d,name='pdev'),
    path('nonf/<int:pk>/',views.non,name='non'),
    path('mystery/<int:pk>/',views.myst,name='mystery'),
    path('love/<int:pk>/',views.love,name='love'),
    path('bio/<int:pk>/',views.bio,name='bio'),

    #book forms urls
    path('pd/book/add',views.pd_bookadd,name='pd_bookadd'),
    path('non/book/add',views.Non_bookadd,name='Non_bookadd'),
    path('Myst/book/add',views.Myst_bookadd,name='Myst_bookadd'),
    path('Romance/book/add',views.Romance_bookadd,name='Romance_bookadd'),
    path('Bio/book/add',views.Bio_bookadd,name='Bio_bookadd'),

    # text edit urls
    path('pd/<int:pk>/edit/', views.pdtext_edit, name='pdtext_edit'),
    path('nontext/<int:pk>/edit/', views.nontext_edit, name='nontext_edit'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)