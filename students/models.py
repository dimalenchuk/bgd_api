from django.db import models


class Person(models.Model):
    first_name = models.CharField('first name',max_length=30)
    last_name = models.CharField('last name',max_length=30)
    phone_number = models.BigIntegerField('phone number', null=True, blank=True)
    e_mail = models.EmailField('email address')


class Student(Person):
    group_id = models.CharField('group name', max_length=10)
    study_year = models.SmallIntegerField('year of studying',max_length=2)
    def __str__(self):
        return self.last_name.lower()

class News(models.Model):
    id = models.AutoField(primary_key=True)
    news_name = models.CharField('news name', max_length=25)
    news_content = models.CharField('news content', max_length=200)
    news_author = models.CharField('news author', max_length= 30)
    news_date = models.DateField('news date', auto_now_add = True)
    class Meta:
        verbose_name_plural = "news"
    def __str__(self):
        return self.news_name.lower()