def add_contacts(phonebook,name,number):
    phonebook[name]=number
    print("contact was added sucessfully")
def search_contact(phonebook,name):
    if name in phonebook:
        print("Contact found:",name,"-",phonebook[name])
    else:
        print("COntact was not found")
my_phonebook={}
add_contacts(my_phonebook,"Arnav","2131283687")
print("---")
search_contact(my_phonebook,"Arnav")
search_contact(my_phonebook,"Virat")