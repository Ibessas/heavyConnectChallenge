from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import ReportResponse
from .models import Report
from .serializer import ReportResponseSerializer
from .serializer import ReportSerializer
from django.http import JsonResponse

class ReportView(APIView):
    def get(self,request):
        reports = Report.objects.all()

        userId = int(request.GET.get('id',None),10) if request.GET.get('id',None) != None else -1
        offset = int(request.GET.get('offset',None),10)+1 if request.GET.get('offset',None) != None else -1
        limit = int(request.GET.get('limit',None),10) if request.GET.get('limit',None) else reports.count()

        reportList = []
        for report in reports:
            add = False

            if report.author.id == userId: add = True
            report_dict = {}
            report_dict['id'] = report.id
            report_dict['first_name'] = report.author.first_name
            report_dict['last_name'] = report.author.last_name
            report_dict['email'] = report.author.email
            
            supervisores = [] 
            for supervisor in report.supervisor.all():
                if supervisor.id == userId: add = True
                supervisor_dict = {}
                supervisor_dict['first_name'] = supervisor.first_name
                supervisor_dict['last_name'] = supervisor.last_name
                supervisor_dict['email'] = supervisor.email
                supervisores.append(supervisor_dict)
            report_dict['supervisor'] = supervisores

            responses = ReportResponse.objects.all()
            responseList = []
            for response in responses:
                if response.report == report:
                    if response.author.id == userId: add = True
                    response_dict = {}
                    response_dict['message'] = response.message
                    response_dict['author_first_name'] = response.author.first_name
                    response_dict['author_last_name'] = response.author.last_name
                    response_dict['email'] = response.author.email
                    responseList.append(response_dict)
            report_dict['responses'] = responseList
            
            if offset > 0:     
                offset = offset - 1
            else:
                if limit > 0:
                    if add or userId == -1:
                        reportList.append(report_dict)
                    limit = limit -1
                else: break
            

        reportList = list(reportList)
        return JsonResponse(reportList,content_type="application/json", safe=False)

        
         

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


