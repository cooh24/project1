from django.shortcuts import render
from dashboard.models import Wildfire
from .forms import WildfireDataForm

# Create your views here.
# def dashboard(request, dmgarea, tempavg):
#     ydata = Wildfire.objects.all(dmgarea=dmgarea)
#     xdata = Wildfire.objects.all(tempavg=tempavg)

#     form = WildfireDataForm()

#     context =
def dashboard(request):
    dataset = Wildfire.objects.all()

    form = WildfireDataForm()

    context = {'dataset':dataset}
    return render(request, 'dashboard/dashboard.html',context)