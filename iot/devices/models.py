from django.db import models

# Create your models here.
class device_List(models.Models):
    '''
    For device_id , put the 'L','F' followed by the
    number as the device_id for Light ,Fan respectively
    '''
    device_id = models.CharField(max_length=100, primary_key=True)
    device_name = models.CharField(max_length=200, primary_key=True))
    
    def __str__(self):
        return self.device_id

class device_Details(models.Models):
    state = (
        ('ON','The device is ON'),
        ('OFF','The device is OFF')
    )
    type_device = (
        ("Light","It's a Light"),
        ("Fan","It's a Fan"),
        ("Sockets","Its a socket")
    )
    device_id = models.ForeignKey(device_List, on_delete=models.CASCADE)
    device_name = models.ForeignKey(device_List, on_delete=models.CASCADE)
    current_state = models.CharField(max_length=2 , choices = state)
    device_type = models.models.CharField(max_length=6 , choices = type_device)
    funtion_id = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.device_id   

class type_Fan(models.Models):
    speed = (
        ('M','manual'),
        ('A','automatic')
    )
    device_id = models.ForeignKey(device_List, on_delete=models.CASCADE)
    funtion_id = models.ForeignKey(device_Details, on_delete=models.CASCADE)
    device_name = models.ForeignKey(device_List, on_delete=models.CASCADE)
    temperature = models.IntegerField()
    Fan_speed = models.CharField(max_length=1, choices = speed)
    
    def __str__(self):
        return self.device_id   

class type_Light(models.Models):
    device_id = models.ForeignKey(device_Details, on_delete=models.CASCADE)
    device_name = models.ForeignKey(device_List, on_delete=models.CASCADE)
    funtion_id = models.ForeignKey(device_Details, on_delete=models.CASCADE)
    intensity = models.IntegerField()
    
    def __str__(self):
        return self.device_id   

class manual_function(models.Models):
    device_id = models.ForeignKey(device_List, on_delete=models.CASCADE)
    device_name = models.ForeignKey(device_List, on_delete=models.CASCADE)
    funtion_id = models.ForeignKey(device_Details, on_delete=models.CASCADE)
    total_on_time = models.IntegerField()
    
    def __str__(self):
        return self.device_id   