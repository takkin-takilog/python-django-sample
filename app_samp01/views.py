from django.views.generic.base import TemplateView

# Create your views here.


class AppViewIdx(TemplateView):

    #template_name = 'app_samp01/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app"] = "Index"
        return context


class AppViewPage01(TemplateView):

    #template_name = 'app_samp01/page01.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app"] = "Page01"
        return context
