from django.shortcuts import render

# Create your views here.
def index(request):
    datas = {

    }
    return render(request,'pages/index.html',datas)

def blog(request):
    datas = {

    }
    return render(request,'pages/blog.html',datas)

def feature(request):
    datas = {

    }
    return render(request,'pages/feature.html',datas)

def elements(request):
    datas = {

    }
    return render(request,'pages/elements.html',datas)

def pricing(request):
    datas = {

    }
    return render(request,'pages/pricing.html',datas)

def services(request):
    datas = {

    }
    return render(request,'pages/services.html',datas)

def single_blog(request):
    datas = {

    }
    return render(request,'pages/single-blog.html',datas)




