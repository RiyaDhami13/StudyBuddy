class Validator:
    @staticmethod
    def is_valid_name(name):
        # Checks if the subject name is not just empty spaces
        return len(name.strip()) > 0
    

    @staticmethod
    def is_valid_choice(choice):
        #Checks if the menu input is within the correct range
        try:
            return start <= int(choice) <= end
        except ValueError:
            return False
        