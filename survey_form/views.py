from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
import json
from survey_form.models import SurveyData


def user_data(request):
    if request.method == 'GET':
        user_id = request.session.get('userid')  ###Fetch UserID from the session and show the respective data #####
        user_id=1  ##### Static as sessions is not created ########
        users_data=list(SurveyData.objects.filter(id=user_id).values())
        if (len(users_data)>0):
            data={'Data':users_data,'responseType': 'success', 'messageType': 'success'}
            Status=status.HTTP_200_OK
        else:
            data={'Data':users_data,'responseType': 'success', 'messageType': 'No Data Found !'}
            Status=status.HTTP_202_ACCEPTED

    elif request.method == 'POST':
        data = json.loads(request.body)
        name=data['name']
        date=data['date']
        organisation=data['organisation']
        designation=data['designation']
        city=data['city']
        age=data['age']
        remark=data['remark']

        qry = SurveyData.objects.create(name=name,city=city,designation=designation,organisation=organisation,age=age,date=date,remark=remark)
        data={'responseType': 'success', 'messageType': 'Successfully Inserted'}
        Status=status.HTTP_201_CREATED

    elif request.method == 'PUT':
        ###### Let's Assume the User is updating these few fields( Designation , City , Age , Date ) in Survey Form #####################
        user_id = request.session.get('userid')   ###Fetch UserID from the session and update the respective data #####
        user_id =1
        data = json.loads(request.body)
        designation=data['designation']
        date=data['date']
        city=data['city']
        age=data['age']

        qry=SurveyData.objects.filter(id=user_id).update(city=city,designation=designation,age=age,date=date)
        data={'responseType': 'success', 'messageType': 'Successfully Updated'}
        Status=status.HTTP_201_CREATED

    return JsonResponse(data,status=Status)
