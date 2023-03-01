

class View:
    def get_chosen_option(self, options):
        print()
        print("Choose an option:")
        chosen = False
        while not chosen:
            for i, option in enumerate(options):
                print(f"{i + 1}. {option}")
            i = input()
            try:
                i = int(i)
                chosen = True
            except ValueError:
                print(f"{i} is not a valid option")

        print(f"You chose {options[i - 1]}")
        print()
        return options[i - 1]

    def show_elements(self, elements):
        print("Places:")
        for i, place in enumerate(elements):
            print(f"{i+1}.{place}")

    def request_input(self, message):
        return input(message)

    def get_boolean_input(self, message):
        i = ""
        while (i != "y" and i != "n"):
            i = input(f"{message} (y/n): ")
        return i == "y"
