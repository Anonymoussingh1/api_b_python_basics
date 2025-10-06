# key value pair
# ordered, mutable, unique keys, fast loopkups

new_dict = {}
# print(type(new_dict))

new_dict = {
            "name" : "Mark",
            "age" : 25,
            "email" : "mark@gmail.com"
            }
print(new_dict["name"])
print(new_dict.values())

new_dict["name"] = "James"
print(new_dict.values())

new_dict["user_name"] = "Jane"
print(new_dict.values())



print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())






# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]