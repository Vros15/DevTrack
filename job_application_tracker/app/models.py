from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class JobApplication(models.Model):
    STATUS_CHOICES = (
        ('saved', 'Saved'),
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='job_applications'
    )
    
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='job_applications'
    )
    
    position = models.CharField(max_length=255)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='saved'
    )

    job_url = models.URLField(blank=True)
    salary = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    applied_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.position} at {self.company.name}"