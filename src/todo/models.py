from django.db import models

class Todo(models.Model):
    __tablename__ = 'todos'
    title = models.CharField(verbose_name='title', max_length=255)
    is_conpleted = models.BooleanField(verbose_name='completed', default=False)

    def __str__(self):
        return "{}".format(self.title)
    
