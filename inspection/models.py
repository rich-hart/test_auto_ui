from django.db import models

class PDF(models.Model):
    pdf_file = models.FileField()

class Option(models.Model):
    TEST_CHOICES = (
    ('Any', 'Any'),
    ('All', 'All'),
    )
    name = models.CharField(max_length=128)
    test_choices = models.CharField(max_length=3, choices=TEST_CHOICES)
     
    def __str__(self):
        return self.name

class CVTest(models.Model):
    pdf_a = models.ForeignKey('PDF',related_name='pdf_a')
    pdf_b = models.ForeignKey('PDF',related_name='pdf_b')
    options = models.ForeignKey('Option')
    test_created = models.DateTimeField(auto_now_add=True)
    results = models.TextField()

