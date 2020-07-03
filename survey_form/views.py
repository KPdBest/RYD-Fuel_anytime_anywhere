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
        users_data=list(SurveyData.object.filter(id=user_id).values())
        if (len(users_data)>0):
            data={'Data':users_data,'responseType': 'success', 'messageType': 'success'}
            Status=status.HTTP_200_OK
        else:
            data={'Data':users_data,'responseType': 'success', 'messageType': 'No Data Found !'}
            Status=status.HTTP_202_ACCEPTED

    elif request.method == 'POST':
        data = json.loads(request.body)
        name=request.data['name']
        date=request.data['date']
        organisation=request.data['organisation']
        designation=request.data['designation']
        city=request.data['city']
        age=request.data['age']
        remark=request.data['remark']

        qry = SurveyData.objects.create(name=name,city=city,designation=designation,organisation=organisation,age=age,date=date,remark=remark)
        data={'responseType': 'success', 'messageType': 'Successfully Inserted'}
        Status=status.HTTP_201_CREATED

    elif request.method == 'PUT':
        ###### Let's Assume the User is updating these few fields( Designation , City , Age , Date ) in Survey Form #####################
        user_id = request.session.get('userid')   ###Fetch UserID from the session and update the respective data #####
        designation=request.data['designation']
        date=request.data['date']
        city=request.data['city']
        age=request.data['age']

        qry=SurveyData.objects.filter(id=user_id).update(city=city,designation=designation,age=age,date=date)
        data={'responseType': 'success', 'messageType': 'Successfully Inserted'}
        Status=status.HTTP_201_CREATED

    return Response(data,status=Status)
