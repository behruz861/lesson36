from django.urls import path

from app.views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('second/', second_view, name='second'),
    path('form/', FeedbackFormView.as_view(), name='form'),
]



