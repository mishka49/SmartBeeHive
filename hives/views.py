import mimetypes

import dateutil.utils

from .services import report_generator

import matplotlib.pyplot as plt
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
import os
from datetime import date


def view_home_page(request):
    return render(request, 'home.html')


def view_hive_page(request):
    hive_id = request.GET.get("hive_id")

    hives = Hive.objects.all()

    data_hives = DataHive.objects.filter(hive_id=hive_id)


    date = []
    weights = []
    temperature = []
    humidity = []
    for data in data_hives:
        date.append(data.date)
        weights.append(data.weight)
        humidity.append(data.humidity)
        temperature.append(data.temperature)

    return render(request, 'hive.html',
                  context={"data_hives": data_hives, "hives": hives, "dates": date, "weights": weights,
                           'temperature': temperature, 'humidity': humidity})


def view_report_page(request):
    hives = Hive.objects.all()
    hive_id = request.GET.get("hive_id")
    reports = ReportHive.objects.filter(hive_id=hive_id)

    for report in reports:
        report_file = report_generator.ReportHive(report.hive_id, report.aver_temp, report.aver_humid,
                                                  report.change_weight,
                                                  report.start_date, report.end_date)

        print(f"view: {report}")

    return render(request, 'report.html', context={'reports': reports, 'hives': hives})


def download_file(request):
    filename = request.GET.get("filename")
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    # Define the full file path
    filepath = BASE_DIR + '/download/reports/' + filename
    # Open the file for reading content
    path_r = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path_r, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response


def view_subscription_page(request):
    subscriptions = Subscription.objects.all()
    dates = dict()

    for sub in subscriptions:
        dates[sub.pk] = (sub.end_date - datetime.date.today()).days

    print(dates)

    return render(request, 'subscription.html', context={"subscriptions": subscriptions, "dates": dates})


def view_addsubscription_page(request):
    service_name = request.GET.get("service")

    services = Service.objects.all()
    hives = Hive.objects.all()

    return render(request, 'add_subscription.html',
                  context={"services": services, "hives": hives, "select_serv": service_name})

def view_delete_subscription(request):
    sub_id = request.GET.get("subscription_id")

    subscription = Subscription.objects.filter(pk=int(sub_id))[0]

    range = (subscription.end_date - datetime.date.today()).days

    return render(request, 'delete_subscription.html', context={"subscription": subscription, "range": range})


def delete_subscription(request):
    sub_id = request.GET.get("subscription_id")

    subscription = Subscription.objects.filter(pk=int(sub_id))
    subscription.delete()

    return HttpResponseRedirect("/subscription")

def get_form_subscription(request):
    if request.method == "POST":
        subscription = Subscription()
        if 'hive' in request.POST:
            subscription.hive_id = Hive.objects.filter(pk=int(request.POST['hive']))[0]
        if 'service' in request.POST:
            subscription.service = Service.objects.filter(name=request.POST['service'])[0]
            print(subscription.service)
        if 'range' in request.POST:
            subscription.end_date = datetime.date.today() + datetime.timedelta(days=int(request.POST['range']) * 30)

            subscription.coast = subscription.service.count_of_request * int(request.POST['range']) * 0.5

            subscription.save()

            return HttpResponseRedirect("/subscription")


def view__page(request):
    return render(request, 'add_subscription.html')


def view_service_page(request):
    services = Service.objects.all()
    count_service = []

    for index, service in enumerate(Service.objects.all()):
        count_service.append(len(Subscription.objects.filter(service=service.pk)))

    return render(request, 'service.html', context={'count_service': count_service, 'services': services})
