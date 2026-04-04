import requests
# url = "https://restful-booker.herokuapp.com/booking"
#
# get_booking_id= requests.get(url)
# print(get_booking_id.status_code)
# print(get_booking_id.text)


url_booking_details="https://restful-booker.herokuapp.com/booking"
get_booking_details = requests.get(url_booking_details)
print(get_booking_details.status_code)
print(get_booking_details.text)

url_creating_booking_details = "https://restful-booker.herokuapp.com/booking"
data = {
    "firstname": "kish",
    "lastname": "karan",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

post_value=requests.post(url_creating_booking_details,data=data)
print(post_value.status_code)
print(post_value.text)
url_auth = "https://restful-booker.herokuapp.com/auth"
data_auth = {
    "username":"admin",
    "password":"password123"
}
response = requests.post(url_auth, json=data_auth)
print(response.status_code)
print(response.text)

# update_booking_url ="https://restful-booker.herokuapp.com/booking/1079"
# data = {
#     "firstname": "Jim",
#     "lastname": "Brown",
#     "totalprice": 111,
#     "depositpaid": True,
#     "bookingdates": {
#         "checkin": "2018-01-01",
#         "checkout": "2019-01-01"
#     },
#     "additionalneeds": "Breakfast"
# }
# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "Cookie": "token=f52624c3d3189db"
# }
# get_post_response = requests.put(update_booking_url, data=data, headers=headers)
# print(get_post_response.status_code)
# print(get_post_response.text)
