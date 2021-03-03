"""NotesSharing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('userlogin', userlogin, name='login'),
    path('login_admin', login_admin, name='login_admin'),
    path('signup', signup , name='signup'),
    path('admin_home', admin_home , name='admin_home'),
    path('logout', Logout, name='logout'),
    path('user_home', user_home, name='user_home'),
    path('upload_notes', upload_notes, name='upload_notes'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('change_password', change_password, name='change_password'),
    path('view_mynotes', view_mynotes, name='view_mynotes'),
    path('view_users', view_users, name='view_users'),
    path('', index, name='index'),
    path('delete_mynotes/<int:uid>', delete_mynotes, name='delete_mynotes'),
    path('delete_users/<int:uid>', delete_users, name='delete_users'),
    path('pending_notes', pending_notes , name='pending_notes'),
    path('accepted_notes', accepted_notes , name='accepted_notes'),
    path('rejected_notes', rejected_notes , name='rejected_notes'),
    path('all_notes', all_notes , name='all_notes'),
    path('view_allnotes', view_allnotes , name='view_allnotes'),
    path('assign_status/<int:uid>', assign_status, name='assign_status'),
    path('delete_notes/<int:uid>', delete_notes, name='delete_notes'),
    path('home_blog/', home_blog, name='home_blog'),
    path('dashboard/', dashboard, name='dashboard'),
    path('blog_logout/', blog_logout, name='blog_logout'),
    path('addpost', add_post, name='addpost'),
    path('updatepost/<int:id>', update_post, name='updatepost'),
    path('delete/<int:id>', delete_post, name='deletepost'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)                                                                                    #whenever we upload file or use file to upload, here in our case we are uploading notes in file format hence we are using this line. 
