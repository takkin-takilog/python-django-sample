from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.


class AppViewIdx(View):

    template_name = 'app_samp01/index.html'

    myapp_data = {
        'app': 'Index'
    }

    def get(self, request):
        return render(request, self.template_name, self.myapp_data)


class AppViewPage01(View):

    template_name = 'app_samp01/page01.html'

    myapp_data = {
        'app': 'Page01'
    }

    def get(self, request):
        return render(request, self.template_name, self.myapp_data)
