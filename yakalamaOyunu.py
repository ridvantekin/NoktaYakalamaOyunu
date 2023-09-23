import turtle
import random
import math

# arayüz penceresi
arayuz = turtle.Screen()
arayuz.title("Turtle Yakalama Oyunu")
arayuz.bgcolor("light blue")
arayuz.setup(width=950, height=680)

# Oyuncu puanı
puan = 0

# Zaman sınırlaması (saniye cinsinden)
zaman = 20



# Turtle'ı oluştur
kb = turtle.Turtle()
kb.shape("turtle")
kb.shapesize(3)
kb.color("red")
kb.penup()
kb.speed(0)

# Puan metni
skorMetni = turtle.Turtle()
skorMetni.color("black")
skorMetni.penup()
skorMetni.hideturtle()
skorMetni.goto(-350, 260)
skorMetni.write("Puan: {}".format(puan), align="left", font=("Times New Roman", 17, "normal"))

# Zaman metni
zamanMetni = turtle.Turtle()
zamanMetni.color("black")
zamanMetni.penup()
zamanMetni.hideturtle()
zamanMetni.goto(200, 260)
zamanMetni.write("Kalan Süre: {}".format(zaman), align="left", font=("Times New Roman", 17, "normal"))

# Yuvarlağa tıklandığında
def click(x, y):
    global puan

    mesafe = math.sqrt((x - kb.xcor())**2 + (y - kb.ycor())**2)
    if mesafe < 20:
        puan += 5
        skorMetni.clear()
        skorMetni.write("Puan: {}".format(puan), align="left", font=("Times New Roman", 17, "normal"))

# Tıklama olayını tanımla
turtle.onscreenclick(click)

# Ana döngümüz
while zaman > 0:
    x = random.randint(-380, 380)  # Rastgele konum
    y = random.randint(-280, 280)

    kb.goto(x, y)
    turtle.update()

    turtle.delay(200)  #saniyenin 5'te 1'i kadar bekle

    zaman -= 1
    zamanMetni.clear()
    zamanMetni.write("Kalan Süre: {}".format(zaman), align="left", font=("Times New Roman", 17, "normal"))


if zaman ==0: #oyun bittiğinde yapılacak olanlar
    turtle.update()
    skorMetni.goto(-50, 0)
    skorMetni.write("Oyun Bitti! Puanınız: {}".format(puan), align="center", font=("Times New Roman", 24, "normal"))
    kb.hideturtle()




turtle.mainloop()
