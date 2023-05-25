import telebot
from telebot import types
import requests
import datetime


TOKEN = "5821613520:AAFM7de1mQvJg1T6HiMskQe72JhS_icoBL8"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Мы рады приветствовать Вас!!! "
                                      "Ваш заказ №_______ "
                                      "Ожидает получения по адресу:______ "
                                      "Забирите его до: дд.мм.гггг Код получения: х-х-х-х.  ")
    return ()


# Сообщение по факту получения
@bot.message_handler(commands=['received'])
def received(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    button1 = types.InlineKeyboardButton('1', callback_data="1")
    button2 = types.InlineKeyboardButton('2', callback_data="2")
    button3 = types.InlineKeyboardButton('3', callback_data="3")
    button4 = types.InlineKeyboardButton('4', callback_data="4")
    button5 = types.InlineKeyboardButton('5', callback_data="5")

    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, " Вы получили заказ! Спасибо, что выбрали именно нас. "
                                      "Оцените пожалуйста работу нашего сервиса и качество доставки от 1 до 5 - это "
                                      "поможет нам стать лучше. ",
                     reply_markup=markup)
    return ()


# Нажали на кнопку 1
@bot.callback_query_handler(func=lambda call1: call1.data == "1")
def answr(call1):
    answr1 = types.InlineKeyboardMarkup(row_width=2)
    yes = types.InlineKeyboardButton('Да', callback_data="yes")
    no = types.InlineKeyboardButton('Нет, спасибо', callback_data="no")
    answr1.add(yes, no)
    bot.send_message(call1.from_user.id, " Хотите оставить небольшой отзыв? Ваше мнение важно для нас.",
                     reply_markup=answr1)
    bot.answer_callback_query(callback_query_id=call1.id)
    mark = 1
    print(mark)

    # продолжение оставления отзыва
    @bot.callback_query_handler(func=lambda callback_obj1: True)
    def callback_function1(callback_obj1):
        if callback_obj1.data == "yes":
            bot.send_message(callback_obj1.from_user.id, "Напишите свой отзыв и отправьте мне, я его передам.")

            # Ответ бота на любое написанное сообщение.
            @bot.message_handler(func=lambda message1: True)
            def answr111(message1):
                bot.reply_to(message1, "Спасибо, что оставили отзыв!")
                bot.answer_callback_query(callback_query_id=callback_obj1.id)
                # сбор инфы о пользователе, текста сообщения
                usertext = message1.text
                print(usertext)
                reviewdata = datetime.datetime.fromtimestamp(message1.date)
                print(reviewdata.strftime('%Y-%m-%d %H:%M:%S'))
                #username = message1.from_user.username
                #print(username)
                #chatid = message1.chat.id
                #print(chatid)
                requests.post('http://26.200.185.61:8080/addReview/',
                              json={
                                  "usertext": usertext,
                                  "mark": mark,
                                  "reviewdate": reviewdata,
                                  "adress": "Москва, Садовая-Кудринская ул., 3Б",
                                  "clusternumber": -999,
                                  "classnumber": 1,  #значение нажатой кнопки
                                  "article": 125478,
                                  "seller": "YandexMarket(TG bot)",
                                  "latitude": 0,
                                  "longtude": 0,
                                  #"username": username,
                                  #"chatid": chatid

                              }
                              )

            return ()
        elif callback_obj1.data == "no":
            bot.send_message(callback_obj1.from_user.id, "Спасибо, что использовали наш сервис, до новых встреч!")
            bot.answer_callback_query(callback_query_id=callback_obj1.id)
            reviewdata = datetime.datetime.fromtimestamp(callback_obj1.date)
            print(reviewdata.strftime('%Y-%m-%d %H:%M:%S'))
            usertext = 0
            #username = callback_obj1.from_user.username
            #print(username)
            #chatid = callback_obj1.from_user.id
            #print(chatid)

            requests.post('http://26.200.185.61:8080/addReview/',
                          json={
                              "usertext": usertext,
                                  "mark": mark,
                                  "reviewdate": reviewdata,
                                  "adress": "Москва, Садовая-Кудринская ул., 3Б",
                                  "clusternumber": -999,
                                  "classnumber": 1,  #значение нажатой кнопки
                                  "article": 125478,
                                  "seller": "YandexMarket(TG bot)",
                                  "latitude": 0,
                                  "longtude": 0,
                                  #"username": username,
                                  #"chatid": chatid
                          }
                          )
        bot.answer_callback_query(callback_query_id=callback_obj1.id)
        return ()

    return ()


# Нажали на кнопку 2
@bot.callback_query_handler(func=lambda call2: call2.data == "2")
def answr(call2):
    answr222 = types.InlineKeyboardMarkup(row_width=2)
    yes = types.InlineKeyboardButton('Да', callback_data="yes")
    no = types.InlineKeyboardButton('Нет, спасибо', callback_data="no")
    answr222.add(yes, no)
    bot.send_message(call2.from_user.id, " Хотите оставить небольшой отзыв? Ваше мнение важно для нас.",
                     reply_markup=answr222)
    bot.answer_callback_query(callback_query_id=call2.id)
    mark = 2
    print(mark)

    # продолжение оставления отзыва
    @bot.callback_query_handler(func=lambda callback_obj2: True)
    def callback_function1(callback_obj2):
        if callback_obj2.data == "yes":
            bot.send_message(callback_obj2.from_user.id, "Напишите свой отзыв и отправьте мне, я его передам.")

            # Ответ бота на любое написанное сообщение.
            @bot.message_handler(func=lambda message2: True)
            def answr1(message2):
                bot.reply_to(message2, "Спасибо, что оставили отзыв!")
                bot.answer_callback_query(callback_query_id=callback_obj2.id)
                # сбор инфы о пользователе, текста сообщения
                usertext = message2.text
                print(usertext)
                reviewdata = message2.date
                print(reviewdata)
                username = message2.from_user.username
                print(username)
                chatid = message2.chat.id
                print(chatid)

                requests.post('http://26.200.185.61:8080/addReview/',
                              json={
                                  "usertext": usertext,
                                  "mark": mark,
                                  "adress": 0,
                                  "reviewdate": reviewdata,
                                  "clusternumber": 0,
                                  "article": 125478,
                                  "seller": "YandexMarket(TG bot)",
                                  "latitude": 0,
                                  "longtude": 0,
                                  "username": username,
                                  "chatid": chatid,
                                  "classnumber": 123
                              }
                              )

            return ()


        elif callback_obj2.data == "no":
            bot.send_message(callback_obj2.from_user.id, "Спасибо, что использовали наш сервис, до новых встреч!")
            bot.answer_callback_query(callback_query_id=callback_obj2.id)
            reviewdata = callback_obj2.message.date
            print(reviewdata)
            username = callback_obj2.from_user.username
            print(username)
            chatid = callback_obj2.from_user.id
            print(chatid)

            requests.post('http://26.200.185.61:8080/addReview/',
                          json={
                              "usertext": 0,
                              "mark": mark,
                              "adress": 0,
                              "reviewdate": reviewdata,
                              "clusternumber": 0,
                              "article": 125478,
                              "seller": "YandexMarket(TG bot)",
                              "latitude": 0,
                              "longtude": 0,
                              "username": username,
                              "chatid": chatid,
                              "classnumber": 123
                          }
                          )
        bot.answer_callback_query(callback_query_id=callback_obj2.id)
        return ()

    return ()


# Нажали на кнопку 3
@bot.callback_query_handler(func=lambda call3: call3.data == "3")
def answr(call3):
    answr333 = types.InlineKeyboardMarkup(row_width=2)
    yes = types.InlineKeyboardButton('Да', callback_data="yes")
    no = types.InlineKeyboardButton('Нет, спасибо', callback_data="no")
    answr333.add(yes, no)
    bot.send_message(call3.from_user.id, " Хотите оставить небольшой отзыв? Ваше мнение важно для нас.",
                     reply_markup=answr333)
    bot.answer_callback_query(callback_query_id=call3.id)
    mark = 3
    print(mark)

    # продолжение оставления отзыва
    @bot.callback_query_handler(func=lambda callback_obj3: True)
    def callback_function1(callback_obj3):
        if callback_obj3.data == "yes":
            bot.send_message(callback_obj3.from_user.id, "Напишите свой отзыв и отправьте мне, я его передам.")

            # Ответ бота на любое написанное сообщение.
            @bot.message_handler(func=lambda message3: True)
            def answr1(message3):
                bot.reply_to(message3, "Спасибо, что оставили отзыв!")
                bot.answer_callback_query(callback_query_id=callback_obj3.id)
                # сбор инфы о пользователе, текста сообщения
                usertext = message3.text
                print(usertext)
                reviewdata = message3.date
                print(reviewdata)
                username = message3.from_user.username
                print(username)
                chatid = message3.chat.id
                print(chatid)

                requests.post('http://26.200.185.61:8080/addReview/',
                              json={
                                  "usertext": usertext,
                                  "mark": mark,
                                  "adress": 0,
                                  "reviewdate": reviewdata,
                                  "clusternumber": 0,
                                  "article": 125478,
                                  "seller": "YandexMarket(TG bot)",
                                  "latitude": 0,
                                  "longtude": 0,
                                  "username": username,
                                  "chatid": chatid,
                                  "classnumber": 123
                              }
                              )

            return ()


        elif callback_obj3.data == "no":
            bot.send_message(callback_obj3.from_user.id, "Спасибо, что использовали наш сервис, до новых встреч!")
            bot.answer_callback_query(callback_query_id=callback_obj3.id)
            reviewdata = callback_obj3.message.date
            print(reviewdata)
            username = callback_obj3.from_user.username
            print(username)
            chatid = callback_obj3.from_user.id
            print(chatid)

            requests.post('http://26.200.185.61:8080/addReview/',
                          json={
                              "usertext": 0,
                              "mark": mark,
                              "adress": 0,
                              "reviewdate": reviewdata,
                              "clusternumber": 0,
                              "article": 125478,
                              "seller": "YandexMarket(TG bot)",
                              "latitude": 0,
                              "longtude": 0,
                              "username": username,
                              "chatid": chatid,
                              "classnumber": 123
                          }
                          )

        return ()

    return ()


# Нажали на кнопку 4
@bot.callback_query_handler(func=lambda call4: call4.data == "4")
def answr444(call4):
    answr444 = types.InlineKeyboardMarkup(row_width=2)
    yes = types.InlineKeyboardButton('Да', callback_data="yes")
    no = types.InlineKeyboardButton('Нет, спасибо', callback_data="no")
    answr444.add(yes, no)
    bot.send_message(call4.from_user.id, " Хотите оставить небольшой отзыв? Ваше мнение важно для нас.",
                     reply_markup=answr444)
    bot.answer_callback_query(callback_query_id=call4.id)
    mark = 4
    print(mark)

    # продолжение оставления отзыва
    @bot.callback_query_handler(func=lambda callback_obj4: True)
    def callback_function1(callback_obj4):
        if callback_obj4.data == "yes":
            bot.send_message(callback_obj4.from_user.id, "Напишите свой отзыв и отправьте мне, я его передам.")

            # Ответ бота на любое написанное сообщение.
            @bot.message_handler(func=lambda message4: True)
            def answr1(message4):
                bot.reply_to(message4, "Спасибо, что оставили отзыв!")
                bot.answer_callback_query(callback_query_id=callback_obj4.id)
                # сбор инфы о пользователе, текста сообщения
                usertext = message4.text
                print(usertext)
                reviewdata = message4.date
                print(reviewdata)
                username = message4.from_user.username
                print(username)
                chatid = message4.chat.id
                print(chatid)

                requests.post('http://26.200.185.61:8080/addReview/',
                              json={
                                  "usertext": usertext,
                                  "mark": mark,
                                  "adress": 0,
                                  "reviewdate": reviewdata,
                                  "clusternumber": 0,
                                  "article": 125478,
                                  "seller": "YandexMarket(TG bot)",
                                  "latitude": 0,
                                  "longtude": 0,
                                  "username": username,
                                  "chatid": chatid,
                                  "classnumber": 123
                              }
                              )

            return ()
        elif callback_obj4.data == "no":
            bot.send_message(callback_obj4.from_user.id, "Спасибо, что использовали наш сервис, до новых встреч!")
            bot.answer_callback_query(callback_query_id=callback_obj4.id)
            reviewdata = callback_obj4.message.date
            print(reviewdata)
            username = callback_obj4.from_user.username
            print(username)
            chatid = callback_obj4.from_user.id
            print(chatid)

            requests.post('http://26.200.185.61:8080/addReview/',
                          json={
                              "usertext": 0,
                              "mark": mark,
                              "adress": 0,
                              "reviewdate": reviewdata,
                              "clusternumber": 0,
                              "article": 125478,
                              "seller": "YandexMarket(TG bot)",
                              "latitude": 0,
                              "longtude": 0,
                              "username": username,
                              "chatid": chatid,
                              "classnumber": 123
                          }
                          )

        return ()

    return ()


# Нажали на кнопку 5
@bot.callback_query_handler(func=lambda call5: call5.data == "5")
def answr555(call5):
    answr555 = types.InlineKeyboardMarkup(row_width=2)
    yes = types.InlineKeyboardButton('Да', callback_data="yes")
    no = types.InlineKeyboardButton('Нет, спасибо', callback_data="no")
    answr555.add(yes, no)
    bot.send_message(call5.from_user.id, " Хотите оставить небольшой отзыв? Ваше мнение важно для нас.",
                     reply_markup=answr555)
    bot.answer_callback_query(callback_query_id=call5.id)
    mark = 5
    print(mark)

    # продолжение оставления отзыва
    @bot.callback_query_handler(func=lambda callback_obj5: True)
    def callback_function1(callback_obj5):
        if callback_obj5.data == "yes":
            bot.send_message(callback_obj5.from_user.id, "Напишите свой отзыв и отправьте мне, я его передам.")

            # Ответ бота на любое написанное сообщение.
            @bot.message_handler(func=lambda message5: True)
            def answr1(message5):
                bot.reply_to(message5, "Спасибо, что оставили отзыв!")
                bot.answer_callback_query(callback_query_id=callback_obj5.id)
                # сбор инфы о пользователе, текста сообщения
                usertext = message5.text
                print(usertext)
                reviewdata = message5.date
                print(reviewdata)
                username = message5.from_user.username
                print(username)
                chatid = message5.chat.id
                print(chatid)

                requests.post('http://26.200.185.61:8080/addReview/',
                              json={
                                  "usertext": usertext,
                                  "mark": mark,
                                  "adress": 0,
                                  "reviewdate": reviewdata,
                                  "clusternumber": 0,
                                  "article": 125478,
                                  "seller": "YandexMarket(TG bot)",
                                  "latitude": 0,
                                  "longtude": 0,
                                  "username": username,
                                  "chatid": chatid,
                                  "classnumber": 123
                              }
                              )

            return ()
        elif callback_obj5.data == "no":
            bot.send_message(callback_obj5.from_user.id, "Спасибо, что использовали наш сервис, до новых встреч!")
            bot.answer_callback_query(callback_query_id=callback_obj5.id)
            reviewdata = callback_obj5.message.date
            print(reviewdata)
            username = callback_obj5.from_user.username
            print(username)
            chatid = callback_obj5.from_user.id
            print(chatid)

            requests.post('http://26.200.185.61:8080/addReview/',
                          json={
                              "usertext": 0,
                              "mark": mark,
                              "adress": 0,
                              "reviewdate": reviewdata,
                              "clusternumber": 0,
                              "article": 125478,
                              "seller": "YandexMarket(TG bot)",
                              "latitude": 0,
                              "longtude": 0,
                              "username": username,
                              "chatid": chatid,
                              "classnumber": 123
                          }
                          )

        return ()

    return ()


# #реализация взаимодействия по команде help
# @bot.message_handler(commands=['help'])
# def help(cmd_help):
#     mrkp = types.InlineKeyboardMarkup(row_width=1)
#     button01 = types.InlineKeyboardButton('Проблемы с товаром',callback_data='11')
#     button02 = types.InlineKeyboardButton('Возникли проблемы с курьером', callback_data='12')
#     button03 = types.InlineKeyboardButton('Проблемы с постаматом', callback_data='13')
#     button04 = types.InlineKeyboardButton('Долго не приходит посылка', callback_data='14')
#     button05 = types.InlineKeyboardButton('Другое', callback_data='15')
#
#     mrkp.add(button01, button02, button03, button04, button05)
#     bot.send_message(cmd_help.chat.id, "Если возникли какие-то проблемы или сложности, просто выберите подходящее, "
#                                        "мы будем рады Вам помочь",
#                      reply_markup=mrkp)
#     return ()
#
#  #нажали на кнопку "проблемы с товаром"
# @bot.callback_query_handler(func=lambda call_help11: call_help11.data == "11")
# def answr2(call_help11):
#     bot.send_message(call_help11.from_user.id, "Подробно опишите возникшую проблему")
#     bot.answer_callback_query(callback_query_id=call_help11.id)
#     @bot.message_handler(func=lambda send_admin11: True)
#     def send_admin(send_admin11):
#         bot.send_message(send_admin11.from_user.id,
#                          "Я отправил проблему нашим специалистам, в скором времени с Вами свяжутся и помогут")
#         username_help = send_admin11.from_user.username
#         bot.send_message('____id admin_____',
#                          "Поступила жалоба(Другое) от: " + username_help)  # вместо id admin надо указать id того, кому будут пересылаться сообщения в ТГ
#         bot.send_message('___id admin______',
#                          send_admin15.text)  # вместо id admin надо указать id того, кому будут пересылаться сообщения в ТГ
#         return ()
#     return ()
#  #нажали на кнопку"Возникли проблемы с курьером"
# @bot.callback_query_handler(func=lambda call_help12: call_help12.data == "12")
# def answr2(call_help12):
#     bot.send_message(call_help12.from_user.id, "Подробно опишите возникшую проблему")
#     bot.answer_callback_query(callback_query_id=call_help12.id)
#     @bot.message_handler(func=lambda send_admin12: True)
#     def send_admin(send_admin12):
#         bot.send_message(send_admin12.from_user.id,
#                          "Я отправил проблему нашим специалистам, в скором времени с Вами свяжутся и помогут")
#         username_help = send_admin12.from_user.username
#         bot.send_message('____id admin_____',
#                          "Поступила жалоба(Другое) от: " + username_help)  # вместо id admin надо указать id того, кому будут пересылаться сообщения в ТГ
#         bot.send_message('___id admin______',
#                          send_admin15.text)  # вместо id admin надо указать id того, кому будут пересылаться сообщения в ТГ
#         return ()
#     return ()
#
#  #нажали на кнопку"Проблемы с постаматом"
# @bot.callback_query_handler(func=lambda call_help13: call_help13.data == "13")
# def answr2(call_help13):
#     bot.send_message(call_help13.from_user.id, "Подробно опишите возникшую проблему")
#     bot.answer_callback_query(callback_query_id=call_help13.id)
#     @bot.message_handler(func=lambda send_admin13: True)
#     def send_admin(send_admin13):
#         bot.send_message(send_admin13.from_user.id,
#                          "Я отправил проблему нашим специалистам, в скором времени с Вами свяжутся и помогут")
#         username_help = send_admin13.from_user.username
#         bot.send_message('____id admin_____',
#                          "Поступила жалоба(Другое) от: " + username_help)  # вместо id admin надо указать id того, кому будут пересылаться сообщения в ТГ
#         bot.send_message('___id admin______',
#                          send_admin15.text)  # вместо id admin надо указать id того, кому будут пересылаться сообщения в ТГ
#         return ()
#     return ()
#
#  #нажали на кнопку"Долго не приходит посылка"
# @bot.callback_query_handler(func=lambda call_help14: call_help14.data == "14")
# def answr2(call_help14):
#     bot.send_message(call_help14.from_user.id, "Подробно опишите возникшую проблему")
#     bot.answer_callback_query(callback_query_id=call_help14.id)
#     @bot.message_handler(func=lambda send_admin14: True)
#     def send_admin(send_admin14):
#         bot.send_message(send_admin14.from_user.id,
#                          "Я отправил проблему нашим специалистам, в скором времени с Вами свяжутся и помогут")
#         username_help = send_admin14.from_user.username
#         bot.send_message('____id admin_____',
#                          "Поступила жалоба(Другое) от: " + username_help)  # вместо id admin надо указать id того, кому будут пересылаться сообщения в ТГ
#         bot.send_message('___id admin______',
#                          send_admin15.text)  # вместо id admin надо указать id того, кому будут пересылаться сообщения в ТГ
#         return ()
#     return ()
#
#  #нажали на кнопку"Другое"
# @bot.callback_query_handler(func=lambda call_help15: call_help15.data == "15")
# def answr2(call_help15):
#     bot.send_message(call_help15.from_user.id, "Подробно опишите возникшую проблему")
#     bot.answer_callback_query(callback_query_id=call_help15.id)
#     @bot.message_handler(func=lambda send_admin15: True)
#     def send_admin(send_admin15):
#         bot.send_message(send_admin15.from_user.id,
#                          "Я отправил проблему нашим специалистам, в скором времени с Вами свяжутся и помогут")
#         username_help = send_admin15.from_user.username
#         bot.send_message('____id admin_____', "Поступила жалоба(Другое) от: "+username_help) #вместо id admin надо указать id того, кому будут пересылаться сообщения в ТГ
#         bot.send_message('___id admin______', send_admin15.text)#вместо id admin надо указать id того, кому будут пересылаться сообщения в ТГ
#         return ()
#
#     return ()


bot.polling(none_stop=True)
