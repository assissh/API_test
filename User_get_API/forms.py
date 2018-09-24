from django import forms
from .models import *

class User_form(forms.ModelForm):
    class Meta:
          model= User_Profile
          fields = ['Name','First_Name','Last_Name','Fathers_Name','Mothers_Name','Address','City','Pin_Code','Phone_No'
                    ,'Education']

    def clean_Name(self):
        Name= self.cleaned_data.get('Name')
        return Name

    def clean_First_Name(self):
        First_Name= self.cleaned_data.get('First_Name')
        return First_Name

    def Last_Name(self):
        Last_Name= self.cleaned_data.get('Last_Name')
        return Last_Name

    def clean_Fathers_Name(self):
        Fathers_Name= self.cleaned_data.get('Fathers_Name')
        return Fathers_Name

    def clean_Mothers_Name(self):
        Mothers_Name= self.cleaned_data.get('Mothers_Name')
        return Mothers_Name

    def clean_Address(self):
        Address= self.cleaned_data.get('Address')
        return Address

    def clean_City(self):
        City= self.cleaned_data.get('City')
        return City

    def clean_Pin_Code(self):
        Pin_Code= self.cleaned_data.get('Pin_Code')
        return Pin_Code

    def clean_Phone_No(self):
        Phone_No= self.cleaned_data.get('Phone_No')
        return Phone_No

    def clean_Education(self):
        Education= self.cleaned_data.get('Education')
        return Education


