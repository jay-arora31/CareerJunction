"""
URL configuration for careerjunctionmain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from .views import *
urlpatterns = [
   
        path('',bloghome,name='blog'),
        path('questionpost/',questionpost,name='questionpost'),
        path('yourquestion/',yourquestion,name='yourquestion'),
        path('edit_question/<int:id>',edit_question,name='edit_question'),
        path('answer_question/<int:id>',answer_question,name='answer_question'),
        path('like_button/<int:id>',like_button,name='like_button'),
        path('dislike_button/<int:id>',dislike_button,name='dislike_button'),
        path('most_answer_question/',most_answer_question,name='most_answer_question'),
        path('unanswer_question/',unanswer_question,name='unanswer_question'),
        path('search_by_category/',search_by_category,name='search_by_category'),
      


]
