import telebot
from telebot.types import InlineKeyboardMarkup as ikm
from telebot.types import InlineKeyboardButton as ikb

button = ikm(row_width=1)
urlButton = ikb('Сайт Преподавателя', url='https://eriksp.ru/')
button.add(urlButton)


button1_1 = ikm(row_width=3)
button_1 = ikm(row_width=1)
inline_kb1_1 = ikb('Эгo', callback_data='button1_1')
inline_kb1_2 = ikb('Персона', callback_data='button1_2')
inline_kb1_3 = ikb('Тень', callback_data='button1_3')
inline_kb1_4 = ikb('Анима-Анимус', callback_data='button1_4')
inline_kb1_5 = ikb('Самость', callback_data='button1_5')
inline_kb1_6 = ikb('Индивидуация', callback_data='button1_6')
inline_kb1_7 = ikb('Комплекс. Архетип. Коллективное бессознательное', callback_data='button1_7')
inline_kb1_8 = ikb('Типология Юнга', callback_data='button1_8')
inline_kb1_9 = ikb('Сновидение.Образы и Символы', callback_data='button1_9')
inline_kb1_10 = ikb('Работа с образами в сновидениях', callback_data='button1_10')
inline_kb1_11 = ikb('Перенос-контрперенос', callback_data='button1_11')
inline_kb1_12 = ikb('Алхимия', callback_data='button1_12')
inline_kb1_13 = ikb('Методы работы в глубинной психологии', callback_data='button1_13')
button1_1.add(inline_kb1_1, inline_kb1_2, inline_kb1_3, inline_kb1_4, inline_kb1_5, inline_kb1_6, inline_kb1_7, inline_kb1_8, inline_kb1_9, inline_kb1_10, inline_kb1_11, inline_kb1_12, inline_kb1_13)
button_1.add(inline_kb1_1, inline_kb1_2, inline_kb1_3, inline_kb1_4, inline_kb1_5, inline_kb1_6, inline_kb1_7, inline_kb1_8, inline_kb1_9, inline_kb1_10, inline_kb1_11, inline_kb1_12, inline_kb1_13)


button2_1 = ikm(row_width=1)
button_2 = ikm(row_width=1)
inline_kb2_2 = ikb('ПСИХОАНАЛИТИЧЕСКАЯ ПСИХОСОМАТИКА', callback_data='button2_2')
inline_kb2_3 = ikb('ДЕПРЕССИЯ И МЕЛАНХОЛИЯ', callback_data='button2_3')
inline_kb2_4 = ikb('ДИАГНОСТИКА И ТЕХНИКА В ПСИХОАНАЛИЗЕ', callback_data='button2_4')
inline_kb2_5 = ikb('СЕСКСУАЛЬНОСТЬ/ПЕРВЕРСИИ/ИНЦЕСТ', callback_data='button2_5')
inline_kb2_6 = ikb('РАННИЕ ОТНОШЕНИЯ', callback_data='button2_6')
inline_kb2_7 = ikb('СНОВИДЕНИЯ И СИМВОЛИЗАЦИЯ', callback_data='button2_7')
inline_kb2_8 = ikb('ПСИХОАНАЛИЗ И КУЛЬТУРА', callback_data='button2_8')
button_2.add(inline_kb2_2, inline_kb2_3, inline_kb2_4, inline_kb2_5, inline_kb2_6, inline_kb2_7, inline_kb2_8)
button2_1.add(inline_kb2_2, inline_kb2_3, inline_kb2_4, inline_kb2_5, inline_kb2_6, inline_kb2_7, inline_kb2_8)


button3_1 = ikm(row_width=1)
button_3 = ikm(row_width=1)
inline_kb3_1 = ikb('ОСНОВЫ ЮА: КОНЦЕПЦИИ И ТЕХНИКИ', callback_data='button3_1')
inline_kb3_2 = ikb('ТЕРАПЕВТИЧЕСКИЕ ПРАКТИКИ', callback_data='button3_2')
inline_kb3_3 = ikb('ВОПРОСЫ СОВРЕМЕННОГО ЮА. ПОСТЪЮНГИАНЦЫ', callback_data='button3_3')
inline_kb3_4 = ikb('ЮНГ И О ЮНГЕ', callback_data='button3_4')
inline_kb3_5 = ikb('АРХЕТИПИЧЕСКАЯ ПСИХОЛОГИЯ', callback_data='button3_5')
inline_kb3_6 = ikb('МИФОАНАЛИЗ', callback_data='button3_6')
inline_kb3_7 = ikb('РАБОТА СО СНОВИДЕНИЯМИ', callback_data='button3_7')
inline_kb3_8 = ikb('КИНО С ПОЗИЦИИ ЮА', callback_data='button3_8')
inline_kb3_9 = ikb('ФЕМИНИСТИЧЕСКОЕ', callback_data='button3_9')
inline_kb3_10 = ikb('РАЗНОЕ', callback_data='button3_10')
button_3.add(inline_kb3_1, inline_kb3_2, inline_kb3_3, inline_kb3_4, inline_kb3_5, inline_kb3_6, inline_kb3_7, inline_kb3_8, inline_kb3_9, inline_kb3_10)
button3_1.add(inline_kb3_1, inline_kb3_2, inline_kb3_3, inline_kb3_4, inline_kb3_5, inline_kb3_6, inline_kb3_7, inline_kb3_8, inline_kb3_9, inline_kb3_10)


button4 = ikm(row_width=1)
inline_kb4_1 = ikb('Фильмы иллюстрирующих механизм последействия травмы по Фрейду.', callback_data='button4_1')
button_3.add(inline_kb4_1)