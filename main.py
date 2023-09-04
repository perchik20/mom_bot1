from telebot import types
import telebot
import config
from gg import button1_1, button_1, button, button_2, button2_1, button_3, button3_1, button4

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['help'])
def say_start(message):
    bot.send_message(message.chat.id, 'Я бот книжник, составленный преподавателем Светланой Эрик специально для учащихся МААП, МиП и «Среда обучения», которые интересуются Юнгианством  и не знают с чего начать читать Юнга, а так же для тех кто пишет ВКР.\nКоманда /blocks выдаст список блоков\n\nЕсли вас заинтересовал бот или вы хотите создать своего обращайтесь к:\nЕгор Алексеевич\nWhatsApp, Telegram: +7-985-751-45-94')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'<b>Привет, {message.from_user.first_name}</b>, Я бот книжник!\nЕсли ты тут первый раз отправь мне команду /help и я тебя все объясню!\nДля выбора блока, отправь мне команду команду /blocks"', reply_markup=button, parse_mode='html')


@bot.message_handler(commands=['blocks'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    btn3 = types.KeyboardButton("3")
    btn4 = types.KeyboardButton("4")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "Выберите номер Блока:\n1. Строение психики по Юнгу\n2. Литература по Психоанализу\n3. Библиотека иностранной литературы Красная Пресня,13n\n4. Фильмы по темам", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def books(message):

    photo = open(r"photos/loh.png", "rb")
    photo1 = open(r"photos/loh1.png", "rb")
    photo2 = open(r"photos/loh2.png", "rb")

    if message.text == "1":
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Строение психики по К.Г. Юнгу:", reply_markup=button_1)

    elif message.text == "2":
        bot.send_message(message.chat.id, 'Весь Фрейд:  “Полное собрание сочинений в 26 томах” (Издательство: ВЕИП; 2005-2021г;ISBN:978-5-91681-010-3 (серия)')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, f'<i><b>Строение психики по Фрейду</b></i>', parse_mode='html')
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, "Литература по Психоанализу:", reply_markup=button_2)

    elif message.text == "3":
        bot.send_message(message.chat.id, "Библиотека иностранной литературы Красная Пресня,13:", reply_markup=button_3)

    elif message.text == "4":
        bot.send_message(message.chat.id, 'Выберите тему', reply_markup=button4)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.message:
        if call.data == 'button1_1':
            msg = 'ЭГО'
            bot.send_message(call.message.chat.id, f'<i><b>{msg}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг.  “Aion”. \nГлава 1: «Эго»')
            bot.send_message(call.message.chat.id, "М.Стайн. «Юнговская карта души.Введение в аналитическую психологию». \nГлава 1: “Поверхность”")
            bot.send_message(call.message.chat.id, 'Э. Самуэлс. «Юнг и постъюнгианцы». \nГлава 3: «Эго»')
            bot.send_message(call.message.chat.id, 'Т. Каблучкова. «Основы аналитической психологии. Архетипический подход. \nГлава 5: “Структуры идентичности: ЭГО”')
            bot.send_message(call.message.chat.id, 'Э.Эдингер. «Эго и Архетип». \nГлава 1: «Инфляция Эго». \nГлава 2: «ОТчуждение Эго».')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

        if call.data == 'button1_2':
            msg_1 = 'ПЕРСОНА'
            bot.send_message(call.message.chat.id, f'<i><b>{msg_1}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'Т. Каблучкова. «Основы аналитической психологии. Архетипический подход”.\nГлава 6: “Структуры идентичности: ПЕРСОНА”.')
            bot.send_message(call.message.chat.id, 'М.Стайн. «Юнговская карта души. Введение в аналитическую психологию».  \nГлава 5: «Тайное и явное в отношениях с окружающими(Тень-Персона)».')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

        if call.data == 'button1_3':
            msg_2 = 'ТЕНЬ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg_2}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг. “Aion”. \nГлава 2: «Тень»')
            bot.send_message(call.message.chat.id, 'М.Стайн. «Юнговская карта души.Введение в аналитическую психологию». \nГлава 5: «Тайное и явное в отношениях с окружающими(Тень-Персона)”')
            bot.send_message(call.message.chat.id, ' Т. Каблучкова. «Основы аналитической психологии. Архетипический подход”. \nГлава 5: “Структуры идентичности: ТЕНЬ”')
            bot.send_message(call.message.chat.id, 'Шалит Э. “ Враг, калека и нищий: тени на пути героя”')
            bot.send_message(call.message.chat.id, 'С.Б. Перера “Комплекс козла отпущения. Мифологические и психологические аспекты коллективной Тени и вины”')
            bot.send_message(call.message.chat.id, 'Д. Хендерсон “ Тень и Самость”')
            bot.send_message(call.message.chat.id, 'Р. Джонсон “Как овладеть своей тенью. Глубинные аспекты темной стороны психики”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

        if call.data == 'button1_4':
            msg_3 = "Анима-Анимус"
            bot.send_message(call.message.chat.id, f'<i><b>{msg_3}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, ' К.Г. Юнг. Aion. Глава 3:«Сизигия Анима и Анимус»')
            bot.send_message(call.message.chat.id, 'М.Стайн. «Юнговская карта души.Введение в аналитическую психологию».\nГлава 6 Путь в глубины души(Анима и Анимус)')
            bot.send_message(call.message.chat.id, 'Т. Каблучкова. «Основы аналитической психологии. Архетипический подход.\nГлава 7. “Структуры идентичности: АНИМА и АНИМУС”')
            bot.send_message(call.message.chat.id, 'М.Стайн «Юнговская карта души. Введение в аналитическую психологию».\nГлава 5: «Путь в глубины души(Анима и Анимус)»')
            bot.send_message(call.message.chat.id, '“Кембриджское руководство по аналитической психологии”.\nГлава 9: Элио Дж.Фраттароли “Я и моя анима: сквозь темное стекло на границе между юнгиансвом и фрейдизмом”.')
            bot.send_message(call.message.chat.id, 'К.Г Юнг. “Архетипы и коллективное бессознательное”. Раздел :”Об архетипах с особым вниманием понятию Анимы”')
            bot.send_message(call.message.chat.id, ' Энн и Барри Уланов “Трансформация сексуальности:архетипический мир Анимы и Анимуса”')
            bot.send_message(call.message.chat.id, 'Д.Хиллман. “Анима”')
            bot.send_message(call.message.chat.id, 'Б.Ханна. “Анимус и Эрос”')
            bot.send_message(call.message.chat.id, ' Б.Ханна.”Анимус”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

        if call.data == 'button1_5':
            msg_4 = "Самость"
            bot.send_message(call.message.chat.id, f'<i><b>{msg_4}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'К.Г.Юнг. Aion.\nГлава 4: «Самость»')
            bot.send_message(call.message.chat.id, 'М.Стайн. «Юнговская карта души. Введение в аналитическую психологию».\nГлава 7: “Трансцендентный центр психики и целостности (Самость)”')
            bot.send_message(call.message.chat.id, 'Т. Каблучкова. «Основы аналитической психологии. Архетипический подход».\nГлава 8: «Структуры идентичности: САМОСТЬ»')
            bot.send_message(call.message.chat.id, 'В. Каст. «Динамика символов. Основы Юнгианской психотерапии».\nГлава:«Аспекты представления о человеке»')
            bot.send_message(call.message.chat.id, 'Э.Эдингер. «Эго и Архетип».\nГлава 3: «Встреча с Самостью»')
            bot.send_message(call.message.chat.id, 'М.Кларк. «Отношение Эго и Самости в клинической практике»')
            bot.send_message(call.message.chat.id, 'К.Г Юнг «Синхрония»')
            bot.send_message(call.message.chat.id, 'Э. Самуэлс. «Юнг и постъюнгианцы».\nГлава 4: “Самость и индивидуация”')
            bot.send_message(call.message.chat.id, ' Р. Дэниэл “Самость. Сущность и проявления центрального архетипа аналитической психологии”')
            bot.send_message(call.message.chat.id, 'Д. Хендерсон “ Тень и Самость”')
            bot.send_message(call.message.chat.id, 'К. Хайнц “Восстановление самости"')
            bot.send_message(call.message.chat.id, 'К. Хайнц “Анализ самости: Систематический подход к лечению нарциссических нарушений личности”')
            bot.send_message(call.message.chat.id, 'Шварц-Салант Н. “Тайна человеческих отношений. Алхимия и трансформация Самости”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

        if call.data == 'button1_6':
            msg_5 = "Индивидуация"
            bot.send_message(call.message.chat.id, f'<i><b>{msg_5}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг “Aion”')
            bot.send_message(call.message.chat.id, 'Э.Эдингер «Эго и Архетип».\nЧасть 1: «Индивидуация и стадии психологического развития». Часть 2: «Индивидуация как путь жизни»')
            bot.send_message(call.message.chat.id, 'К.Г Юнг «Синхрония»')
            bot.send_message(call.message.chat.id, 'Э. Самуэлс. «Юнг и постъюнгианцы».\nГлава 4: “Самость и индивидуация')
            bot.send_message(call.message.chat.id, 'Э. Самуэлс. «Юнг и постъюнгианцы». Глава 4: “Род,пол,брак"')
            bot.send_message(call.message.chat.id, ' К.Г. Юнг. “Символы сновидений в процессе индивидуации. Записи семинара К.Г.Юнга по сновидениям Вольфганга Паули”')
            bot.send_message(call.message.chat.id, 'М.Стайн. “Принцип индивидуации.О развитии человеческого сознания”')
            bot.send_message(call.message.chat.id, 'М.Стайн. “Индивидуация.Собрание сочинений. Том1')
            bot.send_message(call.message.chat.id, 'Журнал Юнгианский анализ №1 (45) 2021.” Диада и индивидуация”')
            bot.send_message(call.message.chat.id, ' Фон Франц М.-Л. “Индивидуация в волшебных сказках”')
            bot.send_message(call.message.chat.id, 'Малер Маргарет С., Пайн Фред, Бергман Анни “Психологическое рождение человеческого младенца: Симбиоз и индивидуация”')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг “Человек и его символы')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

        if call.data == 'button1_7':
            msg_6 = "Комплекс. Архетип. Коллективное бессознательное"
            bot.send_message(call.message.chat.id, f'<i><b>{msg_6}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг. «Душа и миф, шесть Архетипов»')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг  “Архетип и Символ” (Издательство “Канон+” РООИ”Реабилитация”2018).\nГлава 2: “Подход к бессознательному”.\nГлава 3: “Об архетипах коллективного бессознательного”')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг “Алхимия снов и четыре архетипа” (Москва.Медков СБ 2014).”Четыре архетипа:Мать,Дух,Трикстер,Перерождение”.')
            bot.send_message(call.message.chat.id, 'В. Каст. «Динамика симвлучкова. «Основы аналитической психологии. Архетипический подход. Глава  «Архетип».\nГлава 3 «Комплекс»')
            bot.send_message(call.message.chat.id, 'М.Стайн «Юнговская карта души. Введение в аналитическую психологию».\nГлава 2: «Внутренняя вселенная(комплексы)»')
            bot.send_message(call.message.chat.id, 'Э. Самуэлс. «Юнг и постюнгианцы» Глава 2 «Архетип и Комплекс»')
            bot.send_message(call.message.chat.id, 'К.Г Юнг. “Архетипы и коллективное бессознательное”.\nРаздел 1: “Архетипы коллективного бессознательного”.\nРаздел 2. “Концепция коллективного бессознательного”')
            bot.send_message(call.message.chat.id, 'Дж.Ш.Болен. “Богини в каждой женщине. Новая психология женщины. Архетипы богинь”')
            bot.send_message(call.message.chat.id, 'Дж.Ш.Болен. “Боги в каждом мужчине. Архетипы управляющие жизнью мужчин”')
            bot.send_message(call.message.chat.id, 'И.Якоби. “Архетип и Символ”. Часть 1. “Комплекс.Архетип.Символ”')
            bot.send_message(call.message.chat.id, 'М.-Л. фон Франц. “Архетипическое измерение психики”')
            bot.send_message(call.message.chat.id, 'Д.Тейси «Юнг и Экопсихология»')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

        if call.data == 'button1_8':
            msg_7 = "Типология Юнга"
            bot.send_message(call.message.chat.id, f'<i><b>{msg_7}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг. “Психологические типы”')
            bot.send_message(call.message.chat.id, 'Хиллман “Чувствующая функция”')
            bot.send_message(call.message.chat.id, 'М.-Л. Фон Франц “Подчиненная функция”')
            bot.send_message(call.message.chat.id, 'Джон Биби   “Психологические типы”(СТАТЬЯ НА САЙТЕ МААП)')
            bot.send_message(call.message.chat.id, 'Шарп, Дарэл. “Типы личности. Юнговская типологическая модель”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

        if call.data == 'button1_9':
            msg_8 = "Сновидение.Образы и Символы"
            bot.send_message(call.message.chat.id, f'<i><b>{msg_8}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'К.Г Юнг “Человек и его символы”(Медков СБ “Серебрянные нити”.2018г.)\nГлава 2: “Древние мифы и современный человек”.\nГлава 4: “Символы в изобразительном искусстве”')
            bot.send_message(call.message.chat.id, 'Д. Хендерсон, Э. Эдингер “Образы и символы глубин”')
            bot.send_message(call.message.chat.id, 'Э.Эдингер «Эго и Архетип». Часть 3: «Символы и цели»')
            bot.send_message(call.message.chat.id, 'В.Каст “Динамика символов. Основы юнгианской психотерапии”.\nГлава 2: “Аспекты символа”')
            bot.send_message(call.message.chat.id, 'М.Комфорти “Пересекая порог,Архетип начала в психоанализе”')
            bot.send_message(call.message.chat.id, '“Кембриджское руководство по аналитической психологии”.\nГлава 4: П.Кюглер. Психические образы как мост между субъектом и объектом”')
            bot.send_message(call.message.chat.id, 'Д.Холл. Структура сновидения”.\nЧасть 2: “Юнгианское толкование сновидений”')
            bot.send_message(call.message.chat.id, 'И.Якоби. “Архетип и Символ”.\nЧасть 2. “Архетип и сновидения”.')
            bot.send_message(call.message.chat.id, 'Т.Абт. “Территория символа”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

        if call.data == 'button1_10':
            msg_9 = "Работа с образами в сновидениях"
            bot.send_message(call.message.chat.id, f'<i><b>{msg_9}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг. “Алхимия сновидений. Четыре архетипа” \nРаздел 1: “Алхимия сновидений”')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг. “Структура и динамика психического”\nРаздел 4: “Общие аспекты психологии сновидений” “О природе сновидений”')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг. “Символическая жизнь”(Когито,Москва,2003)\nРаздел 1: “Символы и толкование сновидений”')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг. “Символы сновидений в процессе индивидуации. Записи семинара К.Г.Юнга по сновидениям Вольфганга Паули”')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг. “Семинары по детским сновидениям, 1936/1939”')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг. "Анализ сновидений. Семинары 1928-1929"')
            bot.send_message(call.message.chat.id, '.К.Г Юнг. “Человек и его символы”(Медков СБ “Серебрянные нити”.2018г.)\nГлава 5: Индивидуальная символика:случай из психоаналитической практики”')
            bot.send_message(call.message.chat.id, 'М.-Л. фон Франц “Путь сновидений”')
            bot.send_message(call.message.chat.id, 'М.-Л. фон Франц “О снах и смерти”')
            bot.send_message(call.message.chat.id, 'Дж.Хиллман “Присутствие животных”')
            bot.send_message(call.message.chat.id, 'Б.Ханна “Символизм животных”')
            bot.send_message(call.message.chat.id, 'Д. Хендерсон, Э. Эдингер. “Образы и символы глубин”')
            bot.send_message(call.message.chat.id, 'Д. Холл. “Юнгианское толкование сновидений”. Практическое рук-во /Пер. с англ.- СПб.: Б.С.К., 1996. – 168с.')
            bot.send_message(call.message.chat.id, 'Э. Самуэлс. «Юнг и постъюнгианцы». Глава 8: “сновидения”.')
            bot.send_message(call.message.chat.id, 'Р. Джонсон “”Сновидения и активное воображение”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

        if call.data == 'button1_11':
            msg_10 = "Перененос-Контрперенос"
            bot.send_message(call.message.chat.id, f'<i><b>{msg_10}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг « Психология переноса»')
            bot.send_message(call.message.chat.id, 'В. Каст. «Динамика символов. Основы Юнгианской психотерапии».\nГлава 6: «Перенос-контрперенос и формирование новых символов»')
            bot.send_message(call.message.chat.id, '“Кембриджское руководство по аналитической психологии”.\nГлава 8: К.Перри “Перенос и контрперенос”')
            bot.send_message(call.message.chat.id, '“Технические аспекты юнгианского анализа” под редакцией М.Фордхема,Р.Гордон,Д.Хаббэк и К.Ламберта.\nЧасть 2: ”Перенос”\nЧасть 3:”Контперенос”')
            bot.send_message(call.message.chat.id, '“Эротический и эротизированный перенос”. Под редакцией М.В. Ромашкевича.')
            bot.send_message(call.message.chat.id, 'Д. Сэджвик “Раненый целитель”')
            bot.send_message(call.message.chat.id, 'Д. Винер. “Терапевтические отношения. Перенос, контрперенос и обретение смысла”')
            bot.send_message(call.message.chat.id, 'Энн и Барри Уланов “Трансформация сексуальности:архетипический мир Анимы и Анимуса”.\nЧасть 4: “Перенос,Контрперенос и Анима/Анимус”')
            bot.send_message(call.message.chat.id, 'М.-Л. фон Франц. “Психотерапия” Глава 6: “Некоторые аспекты переноса”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

        if call.data == 'button1_12':
            msg_11 = "Алхимия"
            bot.send_message(call.message.chat.id, f'<i><b>{msg_11}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг “Алхимия снов и четыре архетипа” (Москва.Медков СБ 2014).”Индивидуальный символизм снов в отношении алхимии”')
            bot.send_message(call.message.chat.id, 'Д.Миллер. “Трансцендентная функция. Исследование одного открытия Юнга”')
            bot.send_message(call.message.chat.id, 'Рафф Дж. “Мистерии воображения. Алхимия и психология Юнга”')
            bot.send_message(call.message.chat.id, 'К.Г.Юнг "Психология и алхимия"')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

        if call.data == 'button1_13':
            msg_12 = "Методы работы в глубинной психологии"
            bot.send_message(call.message.chat.id, f'<i><b>{msg_12}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'Г. Юнг “Проблемы души нашего времени”')
            bot.send_message(call.message.chat.id, 'М.Нэджи “К.Г. Юнг и Философия”.')
            bot.send_message(call.message.chat.id, 'Э. Самуэлс. «Юнг и постъюнгианцы». Глава 6: “Аналитический процесс”')
            bot.send_message(call.message.chat.id, 'Зеленский В.В. “Базовый курс аналитической психологии, или Юнгианский бревитарий”')
            bot.send_message(call.message.chat.id, 'К.Г. Юнг “Структура и динамика психического”')
            bot.send_message(call.message.chat.id, 'М. Уинборн “Интерпретация в Юнгианском анализе: искусство и техника”')
            bot.send_message(call.message.chat.id, '“Технические аспекты юнгианского анализа” под редакцией М.Фордхема,Р.Гордон,Д.Хаббэк и К.Ламберта.\nЧасть 1: “Техника”')
            bot.send_message(call.message.chat.id, 'Х. Дикман “Методы в аналитической психологии:введение”')
            bot.send_message(call.message.chat.id, 'М.-Л. фон Франц. “Психотерапия”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button1_1)

    if call.message:
        if call.data == 'button2_2':
            msg1 = 'ПСИХОАНАЛИТИЧЕСКАЯ ПСИХОСОМАТИКА'
            bot.send_message(call.message.chat.id, f'<i><b>{msg1}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'А.Жибо.А. Рассохин. “Французская психоаналитическая школа”.  Раздел “Психоанализ и психосоматика”')
            bot.send_message(call.message.chat.id, 'МакДугалл. Дж. “Театры тела” Психоаналитический подход к психосоматическим расстройствам”')
            bot.send_message(call.message.chat.id, 'П.Марти  статья:“Психоанализ и психосоматика”.(Французская психоаналитическая школа. – СПб: Питер, 2005. – С. 514-525)')
            bot.send_message(call.message.chat.id, 'К.Смаджа “Оператуарная жизнь”')
            bot.send_message(call.message.chat.id, 'М.Фэн статья:  “Психосоматика и психоанализ”')
            bot.send_message(call.message.chat.id, 'Ж.Швек. “Добровольные галерщики. Очерки о процессах самоуспокоения”')
            bot.send_message(call.message.chat.id, 'Д.Анзье.  “Я-кожа”')
            bot.send_message(call.message.chat.id, 'Х. Ульник “Кожа в психоанализе”')
            bot.send_message(call.message.chat.id, 'М. Хирш. “Это мое тело и я могу делать с ним что хочу” Психоаналитический взгляд на диссоциацию и инсценировки тела”')
            bot.send_message(call.message.chat.id, 'Ф. Александер. “Психосоматическая медицина. Принципы и применение”')
            bot.send_message(call.message.chat.id, 'Ф.Дольто. “Бессознательный образ тела”(сборник том XVI)')
            bot.send_message(call.message.chat.id, 'П.Марти  работа “Ментализация и психосоматика”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button2_1)

        if call.data == 'button2_3':
            msg2 = 'ДЕПРЕССИЯ И МЕЛАНХОЛИЯ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg2}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'Фрейд  работа: “Горе и меланхолия”')
            bot.send_message(call.message.chat.id, 'Ю.Кристева “Черное солнце. Депрессия и меланхолия”')
            bot.send_message(call.message.chat.id, 'А.Грин  статья “Мертвая мать”')
            bot.send_message(call.message.chat.id, 'А.Грин “Работа негатива. Психоаналитическая работа, фокусированная на концепте негатива”')
            bot.send_message(call.message.chat.id, 'М.М. Решетников “Психодинамика и психотерапия депрессии”')
            bot.send_message(call.message.chat.id, 'Дж. Рейнгольд “Мать,тревога и смерть.Комплекс трагической смерти”')
            bot.send_message(call.message.chat.id, '”Психоанализ депрессий. Учебное пособие для бакалавриата,специалитета и магистратуры” под ред. М. Решетников')
            bot.send_message(call.message.chat.id, 'Б.Розенберг “Мазохизм смерти и мазохизм жизни”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button2_1)

        if call.data == 'button2_4':
            msg3 = 'ДИАГНОСТИКА И ТЕХНИКА В ПСИХОАНАЛИЗЕ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg3}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'Ж.Бержере “Психоаналитическая патопсихология: теория и клиника”')
            bot.send_message(call.message.chat.id, 'О.Кернберг. “Тяжелые личностные расстройства”')
            bot.send_message(call.message.chat.id, 'Х.Кохут. “Анализ самости. Системный подход к лечению нарциссических  нарушений личности”')
            bot.send_message(call.message.chat.id, 'Н.Мак-Вильямс. “Психоаналитическая диагностика”')
            bot.send_message(call.message.chat.id, 'Р.Стайнер  “Психические убежища”')
            bot.send_message(call.message.chat.id, 'Р.Гринсон “Техника и практика психоанализа”')
            bot.send_message(call.message.chat.id, 'П.Куттер  “Современный психоанализ. Введение в психологию бессознательных процессов”')
            bot.send_message(call.message.chat.id, 'Д.Сандлер, Д.Холдер“Пациент и психоаналитик: основы психоаналитического процесса”')
            bot.send_message(call.message.chat.id, 'Антология современного психоанализа.  Под ред. А.В. Рассохина')
            bot.send_message(call.message.chat.id, 'К.Немировский. “Винникотт и Кохут. Новые перспективы в психоанализе.психотерапии и психиатрии”')
            bot.send_message(call.message.chat.id, 'Р.Горацио Этчегоен “Основы психоаналитической техники”')
            bot.send_message(call.message.chat.id, 'М. Балинт “Базисный дефект. Терапевтические аспекты регрессии”')
            bot.send_message(call.message.chat.id, 'У. Бион “Внимание и интерпретация. Научение через опыт переживания”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button2_1)

        if call.data == 'button2_5':
            msg4 = 'СЕСКСУАЛЬНОСТЬ/ПЕРВЕРСИИ/ИНЦЕСТ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg4}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'Дж.МакДугалл “Тысячеликий фаллос”')
            bot.send_message(call.message.chat.id, 'Р.Перельберг  “Психическая бисексуальность”')
            bot.send_message(call.message.chat.id, 'Статьи Эриль А')
            bot.send_message(call.message.chat.id, 'Дж.Митчелл  “Скрытая жизнь братьев и сестер”')
            bot.send_message(call.message.chat.id, 'С.Бенвенуто “Перверсии. Сексуальность, этика, психоанализ”')
            bot.send_message(call.message.chat.id, 'Д.Пайнз “Бессознательное использование своего тела женщиной”')
            bot.send_message(call.message.chat.id, 'Ж.Шасге-Смиргель статья  “Женское чувство вины”')
            bot.send_message(call.message.chat.id, 'Скинайя Козимо “Педофилия и психоанализ”')
            bot.send_message(call.message.chat.id, 'З.Фрейд “Очерки по психологии сексуальности”')
            bot.send_message(call.message.chat.id, 'Письмо З. Ферйда - ТТ(Письмо огомосексуальности. 09.04.1935)')
            bot.send_message(call.message.chat.id, 'Сольда Людит Лё “Причины гомосексуальности”')
            bot.send_message(call.message.chat.id, 'Д. Мельцер “Сексуальные состояния разума”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button2_1)

        if call.data == 'button2_6':
            msg5 = 'РАННИЕ ОТНОШЕНИЯ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg5}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'Д.B.Винникот "Пигля. Отчет о психоаналитическом лечении маленькой девочки”')
            bot.send_message(call.message.chat.id, 'Д.B.Винникот “ Ребенок, семья и внешний мир”')
            bot.send_message(call.message.chat.id, 'Д.B.Винникотт  “ Игра и реальность”')
            bot.send_message(call.message.chat.id, 'Д.B.Винникотт “Разговор с родителями”')
            bot.send_message(call.message.chat.id, 'М. Кляйн Том 1. «Развитие одного ребенка». Работы 1920-1928 гг.')
            bot.send_message(call.message.chat.id, 'М. Кляйн Том 2. «Любовь, вина и репарация» и другие работы 1929–1942 гг. ')
            bot.send_message(call.message.chat.id, 'М. Кляйн Том 5. Эдипов комплекс. Работы 1945–1952 гг.')
            bot.send_message(call.message.chat.id, 'М. Кляйн Том 6. «Зависть и благодарность» и другие работы 1955–1963 гг.')
            bot.send_message(call.message.chat.id, 'Боллас Кристафер ( пока есть только на английском). ')
            bot.send_message(call.message.chat.id, 'Собрание трудов в 2-х томах Ф. Дольто. “Психоанализ и воспитание”')
            bot.send_message(call.message.chat.id, 'Ф. Дольто “На стороне ребенка”')
            bot.send_message(call.message.chat.id, 'Ф. Дольто  "На стороне подростка"')
            bot.send_message(call.message.chat.id, 'Ф. Дольто «Ребенок зеркала»')
            bot.send_message(call.message.chat.id, 'Ф. Дольто «Заповедный мир детства»')
            bot.send_message(call.message.chat.id, 'Маргарет С. Малер, Фред Пайн, Анни Бергман ”Психологическое рождение человеческого младенца. Симбиоз и индивидуация”')
            bot.send_message(call.message.chat.id, 'Маргарет С. Малер, Джон Б. Мак-Девитт  “Процесс сепарации-индивидуации и формирования идентичности”')
            bot.send_message(call.message.chat.id, 'Беттельхейм Б. “Пустая крепость. Детский аутизм и рождение Я”')
            bot.send_message(call.message.chat.id, 'Дж. Маганья “Наблюдение за младенцами в семьях”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button2_1)

        if call.data == 'button2_7':
            msg6 = 'СНОВИДЕНИЯ И СИМВОЛИЗАЦИЯ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg6}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'З. Фрейд “Толкование сновидений”')
            bot.send_message(call.message.chat.id, 'Современная теория сновидений. Под ред. Сары Фландерс')
            bot.send_message(call.message.chat.id, 'Р.Руссийон статья :“Работа символизации”')
            bot.send_message(call.message.chat.id, 'Р.Руссийон статья: “Символизирующая функция объекта”')
            bot.send_message(call.message.chat.id, '“Современная теория сновидений” Предисловие и общая редакция Сары Фландерс')
            bot.send_message(call.message.chat.id, 'Абрахам К. Сновидение и миф. Очерк коллективной психологии / Между Эдипом и Озирисом: Становление психоаналитической концепции мифа. М., 1998')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button2_1)


        if call.data == 'button2_8':
            msg7 = 'ПСИХОАНАЛИЗ И КУЛЬТУРА'
            bot.send_message(call.message.chat.id, f'<i><b>{msg7}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id, 'Г.Хьюер  “Сексуальные революции: Отто Гросс, психоанализ и культура”')
            bot.send_message(call.message.chat.id, 'Эткинд “Эрос невозможного. История психоанализа в России”')
            bot.send_message(call.message.chat.id, 'З.Фрейд “Психоанализ творчества. Леонардо да Винчи,Микеланджело, Достоевский”')
            bot.send_message(call.message.chat.id, 'Отто Ранк “Миф о рождении героя”')
            bot.send_message(call.message.chat.id, 'К.Хорни “Невротическая личность нашего времени”')
            bot.send_message(call.message.chat.id, 'Меню', reply_markup=button2_1)
    if call.message:
        if call.data == 'button3_1':
            msg = 'ОСНОВЫ ЮА: КОНЦЕПЦИИ И ТЕХНИКИ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id,
                             'Автор: Kenneth Lambert\n\nОригинальное название: Analysis, repair and individuation\n\nНазвание на Русском: Анализ, выздоровление и индивидуация')
            bot.send_message(call.message.chat.id,
                             'Автор: Michael Fordham, Judith Hubback, Rosemary Gordon, Kenneth Lambert\n\nОригинальное название: Technique in Jungian analysis\n\nНазвание на Русском: Технические аспекты юнгианского анализа')
            bot.send_message(call.message.chat.id,
                             'Автор: Michael Conforti\n\nОригинальное название: Threshold experiences / The Archetype of Beginnings\n\nНазвание на Русском: Пересекая порог. Архетип начала в психоанализе')
            bot.send_message(call.message.chat.id,
                             'Автор: Joseph Cambray, Linda Carter\n\nОригинальное название: Analytical Psychology / Contemporary Perspectives in Jungian Analysis\n\nНазвание на Русском: Аналитическая психология / Современный взгляд на аналитическую психологию')
            bot.send_message(call.message.chat.id,
                             'Автор: Elphis Christopher&Hester McFarland Solomon\n\nОригинальное название: Contemporary Jungian clinical practice\n\nНазвание на Русском: Современная юнгианская клиническая практика')
            bot.send_message(call.message.chat.id,
                             'Автор: Andrew Samuels, Bani Shorter, Fred Plaut\n\nОригинальное название: A critical dictionary of Jungian analysis\n\nНазвание на Русском: Ключевые понятия юнгианского анализа')
            bot.send_message(call.message.chat.id,
                             'Автор: Dale Mathers\n\nОригинальное название: An Introduction to Meaning and Purpose in Analytical Psychology\n\nНазвание на Русском: Введение в смысл и цели аналитической психологии')
            bot.send_message(call.message.chat.id,
                             'Автор: Renos K. Papadopoulos\n\nОригинальное название: The Handbook of Jungian Psychology / Theory, Practice and Applications\n\nНазвание на Русском: Руководство по юнгианской психологии / Теория, Практика и применение')
            bot.send_message(call.message.chat.id,
                             'Автор: Mario Jacoby\n\nОригинальное название: Shame and the origins of self-esteem\n\nНазвание на Русском: Стыд и истоки самоуважения')
            bot.send_message(call.message.chat.id,
                             'Автор: Hans Dieckmann\n\nОригинальное название: Methods in Analytical Psychology / An introduction\n\nНазвание на Русском: Методы в аналитической психологии / Введение')
            bot.send_message(call.message.chat.id,
                             'Автор: Michael Fordhamn, Roger Hobdell\n\nОригинальное название: Freud, Jung, Klein, the fenceless field / Essays on psychoanalysis and analytical psychology\n\nНазвание на Русском: Фрейд, Юнг, Кляйн, поле без ограждений / Эссе о психоаналитике и аналитической психологии')
            bot.send_message(call.message.chat.id,
                             'Автор: Richard Feldstein, Henry Sussman\n\nОригинальное название: Psychoanalysis and…\n\nНазвание на Русском: Психоанализ и…')
            bot.send_message(call.message.chat.id,
                             'Автор: Hindle Zinkin, Rosemary Gordon, Jane Haynes\n\nОригинальное название: Dialogue in the analytic setting / Selected Papers of Louis Zinkin on Jung and on Group Analysis\n\nНазвание на Русском: Диалог в аналитическом сеттинге / Избранные работы Льюис Зинкин о Юнге и групповом анализе')
            bot.send_message(call.message.chat.id,
                             'Автор: Robert Withers\n\nОригинальное название: Controversies in Analytical Psychology\n\nНазвание на Русском: Противоречия в аналитической психологии')
            bot.send_message(call.message.chat.id, "Меню:", reply_markup=button3_1)

        if call.data == 'button3_2':
            msg1 = 'ТЕРАПЕВТИЧЕСКИЕ ПРАКТИКИ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg1}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id,
                             'Автор: Jay Haley\n\nОригинальное название: Uncommon Therapy\n\nНазвание на Русском: Необычная терапия')
            bot.send_message(call.message.chat.id,
                             'Автор: Herald C. Lyon Jr.\n\nОригинальное название: Learning to Feel-Feeling to Learn\n\nНазвание на Русском: Учиться чувствовать – Чувство, что нужно учиться')
            bot.send_message(call.message.chat.id,
                             'Автор: Carl R. Rogers\n\nОригинальное название: Freedom to Learn\n\nНазвание на Русском: Свобода учиться')
            bot.send_message(call.message.chat.id,
                             'Автор: L. Sherilyn Cormier, William H. Cormier, Roland J. Weisser, Jr.\n\nОригинальное название: Interviewing and Helping Skills for Healing Professionals\n\nНазвание на Русском: Интервью и навыки оказания помощи для профессионалов в области исцеления')
            bot.send_message(call.message.chat.id,
                             'Автор: Alfred Benjamin\n\nОригинальное название: The Helping Interview\n\nНазвание на Русском: Помогающее интервью')
            bot.send_message(call.message.chat.id,
                             'Автор: A.V. Petrovsky and M.G. Yaroshevsky\n\nОригинальное название: A Сoncise Psychological Dictionary\n\nНазвание на Русском: Краткий психологический словарь')
            bot.send_message(call.message.chat.id,
                             'Автор: Lawrence M. Brammer\n\nОригинальное название: The Helping Relationship/ Process and Skills\n\nНазвание на Русском: Помогающие отношения / Процесс и навыки')
            bot.send_message(call.message.chat.id,
                             'Автор: Sidney m. Jourard\n\nОригинальное название: Healthy Personality / An Approach from The Viewpoint of Humanistic Psychology\n\nНазвание на Русском: Здоровая личность /Подход с точки зрения гуманистической психологии')
            bot.send_message(call.message.chat.id,
                             'Автор: Joseph Wolpe, Arnold A. Lazarus\n\nОригинальное название: Behavior Therapy Techniques\n\nНазвание на Русском: Техники поведенческой терапии')
            bot.send_message(call.message.chat.id,
                             'Автор: Ashok Bedi, M.D.\n\nОригинальное название: Path of the Soul\n\nНазвание на Русском: Путь души')
            bot.send_message(call.message.chat.id,
                             'Автор: Ashok Bedi, M.D. and Boris Matthews, Ph.D.\n\nОригинальное название: Retire Your Family Karma\n\nНазвание на Русском: Избавление от семейной кармы в психотерапии')
            bot.send_message(call.message.chat.id,
                             'Автор: Dr. Frederick B. Levenson\n\nОригинальное название: The Causes and Prevention of Cancer\n\nНазвание на Русском: Причины и предотвращение рака')
            bot.send_message(call.message.chat.id,
                             'Автор: Joan Chodorow\n\nОригинальное название: Dance Therapy and Depth Psychology\n\nНазвание на Русском: Терапия танцем и глубинная психология')
            bot.send_message(call.message.chat.id,
                             'Автор: Anna Maguire\n\nОригинальное название: Skin Disease / A message from The Soul / A treatise from a Jungian perspective of Psychosomatic Dermatology\n\nНазвание на Русском: Заболевания кожи / Голос души / Юнгианский взгляд на анализ психосоматической дерматологии ')
            bot.send_message(call.message.chat.id,
                             'Автор: Marion Milner\n\nОригинальное название: The hands of living God / An Account of a Psycho-analytic Treatment\n\nНазвание на Русском: Руки живого Бога / Отчет о психоаналитическом лечении')
            bot.send_message(call.message.chat.id,
                             'Автор: Anthony Molino\n\nОригинальное название: The Couch and the Tree / Dialogues in Psychoanalysis and Buddhism\n\nНазвание на Русском: Кушетка и дерево. Диалоги в психоанализе и буддизме')
            bot.send_message(call.message.chat.id,
                             'Автор: Raymond Corsini\n\nОригинальное название: Current Psychotherapies\n\nНазвание на Русском: Современная психотерапия')
            bot.send_message(call.message.chat.id, "Меню:", reply_markup=button3_1)

        if call.data == 'button3_3':
            msg2 = 'ВОПРОСЫ СОВРЕМЕННОГО ЮА. ПОСТЪЮНГИАНЦЫ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg2}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id,
                             'Автор: Ann Casement, David Tacey\n\nОригинальное название: The Idea of the Numinous / Contemporary Jungian and Psychoanalytic Perspectives\n\nНазвание на Русском: Идея нуминозного, современные юнгианские и психоаналитические перспективы')
            bot.send_message(call.message.chat.id,
                             'Автор: Thomas Moore\n\nОригинальное название: Dark Nights of the Soul / A Guide to Finding Your Way Through Life’s Ordeals\n\nНазвание на Русском: Темная ночь души')
            bot.send_message(call.message.chat.id,
                             'Автор: Thomas Moore\n\nОригинальное название: Care of the soul / A guide for cultivating depth and sacredness in everyday life\n\nНазвание на Русском: Забота о душе ')
            bot.send_message(call.message.chat.id,
                             'Автор: Ann Belford Ulanov\n\nОригинальное название: Finding space / Winnicott, God, and Psychic Reality\n\nНазвание на Русском: Поиск пространство / Винникотт, Бог и психическая реальность')
            bot.send_message(call.message.chat.id,
                             'Автор: Luigi Zoja\n\nОригинальное название: Drugs, Addiction and Initiation: The modern search for ritual\n\nНазвание на Русском: Наркомания: патология или поиск инициации')
            bot.send_message(call.message.chat.id,
                             'Автор: Joseph L. Henderson\n\nОригинальное название: Shadow and Self / Selected papers in Analytical Psychology\n\nНазвание на Русском: Тень и самость / Избранные работы по аналитической психологии')
            bot.send_message(call.message.chat.id,
                             'Автор: Nathen Schwartz-Salant\n\nОригинальное название: The Mystery of Human Relationship / Alchemy and the Transformation of the Self\n\nНазвание на Русском: Тайна человеческий отношений / Алхимия и трансформация самости')
            bot.send_message(call.message.chat.id,
                             'Автор: Dale Mathers, Melvin E. Miller and Osamu Ando\n\nОригинальное название: Self and No-self / Continuing the Dialogue Between Buddhism and Psychotherapy\n\nНазвание на Русском: Self и No-Self: Продолжение диалога между буддизмом и психотерапией.')
            bot.send_message(call.message.chat.id,
                             'Автор: Ann Casement\n\nОригинальное название: Post-Jungians Today / Key papers in contemporary analytical psychology\n\nНазвание на Русском: Постъюнгианство сегодня')
            bot.send_message(call.message.chat.id,
                             'Автор: Gottfried Heuer\n\nОригинальное название: Sacral Revolutions / Reflecting on the Work of Andrew Samuels / Cutting Edges in Psychoanalysis and Jungian Analysis\n\nНазвание на Русском: Сакральные революции / Размышляя над работами Эндрю Сэмуэльса / Передовая психоанализа и аналитической психологии')
            bot.send_message(call.message.chat.id,
                             'Автор: Ian Alister, Christopher Hauke\n\nОригинальное название: Contemporary Jungian Analysis / Post-Jungian Perspectives from the Society of Analytical Psychology\n\nНазвание на Русском: Современный юнгианский анализ / Постъюнгианский взгляд общества аналитической психологии')
            bot.send_message(call.message.chat.id,
                             'Автор: Andrew Samuels\n\nОригинальное название: A New Therapy for Politics?\n\nНазвание на Русском: Новая терапия в политике?')
            bot.send_message(call.message.chat.id, "Меню:", reply_markup=button3_1)

        if call.data == 'button3_4':
            msg3 = 'ЮНГ И О ЮНГЕ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg3}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id,
                             'Автор: C.G. Jung\n\nОригинальное название: C.G. Jung / Jung on Active Imagination\n\nНазвание на Русском: Юнг об активном воображении')
            bot.send_message(call.message.chat.id,
                             'Автор: Marilyn Nagy\n\nОригинальное название: Philosophical issues in the psychology of C.G. Jung\n\nНазвание на Русском: Философские вопросы в психологии К.Г. Юнга')
            bot.send_message(call.message.chat.id,
                             'Автор: Emma Jung\n\nОригинальное название: Animus and anima\n\nНазвание на Русском: Анимус и анима')
            bot.send_message(call.message.chat.id,
                             'Автор: Gerhard Adler\n\nОригинальное название: C.G. Jung Letters\n\nНазвание на Русском: Письма К.Г. Юнга')
            bot.send_message(call.message.chat.id,
                             'Автор: Coline Covington and Barbara Wharton\n\nОригинальное название: Sabina Spielrein / Forgotten Pioneer of Psychoanalysis\n\nНазвание на Русском: Сабина Шпильрейн / Забытый первопроходец психоанализа')
            bot.send_message(call.message.chat.id,
                             'Автор: Elphis Christopher and Hester Colomon\n\nОригинальное название: Jungian thought in the modern world\n\nНазвание на Русском: Юнгианская мысль в современном мире')
            bot.send_message(call.message.chat.id,
                             'Автор: David Tacey\n\nОригинальное название: Edge of the Sacred / Jung, Pyshe, Earth\n\nНазвание на Русском: Юнг и экопсихология')
            bot.send_message(call.message.chat.id,
                             'Автор: Robert Henderson\n\nОригинальное название: Living with Jung / “Enterviews” with Jungian Analysts\n\nНазвание на Русском: Жить с Юнгом / Беседы с юнгианскими аналитиками')
            bot.send_message(call.message.chat.id,
                             'Автор: Aniela Jaffe\n\nОригинальное название: From the life and work of C.G. Jung\n\nНазвание на Русском: О жизни и работе К.Г.Юнга')
            bot.send_message(call.message.chat.id,
                             'Автор: Theo A. Cope\n\nОригинальное название: Fear of Jung / The Complex Doctrine and Emotional Science\n\nНазвание на Русском: Страх Юнга / Комплекс доктрины и эмоциональная наука')
            bot.send_message(call.message.chat.id,
                             'Автор: Gottfrield M. Heuer\n\nОригинальное название: Freud’s ‘outstanding’ colleague / Jung’s Twin Brother\n\nНазвание на Русском: «Выдающийся» коллега Фрейда / Брат-близнец Юнга')
            bot.send_message(call.message.chat.id,
                             'Автор: John P. Conger\n\nОригинальное название: Jung & Reich / The Body as Shadow\n\nНазвание на Русском: Юнг и Райх / Тело как тень')
            bot.send_message(call.message.chat.id,
                             'Автор: Paul Bishop\n\nОригинальное название: Jung in contexts / A reader\n\nНазвание на Русском: Юнг в контексте / Чтец')
            bot.send_message(call.message.chat.id,
                             'Автор: Georg Nicolaus\n\nОригинальное название: C.G. Jung and Nikolai Berdyaev / Individuation and Person / A Critical Comparison\n\nНазвание на Русском: К. Г. Юнг и Н. Бердяев. Индивидуация и Личность. Критическое сравнение. ')
            bot.send_message(call.message.chat.id,
                             'Автор: Marvin Spiegelman Ph.D. and Mokusen Miyki, Ph.D.\n\nОригинальное название: Buddhism and Jungian Psychology\n\nНазвание на Русском: Буддизм и юнгианская психология ')
            bot.send_message(call.message.chat.id,
                             'Автор: Wolfgang Giegerich, David L. Miller, Greg Mogenson\n\nОригинальное название: Dialectics&Analytical Psychology\n\nНазвание на Русском: Диалектика и аналитическая психология')
            bot.send_message(call.message.chat.id,
                             'Автор: Christopher Hauke\n\nОригинальное название: Jung and the Postmodern / The interpretation of Realities\n\nНазвание на Русском: Юнг и постмодерн / Интерпретация реальности')
            bot.send_message(call.message.chat.id,
                             'Автор: Sonu Schamdasani\n\nОригинальное название: Jung and making of Modern Psychology / The Dream of a science\n\nНазвание на Русском: Юнг и создание современной психологии / мечта о науке')
            bot.send_message(call.message.chat.id,
                             'Автор: Raya A. Jones\n\nОригинальное название:  Jung, Psychology, Postmodernity\n\nНазвание на Русском: Юнг, психология, постмодернизм')
            bot.send_message(call.message.chat.id, "Меню:", reply_markup=button3_1)

        if call.data == 'button3_5':
            msg4 = 'АРХЕТИПИЧЕСКАЯ ПСИХОЛОГИЯ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg4}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id,
                             'Автор: James Hillman\n\nОригинальное название: The Soul’s Code In Search of Character and Calling\n\nНазвание на Русском: Код души. В поиске характера и призвания\n\nПеревод: да')
            bot.send_message(call.message.chat.id,
                             'Автор: James Hillman\n\nОригинальное название: Healing Fiction\n\nНазвание на Русском: Исцеляющий вымысел\n\nПеревод: да')
            bot.send_message(call.message.chat.id,
                             'Автор: James Hillman\n\nОригинальное название: Facing The Gods\n\nНазвание на Русском: Встреча с богами\n\nПеревод: да')
            bot.send_message(call.message.chat.id,
                             'Автор: James Hillman\n\nОригинальное название: Loose Ends\n\nНазвание на Русском: Нерешенные вопросы\n\nПеревод: да')
            bot.send_message(call.message.chat.id, "Меню:", reply_markup=button3_1)

        if call.data == 'button3_6':
            msg5 = 'МИФОАНАЛИЗ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg5}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id,
                             'Автор: Sylvia Brinton Perera\n\nОригинальное название: The scapegoat Complex / Toward a Mythology of Shadow and Guilt\n\nНазвание на Русском: Комплекс козла отпущения / К мифологии тени и вины')
            bot.send_message(call.message.chat.id,
                             'Автор: Michael Vannoy Adams\n\nОригинальное название: The mythological unconscious\n\nНазвание на Русском: Мифологическое бессознательное')
            bot.send_message(call.message.chat.id,
                             'Автор: Virginia Beane Rutter and Thomas Singer\n\nОригинальное название: Ancient Greece, Modern Psyche / Archetypes Evolving\n\nНазвание на Русском: Древняя Греция, современная психика / Развитие архетипов')
            bot.send_message(call.message.chat.id,
                             'Автор: G. Jung Institute of San Francisco\n\nОригинальное название: The Shaman From Elko\n\nНазвание на Русском: Шаман из Элько')
            bot.send_message(call.message.chat.id,
                             'Автор: Nancy Cater\n\nОригинальное название: Electra / Tracing a Feminine Myth Through the Western Imagination\n\nНазвание на Русском: Комплекс Электры в психологии женщины')
            bot.send_message(call.message.chat.id,
                             'Автор: Nancy J. Dougherty, Jacqueline J. West\n\nОригинальное название: The matrix and meaning of character / An Archetypal and Developmental Approach\n\nНазвание на Русском: Матрица и потенциал характера. С позиций архетипического подхода и теорий развития. В поисках неиссякаемого источника духа')
            bot.send_message(call.message.chat.id, "Меню:", reply_markup=button3_1)

        if call.data == 'button3_7':
            msg6 = 'РАБОТА СО СНОВИДЕНИЯМИ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg6}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id,
                             'Автор: Karen Signell\n\nОригинальное название: Wisdom of The Heart / Working with Women’s Dreams\n\nНазвание на Русском: Мудрость сердца / Работая с женскими снами')
            bot.send_message(call.message.chat.id,
                             'Автор: Maria F.  Mahoney\n\nОригинальное название: The Meaning in Dreams and Dreaming\n\nНазвание на Русском: Смысл во снах и сновидениях')
            bot.send_message(call.message.chat.id,
                             'Автор: Jeremy Taylor\n\nОригинальное название: Where People Fly and Water Runs Uphill\n\nНазвание на Русском: Где люди летают вода течет в гору')
            bot.send_message(call.message.chat.id,
                             'Автор: Edward C. Whitmont and Sylvia Brinton Perera\n\nОригинальное название: Dreams, a Portal to The Source\n\nНазвание на Русском: Сны, портал к источнику')
            bot.send_message(call.message.chat.id,
                             'Автор: Peter O’Connor\n\nОригинальное название: Dreams and The Search for Meaning\n\nНазвание на Русском: Сны и поиск смысла')
            bot.send_message(call.message.chat.id,
                             'Автор: Donald Broadribb\n\nОригинальное название: The Dream Story\n\nНазвание на Русском: История сновидения')
            bot.send_message(call.message.chat.id,
                             'Автор: Stephen Aizenstat, Ph.D.\n\nОригинальное название: Dream, Tending / Awakening to the Healing Power of Dreams\n\nНазвание на Русском: Дримтендинг. Метод исцеления сновидениями ')
            bot.send_message(call.message.chat.id,
                             'Автор: Lucy Huskinson\n\nОригинальное название: Dreaming The Myth Onwards / New Directions in Jungian Therapy and Thought\n\nНазвание на Русском: Развитие мифа во снах / Новые направления в Юнгианской терапии и мысли')
            bot.send_message(call.message.chat.id,
                             'Автор: Scott Moss\n\nОригинальное название: Dreams, Images and Fantasy, A Semantic Differential Casebook\n\nНазвание на Русском: Сны, образы и фантазии / Случаи пациентов с семантической и дифференциальной позиций')
            bot.send_message(call.message.chat.id, "Меню:", reply_markup=button3_1)

        if call.data == 'button3_8':
            msg7 = 'КИНО С ПОЗИЦИИ ЮА'
            bot.send_message(call.message.chat.id, f'<i><b>{msg7}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id,
                             'Автор: Greg Singh\n\nОригинальное название: Film after Jung / Post-Jungian Approaches to Film Theory\n\nНазвание на Русском: Кино после Юнга / Постъюнгианские подходы к теории кино')
            bot.send_message(call.message.chat.id,
                             'Автор: John Izod\n\nОригинальное название: Screen, Culture, Psyche / A Post-Jungian Approach to Working with the Audience\n\nНазвание на Русском: Экран, культура, психика / Постъюнгианский подход к работе а аудиторией')
            bot.send_message(call.message.chat.id,
                             'Автор: Terrie Waddell\n\nОригинальное название: Mis/takes / Archetype, Myth and Identity in Screen Fiction\n\nНазвание на Русском: Ошибки / Архетип, миф  и идентичность в кино')
            bot.send_message(call.message.chat.id, "Меню:", reply_markup=button3_1)

        if call.data == 'button3_9':
            msg8 = 'ФЕМИНИСТИЧЕСКОЕ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg8}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id,
                             'Автор: Jane Hollister Wheelwright\n\nОригинальное название: For women growing older / The Animus\n\nНазвание на Русском: Для стареющих женщин / Анимус')
            bot.send_message(call.message.chat.id,
                             'Автор: Robin Rush Linden, Darlene R. Pagano, Diana E.H. Russel, Susan Leigh Star\n\nОригинальное название: Against sadomasochism / A radical feminist analysis\n\nНазвание на Русском: Против садомазохизма / Радикальный феминистический анализ')
            bot.send_message(call.message.chat.id,
                             'Автор: Kim Chernin\n\nОригинальное название: The Obsession / Reflections on the Tyranny of Slenderness\n\nНазвание на Русском: Одержимость / Рефлексия над тиранией худобы')
            bot.send_message(call.message.chat.id,
                             'Автор: Lisa Schoenfielder and Barb Wieser, Vivian Mayer\n\nОригинальное название: Shadow on a tightrope / Writings by women on fat oppression\n\nНазвание на Русском: Тень на канате / Заметки женщины об угнетении толстых')
            bot.send_message(call.message.chat.id, "Меню:", reply_markup=button3_1)

        if call.data == 'button3_10':
            msg9 = 'РАЗНОЕ'
            bot.send_message(call.message.chat.id, f'<i><b>{msg9}</b></i>', parse_mode='html')
            bot.send_message(call.message.chat.id,
                             'Автор: Meredith B. Mitchell, Ph.D.\n\nОригинальное название: Hero or victim?\n\nНазвание на Русском: Герой или жертва?')
            bot.send_message(call.message.chat.id,
                             'Автор: M. Scott Peck, M.D.\n\nОригинальное название: The road less traveled\n\nНазвание на Русском: Нехоженая дорога')
            bot.send_message(call.message.chat.id,
                             'Автор: Eve Jackson\n\nОригинальное название: Food and Transformation / Imagery and Symbolism of Eating\n\nНазвание на Русском: Еда и трансформация / Образы и символы еды')
            bot.send_message(call.message.chat.id,
                             'Автор: Lillian Breslow Rubin\n\nОригинальное название: Worlds of Pain / Life in the Working-Class Family\n\nНазвание на Русском: Миры боли / Жизнь семьи из рабочего класса')
            bot.send_message(call.message.chat.id,
                             'Автор: Arthur Egendorf\n\nОригинальное название: Healing from the war / Trauma&Transformation after Vietnam\n\nНазвание на Русском: Исцеление от войны / Травма и трансформация после Вьетнама')
            bot.send_message(call.message.chat.id,
                             'Автор: Clarke G. Carney, Sarah Lynne McMahon\n\nОригинальное название: Exploring Contemporary Male/ Female Roles\n\nНазвание на Русском: Исследуя современные роли мужчины и женщины')
            bot.send_message(call.message.chat.id,
                             'Автор: Anthony Storr\n\nОригинальное название: Solitude / A return to the self\n\nНазвание на Русском: Одиночество / Возвращение к себе')
            bot.send_message(call.message.chat.id,
                             'Автор: Jane Hollister Wheelwright\n\nОригинальное название: The Ranch Papers / A California Memoir\n\nНазвание на Русском: Заметки с ранчо / Калифорнийские мемуары')
            bot.send_message(call.message.chat.id,
                             'Автор: Jane Hollister Wheelwright, Lynda Wheelwright Schmidt\n\nОригинальное название: The Long Shore / A psychological Experience of the Wilderness\n\nНазвание на Русском: Длинный берег / Психологический опыт на дикой природе')
            bot.send_message(call.message.chat.id,
                             'Автор: Oscar Handlin\n\nОригинальное название: The uprooted\n\nНазвание на Русском: Вырванный с корнем')
            bot.send_message(call.message.chat.id,
                             'Автор: Benjamin Sells\n\nОригинальное название: The Soul of the Law / Understanding Lawyers and the law\n\nНазвание на Русском: Душа закона / Понять юристов и закон')
            bot.send_message(call.message.chat.id,
                             'Автор: David Brandon\n\nОригинальное название: Zen in the Art of Helping\n\nНазвание на Русском: Дзен в искусстве помощи')
            bot.send_message(call.message.chat.id,
                             'Автор: Joseph Coppin, Elizabeth Nelson\n\nОригинальное название: The Art of Inquiry / A depth Psychological Perspective\n\nНазвание на Русском: Искусство исследования / Взгляд со стороны глубинной психологии')
            bot.send_message(call.message.chat.id,
                             'Автор: James Fadiman, Robert Frager\n\nОригинальное название: Personality and personal growth\n\nНазвание на Русском: Личность и личностный рост')
            bot.send_message(call.message.chat.id,
                             'Автор: Erich Fromm\n\nОригинальное название: Love, sexuality, and matriarchy: about gender\n\nНазвание на Русском: Любовь,сексуальность и матриархат: о гендере' )
            bot.send_message(call.message.chat.id, "Меню:", reply_markup=button3_1)

        if call.data == 'button4_1':
            bot.send_message(call.message.chat.id,
                             '✅1.  «Чёрное лебедь» (2010) — Главная героиня, балерина Нина, сталкивается с конфликтом '
                             'между своими амбициями и внутренними страхами, что приводит к появлению болезненных '
                             'расстройств и размыванием границы между реальностью и фантазией.')
            bot.send_message(call.message.chat.id,
                             '✅2.  «Остров проклятых» (2010) — В этом фильме федеральные маршалы расследуют отравление '
                             'пациентов из психиатрической больницы на острове. По мере раскрытия загадочных событий '
                             'становится ясно, что травма прошлого играет решающую роль '
                             'в психическом состоянии персонажей.')
            bot.send_message(call.message.chat.id,
                             '✅3.  "Блеск" (Shine, 1996) - этот фильм рассказывает историю Дэвида Хелфгота, музыканта '
                             'с блестящими способностями, который столкнулся с давлением отца и подавленными травмами '
                             'в детстве. Внутренний конфликт и его последствия подробно показаны в фильме.')
            bot.send_message(call.message.chat.id,
                             '✅4.«Вечное сияние чистого разума» (2004) — этот фильм исследует тему памяти и забвения,'
                             ' когда главные герои решают стереть воспоминания о своих отношениях. Путешествие в их '
                             'внутренний мир происходит, как травмы и эмоциональные события, которые '
                             'могут оказать влияние на психику.')
            bot.send_message(call.message.chat.id,
                             '✅5.«Под песком» (2000) — В этом фильме главная героиня сталкивается с трагическим'
                             ' отравлением мужа и начинает переживать его присутствие и общение в своем воображении. '
                             'Это можно рассматривать как пример работы механизма последействия травмы '
                             'и проявления бессознательных желаний.')
            bot.send_message(call.message.chat.id, "Меню:", reply_markup=button4)


bot.infinity_polling(1000)
