class RomanNumeralConverter:
    def __init__(self, number):
        self.number = number

    def validate_number(self):
        if not isinstance(self.number, int):
            raise TypeError("The value must be an integer.")

        if self.number < 1 or self.number > 3999:
            raise ValueError("The number must be between 1 and 3999.")

    def convert(self):
        self.validate_number()

        roman_values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        number = self.number
        roman_numeral = ""

        for value, symbol in roman_values:
            while number >= value:
                roman_numeral += symbol
                number -= value

        return roman_numeral



try:
    integer_value = int(input("Enter an integer from 1 to 3999: "))

    converter = RomanNumeralConverter(integer_value)
    result = converter.convert()

    print("Roman numeral:", result)

except (ValueError, TypeError) as error:
    print("Error:", error)