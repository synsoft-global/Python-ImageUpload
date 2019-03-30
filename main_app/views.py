from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image
# Create your views here.

def index(request):
  if request.method == 'POST' and request.FILES['myfile']:
    myfile = request.FILES['myfile']
    # Testing the file if it is an image
    try:
      Image.open(myfile)
    except IOError:
      return render(request, 'main_app/index.html',{'error': 'Not a valid Image'}, status=400)
    # Initiating the filestorage to save file
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    # Redirecting the file after image upload
    return render(request, 'main_app/image.html', {'uploaded_file_url': uploaded_file_url})
  return render(request, 'main_app/index.html',{'error': ''})