from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

     # Método para representar el objeto como una cadena
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'tasks'
        ordering = ['completed', 'created_at']
