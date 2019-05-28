from django.db import models
from django.contrib.auth.models import User
# Create your models here.

APPROACH_CHOICES = [
    ('classification', 'Classification'),
    ('clustering', 'Clustering'),
    ('dimension_reduction', 'Dimension Reduction')
]

SVC = 'SVC'
KNN = 'KNN'

METHOD_CHOICES = [
    (SVC, 'SVM - Classification'),
    (KNN, 'KNN - Classification')
]

METHOD_PARAMS = {
    SVC: ['kernel'],
    KNN: ['neighbors']
}


class MachineBase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)
    is_public = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Data(MachineBase):
    data_json = models.TextField()
    features_json = models.TextField(blank=True, null=True)


class Machine(MachineBase):

    KERNEL_CHOICES = [
        ('linear', 'Linear'),
        ('rbf', 'RBF'),
        ('poly', 'Polynomial')]

    method = models.CharField(max_length=50, choices=METHOD_CHOICES)
    kernel = models.CharField(max_length=50, choices=KERNEL_CHOICES, null=True, blank=True)
    neighbors = models.IntegerField(default=5, null=True, blank=True)
    clusters = models.IntegerField(default=2, null=True, blank=True)


class Train(MachineBase):
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    has_label = models.BooleanField(default=True)
    label = models.IntegerField()
    is_trained = models.BooleanField(default=False)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    trained_model = models.TextField(null=True, blank=True)

