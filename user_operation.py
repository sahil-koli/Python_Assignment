from init import initial

class user(initial):

    def __init__(self, *args, **kwargs):
        super(user, self).__init__(*args, **kwargs)

    
    def login(self):
        """Method for login """
        username = str(input('Enter username :- '))
        password = str(input('Enter password :- '))
        for user_data in self.users:
            if user_data.get('name')==username and user_data.get('password')==password:
                self.dashboard(user_data.get('name'),self.user_role[user_data.get('name')])
                break
        else:
            print('user not found Try with some another user')
            self.login()
        return 'Closing Application'
    
    def dashboard(self, name, role):
        """Method to show allowed operation to user according to role"""
        print(f'hi! you are logged in as {role}')
        if role == 'admin':
            print("press 1 for login as another user\npress 2 for create user\npress 3 for edit role") 
        else:
            print('press 1 for login as another user\npress 2 for view roles\npress 3 for access resource')
        try:
            user_input = int(input())
        except Exception as err:
            return None
        if user_input == 1:
            self.login()
        elif user_input == 2:
            self.create_user() if role=='admin' else self.get_roles_list()
        elif user_input == 3:
            self.edit_role() if role=='admin' else self.access_resources()
        else:
            print('you enter press wrong key please try again')
            self.dashboard(name, role)
        self.ask_to_close(name, role)
        return None

    
    def edit_role(self):
        """Method fo edit role of any user"""
        try:
            user_input = str(input('Enter name of user you want to edit the roll :- '))
            user_roll = str(input('Enter roll :- '))
        except Exception as err:
            return None
        if self.user_role.get(user_input):
            self.user_role[user_input] = user_roll
        else:
            print('user not found Try with some another user')
            self.edit_role()
        return None

    def get_roles_list(self):
        """Method to get list of all roles"""
        print('List of roles', list(set(self.user_role.values())))
        return None
    
    def access_resources(self):
        """Method to get list of all resources"""
        print('resources -->', self.resource)
        print('you have view access for recouse')
    
    def ask_to_close(self, name, role):
        """Method to check with use taht user wants to continue or close app """
        try:
            user_input = int(input("press 1 for close application\npress 2 for see options again:- "))
        except Exception as err:
            print(err)
            return None
        if user_input == 2 :
            self.dashboard(name, self.user_role.get(name))
        else :
            return None







