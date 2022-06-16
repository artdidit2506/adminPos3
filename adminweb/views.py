from django.shortcuts import render
from django.apps import apps

# Create your views here.
def index(request):
    return render(request, 'adminweb/index.html')

def users(request):
    return render(request, 'adminweb/users-profile.html')

def pagesFaq(request):
    return render(request, 'adminweb/pages-faq.html')

def pagesContact(request):
    return render(request, 'adminweb/pages-contact.html')

def pagesRegister(request):
    return render(request, 'adminweb/pages-register.html')

def pagesLogin(request):
    return render(request, 'adminweb/pages-login.html')

def pagesError(request):
    return render(request, 'adminweb/pages-error-404.html')

def pagesBlank(request):
    return render(request, 'adminweb/pages-blank.html')

def componentsAlerts(request):
    return render(request, 'adminweb/components/alerts.html')

def componentsAccordiants(request):
    return render(request, 'adminweb/components/accordiants.html')

def componentsBadges(request):
    return render(request, 'adminweb/components/badges.html')

def componentsBreadcrumbs(request):
    return render(request, 'adminweb/components/breadcrumbs.html')

def componentsButtons(request):
    return render(request, 'adminweb/components/buttons.html')

def componentsCards(request):
    return render(request, 'adminweb/components/cards.html')

def componentsCarousel(request):
    return render(request, 'adminweb/components/carousel.html')

def componentsList(request):
    return render(request, 'adminweb/components/list-group.html')

def componentsModal(request):
    return render(request, 'adminweb/components/modal.html')

def componentsTabs(request):
    return render(request, 'adminweb/components/tabs.html')

def componentsPagination(request):
    return render(request, 'adminweb/components/pagination.html')

def componentsProgress(request):
    return render(request, 'adminweb/components/progress.html')

def componentsSpinners(request):
    return render(request, 'adminweb/components/spinners.html')

def componentsTooltips(request):
    return render(request, 'adminweb/components/tooltips.html')


# Form
def formElements(request):
    return render(request, 'adminweb/forms/elements.html')

def formLayouts(request):
    return render(request, 'adminweb/forms/layouts.html')

def formEditors(request):
    return render(request, 'adminweb/forms/editors.html')

def formValidation(request):
    return render(request, 'adminweb/forms/validation.html')

# Tables
def formGeneral(request):
    return render(request, 'adminweb/tables/tables-general.html')

def formData(request):
    return render(request, 'adminweb/tables/tables-data.html')

# Charts

def formChartjs(request):
    return render(request, 'adminweb/charts/charts-chartjs.html')

def formApexcharts(request):
    return render(request, 'adminweb/charts/charts-apexcharts.html')

def formEcharts(request):
    return render(request, 'adminweb/charts/charts-echarts.html')

# Icons

def formIconsbootstrap(request):
    return render(request, 'adminweb/icons/icons-bootstrap.html')

def formIconsremix(request):
    return render(request, 'adminweb/icons/icons-remix.html')

def formIconsboxicon(request):
    return render(request, 'adminweb/icons/icons-boxicons.html')