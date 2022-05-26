from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import CartoonEntry
from django.core import serializers
from .forms import CartoonForm

# Create your views here.
def enter_cartoon_data(request):
    submitted = False
    if request.method == 'POST':
        # print(request.POST)
        form = CartoonForm(request.POST)
        if form.is_valid():
            print("VALID")
            form.save()
            return HttpResponseRedirect("/FormTest/enterData")
        print("INVALID")

    form = CartoonForm()

    context = {"form": form}
    return render(request, "enterData.html", context)
        # cartoon_name = request.POST['cartoonName']
        # episode_count = request.POST['episodeCount']
        # date_finished = request.POST['dateFinished']
        # rating = request.POST['rating']
        # print(f'{cartoon_name=}, {episode_count=}, {date_finished=}, {rating=}')
        # obj = CartoonEntry()
        # obj.cartoon_name = cartoon_name
        # obj.episode_count = episode_count
        # obj.date_finished = date_finished
        # obj.rating = rating
        # obj.save()
    #     return HttpResponseRedirect("/FormTest/enterData")
    
    # # Grab entries and save to dict
    # data = serializers.serialize("python", CartoonEntry.objects.all())
    # context = {
    #     'data': data
    # }
    # return render(request, 'enterData.html', context)

def show_cartoon_list(request):
    if request.method == "GET":
        data = serializers.serialize("python", CartoonEntry.objects.all())
        context = {
            'data': data
        }
    return render(request, "viewData.html", context)