from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import ReportResponse
from .models import Report
from .models import User
from .serializer import ReportResponseSerializer
from .serializer import ReportSerializer
from django.http import JsonResponse
from django.core import serializers


class ReportView(APIView):
    def get(self,request):
    
        userId = int(request.GET.get('id',None),10) if request.GET.get('id',None) != None else None
        offset = int(request.GET.get('offset',None),10) if request.GET.get('offset',None) != None else 0
        limit = int(request.GET.get('limit',None),10) if request.GET.get('limit',None) else None

        reports = Report.objects.all() if userId == None else Report.objects.all().filter(author_id=userId) | Report.objects.filter(supervisor__id=userId) | Report.objects.filter(reportresponse__author__id=userId)

        reports = reports[offset: limit+offset if limit != None else None]

        reportList = self.jsonReports(reports, userId)
    
        reportList = list(reportList)
        return JsonResponse(reportList,content_type="application/json", safe=False)

    def jsonReports(self, reports, userId):
        reportList = []
        for report in reports:
            report_dict = {}
            report_dict['id'] = report.id
            report_dict['author_id'] = report.author.id
            report_dict['first_name'] = report.author.first_name
            report_dict['last_name'] = report.author.last_name
            report_dict['email'] = report.author.email
            report_dict['message'] = report.message

            report_dict['supervisor'] = self.jsonSupervisors(report.supervisor.all())

            responses = ReportResponse.objects.filter(report = report) if userId == None else ReportResponse.objects.filter(author_id = userId) & ReportResponse.objects.filter(report = report)

            report_dict['responses'] = self.jsonResponses(responses)

            reportList.append(report_dict)
        return reportList

    def jsonSupervisors(self, supervisorList):
        supervisors = [] 
        for supervisor in supervisorList:
            supervisor_dict = {}
            supervisor_dict['id'] = supervisor.id
            supervisor_dict['first_name'] = supervisor.first_name
            supervisor_dict['last_name'] = supervisor.last_name
            supervisor_dict['email'] = supervisor.email
            supervisors.append(supervisor_dict)
        return supervisors

    def jsonResponses(self, responses):
        responseList = []
        for response in responses:
                response_dict = {}
                response_dict['id'] = response.id
                response_dict['message'] = response.message
                response_dict['author_first_name'] = response.author.first_name
                response_dict['author_last_name'] = response.author.last_name
                response_dict['email'] = response.author.email
                responseList.append(response_dict)
        return responseList      

    def post(self, request, format=None):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResponseView(APIView):
    def get(self, request):
        responses = ReportResponse.objects.all()
        responseList = []
        for response in responses:
            response_dict = {}
            response_dict['message'] = response.report.message
            response_dict['author_first_name'] = response.report.author.first_name
            response_dict['author_last_name'] = response.report.author.last_name
            response_dict['email'] = response.report.author.email
            supervisors = [] 

            for supervisor in response.report.supervisor.all():
                supervisor_dict = {}
                supervisor_dict['first_name'] = supervisor.first_name
                supervisor_dict['last_name'] = supervisor.last_name
                supervisor_dict['email'] = supervisor.email
                supervisors.append(supervisor_dict)

            response_dict['supervisors'] = supervisors
            response_dict['message'] = response.message

            responseList.append(response_dict)
        responseList = list(responseList)
        return JsonResponse(responseList,content_type="application/json", safe=False)

    def post(self, request, format=None):
        serializer = ReportResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        userList = []
        for user in users:
            user_dict = {}
            user_dict['id'] = user.id
            user_dict['first_name'] = user.first_name
            user_dict['last_name'] = user.last_name
            user_dict['email'] = user.email

            userList.append(user_dict)
        userList = list(userList)
        return JsonResponse(userList,content_type="application/json", safe=False)
