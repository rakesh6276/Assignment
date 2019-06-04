import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import ExcelUploadForm
from .serializers import PitchesSerializerget, PitchesSerializer
from .models import Pitches

# function to read excel file from dict_function
def excel_handle(request):
    if request.method == 'POST':
        book = request.FILES['excel_file']
        df = pd.read_excel(book)
        data = dict_format(df.to_dict())
        for obj in data:
            data = Pitches.objects.create(ba=obj['ba'],
                                          sku_code=obj['sku_code'],
                                          name=obj['name'],
                                          description=obj['description'],
                                          ean=obj['ean'],
                                          manufacturer=obj['manufacturer'],
                                          brand=obj['brand'],
                                          flavor=obj['flavor'],
                                          package=obj['package'],
                                          size=obj['size'],
                                          height=obj['height'],
                                          width=obj['width'],
                                          depth=obj['depth'])
        return HttpResponse("File Uploaded Successfully")
    return render(request, 'index.html', {'form': ExcelUploadForm})

#converting files from dictonary to list
def dict_format(dictionary):
    DataList=[]
    for i in range(len(dictionary[list(dictionary.keys())[0]])):
        temp_dict={}
        for data in dictionary: temp_dict[data]=dictionary[data][i]
        DataList.append(temp_dict)
    return DataList

#function to filter name, brand, sku_code and brand
@api_view(['GET'])
def data_view(request):
    name = request.data["name"]
    brand = request.data["brand"]
    sku_code = request.data["sku_code"]
    package = request.data["package"]
    serialized_queryset = PitchesSerializerget(Pitches.objects.filter(name=name, brand=brand, sku_code=sku_code, package=package).all(), many=True)
    return Response({"status":"success","message":"data is fetched successfully","data":serialized_queryset.data})

#class to list and create prodcuts
class prodcutsListCreate(generics.ListCreateAPIView):
    queryset = Pitches.objects.all()
    serializer_class = PitchesSerializer
    #print(serializer_class)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PitchesSerializer(queryset, many=True)
        return Response(serializer.data)
