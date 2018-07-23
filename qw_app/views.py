from django.shortcuts import render, redirect

from qw_app.models import *


def goHome(request):
    div1s = Fition.objects.filter().order_by("-click")[:4]
    div2s = Fition.objects.filter().order_by("click")[:11]
    div3s = Fition.objects.filter(fictionType_id=1).order_by("-click")[:13]
    div31s = div3s.first()
    div32s = div3s[1:]
    div4s = Fition.objects.filter(fictionType_id=4).order_by("-click")[:13]
    div41s = div4s.first()
    div42s = div4s[1:]
    div5s = Fition.objects.filter(fictionType_id=2).order_by("-click")[:13]
    div51s = div5s.first()
    div52s = div5s[1:]
    div6s = Fition.objects.filter(fictionType_id=3).order_by("-click")[:13]
    div61s = div6s.first()
    div62s = div6s[1:]
    div7s = Fition.objects.filter(fictionType_id=5).order_by("-click")[:13]
    div71s = div7s.first()
    div72s = div7s[1:]
    div8s = Fition.objects.filter(fictionType_id=6).order_by("-click")[:13]
    div81s = div8s.first()
    div82s = div8s[1:]
    div9s = Fition.objects.all()[:25]
    div10s = Fition.objects.order_by("put_time")[:25]
    return render(request, "apps/index.html",
                  {"div1s": div1s, "div2s": div2s,
                   "div31s": div31s, "div32s": div32s,
                   "div41s": div41s, "div42s": div42s,
                   "div51s": div51s, "div52s": div52s,
                   "div61s": div61s, "div62s": div62s,
                   "div71s": div71s, "div72s": div72s,
                   "div81s": div81s, "div82s": div82s,
                   "div9s": div9s, "div10s": div10s,
                   })


def xuanhuan(request):
    model1 = Fition.objects.filter(fictionType_id=1).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='玄幻小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=1).order_by("-click")[6:56]
    return render(request, "apps/nav.html",
                  {"model1": model1,
                   "model2": model2,
                   "model3": model3,
                   'name': '玄幻'})


def xiuzhen(request):
    model1 = Fition.objects.filter(fictionType_id=4).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='仙侠')
    model3 = Fition.objects.filter(fictionType_id=4).order_by("-click")[6:56]
    return render(request, "apps/nav.html",
                  {"model1": model1,
                   "model2": model2,
                   "model3": model3,
                   'name': '修真'})


def dushi(request):
    model1 = Fition.objects.filter(fictionType_id=2).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='都市小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=2).order_by("-click")[6:56]
    return render(request, "apps/nav.html",
                  {"model1": model1,
                   "model2": model2,
                   "model3": model3,
                   'name': '都市'})


def lishi(request):
    model1 = Fition.objects.filter(fictionType_id=3).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='军史小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=3).order_by("-click")[6:56]
    return render(request, "apps/nav.html",
                  {"model1": model1,
                   "model2": model2,
                   "model3": model3,
                   'name': '历史'})


def wangyou(request):
    model1 = Fition.objects.filter(fictionType_id=5).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='网游小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=5).order_by("-click")[6:56]
    return render(request, "apps/nav.html",
                  {"model1": model1,
                   "model2": model2,
                   "model3": model3,
                   'name': '网游'})


def kehuan(request):
    model1 = Fition.objects.filter(fictionType_id=6).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='科幻小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=6).order_by("-click")[6:56]
    return render(request, "apps/nav.html",
                  {"model1": model1,
                   "model2": model2,
                   "model3": model3,
                   'name': '科幻'})


def kongbu(request):
    model1 = Fition.objects.filter(fictionType_id=7).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='言情小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=7).order_by("-click")[6:56]
    return render(request, "apps/nav.html",
                  {"model1": model1,
                   "model2": model2,
                   "model3": model3,
                   'name': '言情'})


def quanben(request):
    model1 = Fition.objects.filter(fictionType_id=8).order_by("-click")[:6]
    model2 = Chapter.objects.filter(fiction__fictionType__name='其他小说').order_by("updata_time")[0:50]
    model3 = Fition.objects.filter(fictionType_id=8).order_by("-click")[6:56]
    return render(request, "apps/nav.html",
                  {"model1": model1,
                   "model2": model2,
                   "model3": model3,
                   'name': '全本'})


def shuji(request):
    book_id = request.GET.get("id")
    book = Fition.objects.filter(id=book_id)
    chapters = Chapter.objects.filter(fiction_id=book_id)
    chapter = chapters.last()
    return render(request, "apps/detail.html",
                  {'chapters': chapters, 'book': book, 'chapter': chapter})


def content(request):
    content_id = request.GET.get("id")
    book_content = Chapter.objects.get(id=content_id)
    contents = Chapter.objects.get(id=content_id).content
    return render(request, 'apps/content.html',
                  {'contents': contents, 'book_content': book_content})


def search(request):
    searchkey = request.GET.get('searchkey')
    if not searchkey:
        error_msg = "请输入搜索关字"
        return render(request, 'apps/base.html', {'error_msg': error_msg})

    try:
        fiction_list = Fition.objects.filter(name=searchkey)
        return redirect('/qwread/shuji/?id={}'.format(fiction_list.first().id))
    except:
        error_msg = "暂时没有您搜索的《{}》资源".format(searchkey)
        return render(request, 'apps/base.html', {'error_msg': error_msg})
