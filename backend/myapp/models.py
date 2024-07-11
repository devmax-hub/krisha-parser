from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Города"
        verbose_name = "Город"


class Author(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Авторы"
        verbose_name = "Автор"


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"

    def __str__(self):
        return self.name


class Object(models.Model):
    url = models.URLField(max_length=200, default="No URL")
    room = models.IntegerField(default=0)
    square = models.FloatField(default=0)
    city = models.CharField(max_length=100, default="No city")
    description = models.TextField(default="No description")
    photo = models.URLField(max_length=200, default="No photo")

    def __str__(self):
        return f"{self.city} - {self.room} rooms"

    class Meta:
        verbose_name_plural = "Недвижимостий"
        verbose_name = "Недвижимость"


class Parser(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)  # True if running, False if stopped

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Парсеры"
        verbose_name = "Парсер"


class SetFilter(models.Model):
    name = models.CharField(max_length=100)
    filter_json = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Фильтры"
        verbose_name = "Фильтр"
