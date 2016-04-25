from django.conf.urls import url
from . import views

from .utils import scheduler

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^about$', views.about, name='about'),
    url(r'^login$', views.login, name='login'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^geturl$', views.geturl, name='geturl'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^verify$', views.verify, name='verify'),
    url(r'^resend$', views.resend, name='resend'),
    url(r'^forgot$', views.forgot, name='forgot'),
    url(r'^update$', views.update, name='update'),

    url(r'^profile/image$', views.image, name='image'),
    url(r'^profile/update$', views.profileUpdate, name='profileUpdate'),

    url(r'^alert/delete/(?P<pk>[0-9]+)?$', views.alertDelete, name="alertDelete"),
    url(r'^alert$', views.alert, name='alert'),
]
