# from django.db import models

# # Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     apartment = models.CharField(max_length=50)
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=128)  # Increased length for hashed passwords

#     def __str__(self):
#         return self.username

# class Complaint(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=100)
#     message = models.TextField()

#     def __str__(self):
#         return f"Complaint by {self.user.username} - {self.subject}"
    
# class ParkingSlot(models.Model):
#     number = models.IntegerField()  # Slot number
#     is_occupied = models.BooleanField(default=False)  # Whether the slot is occupied
#     status = models.CharField(max_length=100)  # Slot status description
#     updated_at = models.DateTimeField(auto_now=True)  # Timestamp of the last update

#     def __str__(self):
#         return f"Slot {self.number} - {'Occupied' if self.is_occupied else 'Available'}"


from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    apartment = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Increased length for hashed passwords

    def __str__(self):
        return self.username

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"Complaint by {self.user.username} - {self.subject}"

class ParkingSlot(models.Model):
    number = models.IntegerField()  # Slot number
    is_occupied = models.BooleanField(default=False)  # Whether the slot is occupied
    status = models.CharField(max_length=100)  # Slot status description
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of the last update

    def __str__(self):
        return f"Slot {self.number} - {'Occupied' if self.is_occupied else 'Available'}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()  # Email field for contact
    message = models.TextField()  # Message content

    def __str__(self):
        return f"Contact from {self.name} - {self.email}"
