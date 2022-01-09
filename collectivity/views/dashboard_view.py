from django.views import View
from django.shortcuts import render

from collectivity.models.collectivity import Collectivity

from information.forms.navbar_search_form import NavbarSearchForm


class DashboardView(View):
    """Dashboard view  class.
    """

    def __init__(self):
        super().__init__()
        self.render = 'collectivity/dashboard.html'
        self.context = {
            'navbar_search_form': NavbarSearchForm(),
        }

    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.render, self.context)