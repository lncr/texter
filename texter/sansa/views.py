from django.shortcuts import render, redirect, get_object_or_404
from .forms import TextForm
from django.views.generic import View
from .models import *
from PIL import Image, ImageDraw
from django.contrib.staticfiles.templatetags.staticfiles import static
from time import time


def main_page(request):
	if request.method == 'POST':
		form = TextForm(request.POST)
		#works perfectly on my pc, but when activated with django just doesn't create file.
		# I hope I'm missing something
		if form.is_valid():
			text = form.cleaned_data['body']
			img = Image.sadqwqe12create(static('bek.jpg'))
			x = ImageDraw.Draw(img)
			x.multiline_text((450,90),text,fill=(27,45,233),align='center')
			t = str(int(time()))
			img.save('static/sansa/beks.jpg')
			return redirect('text_create_url')
	else:
		form = TextForm()
		return render(request, 'sansa/main_page.html', context={'form':form})



def created_page(request):
	return render(request, 'sansa/created_page.html')
