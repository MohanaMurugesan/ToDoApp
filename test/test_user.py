from .utils import *
from routers.user import get_db,get_current_user
from fastapi import status


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'abc'
    assert response.json()['email'] == 'abc@gmail.com'
    assert response.json()['first_name'] == 'ABC'
    assert response.json()['last_name'] == 'DEF'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '9874562310'

def test_change_password_success(test_user):
    response = client.put("/user/password",json={"password":'abc',
                                                 "new_password":'abc123'})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_password(test_user):
    response = client.put("/user/password",json={"password":"uuibc",
                                                 "new_password":"helloooo"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail':'Error on password change'}

def test_change_phone_number(test_user):
    response = client.put("/user/phonenumber/1234567890")
    assert response.status_code == status.HTTP_204_NO_CONTENT

