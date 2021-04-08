from django.shortcuts import render
from .forms import ImageForm
from .models import Image, Text

from .text_forms import TextForm

# from keras.applications.vgg16 import preprocess_input

from Pollen.predict_integrate import *
from Pollen.classify_integrate import *
import datetime, calendar
# Create your views here.
def home(request):
	return render(request, 'Pollen_templates/home.html', {})

def pollen_info(request):
	return render(request, 'Pollen_templates/pollen_info.html', {'title': 'Pollen-Info'})

def predict(request):
	if request.method == 'POST':
		form = TextForm(request.POST)
		if form.is_valid():
			form.save()
	form = TextForm()

	return render(request, 'Pollen_templates/predict.html', {'title': 'Predict', 'form': form})

def predictCity(request):
	day=datetime.datetime.today().strftime('%A')
	date1 = datetime.datetime.today().strftime ('%Y-%m-%d')
	NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
	date2= NextDay_Date.strftime('%Y %m %d')
	NextDay1_Date = datetime.datetime.today() + datetime.timedelta(days=2)
	date3 = NextDay1_Date.strftime('%Y %m %d')
	day_2=calendar.day_name[datetime.datetime.strptime(date2, '%Y %m %d').weekday()]
	day_3=calendar.day_name[datetime.datetime.strptime(date3, '%Y %m %d').weekday()]

	city=request.POST['selectCity']
	data=pred(city)
	ans=data[0]
	temp=[]
	for i in range(1,len(data)):
		temp.append(data[i])
	day1=ans[0]
	day2=ans[1]
	day3=ans[2]
	print(day1)
	context = {'city':city,'ans':ans,'temp':temp, 'title': 'Predict-City' ,'day1': day1,'day2': day2, 'day3': day3, 'day': day,'day_2': day_2, 'day_3': day_3, 'date1': date1, 'date2': date2, 'date3': date3}
	return render(request, 'Pollen_templates/predict.html', context)

def classify(request):
	
	form = ImageForm()
	img1 = Image.objects.get(id=28)

	return render(request, 'Pollen_templates/classify.html', {'title': 'Classify','form': form ,'img1': img1, 'des': 'Please select an image'})

def classifyTaxa(request):
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	form = ImageForm()
	img1 = Image.objects.latest('id')
	
	path = "."+img1.photo.url
	l=clf(path)
	ans = l[0]
	des = l[1]
	return render(request, 'Pollen_templates/classify.html', {'title': 'Classify-Taxa', 'form': form, 'taxa': ans, 'img1': img1, 'des': des})
