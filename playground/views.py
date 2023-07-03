from django.shortcuts import render
import requests
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import logging

logger=logging.getLogger(__name__)


class HelloView(APIView):
    def get(self,request):
        
        response= requests.get('https://httpbin.org/delay/2')
        data=response.json()
        return render(request, 'hello.html', {'name':'Oogway'})
