def heat_unit():
    donusum= input("Lütfen bir dönüşüm seçiniz:")
    if donusum == "fahrenheit":
       Fahrenheit = float(input("Fahrenheit cinsinden sıcaklık nedir:"))
       Celsius = (Fahrenheit - 32) * 5/9
       print("Sıcaklık", (round(Celsius)) , "Celsius derecedir.")
    elif donusum == "celsius":
       Celsius = float(input("Celcius cinsinden sıcaklık nedir:"))
       Fahrenheit = 9/5 * Celsius + 32 
       print("Sıcaklık", (round(Fahrenheit)) , "Fahrenheit derecedir.")
    elif donusum == "kelvin":
        Kelvin = float(input("Kelvin cinsinden sıcaklık nedir:"))
        Reaumur = (Kelvin - 273) * 4/5
        print("Sıcaklık" , (round(Reaumur)) , "Reaumur derecedir.")
    elif donusum == "reaumur":
        Reaumur = float(input("Reaumur cinsinden sıcaklık nedir:"))
        Kelvin = (Reaumur * 5/4) + 273
        print("Sıcaklık" , (round(Kelvin)) , "Kelvin derecedir.")
heat_unit()


