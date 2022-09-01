from django.db import models
from django.contrib.auth.models import User


class TaskUser(models.Model):
    first_name = models.CharField('Фамилия', max_length=60)
    last_name = models.CharField('Имя', max_length=60)
    email = models.EmailField('Email', blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name        = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Task(models.Model):
    title = models.CharField ('Название', max_length=50)  # CharField() - текст до 255 символов
    task  = models.TextField ('Описание')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    admin = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) # on_delete=models.SET_NULL
                                                                                      # эта строка нужна для того, чтобы когда автор статьи или в нашем
                                                                                      # случае задачи удалил свой профиль с сайта его задача/статья осталась на сайте
                                                                                      # blank=True - настройка говорит что это поле не обязательно для заполнения
    attendees = models.ForeignKey(TaskUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = 'Задача'
        verbose_name_plural = 'Задачи'


