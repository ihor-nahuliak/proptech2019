from django.db import models
from datetime import datetime

# Create your models here.



# {
#     'TransactionType': 'Pay Bill', 
#     'TransID': 'NHP61HABHK',    
#     'TransTime': '20190825023843', 
#     'TransAmount': '5.00', 
#     'BusinessShortCode': '601397', 
#     'BillRefNumber': '17258', 
#     'InvoiceNumber': '', 
#     'OrgAccountBalance': '84832.00', 
#     'ThirdPartyTransID': '', 
#     'MSISDN': '254708374149', 
#     'FirstName': 'John', 
#     'MiddleName': 'J.', 
#     'LastName': 'Doe'
# }        
class C2BPayment(models.Model):
    TransactionType = models.CharField(max_length=50, blank = False)
    TransID = models.CharField(max_length=50, blank = False)
    TransTime = models.CharField(max_length=50, blank = False)
    TransAmount = models.CharField(max_length=50, blank = False)
    BusinessShortCode = models.CharField(max_length=50, blank = False)
    BillRefNumber = models.CharField(max_length=50, blank = False)
    InvoiceNumber = models.CharField(max_length=50, blank = True, default = None)
    OrgAccountBalance = models.CharField(max_length=50, blank = False)
    ThirdPartyTransID = models.CharField(max_length=50, blank = True, default = None)
    MSISDN = models.CharField(max_length=50, blank = False)
    FirstName = models.CharField(max_length=20, blank = False)
    MiddleName = models.CharField(max_length=20, blank = False)
    LastName = models.CharField(max_length=20, blank = False)


    def __str__(self):
        return 'C2BPayment (TransactionType: {self.TransactionType}, TransID: {self.TransID}, TransTime: {self.TransTime}, TransAmount: {self.TransAmount}, FirstName: {self.FirstName}, MiddleName: {self.MiddleName}, LastName: {self.LastName})'