from rest_framework import serializers
from .models import Result, DetailedMetric, Metric, Sample, ExternalFactor, Supplement, SupplementBase, Product, Recipe, BasicIngredient, BasicIngredientBase, Category, Experiment


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = ('id', 'name',  'description', 'link', 'author', 'create_date',
                  'number_of_measured_properties', 'number_of_samples',  'public_view',
                  'product', 'detailed_metrics', 'samples')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')


class BasicIngredientBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicIngredientBase
        fields = ('name')


class BasicIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicIngredient
        fields = ('name', 'percentage', 'basicIngredientBase')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'grammage', 'ingredients')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description',  'category', 'recipe')


class SupplementBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplementBase
        fields = ('name')


class SupplementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplement
        fields = ('name', 'percentage', 'basicIngredientBase', 'supplement_base')


class ExternalFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalFactor
        fields = ('name', 'number_of_values', 'unit', 'values')


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('id', 'externalFactor', 'supplement')


class DetailedMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailedMetric
        fields = ('id', 'number_of_repeat', 'number_of_series', 'metric', 'sample')


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ('name', 'unit', 'scale')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'value', 'number_of_measure', 'number_of_serie', 'detailed_metric')