from django.urls import path
from .views import home, about, contact, single_post, search


urlpatterns = [
    path('', home, name='home'), # domennomi
    path('single-post', single_post, name='singlepost'),
    path('search', search, name='qidiruv'),
    path('about', about, name='about'), # domennomi/about
    path('contact', contact, name='contact') # domennomi/contact
]

# abc.uz/api/v1/infos