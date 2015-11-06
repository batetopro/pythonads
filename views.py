from django.http import HttpResponse, HttpResponseNotFound
from utils import list_folder, download_ad, serve_file, check_ad
from django.template import Context, loader
import time

ad_path = './data/ads'

def index(request):
    ads = ','.join(list_folder(ad_path))
    t = loader.get_template('index.html')
    c = Context({'ads': ads,})
    return HttpResponse(t.render(c))

def preview(request, path):
    data = serve_file(path, ad_path)
    if not data:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return HttpResponse(data)

def check(request, path):
    check = check_ad(path)
    if check:
        return HttpResponse('ok')
    else:
        return HttpResponse('false')

def download(request):
    url = request.GET.get('url')
    if not url:
        return HttpResponse('false')

    if not download_ad(url, ad_path):
        return HttpResponse('false')

    return HttpResponse("ok")