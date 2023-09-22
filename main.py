import turtle
import time

arayuz = turtle.Screen()
arayuz = turtle.bgcolor("light blue")
arayuz.title("Yakalama Oyunu")

imlec = turtle.Turtle()


baslangic_zamani = time.time()

for i in range(1000000):
    pass

bitis_zamani = time.time()

gecen_sure = bitis_zamani - baslangic_zamani

gecen_sure_str = time.strftime("%H saat, %M dakika ve %S saniye", time.gmtime(gecen_sure))

imlec.write(f"Geçen Süre: {gecen_sure_str}",align="center",font=("Arial",12,"normal"))
print(f"Geçen süre: {gecen_sure_str}")















turtle.done()