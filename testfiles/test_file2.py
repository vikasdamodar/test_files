class Converter:

    def temp_convert(self, temp, unit, desc=False):
        desc_value = ""
        if unit == "Fahrenheit":
            conv_temp = round((temp - 32)*(5/9))
            conv_to = "°C "
        elif unit == "Celsius":
            conv_temp = round((temp*9/5)+32)
            conv_to = "°F  "
        else:
            return None
        if desc:
            desc_value = self.find_desc(temp, conv_temp, unit)
        return str(conv_temp)+conv_to+desc_value

    def find_desc(self, temp, conv_temp, unit):
        description = {
            (-40, -40): "This is where Celsius equals Fahrenheit. It's the temperature of an extremely cold day.",
            (-18, 0): "An average cold winter day.", (0, 32): "The freezing point of water.",
            (10, 50): "A cool day.", (21, 70): "A typical room temperature.", (30, 86): "A hot day.",
            (37, 99): "Body temperature.", (40, 104): "Bath water temperature.",
            (100, 212): "Boiling point of water at sea level.", (180, 356): "Baking temperature in an oven."
            }
        try:
            if unit == "Fahrenheit":
                desc = description[(conv_temp, temp)]
            else:
                desc = description[(temp, conv_temp)]
        except KeyError:
            desc = "No Description"

        return desc


obj = Converter()
value = obj.temp_convert(38, "Celsius", True)
print(value)