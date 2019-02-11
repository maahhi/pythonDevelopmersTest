from random import randint


def weather():
    weathers = ["صاف و آفتابی",
                "نیمه ابری",
                "برفی"]
    return weathers[randint(0,2)]


def time():
    times = ["اذان ظهر ساعت 12:19",
             "غروب خورشید ساعت 17:41",
             "اذان مغرب ساعت 18:00"]
    return times[randint(0, 2)]


def exchangerate():
    exchangerates = ["دلار آمریکا 11 هزار و 700 تومان",
                     "یورو 13 هزار و 700 تومان",
                     "پوند انگلیس 15 هزار و 321 تومان"]
    return exchangerates[randint(0, 2)]


def hafez():
    hafezs  = ["دل و دینم شد و دلبر به ملامت برخاست",
               "ما را ز خیال تو چه پروای شراب است",
               "منم که گوشه میخانه خانقاه من است"]
    return hafezs[randint(0, 2)]

# a dictionary : keys = services name, values = correspondent function
SERVICES={
    'آب و هوا':weather,
    'اوقات شرعی':time,
    'نرخ ارز':exchangerate,
    'فال حافظ':hafez
}
