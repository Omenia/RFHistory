# from django.shortcuts import render
from django.http import HttpResponse
from ServerApp.forms import UploadFileForm
from ServerApp.upload_file_handler import handle_uploaded_file
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the RFHistory index.")


@csrf_exempt
def upload_output(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse(status=200)
    return HttpResponse(status=400)
