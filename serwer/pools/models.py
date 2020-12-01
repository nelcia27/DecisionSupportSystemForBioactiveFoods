from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, validate_comma_separated_integer_list


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=300, unique=True)

    def __str__(self):
        return self.name


class BasicIngredientBase(models.Model):
    name = models.CharField(primary_key=True, max_length=300, unique=True)

    def __str__(self):
        return self.name


class BasicIngredient(models.Model):
    name = models.CharField(primary_key=True, max_length=300, unique=True)
    percentage = models.PositiveIntegerField(default=10,
                                             blank=False,
                                             validators=[MinValueValidator(0), MaxValueValidator(100)])
    basicIngredientBase = models.ForeignKey(BasicIngredientBase, on_delete=models.CASCADE)


class Recipe(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    grammage = models.PositiveIntegerField(default=100, blank=False)
    ingredients = models.ManyToManyField(BasicIngredient)


class Product(models.Model):
    name = models.CharField(primary_key=True, max_length=300, unique=True)
    description = models.CharField(max_length=1500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SupplementBase(models.Model):
    name = models.CharField(primary_key=True, max_length=300, unique=True)

    def __str__(self):
        return self.name


class Supplement(models.Model):
    name = models.CharField(primary_key=True, max_length=300, unique=True)
    percentage = models.PositiveIntegerField(default=10,
                                             blank=False,
                                             validators=[MinValueValidator(0), MaxValueValidator(100)])
    basicIngredientBase = models.ForeignKey(BasicIngredientBase, on_delete=models.CASCADE)
    supplement_base = models.ForeignKey(SupplementBase, on_delete=models.CASCADE)


class ExternalFactor(models.Model):
    name = models.CharField(primary_key=True, max_length=300, unique=True)
    number_of_values = models.PositiveIntegerField(default=3, blank=False)
    unit = models.CharField(max_length=30)
    values = models.CharField(validators=[validate_comma_separated_integer_list], max_length=150)

    def __str__(self):
        return self.name


class Sample(models.Model):
    id = models.AutoField(primary_key=True)
    externalFactor = models.ForeignKey(ExternalFactor, on_delete=models.CASCADE)
    supplement = models.ManyToManyField(Supplement)


class Metric(models.Model):
    name = models.CharField(primary_key=True, max_length=300, unique=True)
    unit = models.CharField(max_length=30)
    scale = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class DetailedMetric(models.Model):
    id = models.AutoField(primary_key=True)
    number_of_repeat = models.PositiveIntegerField(default=1, blank=False)
    number_of_series = models.PositiveIntegerField(default=1, blank=False)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)


class Result(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.FloatField(blank=False)
    number_of_measure = models.PositiveIntegerField(blank=False)
    number_of_serie = models.PositiveIntegerField(blank=False)
    detailed_metric = models.ForeignKey(DetailedMetric, on_delete=models.CASCADE)


class Experiment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400)
    description = models.CharField(max_length=1500)
    link = models.CharField(max_length=600)
    author = models.CharField(max_length=300)
    create_date = models.DateTimeField(auto_now_add=True)
    number_of_measured_properties = models.PositiveIntegerField(default=1, blank=False)
    number_of_samples = models.PositiveIntegerField(default=1, blank=False)
    public_view = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    detailed_metrics = models.ManyToManyField(DetailedMetric)
    samples = models.ManyToManyField(Sample)

    def __str__(self):
        return self.name




