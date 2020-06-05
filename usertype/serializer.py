from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from .models import User , Hospital
from django.contrib.auth import get_user_model


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    Full_Name = serializers.CharField()
    Hospital_Name = serializers.CharField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    is_Doctor = serializers.BooleanField(required = False)
    is_Hospital = serializers.BooleanField(required = False)
    Phone_Number  =  serializers.IntegerField(required= False)


    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def get_cleaned_data(self):
        return {
            'Full_Name': self.validated_data.get('Full_Name', ''),
            'password': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'is_Hospital': self.validated_data.get('is_Hospital', ''),
            'is_Doctor': self.validated_data.get('is_Doctor', ''),
            'Hospital_Name': self.validated_data.get('Hospital_Name', ''),
            'Phone_Number': self.validated_data.get('Phone_Number', '')
        }

    def save(self, request):
        cleaned_data = self.get_cleaned_data()
        user = User.objects.create_user(**cleaned_data)
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = [ 'email' ,'Hospital_Name','Phone_Number' ,'password' , ]

class HospitalRegisterSerializer(serializers.ModelSerializer):
    User_Email = CustomUserSerializer()
    
    class Meta:
        model =  Hospital
        fields = ['User_Email' , 'Address']
    
    def create(self , validated_data):
        user_data =  validated_data.pop('User_Email')
        User_Email =  User.objects.create(**user_data , is_Hospital = True)
        
        hospital = Hospital.objects.create(User_Email=User_Email, **validated_data)
        return hospital

