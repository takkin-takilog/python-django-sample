from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.


class AppView(View):

    template_name = 'app_samp01/index.html'

    myapp_data = {
        'app': 'Django'
    }

    def get(self, request):
        return render(request, self.template_name, self.myapp_data)
