from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

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
