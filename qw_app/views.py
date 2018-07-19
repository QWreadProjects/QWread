from django.shortcuts import render
from qw_app.models import *
from django.db.models import Count, Min, Sum, Max, Avg


# Create your views here.
def goHome(request):
    div1s = Fition.objects.filter().order_by("-click")[:4]
    div2s = Fition.objects.filter().order_by("click")[:6]
    div3s = Fition.objects.filter(fictionType_id=13).order_by("-click")[:13]
    div31s = div3s.first()
    div32s = div3s[1:]
    div4s = Fition.objects.filter(fictionType_id=16).order_by("-click")[:13]
    div41s = div4s.first()
    div42s = div4s[1:]
    div5s = Fition.objects.filter(fictionType_id=15).order_by("-click")[:13]
    div51s = div5s.first()
    div52s = div5s[1:]
    div6s = Fition.objects.filter(fictionType_id=14).order_by("-click")[:13]
    div61s = div6s.first()
    div62s = div6s[1:]
    div7s = Fition.objects.filter(fictionType_id=17).order_by("-click")[:13]
    div71s = div7s.first()
    div72s = div7s[1:]
    div8s = Fition.objects.filter(fictionType_id=19).order_by("-click")[:13]
    div81s = div8s.first()
    div82s = div8s[1:]
    div9s = Chapter.objects.order_by("updata_time")[:25]
    div10s = Fition.objects.order_by("put_time")[:25]
    return render(request, "",
                  {"div1s": div1s,
                   "div2s": div2s,
                   "div31s": div31s,
                   "div32s": div32s,
                   "div41s": div41s,
                   "div42s": div42s,
                   "div51s": div51s,
                   "div52s": div52s,
                   "div61s": div61s,
                   "div62s": div62s,
                   "div71s": div71s,
                   "div72s": div72s,
                   "div81s": div81s,
                   "div82s": div82s,
                   "div9s": div9s,
                   "div10s": div10s,
                   }
                  )
def xuanhuan(request):
    model1 = Fition.objects.filter(fictionType_id=13).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='玄幻小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=13).order_by("-click")[6:56]
    return render(request,"",
                  {"model1":model1,
                   "model2":model2,
                   "model3":model3})

def xiuzhen(request):
    model1 = Fition.objects.filter(fictionType_id=16).order_by("-click")[:6]
    model2 = Chapter.objects.order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=16).order_by("-click")[6:56]
    return render(request,"",
                  {"model1":model1,
                   "model2":model2,
                   "model3":model3})


def dushi(request):
    model1 = Fition.objects.filter(fictionType_id=15).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='都市小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=15).order_by("-click")[6:56]
    return render(request,"",
                  {"model1":model1,
                   "model2":model2,
                   "model3":model3})


def lishi(request):
    model1 = Fition.objects.filter(fictionType_id=14).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='军史小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=14).order_by("-click")[6:56]
    return render(request,"",
                  {"model1":model1,
                   "model2":model2,
                   "model3":model3})



def wangyou(request):
    model1 = Fition.objects.filter(fictionType_id=17).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='网游小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=17).order_by("-click")[6:56]
    return render(request,"",
                  {"model1":model1,
                   "model2":model2,
                   "model3":model3})


def kehuan(request):
    model1 = Fition.objects.filter(fictionType_id=19).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='科幻小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=19).order_by("-click")[6:56]
    return render(request,"",
                  {"model1":model1,
                   "model2":model2,
                   "model3":model3})



def kongbu(request):
    model1 = Fition.objects.filter(fictionType_id=21).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='灵异小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=21).order_by("-click")[6:56]
    return render(request,"",
                  {"model1":model1,
                   "model2":model2,
                   "model3":model3})


def quanben(request):
    model1 = Fition.objects.filter(fictionType_id=20).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='其他小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=20).order_by("-click")[6:56]
    return render(request,"",
                  {"model1":model1,
                   "model2":model2,
                   "model3":model3})
