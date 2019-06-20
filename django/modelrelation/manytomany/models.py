from django.db import models


# Doctor 테이블 설정
class Doctor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}번 의사: {self.name}'


# Patient 테이블 설정
class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctors = models.ManyToManyField(Doctor,
                                     # related_name: 역참조
                                     related_name='patients')

    def __str__(self):
        return f'{self.id}번 환자: {self.name}'


# # Reservation 테이블 설정
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.doctor}의 환자: {self.patient}'