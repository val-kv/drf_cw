from drf_yasg.inspectors import SwaggerAutoSchema


class CustomAutoSchema(SwaggerAutoSchema):
    def get_operation(self, operation_keys=None):
        # Получаем информацию о методе и пути запроса
        operation = super().get_operation(operation_keys=None)

        # Проверяем, что пользователь авторизован
        if not getattr(operation, 'permissions', {}).get('get', {}).get('is_authenticated', True):
            operation['permissions'] = {
                'get': {
                    'is_authenticated': True,
                    'is_superuser': False,
                    'is_staff': False,
                    'is_admin': False,
                },
                'post': {
                    'is_authenticated': True,
                    'is_superuser': False,
                    'is_staff': False,
                    'is_admin': False,
                },
                'put': {
                    'is_authenticated': True,
                    'is_superuser': False,
                    'is_staff': False,
                    'is_admin': False,
                },
                'patch': {
                    'is_authenticated': True,
                    'is_superuser': False,
                    'is_staff': False,
                    'is_admin': False,
                },
                'delete': {
                    'is_authenticated': True,
                    'is_superuser': False,
                    'is_staff': False,
                    'is_admin': False,
                },
            }

        return operation
