from .models import User_Profile
from rest_framework import serializers


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Profile
        fields = ('Name','First_Name','Last_Name','Fathers_Name','Mothers_Name','Address','City','Pin_Code','Phone_No','Education')


