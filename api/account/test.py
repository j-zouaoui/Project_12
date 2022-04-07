validated_data={
    "user": {
        "id": 10,
        "password": "testing321",

        "username": "New_user_10_A",
        "first_name": "",
        "last_name": "",
        "email": "",

        "date_joined": "2022-03-28T13:36:42.880301Z",

    }
}

user_updated_data = validated_data.pop('user')
print(user_updated_data)

for attr, value in validated_data.items():
    if attr in info.relations and info.relations[attr].to_many:
        m2m_fields.append((attr, value))
    else:
        setattr(instance, attr, value)
print(instance)