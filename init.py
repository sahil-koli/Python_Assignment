

class initial():

    def __init__(self, *args, **kwargs):
        """Consturctor of app which initialize the user data"""
        self.users = []
        self.user_role = {}
        self.resource = []

    def create_Resources(self, name, data):
        """Method to create resources"""
        user_data = {'name':name, "data":data}
        self.resource.append(user_data)
        return "resource created", 200

    def create_user(self, name= None, password=None, role=None):
        """Method to create new user"""
        try:
            if not name :
                name =  input('Enter name of user :- ')
            if not password:
                password = input('Enter password :- ')
            if not role:
                role = input('Enter role (admin, user1) :- ')
        except Exception as err:
            print('Wrong information by user , User not crated')
            return None
        if role not in ('admin', 'user1'):
            print('You selected wrong role')
            return None
        user_data = {'name':name, "password":password}
        self.users.append(user_data)
        self.user_role[name]=role
        print(f'User created sucessfully with name as {user_data.get("name")}')
        return "user created", 200

