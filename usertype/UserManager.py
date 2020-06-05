from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self , 
                        email ,
                        Full_Name = None ,
                        Hospital_Name = None,
                        password =None,
                        is_Hospital =  None ,
                        is_Doctor = None,
                        Phone_Number =  None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            email = self.normalize_email(email),
            Full_Name =  Full_Name,
            Hospital_Name = Hospital_Name,
            is_Doctor = is_Doctor,
            is_Hospital = is_Hospital,
            Phone_Number =  Phone_Number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self ,
                            email ,
                            Full_Name = None,
                            Hospital_Name = None,
                            password = None,
                            is_Hospital = None , 
                            is_Doctor =  None,
                            Phone_Number =  None):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have an email address")

        user = self.create_user(
            email,
            Full_Name = Full_Name,
            password=password,
            Hospital_Name =  Hospital_Name,
            is_Doctor = is_Doctor,
            is_Hospital = is_Hospital,
            Phone_Number= Phone_Number,
        )

        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user