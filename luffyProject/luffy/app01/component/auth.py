from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import exceptions
from app01 import models

class Authentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('登录认证失败')
        else:
            return token_obj.user.user, token_obj.token