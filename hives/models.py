from django.db import models


class Hive(models.Model):
    coordinate = models.CharField(max_length=100, verbose_name="Координаты")

    # user = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class DataHive(models.Model):
    hive_id = models.ForeignKey('Hive', on_delete=models.SET_NULL, null=True, verbose_name='Номер улья')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    temperature = models.FloatField(verbose_name='Температура')
    humidity = models.FloatField(verbose_name='Влажность')
    weight = models.FloatField(verbose_name='Вес')

    class Meta:
        ordering = ['-hive_id', ]

    def __str__(self):
        return str(self.hive_id)


class Subscription(models.Model):
    start_date = models.DateField(auto_now_add=True, verbose_name='Начало')
    end_date = models.DateField(verbose_name="Конец")
    hive_id = models.OneToOneField('Hive', on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True)
    coast = models.FloatField(verbose_name='Стоимость')

    class Meta:
        ordering = ['hive_id']

    def __str__(self):
        return str(self.pk)


class Service(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    count_of_request = models.IntegerField(verbose_name='Количество запросов')

    class Meta:
        ordering = ['-count_of_request']

    def __str__(self):
        return self.name


class ReportHive(models.Model):
    hive_id = models.ForeignKey('Hive', on_delete=models.SET_NULL, null=True, verbose_name='Улей')
    aver_temp = models.FloatField(verbose_name='Ср температура')
    aver_humid = models.FloatField(verbose_name='Ср влажность')
    change_weight = models.FloatField(verbose_name='Изм веса')
    start_date = models.DateField(verbose_name='Начало', null=True)
    end_date = models.DateField(verbose_name='Конец', null= True)

    class Meta:
        ordering = ['hive_id']

    def __str__(self):
        return str(self.hive_id)


class Card(models.Model):
    number = models.CharField(max_length=19, verbose_name='Номер')
    valid = models.DateField(verbose_name='Срок действия')
    cvv = models.CharField(max_length=3, verbose_name='CVV')

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)
