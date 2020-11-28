from django.contrib import admin
from .models import Result, DetailedMetric, Metric, Sample, ExternalFactor, Supplement, SupplementBase, Product, Recipe, BasicIngredient, BasicIngredientBase, Category, Experiment

admin.site.register(Experiment)
admin.site.register(Result)
admin.site.register(DetailedMetric)
admin.site.register(Metric)
admin.site.register(Sample)
admin.site.register(ExternalFactor)
admin.site.register(Supplement)
admin.site.register(SupplementBase)
admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(BasicIngredient)
admin.site.register(BasicIngredientBase)
admin.site.register(Category)