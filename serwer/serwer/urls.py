"""serwer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pools import views

router = routers.DefaultRouter()
router.register(r'Result', views.ResultView, 'Result')
router.register(r'DetailedMetric', views.DetailedMetricView, 'DetailedMetric')
router.register(r'Metric', views.MetricView, 'Metric')
router.register(r'Sample', views.SampleView, 'Sample')
router.register(r'ExternalFactor', views.ExternalFactorView, 'ExternalFactor')
router.register(r'Supplement', views.SupplementView, 'Supplement')
router.register(r'SupplementBase', views.SupplementBaseView, 'SupplementBase') #problem
router.register(r'Product', views.ProductView, 'Product')
router.register(r'Recipe', views.RecipeView, 'Recipe')
router.register(r'BasicIngredient', views.BasicIngredientView, 'BasicIngredient')
router.register(r'BasicIngredientBase', views.BasicIngredientBaseView, 'BasicIngredientBase') #problem
router.register(r'Category', views.CategoryView, 'Category') #problem
router.register(r'Experiment', views.ExperimentView, 'Experiment')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
 # path('pools/', include('pools.urls')),