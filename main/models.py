from django.db import models

class CompanyInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название сайта")
    description = models.TextField(verbose_name="Описание сайта")
    logo = models.ImageField(upload_to="logo/", verbose_name="Логотип сайта")
    icon = models.ImageField(upload_to="icon/", verbose_name="Иконка сайта")
    email = models.EmailField(verbose_name="Контактный email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    working_hours = models.CharField(max_length=100, verbose_name="Часы работы")

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

    def __str__(self):
        return self.title