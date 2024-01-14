from django.db import models

# Create your models here.
class JobModel(models.Model):
    job_title = models.CharField(verbose_name="Job Title", name="job_title", max_length=200)
    job_description = models.TextField(verbose_name="Job Description", name="job_description", max_length=2000)

    def __str__(self) -> str:
        return f'{self.job_title}'
    
class JobImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE, related_name="job_images")

    def __str__(self):
        return f'{self.job.job_title} image'