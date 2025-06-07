from faker import Faker

faker = Faker('ru_RU')

print(faker.name())

address_sndr =  faker.postcode() + ", Российская Федерация, " + faker.city() + ", "+ faker.street_address()
address_rcpn =  faker.postcode() + ", Российская Федерация, г. Москва, " + faker.street_address()

print(f"{address_sndr}\n"
      f"{address_rcpn}")