from django.urls import path
from website.views import *

urlpatterns = [
    # path ('url address' , 'view')
    # path("http-test", http_test),
    path("home", index_view),
    path("about", about_view),
    path("contact", contact_view),
]