from django.conf.urls import url

from .views import reset_password, verify_email, verify_registration

app_name = 'rest_registration_verification_redirects'
urlpatterns = [
    url('verify-registration/$', verify_registration,
        name='verify-registration'),
    url('verify-email/$', verify_email, name='verify-email'),
    url('reset-password/$', reset_password, name='reset-password'),
]
