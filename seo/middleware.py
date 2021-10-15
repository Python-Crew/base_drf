from seo.models import Page
from seo.serializers import CombineSerializer

from django.shortcuts import redirect


class IncludeSEOInfo:
    def __init__(self, get_response):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request, *args, **kwargs):

        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        request_url = request.get_full_path()
        page = Page.objects.filter(url=request_url)
        if len(page) > 0:
            if page[0].operation == 'redirect':
                return redirect(
                    page[0].redirect_to,
                    status=page[0].redirect_status
                )

    def process_exception(self, request, response):
        return response

    def process_template_response(self, request, response):
        request_url = request.get_full_path()
        page = Page.objects.filter(url=request_url)
        if len(page) > 0:
            if page[0].operation == "seo_info":
                serializer = CombineSerializer(page[0])
                response.data.setdefault('seo', serializer.data)
        return response
