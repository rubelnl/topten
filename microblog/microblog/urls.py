from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from users_app.views import RegistrationView, LoginView, logout

#from django.views.static import serve

urlpatterns = [
    path('', include(('blog_app.urls', 'blog_app'))),
    path('users/', include(('users_app.urls', 'users_app'))),
    path('admin/', admin.site.urls),

    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),    
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users_app/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users_app/password_reset_done.html'), name='password_reset_done'),    
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users_app/password_reset_confirm.html'), name='password_reset_confirm'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    #urlpatterns += url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
