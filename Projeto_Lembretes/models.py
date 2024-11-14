from django.db import models


class Topic(models.Model):
    """Topico pelo qual usuário está vendo"""
    """text é uma variável do banco que vai ser do tipo char"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representacao em string do modelo"""
        return self.text

class Entry(models.Model):
    """Uma anotacao sobre o topico"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Devolve uma representacao em string do modelo"""
        return self.text[:50] + '...'
