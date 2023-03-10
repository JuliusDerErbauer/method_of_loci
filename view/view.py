

class View:
    def get_chosen_option(self, options):
        print()
        print("Choose an option:")
        chosen = False
        i = 0
        while not chosen:
            for i, option in enumerate(options):
                print(f"{i + 1}. {option}")
            i = input()
            try:
                i = int(i)
                if i in range(1, len(options) + 1):
                    chosen = True
                else:
                    print(f"{i} is not a valid option")
            except ValueError:
                print(f"{i} is not a valid option")

        print(f"You chose {options[i - 1]}")
        print()
        return options[i - 1]

    def get_chose_option_by_id(self, options):
        print()
        print("Choose an option:")
        chosen = False
        i = 0
        while not chosen:
            for i, option in enumerate(options):
                print(f"{i + 1}. {option['name'][0]}")
            i = input()
            try:
                i = int(i)
                chosen = True
            except ValueError:
                print(f"{i} is not a valid option")

        print(f"You chose {options['name'][0]}")
        print()
        return options['id'][i - 1]

    def show_elements(self, elements):
        print("Places:")
        for i, element in enumerate(elements):
            print(f"{i+1}. {element}")

    def request_input(self, message):
        return input(message)

    def get_boolean_input(self, message):
        i = ""
        while (i != "y" and i != "n"):
            i = input(f"{message} (y/n): ")
        return i == "y"

    def show_message(self, message):
        print(message)