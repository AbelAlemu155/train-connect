

class User(object):
    def __init_(self,id, first_name, last_name, phone_number, date_of_birth, user_role, gender, street, city, state, email ):
        self.id=id
        self.first_name=first_name
        self.last_name= last_name
        self.phone_number= phone_number
        self.date_of_birth= date_of_birth
        self.user_role= user_role
        self.gender= gender
        self.street= street
        self.city=city
        self.state=state
        self.email=email
    @staticmethod
    def tuple_to_object(tuple):
        return User(tuple)
    
    



