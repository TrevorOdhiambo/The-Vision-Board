from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'
