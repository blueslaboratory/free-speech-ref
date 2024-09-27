from datetime import datetime


print(datetime.now())


msg = (
        "Yellow Card 🟨❕\n\n"
        "Please take some time to reflect on your language, you can make your point come across in a polite and respectful way.\n\n"
        "We are better than this, I believe in you."
)


# print(msg)



print("######################")
print("#### FORSITO LOOP ####")
print("######################")

data = {'data': {'id': '1831237855265382400', 'name': 'Free Speech Referee 🤖🟨🟥', 'username': 'free_speech_ref'}}
print(data)


print("\nData and keys:")
for k, v in data['data'].items():
    print(k, v)
        
print("\nKeys:")
for k in data['data']:
    print(k)
    print(data['data'][k])

print("\nKeys 2:")
for k in data['data'].keys():
    print(k)

print("\nValues:")
for v in data['data'].values():
    print(v)