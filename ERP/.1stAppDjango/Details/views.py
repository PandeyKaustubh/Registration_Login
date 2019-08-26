from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from Details.models import details,dataTable

def myfunc(request):
	if request.method == 'POST' :
		obj=dataTable.objects.all()
		data = json.loads(request.body)
		for x in obj :
			if(x.Username==data['Username'] and x.Password==data['Password']) :
				query4=dataTable.objects.filter(Username=data['Username']).values('link')
				query5=details.objects.filter(id=query4[0]['link']).values('Fname','Lname','Mobile_no','Email','School','HighestQualification','Gender','City','State','PinCode','Address')
				return JsonResponse(list(query5),safe=False)
			elif(x.Username==data['Username'] and x.Password!=data['Password']):
				data4={"Status":"wrongpass"}
				return JsonResponse(data4)
			
			

		try:
			query = details.objects.create(Fname=data['Fname'],Lname=data['Lname'],City=data['City'],School=data['School'],HighestQualification=data['HighestQualification'] ,State=data['State'],PinCode=data['PinCode'],Mobile_no=data['Mobile_no'],Email=data['Email'],Address=data['Address'],Gender=data['Gender'])
			query3=dataTable.objects.create(Username=data['Username'],Password=data['Password'], link=query)
			if(query.Fname==data['Fname']):
				data5={"Status":"OK"}
				return JsonResponse(data5)
		except:
			q={"Status":"invalid"}
			return JsonResponse(q)




	elif request.method == 'GET' :
		 # Fname= request.GET.['Fname']
		 # Lname= request.GET.['Lname']
		 # Mobile_no= request.GET['Mobile_no']
		 # Email= request.GET['Email']
		 # Qualified= request.GET['Qualified']
		 # Status=request.GET['Status']
		 # query = details.objects.create(Fname=Fname,Lname=Lname,Mobile_no=Mobile_no,Email=Email,Qualified=Qualified,Status)
		 # return HttpResponse("GET Chal Gya")
		 obj=details.objects.all()
		 # obj=details.objects.all().values('Fname','Lname','Mobile_no','Email','Qualified','Status')
		 # return JsonResponse(list(obj),safe=False)
		 data=[]
		 data1={}
		 for x in obj:
		 	data1={"Fname":x.Fname,"Lname":x.Lname,"City":x.City,"School":x.School,"HighestQualification":x.HighestQualification,"State":x.State,"PinCode":x.PinCode,"Mobile_no":x.Mobile_no,"Email":x.Email,"Address":x.Address,"Gender":x.Gender}
		 	# print(data1)
		 	data.append(data1)


		 return JsonResponse(data,safe=False)
		


	elif request.method == 'PUT' :
		id1 = json.loads(request.body)
		query = details.objects.filter(id=id1['id']).update(Fname="Kaustubh Pandey",Mobile_no='100100')
		return HttpResponse("PUT Chal Gya")

	elif request.method == 'DELETE' :
		id1 = json.loads(request.body)
		query = details.objects.filter(id=id1['id']).delete()
		return HttpResponse("Delete Chal Gya")