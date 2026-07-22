to_do_list = ""
amount_of_items = 0

while True:
    command = input("What would you like to do? (add/check): ")
    if command == "add":
        add_to_list = input("Enter item: ")
        amount_of_items += 1
        to_do_list += f"{amount_of_items}) {add_to_list} - Not Done\n"
        print(f"{to_do_list}")
    elif command == "check":
        check_number = input("What item would you like to check?: ")
        items = to_do_list.splitlines()
        items[int(check_number) - 1] = items[int(check_number) - 1].replace("Not Done", "Done")
        to_do_list = "\n".join(items)
        print(f"{to_do_list}\n")