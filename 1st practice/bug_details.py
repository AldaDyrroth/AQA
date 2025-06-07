bug = {
    "id": "1",
    "name": "Регистрация",
    "status": "open"
}
for key, value in bug.items():
    print(f"{key}: {value}")
print('')
bug["status"] = "in progress"

for key, value in bug.items():
    print(f"{key}: {value}")
