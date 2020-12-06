from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
import io
from django.http.response import HttpResponse
import xlsxwriter
from .ExcelFunctions import generate_empty_xlsx
import json

class ResultView(viewsets.ModelViewSet):
  serializer_class = ResultSerializer
  queryset = Result.objects.all()


class DetailedMetricView(viewsets.ModelViewSet):
  serializer_class = DetailedMetricSerializer
  queryset = DetailedMetric.objects.all()


class MetricView(viewsets.ModelViewSet):
  serializer_class = MetricSerializer
  queryset = Metric.objects.all()


class SampleView(viewsets.ModelViewSet):
  serializer_class = SampleSerializer
  queryset = Sample.objects.all()


class ExternalFactorView(viewsets.ModelViewSet):
  serializer_class = ExternalFactorSerializer
  queryset = ExternalFactor.objects.all()


class SupplementView(viewsets.ModelViewSet):
  serializer_class = SupplementSerializer
  queryset = Supplement.objects.all()


class SupplementBaseView(viewsets.ModelViewSet):
  serializer_class = SupplementBaseSerializer
  queryset = SupplementBase.objects.all()


class ProductView(viewsets.ModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()


class RecipeView(viewsets.ModelViewSet):
  serializer_class = RecipeSerializer
  queryset = Recipe.objects.all()


class BasicIngredientView(viewsets.ModelViewSet):
  serializer_class = BasicIngredientSerializer
  queryset = BasicIngredient.objects.all()


class BasicIngredientBaseView(viewsets.ModelViewSet):
  serializer_class = BasicIngredientBaseSerializer
  queryset = BasicIngredientBase.objects.all()


class CategoryView(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()


class ExperimentView(viewsets.ModelViewSet):
  serializer_class = ExperimentSerializer
  queryset = Experiment.objects.all()




#request body:
#experiment_data, supplement_name, percentage_of_supplement, metrices
#experiment_data [nazwa,opis,link autor,data utworzenia]
#metrices list of lists of elements ['name','num_series', 'num_repeats', 'id_próbki', 'num_of_values_external_factor', 'list_of_values_external_factor', 'metrice_id']
def generate_experiment_excel(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    output = io.BytesIO()

    workbook = generate_empty_xlsx(output, body['experiment_data'], body['supplement_name'], body['percentage_of_supplement'],body['metrices'])
    workbook.close()
    output.seek(0)

    filename = body['supplement_name'] + "_" + str(body['percentage_of_supplement']) + "%" + ".xlsx"
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=" + filename
    output.close()

    return response


