from django.contrib.auth.models import User
from django_multitenant.utils import *

class SetCurrentTenantFromUser(object):
    def process_request(self, request):
        if not hasattr(self, 'authenticator'):
            # from rest_framework_jwt.authentication import JSONWebTokenAuthentication
            # self.authenticator = JSONWebTokenAuthentication()
            try:
                user = User.objects.all()[0]
            except:
                pass

            try:
                # Assuming your app has a function to get the tenant associated for a user
                current_tenant = get_tenant_for_user(user)
            except Exception as e:
                print(e)

        set_current_tenant(current_tenant)


    def process_response(self, request, response):
        set_current_tenant(None)
        return response
