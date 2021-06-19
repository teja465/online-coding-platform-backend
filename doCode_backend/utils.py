from django.contrib.auth.models import User
def my_jwt_response_handler(token, user=None, request=None):
    print("in jwt m()")
    print("token",token)
    [print(1) for i in range(10)]
    # print(User.data)
    return {
        'token': token,
        # 'user': User.data
    }