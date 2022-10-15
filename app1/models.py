from django.db import models


# Create your models here.


class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_about = models.TextField(max_length=800, default=None)
    user_age = models.IntegerField(null=True)
    user_city = models.TextField(max_length=255)
    user_country = models.TextField(max_length=255)
    user_email = models.TextField(max_length=255, unique=True)
    user_first_name = models.TextField(max_length=255)
    user_jop_title = models.TextField(max_length=255)
    user_last_name = models.TextField(max_length=255)
    user_password = models.TextField(max_length=255)
    user_phone = models.TextField(max_length=13, unique=True)





class course(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.TextField(max_length=255)
    course_provider=models.TextField(max_length=255)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)


class education(models.Model):
    education_id=models.AutoField(primary_key=True)
    education_degree=models.TextField(max_length=255)
    education_place=models.TextField(max_length=255)
    end_date=models.TextField(max_length=100)
    start_date = models.TextField(max_length=100)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)



class skill(models.Model):
    skill_id=models.AutoField(primary_key=True)
    skill_name=models.TextField(max_length=255)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)


class experience(models.Model):
    experience_id=models.AutoField(primary_key=True)
    end_date=models.TextField(max_length=100)
    experience_place=models.TextField(max_length=255)
    experience_position=models.TextField(max_length=255)
    start_date=models.TextField(max_length=100)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)




