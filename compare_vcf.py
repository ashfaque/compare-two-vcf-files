import vobject

# Opening the vcf files:-
file = open("Contacts.vcf", "r")
fileS = open("ContactsS.vcf", "r")

# Converting file1 to readable txt format
with open("Contacts.txt", "w") as Contacts:
    for vcard in vobject.readComponents(file):
        Contacts.write("\n")
        Contacts.write(str({vcard.contents["fn"][0].value: [tel.value for tel in vcard.contents["tel"]]}))

# Converting file2 to readable txt format
with open("ContactsS.txt", "w") as ContactsS:
    for vcardS in vobject.readComponents(fileS):
        ContactsS.write("\n")
        ContactsS.write(str({vcardS.contents["fn"][0].value: [tel.value for tel in vcardS.contents["tel"]]}))


with open("Contacts.txt", "r") as ReadContacts:
    with open("ContactsS.txt", "r") as ReadContactsS:
        with open("diff.txt", "a+") as diff_file:
            rContactsS = ReadContactsS.read()
            diff_file.write("------------------------------------------In Contacts and not in ContactsS------------------------------------------\n")
            for line in ReadContacts.readlines():
                if not line.rstrip() in rContactsS:
                    diff_file.write("\n")
                    diff_file.write(line.rstrip())


with open("Contacts.txt", "r") as ReadContacts:
    with open("ContactsS.txt", "r") as ReadContactsS:
        with open("difference.txt", "a+") as diff_file:
            rContacts = ReadContacts.read()
            diff_file.write("\n\n------------------------------------------In ContactS and not in Contacts------------------------------------------\n")
            for line in ReadContactsS.readlines():
                if not line.rstrip() in rContacts:
                    diff_file.write("\n")
                    diff_file.write(line.rstrip())


# Closing opened files
file.close()
fileS.close()


# for vcard in vobject.readComponents(file):
#     print("vcard------------>",vcard)
#     print("vcard.contents--------------->",vcard.contents)
#     print("vcard.contents['fn']------------------>",vcard.contents["fn"])
#     print("vcard.contents[\"fn\"][0]---------------->",vcard.contents["fn"][0])
#     print("KEY----------NAME------------->",vcard.contents["fn"][0].value)
#     print()
#     print("vcard.contents---------->",vcard.contents)
#     print("vcard.contents[\"tel\"]---------->",vcard.contents["tel"])
#     print("VALUE--------LIST PH NO.--------->", [tel.value for tel in vcard.contents["tel"]])
# ? Using List Comprehension in Dictionary Comprehension {vcardRev.contents["fn"][0].value: [tel.value for tel in vcardRev.contents["tel"]]}