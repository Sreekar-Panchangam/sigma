from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

class IndexView(APIView):
    def get(self, request):
        return render(request, "index.html")

def favicon(request):
    return HttpResponse(status=204)
