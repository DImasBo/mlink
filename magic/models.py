from django.db import models
from django.urls import reverse

from magic.utils import generate_random_string


class MagicURL(models.Model):
    origin_url = models.URLField(max_length=2000)
    id_path = models.CharField(max_length=15, unique=True, blank=True)
    count_open = models.IntegerField(default=0)

    def _generate_id_path(self):
        new_id_path = generate_random_string()
        obj = MagicURL.objects.filter(id_path=new_id_path).first()
        if obj:
            return self._generate_id_path()
        return new_id_path

    def save(self, *args, **kwargs):
        if not self.id_path:
            self.id_path = self._generate_id_path()
        super().save(*args, **kwargs)

    def add_count_open(self, count=1):
        self.count_open += count
        self.save()
        return self.count_open

    def __str__(self):
        return '<%s %s %d>' % (self.__class__.__name__, self.id_path, self.count_open)

    def get_url_by_id_path(self):
        return reverse('redirect_link', kwargs={"id_path": self.id_path})

    def get_absolute_url(self):
        return reverse('detail_link',  kwargs={"id_path": self.id_path})
