
from init import initial
from user_operation import user

def run():
    app = user()
    app.create_Resources('res_1', 'data in res 1')
    app.create_Resources('res_2', 'data in res 2')
    app.create_user('admin', '1234', 'admin')
    app.create_user('user1', '1234', 'User1')
    status = app.login()
    print(status)


if __name__ == "__main__":
    run()
    