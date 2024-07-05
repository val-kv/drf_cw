from drf_yasg.inspectors import SwaggerAutoSchema


class CustomAutoSchema(SwaggerAutoSchema):
    def get_link(self, path, method, base_url, components, request):
        if path == '/custom/endpoint/':
            return None
        return super().get_link(path, method, base_url, components, request)
