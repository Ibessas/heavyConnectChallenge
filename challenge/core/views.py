from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ReportResponse
from .models import Report
from .serializer import ReportResponseSerializer 
from .serializer import ReportSerializer 
from django.http import JsonResponse

class ReportList(APIView):
    def get(self,request):
        reports = Report.objects.all()
        reportList = []
        for report in reports:
            report_dict = {}
            report_dict['first_name'] = report.author.first_name
            report_dict['last_name'] = report.author.last_name
            report_dict['email'] = report.author.email
            supervisores = [] 

            for supervisor in report.supervisor.all():
                supervisor_dict = {}
                supervisor_dict['first_name'] = supervisor.first_name
                supervisor_dict['last_name'] = supervisor.last_name
                supervisor_dict['email'] = supervisor.email
                supervisores.append(supervisor_dict)

            report_dict['supervisor'] = supervisores
            
            reportList.append(report_dict)

        reportList = list(reportList)
        return JsonResponse(reportList,content_type="application/json", safe=False)
         

    def post(self, request, format=None):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ResponseList(APIView):
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





##class UserViewSet(viewsets.ModelViewSet):
#   queryset = User.objects.all()
#    serializer_class = UserSerializer

#class ReportViewSet(viewsets.ModelViewSet):
#    queryset = Report.objects.all()
#    serializer_class = ReportSerializer

#class ReportResponseViewSet(viewsets.ModelViewSet):
#    queryset = ReportResponse.objects.all()
#    serializer_class = ReportResponseSerializer