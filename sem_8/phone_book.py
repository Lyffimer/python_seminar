from os import path


file_base = "sem_8/base.txt"
last_id = 0
all_data = []
# open(file_base, "a", encoding="utf-8")

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])

        return all_data

    # if last_id:
    #     with open(file_base, encoding="utf-8") as f:
    #         all_data = [i.strip() for i in f]
    #         last_id = all_data[-1][0]
    #         print(all_data[-1][0])
            
    #     return all_data
        
    # return []


def show_all():
    # print(all_data)
    # print(last_id)
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")

def add_new_contact():
    global last_id

    array = ['surname', 'name', 'patronymic', 'phone number']
    answer = []
    for i in array:
        answer.append(data_validation(i))

    if not database_check(0, " ".join(answer)):
        last_id += 1
        answer.insert(0, str(last_id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answer)}\n')
        print("New contact added!\n")
    else:
        print("Such contact already exists!")


    # string = ""
    # last_id += 1
    #     f.write(f"{last_id} {string}\n")

def data_validation(value):
    while True:
        enter_word = input(f"Enter {value}: ")
        if value in "surname name patronymic":
            if enter_word.isalpha():
                return enter_word
        if value in 'phone number' and enter_word.isdigit():
            return enter_word
        print("Data is incorrect!")
    
def database_check(val_id, data):
    if val_id:
        contact_check = [i for i in all_data if val_id == i.split()[0]]
    else:
        contact_check = [i for i in all_data if data in i]
    return contact_check



def record_search():
    global last_id, all_data
    desired = database_check(0, input("Enter a search term "))
    if desired:
        print(*desired, sep="\n")
    else:
        print("Nothing was found")
    # # second_id = 0
    # desired = input("Enter a search term ")
    # for register in all_data:
    #     if desired in register:
    #         # second_id = int(register[0])
    #         print(register)
    #         # print(second_id)

def edit_menu():

    add_dict = {"1": "surname", "2": "name", "3": "patronymic", "4": "phone number"}

    show_all()
    record_id = input("Enter the record id: ")

    if database_check(record_id, ""):
        while True:
            print("\nChanging:")
            change = input("1. surname\n"
                           "2. name\n"
                           "3. patronymic\n"
                           "4. phone number\n"
                           "5. exit\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_validation(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("The data is not recognized, repeat the input.")
    else:
        print("The data is not correct!")



def change_contact(data_tuple):

    global all_data
    symbol = "\n"

    convert_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v.split()[0] == convert_id:
            v = v.split()
            v[int(num_data)] = data
            if database_check(0, " ".join(v[1:])):
                print("The data already exists!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Record changed!\n")

def delete_entry():
    global all_data

    symbol = "\n"
    show_all()
    delet_record = input("Enter the record id: ")

    if database_check(delet_record, ""):
        all_data = [k for k in all_data if k.split()[0] != delet_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Record deleted!\n")
    else:
        print("The data is not correct!")

def exp_imp_menu():

    while True:
        print("\nExp/Imp menu:")
        move = input("1. Export\n"
                     "2. Import\n"
                     "3. exit\n")

        match move:
            case "1":
                exp_bd(input("Enter the name of the file: "))
            case "2":
                ipm_bd(input("Enter the name of the file: "))
            case "3":
                return 0
            case _:
                print("The data is not recognized, repeat the input.")

def exp_bd(name):

    symbol = "\n"

    change_name = f"{name}.txt"
    if not path.exists(change_name):
        with open(change_name, "w", encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')


def ipm_bd(name):
    global file_base

    if path.exists(name):
        file_base = name
        # read_records()



def main_menu():
    play = True
    while play:
        read_records()
        answer = input('Phone book:\n'
                        '1. Show all records\n'
                        '2. add a record\n'
                        '3. Record Search\n'
                        '4. Change\n'
                        '5. Delete entry\n'
                        '6. Exp/Imp\n'
                        '7. Exit\n')
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                record_search()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                delete_entry()
            case "6":
                exp_imp_menu()
            case "7":
                play = False
            case _:
                print("Try again!\n")
                
main_menu()
