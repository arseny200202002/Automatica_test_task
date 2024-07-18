from rest_framework.authentication import BaseAuthentication 
from rest_framework.exceptions import AuthenticationFailed 

from .models import Employee

class PhoneAuthentication(BaseAuthentication): 
    def authenticate(self, request): 
        phone_number = request.data.get('phone_number') 
        if phone_number: 
            try: 
                user = Employee.objects.get(phone_number=phone_number) 
                return user 
            except Employee.DoesNotExist: 
                raise AuthenticationFailed('Пользователь с указанным номером телефона не найден') 
            return None
        if not phone_number:
            raise AuthenticationFailed('Для прохождения аутентификации укажите номер телефона в заголовке запроса')