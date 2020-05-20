from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views import generic
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

import requests
import logging
import json

logger = logging.getLogger(__name__)

class Emp_api_index(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'emp/index.html'

        r = requests.get('http://emp_api:5001/hello')
        rr = {
            "result":r.text
        }
        
        return render(request, template_name, rr)


class Emp_api_testFox(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'emp/testFox.html'

        r = requests.get('http://emp_api:5001/hello')
        rr = {
            "result": r.text
        }

        return render(request, template_name, rr)

@csrf_exempt
def insert_ajax(request):

    param = json.loads(request.POST['param'])

    datas = {
        'email' : param['email'],
        'password' : param['password'],
        'addr' : param['state'] + ' ' + param['city'] + ' ' + param['addr'] + ' ' + param['addrDetl'] + param['zip'],
        'sex' : param['chk']
    }
    logger.info('request.post : ' + request.POST['param'])
    logger.info(datas)
    #r = requests.post('http://emp_api:5000/save',data=json.dumps(datas))
    r = requests.post('http://emp_api:5001/save', data=datas)
    logger.info(r)
    logger.info(r.text)
    logger.info(r.json())
    return JsonResponse(r.json())

@csrf_exempt
def update_ajax(request):

    param = json.loads(request.POST['param'])
    logger.info(param)
    # datas = {
    #     'email' : param['email'],
    #     'password' : param['password'],
    #     'addr' : param['addr'],
    #     'sex' : param['sex']
    # }
    logger.info('request.post : ' + request.POST['param'])
    # logger.info(datas)
    r = requests.post('http://emp_api:5001/update', json=param)
    logger.info(r)
    logger.info(r.text)
    logger.info(r.json())
    return JsonResponse(r.json())

def search_ajax(request):

    param = json.loads(request.GET['param'])

    datas = {
        'email' : param['searchemail']
    }
    logger.info(datas)
    r = requests.get('http://emp_api:5001/search', params=datas)
    logger.info(r)
    logger.info(r.text)
    logger.info("----------------")
    logger.info(r.json())
    logger.info(json.loads(r.text))
    # return JsonResponse(r.json())
    return JsonResponse(r.json(), safe=False)


class Emp_api_signUpForm(generic.TemplateView): #app.py내 Class 호출.
    def get(self, request, *args, **kwargs):

        logger.info("Views Start")      #front에 찍힘.

        template_name = 'emp/signUpForm.html'

        r = requests.get('http://emp_api:5001/SignForm')
        rr = {
            "result": r.text
        }

        logger.info("Views End")

        return render(request, template_name, rr)