"""digitalhealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.auth.views import login,logout
from django.contrib import admin
from hospital import views
from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',login, {'template_name':'login.html'},name='login' ),
    url(r'^logout/',logout,{'next_page':'/'},name='logout'),
    url(r'^$', views.home, name='home'),
    url(r'^aboutus/', views.aboutus, name='about-us'),
    url(r'^department/', views.department, name='depart-ment'),
    url(r'^signup/', accounts_views.signup, name='sign-up'),
    url(r'^forgetpassword/', views.forgetpw, name='forget-pw'),
    url(r'^resetpassword/', views.resetpw, name='reset-pw'),
    url(r'^user', views.user, name='user'),
    url(r'^profile/', views.profiles, name='profile'),
    '''url(r'^reset/$',
    auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ),
    name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
        '''
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
