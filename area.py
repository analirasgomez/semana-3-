def calculate_area (radio):
    area = 3.14159 * radio**2
    return area

radio_input = float (input("radio:"))
area_calculada = calculate_area (radio_input)
print (area_calculada)
