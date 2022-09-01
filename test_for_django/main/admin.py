from django.contrib import admin
from .models import Task, TaskUser


admin.site.register(TaskUser)
#admin.site.register(Task) - регистрация для показа панели админа по умолчанию

@admin.register(Task)                   # регистрация для кастомной панели админа
class TaskAdmin(admin.ModelAdmin):      # наследуем форму от встроенного модуля Админ
    list_display = ('title', )          # говорим что будет отображаться при показе панели (поля из модуля TASK)
    ordering = ('title', )              # сортировка по имени (для обратного порядка нужно указать "-title")
                                        # может сортировать по любому полю, а не только title
    search_fields = ('title', )         # панель поиска, указываем в каких полях он будет искать соответствие
