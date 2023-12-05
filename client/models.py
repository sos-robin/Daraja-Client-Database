from django.db import models
# Client information   

class Client(models.Model):
    CATEGORY_CHOICES = (
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    )

    name = models.CharField(max_length=200, null=True)
    job_title = models.CharField(max_length=200, null=True)
    personal_contact = models.CharField(max_length=10)
    personal_image = models.ImageField(upload_to='images/', null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True)
    company_contact = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=20, null=True)
    company_website = models.URLField(max_length=30, null=True)
    address = models.CharField(max_length=20, null=True)
    company_image = models.ImageField(upload_to='images/', null=True, blank=True)

    product_name = models.CharField(max_length=200, null=True)
    product_category = models.CharField(max_length=200, null=True, choices=CATEGORY_CHOICES)
    product_price = models.FloatField(null=True,)
 

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        # Set the product price based on the category
        category_price = {
            'Basic': 3000,
            'Standard': 4999,
            'Premium': 5999,
        }
        self.product_price = category_price.get(self.product_category)
        super().save(*args, **kwargs)


class Payment(models.Model):
    STATUS_CHOICES = (
        ('Unpaid', 'Unpaid'),
        ('Incomplete', 'Incomplete'),
        ('Completed', 'Completed'),
    )

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    id = models.AutoField(primary_key=True, default=1000)
    # Other fields in the Payment model

    current_monthly_bill = models.IntegerField(blank=True, null=True)
    Amount_paid = models.IntegerField(blank=True, null=True)
    date_of_payment = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS_CHOICES)

    def __str__(self):
        return self.status

    

class Clients_compaints(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='compaints')
    complaint = models.TextField(max_length=200, null=True, blank=True)

class Clients_feedback(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='feedbacks')
    feedback = models.TextField(max_length=200,null=True,blank=True)

class Clients_preference (models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='preferences')
    preference = models.TextField(max_length=200,null=True,blank=True)

class Clients_General_notes(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='notes')
    notes = models.TextField(max_length=200,null=True,blank=True)


# particular product the client has taken
  





    