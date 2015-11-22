from django.http import HttpResponse, HttpResponseNotFound
from utils import list_folder, download_ad, serve_file, check_ad, file_exists
from django.template import Context, loader
import time

ad_path = './data/ads'

def index(request):
    ads = ','.join(list_folder(ad_path))
    t = loader.get_template('index.html')
    c = Context({'ads': ads,})
    return HttpResponse(t.render(c))

def checker(request, path):
    if not file_exists(path, ad_path):
        return HttpResponseNotFound('<h1>Page not found</h1>')

    #checkers = ['now', 'true', 'rand', 'rand', 'false']
    checkers = ['now', 'true', 'rand', 'rand', 'rand']


    t = loader.get_template('checker.html')
    c = Context({
        'name': path,
        'checkers': ','.join(checkers),
    })
    return HttpResponse(t.render(c))

def preview(request, path):
    if not file_exists(path, ad_path):
        return HttpResponseNotFound('<h1>Page not found</h1>')
    return HttpResponse(serve_file(path, ad_path))

def check(request, checker, path):
    check = check_ad(checker, path)
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