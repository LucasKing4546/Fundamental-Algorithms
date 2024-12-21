class Patient:
    def __init__(self, first_name: str, last_name: str, pnc: int, disease: str, age: int):
        if isinstance(first_name, str) and isinstance(last_name, str) and isinstance(pnc,int) and isinstance(disease, str) and isinstance(age, int):
            self.__first_name = first_name
            self.__last_name = last_name
            self.__pnc = pnc
            self.__disease = disease
            self.__age = age
        else:
            raise ValueError('Invalid inputs')

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_pnc(self):
        return self.__pnc

    def get_disease(self):
        return self.__disease

    def get_age(self):
        return self.__age

    def set_first_name(self, first_name: str):
        if not isinstance(first_name, str):
            raise ValueError('First name must be a string')
        self.__first_name = first_name

    def set_last_name(self, last_name: str):
        if not isinstance(last_name, str):
            raise ValueError('Last name must be a string')
        self.__last_name = last_name

    def set_pnc(self, pnc: int):
        if not isinstance(pnc, (int, float)):
            raise ValueError('PNC must be a number')
        self.__pnc = pnc

    def set_disease(self, disease: str):
        if not isinstance(disease, str):
            raise ValueError('Disease must be a string')
        self.__disease = disease

    def set_age(self, age: int):
        if not isinstance(age, int):
            raise ValueError('Age must be a number')
        self.__age = age


    def __repr__(self):
        return f"Patient: {self.__first_name} {self.__last_name}, PNC: {self.__pnc}, Disease: {self.__disease}, Age: {self.__age}\n"

    def __eq__(self, other):
        if not isinstance(other, Patient):
            return False
        return (self.__first_name == other.__first_name and
                self.__last_name == other.__last_name and
                self.__pnc == other.__pnc and
                self.__disease == other.__disease and
                self.__age == other.__age)
