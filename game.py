def epilogue_part2():
    global player_name
    global good_people_dict
    print()
    print(" Сегодняшний день дал вам многое понять. Например, что пора бы сесть за проект.")
    print(" Что будем делать?")
    print()
    print(" 1 — Делать проект")
    if good_people_dict["Гардеробщица_Номер"] == "Yes" or good_people_dict["Бариста_Номер"] == "Yes":
        print(" # — Созидать этот мир.")
    print()
    variant = input("<?>: ")
    if variant == "1" or variant == " 1":
        print()
        unremarkble()
    elif variant == "#" or variant == " #":
        print()
        if good_people_dict["Гардеробщица_Номер"] == "Yes":
            print(" Вы вышли на балкон.")
            print()
            sleeping(60_000_000)
            print(" На ваш телефон приходит сообщение от Гардеробщицы.")
            print()
            sleeping(70_000_000)
            print(" — Здравствуй,", player_name, ".")
            sleeping(70_000_000)
            print(" — Я надеюсь, вы достойно провели этот день.")
            sleeping(70_000_000)
            print(" — Надеюсь, вы удовлетоврены тем, что совершили.")
            sleeping(70_000_000)
            print(" — Каждое совершаемое действие имеет определенный вес, задает определённый вектор.")
            sleeping(70_000_000)
            print(" — Я хочу вам сказать: тот вектор, что вы выбрали, вероятнее всего не ваш.")
            sleeping(70_000_000)
            print(" — Вы достигли того, что хотели. Но это не то, что можно считать «истинным путём».")
            sleeping(70_000_000)
            print(" — Это не каночниный путь. Вам предстоит жить с этим.")
            sleeping(70_000_000)
            print(" — Теперь вы знаете правду.")
            sleeping(70_000_000)
            print(" — До скорых встреч,", player_name, ".")
            sleeping(70_000_000)
            print(" — Возможно, когда то вы поймете меня.")
            print()
            sleeping(70_000_000)
            print(" Сообщение было прочитано вами. Вы вернулись с балкона и легли спать. День закончен.")
            print()
            for _ in range(6):
                print(".")
                sleeping(70_000_000)
            print()
            print(" Stunning Ending.")
            print()
            sleeping(70_000_000)
            authors()
        elif good_people_dict["Бариста_Номер"] == "Yes":
            print(" Вы вышли на балкон.")
            print()
            sleeping(60_000_000)
            print(" На ваш телефон приходит сообщение от Баристы.")
            print()
            sleeping(70_000_000)
            print(" — Я ждал вас. Ждал на «Культе».")
            sleeping(70_000_000)
            print(" — Мне казалось, что мы интересны друг другу.")
            sleeping(70_000_000)
            print(" — Казалось, что наша встреча предначертана судьбой.")
            sleeping(70_000_000)
            print(" — Возможно, я ошибался.")
            sleeping(70_000_000)
            print(" — Порой, нам стоит пойти другой дорогой. Попробовать вести себя иначе.")
            sleeping(70_000_000)
            print(" — В принципе, вы так и поступили.")
            sleeping(70_000_000)
            print(" — Прощайте. Возможно, мы с вами больше не увидимся.")
            sleeping(90_000_000)
            print(" — Лишь если ваша дорога будет Кофейной...")
            print()
            sleeping(70_000_000)
            print(" Сообщение было прочитано вами. Вы вернулись с балкона и легли спать. День закончен.")
            print()
            for _ in range(6):
                print(".")
                sleeping(60_000_000)
            print()
            print(" Hinting Ending.")
            print()
            sleeping(70_000_000)
            authors()
        elif good_people_dict["Гардеробщица_Номер"] == "No" and good_people_dict["Бариста_Номер"] == "No":
            print()
            sleeping(70_000_000)
            print("<?>: Чего вы ждали увидеть? Вы пытаетесь открыть занавес того, к чему не пришли.")
            sleeping(70_000_000)
            print("<?>: Ступайте спать. Или проходить игру заново. Нам больше не о чем говорить.")
            sleeping(70_000_000)
            print()
            for _ in range(4):
                print(".")
                sleeping(60_000_000)
            print()
            print("Fourth Wall Ending.")
            sleeping(70_000_000)
            authors()
    else:
        print()
        print(" Вы постояли на балконе еще несколько минут. Затем вернулись в комнату.")
        sleeping(70_000_000)
        print(" Вы задумались над сегодняшним днём. Он был... таков, каким он случился.")
        sleeping(70_000_000)
        print(" Пора за работу.")
        print()
        unremarkble()


def unremarkble():
    sleeping(60_000_000)
    for _ in range(5):
        print(".")
        sleeping(90_000_000)
    print()
    print(" Вы провели вечер за работой над проектом. День был трудный, но вы справились.")
    print()
    sleeping(90_000_000)
    print(" Вы можете гордиться собой.")
    print()
    sleeping(60_000_000)
    for _ in range(6):
        print(".")
        sleeping(60_000_000)
    print()
    print(" Unremarkble Ending.")
    print()
    sleeping(60_000_000)
    authors()


def epilogue():
    global good_people_dict
    global toHelpFriend
    global BestEndingPoints
    sleeping(90_000_000)
    print(" Последняя пара проходит совершенно незаметно, и после её окочания")
    print(" вы отправляетесь домой, в «Дубки».")
    print()
    if toHelpFriend:
        print(" Вернувшись домой, вы вспомнили о том, что ваша подруга пригласила вас на тусовку.")
        print(" Пора принять решение: ехать или не ехать...")
        print()
        print(" 1 — Поехать")
        print(" 2 — Остаться дома")
        print()
        variant = int(input("<?>: "))
        if variant == 1:
            print()
            good_people_dict["Гардеробщица_FinalMessage"] = "No"
            good_people_dict["Бариста_FinalMessage"] = "No"
            print(" Вы красиво оделись и поехали на тусовку.")
            print()
            sleeping(90_000_000)
            print(" Оставшаяся часть дня прошла великолепно!")
            sleeping(100_000_000)
            print(" Большая компания друзей, приятная музыка...")
            sleeping(100_000_000)
            print(' "Это был отличный день" — подумали вы.')
            sleeping(100_000_000)
            print()
            print(" We lonely dancers")
            print("  Join me for the night...")
            sleeping(80_000_000)
            print("   We're lonely dancers, baby")
            sleeping(60_000_000)
            print("    Dance with me so we don't")
            sleeping(100_000_000)
            print("       cryyyyyyyyyyyyy....")
            print()
            if good_people_dict["Бариста"] == "No":
                for _ in range(6):
                    print(".")
                    sleeping(60_000_000)
                print()
                if BestEndingPoints == 4:
                    print(" Canonical Ending.")
                elif BestEndingPoints < 4:
                    print(" Usual Ending.")
                print()
                sleeping(60_000_000)
                authors()
            else:
                print()
                sleeping(100_000_000)
                for _ in range(5):
                    print(".")
                    sleeping(90_000_000)
                print()
                print(" Вы вышли на улицу.")
                print(" В этот же момент к вам подошёл Н, ранее стоявший неподалеку")
                sleeping(60_000_000)
                print(" — Вы здесь. Это достойно.")
                sleeping(90_000_000)
                print(" — Я думаю, у вас есть ко мне вопросы.")
                sleeping(90_000_000)
                print(" — Возможно, вы хотели бы их задать мне прямо сейчас.")
                sleeping(90_000_000)
                print()
                print(" 1 — Что за стихи?")
                print(" 2 — Кто ты такой?")
                if BestEndingPoints == 4 or BestEndingPoints == 0:
                    print(" 3 — Какова альтернатива?")
                print()
                variant_1 = int(input("<?>: "))
                if variant_1 == 1:
                    print()
                    print(" — Поэзия... её нужно уметь ощущать.")
                    sleeping(90_000_000)
                    print(" — Я все ещё не уверен, что вы сможете понять это.")
                    sleeping(90_000_000)
                    print(" — Строки, что я пишу, полностью прожиты мной.")
                    sleeping(90_000_000)
                    print(" — Написать стих — это не просто прожить один день студента ВШЭ.")
                    sleeping(90_000_000)
                    print(" — Написать стих — особое занятие. Это выше по сложности, чем варка кофе.")
                    sleeping(90_000_000)
                    print(" — Кофе выпьешь и в скором времени забудешь. Поэзия и эмоции от неё не забываются никогда.")
                    sleeping(90_000_000)
                    print(" — Поэзия и кофе — две субстанции, переплетающиеся в моём конструкте.")
                    sleeping(90_000_000)
                    print(" — Это всё, что я имею.")
                    sleeping(90_000_000)
                elif variant_1 == 2:
                    print()
                    print(" — Меня зовут Н.")
                    print(" — Вы меня видели сегодня в кофейне, и, наверное, думаете, что я обыкновенный бариста.")
                    sleeping(90_000_000)
                    print(" — Это не совсем верно.")
                    sleeping(90_000_000)
                    print(" — Сложно понятно объяснить, кто я такой.")
                    sleeping(60_000_000)
                    print(" — Я занимаюсь кофе, поэзией.")
                    print(" — Да и...")
                    sleeping(90_000_000)
                    print(" — ...порой я ощущаю, что я — не совсем тот, кем я являюсь.")
                    sleeping(90_000_000)
                    print(" — Я чувствую, что часть моего существования — просто условность.")
                    sleeping(60_000_000)
                    print(" — Я ведь уже говорил вам сегодня: я не люблю кофе.")
                    sleeping(90_000_000)
                    print(" — И поэтому часто я задаюсь вопросом: зачем я его делаю? Нужно ли мне это всё?")
                    sleeping(90_000_000)
                    print(" — У меня нет точного ответа, за исключением уже сказанного вам сегодня.")
                    sleeping(90_000_000)
                    print(" — Это всё, что я имею.")
                    sleeping(90_000_000)
                elif variant_1 == 3 and (BestEndingPoints == 0 or BestEndingPoints == 4):
                    print()
                    print(" — Альтернатива? Если речь идёт о пути... я могу ответить лишь условно.")
                    sleeping(90_000_000)
                    print(" — Задайте себе вопрос: какой я человек?")
                    sleeping(90_000_000)
                    print(" — Вспомните то, что вы делали раньше. Сегодня.")
                    sleeping(90_000_000)
                    print(" — Ответ вас может шокировать.")
                    sleeping(90_000_000)
                    print(" — Вы становились лучше?")
                    sleeping(90_000_000)
                    print(" — Или вы становились счастливее?")
                    sleeping(90_000_000)
                    print(" — Подумайте над этим.")
                    print()
                    sleeping(90_000_000)
                    print(" — Опробовать другое, после долго следования одному...")
                    sleeping(90_000_000)
                    print(" — ...это и есть альтернатива")
                    sleeping(90_000_000)
                    print(" — Это всё, что я могу сказать.")
                    sleeping(90_000_000)
                else:
                    print()
                    print(" — Я вас не понимаю... и скорее всего сейчас не пойму...")
                    sleeping(90_000_000)
                print()
                print(" — Мы обязательно ещё встретимся. Вы узнаете правду, когда это будет реально возможно.")
                sleeping(90_000_000)
                print(" — Это будет особая дорога.")
                sleeping(90_000_000)
                print(" — Кофейная дорога.")
                print()
                sleeping(90_000_000)
                for _ in range(5):
                    print(".")
                    sleeping(60_000_000)
                print()
                print(" Philosophical Ending.")
                sleeping(90_000_000)
                print()
                authors()
        elif variant == 2:
            print()
            print(" Вы остались дома, и занялись своими делами.")
            print(" Через некоторое время вам звонит подруга.")
            print(" Вы поднимаете трубку.")
            print()
            print(" — Ало. Ты где? Скоро уже всё начнется!")
            print()
            print(" 1 — Сказать правду")
            print(" 2 — Соврать")
            print()
            variant_2 = int(input("<?>: "))
            if variant_2 == 1:
                print()
                print(" Вы рассказываете подруге о наличии важных дел, из-за которых вы не можете поехать на тусовку.")
                print(" Подруга относится с пониманием к вашему решению. Звонок завершается.")
                print()
                sleeping(60_000_000)
                epilogue_part2()
            elif variant_2 == 2:
                print()
                print(" Вы сказали своей подруге, что очень неважно себя чуствуете.")
                sleeping(40_000_000)
                print(" Ваша подруга вам не поверила.")
                sleeping(40_000_000)
                print(" Звонок был сброшен.")
                epilogue_part2()
            else:
                print()
                print(" — Не хочешь — не приезжай. Я не собираюсь тебя уговаривать.")
                sleeping(40_000_000)
                print(" Звонок был сброшен.")
                epilogue_part2()
    else:
        print()
        print(" Вернувшись домой и немного отдохнув от трудного дня, вы решили провести вечер с пользой.")
        sleeping(60_000_000)
        print()
        unremarkble()


# — « »


def lunch_in_cafe_menu():
    global MoneyAmount
    print(" 1 — Слойка с сыром (250 руб.)")
    print(" 2 — Сосиска в тесте (100 руб.)")
    print(" 3 — Чай чёрный / зелёный (100 руб.)")
    print(" 4 — Уйти из столовой")
    print()
    variant = int(input("<?>: "))
    if variant == 1 and MoneyAmount >= 250:
        print()
        print(" — Ваша слойка с сыром!")
        MoneyAmount -= 250
        sleeping(60_000_000)
        print(" Вы уходите из столовой.")
        sleeping(60_000_000)
        epilogue()
    elif variant == 1 and MoneyAmount < 250:
        print()
        print(' "У вас недостаточно средств на карте."')
        lunch_in_cafe_menu()
    elif variant == 2 and MoneyAmount >= 100:
        print()
        print(" — Ваша сосиска в тесте!")
        MoneyAmount -= 100
        print(" Вы уходите из столовой.")
        sleeping(60_000_000)
        epilogue()
    elif (variant == 2 or variant == 3) and MoneyAmount < 100:
        print()
        print(" — У вас недостаточно средств на карте.")
        lunch_in_cafe_menu()
    elif variant == 3 and MoneyAmount >= 100:
        print()
        print(" — Ваш чай!")
        MoneyAmount -= 100
        sleeping(60_000_000)
        print(" Вы уходите из столовой.")
        sleeping(60_000_000)
        epilogue()
    elif variant == 4:
        print()
        print(" Вы покинули столовую.")
        print()
        sleeping(60_000_000)
        epilogue()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        lunch_in_cafe_menu()


def lunch_in_cafe():
    print()
    print(" Ваши друзья ушли во двор ВУЗа, а вы тем временем реишили спуститься в столовую.")
    print(' "Заказывайте." — неожиданно произнес администратор столовой.')
    print()
    print(" Вы берёте меню в руки, и видите различную выпечку. Также в ассортименте есть чай.")
    print()
    lunch_in_cafe_menu()
    print()


def smoking_step():
    global good_people_dict
    global ManTalk
    global OldWomanTalk
    global BestEndingPoints
    print()
    print(" Вы вышли на улицу.")
    print(" Табачный дым пронизывает вас и ваших друзей,")
    print(" пока они весело что-то обсуждают между собой.")
    print()
    print(" 1 — Промолчать")
    print(" 2 — Поддержать разговор")

    if good_people_dict["Бариста"] == "Yes":
        print(" 3 — Спросить друзей про баристу")

    if good_people_dict["Гардеробщица"] == "Yes":
        print(" 4 — Спросить друзей про гардеробщицу")

    print()
    variant = int(input("<?>: "))
    if variant == 1:
        print()
        print(" Вы молча докурили сигарету, и отправились на занятия.")
        good_people_dict["Бариста_Номер"] = "No"
        good_people_dict["Гардеробщица_Номер"] = "No"
        print()
        epilogue()
    elif variant == 2:
        print()
        print(" Легко узнав тему разговора, вы отлично поговорили с друзьями.")
        print(" А вот и время пары. Пора на занятия.")
        good_people_dict["Бариста_Номер"] = "No"
        good_people_dict["Гардеробщица_Номер"] = "No"
        BestEndingPoints += 1
        print()
        epilogue()
    elif variant == 3 and ManTalk:
        print()
        print(" — Он странный парень...")
        sleeping(60_000_000)
        print(" —— Даже очень...")
        sleeping(60_000_000)
        print(" — Во всяком случае, у него доброе сердце. Это редкость в наше время.")
        print()
        sleeping(70_000_000)
        print(" —— Было время, когда я хотела пообщаться с ним поближе.")
        sleeping(70_000_000)
        print(" —— Не получилось, он чересчур закрыт. Никому не доверяет особо.")
        sleeping(70_000_000)
        print(" —— Вот его контакт. Может у тебя получится.")
        good_people_dict["Бариста_Номер"] = "Yes"
        print()
        sleeping(60_000_000)
        print(" — Пойдёмте. Пора на пару.")
        good_people_dict["Гардеробщица_Номер"] = "No"
        print()
        epilogue()
    elif variant == 3 and not ManTalk:
        print()
        print(" — По-моему, ты пытаешься спросить то, что не может спрашиваться...")
        print(" — Пойдёмте. Пора на пару.")
        epilogue()
    elif variant == 4 and OldWomanTalk:
        print()
        print(" — Добрая женщина. Давно работает.")
        sleeping(60_000_000)
        print(" —— Да... Говорят, что она очень мудра.")
        sleeping(60_000_000)
        print(" — Я тоже об этом слышал. Она интересуется тем, как человек может влиять на свою судьбу.")
        sleeping(60_000_000)
        print(" —— Не просто интересуется. Она знает истинную судьбу. Я уверена.")
        sleeping(60_000_000)
        print()
        print(" —— Тебе стоит с ней поговорить лично. Вот её контакт.")
        print()
        good_people_dict["Гардеробщица_Номер"] = "Yes"
        good_people_dict["Бариста_Номер"] = "No"
        sleeping(60_000_000)
        print(" — Пойдёмте. Пора на пару.")
        print()
        epilogue()
    elif variant == 4 and not OldWomanTalk:
        print()
        print(" — По-моему, ты пытаешься спросить то, что не может спрашиваться...")
        print(" — Пойдёмте. Пора на пару.")
        print()
        epilogue()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        smoking_step()


def lunch_step():
    global good_people_dict
    print()
    print(" Пара закончилась. Вы проголодались.")
    print()
    print(" 1 — Пойти в столовую")
    print(" 2 — Пойти покурить")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        good_people_dict["Гардеробщица_Номер"] = "No"
        good_people_dict["Бариста_Номер"] = "No"
        print()
        print(" Вы отправились в столовую.")
        lunch_in_cafe()
    elif variant == 2:
        print()
        print(" Вместо столовой, вы ушли на улицу, чтобы покурить с друзьями.")
        smoking_step()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        lunch_step()


def chosing_cabinet():
    global toHelpFriend
    print()
    print(" 1 — R304")
    print(" 2 — R307")
    print(" 3 — R305")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        print()
        print(" За сильно скрепящей дверью, в небольшой аудитории, сидят экономисты.")
        print(" Вам явно не сюда.")
        chosing_cabinet()
    elif variant == 2:
        print()
        print(" Вы заходите в кабинет, где прямо сейчас проходит уборка.")
        print(" На вас осуждающе смотрит уборщица.")
        print(" P.S.: Отсюда лучше уйти...")
        chosing_cabinet()
    elif variant == 3:
        print()
        print(" Вы проходите в аудиторию и занимаете свободное место")
        if toHelpFriend:
            print(" Радостный взгляд подруги встречает вас!")
            print(" Вы сели к ней. За разговором с ней, лекция пролетела совершенно незаметно.")
            lunch_step()
        else:
            print(" Равнодушный взгляд подруги встречает вас.")
            print(" Вы расположились на последнем ряду аудитории. Пара шла скучновато,")
            print(" но вы смогли узнать что-то новое.")
            lunch_step()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        chosing_cabinet()


def second_pair():
    print()
    print(" Подходит время второй пары.")
    print(" Вы поднимаетесь на второй этаж, и пытаетесь вспомнить аудиторию,")
    print(" в которой будет ваше занятие.")
    chosing_cabinet()


def break_dialog():
    global toHelpFriend
    global BestEndingPoints
    print()
    print(" Остаток первой пары вы проводите на лавочке в атриуме.")
    print(" На перерыве к вам подходит ваша подруга.")
    print(" Она рассказывает вам о своем новом проекте и о том, ")
    print(" что было на пропущенной вами паре. ")
    print(" В процессе беседы, вас зовут помочь в организации тусовки сегодня вечером.")
    print()
    print(" 1 — Согласиться")
    print(" 2 — Отказаться")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        print()
        toHelpFriend = True
        print(" Вы пообешали помочь своей подруге.")
        print(" — Спасибо тебе! Я пойду в R305, встретимся там.")
        second_pair()
    elif variant == 2:
        print()
        toHelpFriend = False
        print(" С большим разочарованием, подруга уходит от вас.")
        second_pair()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        break_dialog()


def coffee_order():
    global americano_answers
    global cacao_answers
    global raf_answers
    global MoneyAmount
    print()
    for pos in coffee_menu:
        print(" ", coffee_menu[pos], " : ", pos, " руб.")
        sleeping(40_000_000)
    print()
    print(" — Что будете пить?")
    print()
    variant_1 = input("<?>: ")
    if variant_1 in cacao_answers:
        print()
        print(" — Ваш какао!")
        print()
        MoneyAmount -= 300
        print(" *Остаток на счёте*: ", MoneyAmount, " руб.")
        break_dialog()
    elif variant_1 in raf_answers and MoneyAmount >= 350:
        print()
        print(" — Ваш Раф!")
        print()
        MoneyAmount -= 350
        print(" *Остаток на счёте*: ", MoneyAmount, " руб.")
        break_dialog()
    elif variant_1 in raf_answers and MoneyAmount < 350:
        print()
        print(" — Не хватает средств! Может другой напиток?")
        print()
        print(" 1 — Да, выберу другой")
        print(" 2 — Я пожалуй пойду...")
        variant_2 = int(input("<?>: "))
        if variant_2 == 1:
            coffee_order()
        elif variant_2 == 2:
            print()
            print(" — До скорых встреч!")
            break_dialog()
        else:
            print()
            print(" — Боюсь, я не понимаю вас!")
            coffee_order()
    elif variant_1 in americano_answers:
        print()
        print(" — Ваш Американо!")
        print()
        MoneyAmount -= 200
        print(" *Остаток на счёте*: ", MoneyAmount, " руб.")
        break_dialog()
    else:
        print()
        print(" — Боюсь, я не понимаю вас!")
        coffee_order()


def coffee_break():
    global good_people_dict
    global coffee_menu
    global ManTalk
    print(" Вы пришли в кофейню.")
    print(" Бариста ждёт вашего пожелания...")
    print()
    print(" 1 — Показать меню")
    print(" 2 — Поговорить с баристой")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        coffee_order()
        good_people_dict["Бариста"] = "No"
        ManTalk = False
    elif variant == 2:
        print()
        good_people_dict["Бариста"] = "Yes"
        ManTalk = True
        print(" — Зови меня Н. Здесь я появился недавно и не на долго.")
        print()
        sleeping(60_000_000)
        print(" — Я не особо люблю кофе, оно мне не доставляет удовольствие...")
        sleeping(60_000_000)
        print(" — Зато приносит другим — для меня это большее удовольствие, нежели сам напиток.")
        sleeping(60_000_000)
        print(" — Ещё я пишу стихи... мне это помогает в период грусти и размышлений...")
        sleeping(60_000_000)
        print(" — Но сейчас я не готов тебе их читать. Придёт время — и ты обязательно услышишь эти строки.")
        sleeping(60_000_000)
        print()
        print(" 1 — Уйти из кофейни")
        print(" 2 — Посмотреть меню")
        print()
        variant = int(input("<?>: "))
        if variant == 1:
            print()
            break_dialog()
        elif variant == 2:
            print()
            coffee_order()
        else:
            print(" — Я думаю, тебе лучше идти. Скоро будет перерыв.")
            break_dialog()


def past_usefull_talking():
    global ManTalk
    global good_people_dict
    print()
    print(" 1 — Пойти за кофе в «Грушу» :)")
    print(" 2 — Пройти мимо столовой :(")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        print()
        coffee_break()
    elif variant == 2:
        good_people_dict["Бариста"] = "No"
        ManTalk = False
        print()
        print(" Не обратив внимание на приятнейший аромат кофе,")
        print(" вы проходите мимо и идёте ждать окончание пары.")
        break_dialog()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        past_usefull_talking()


def usefull_talking():
    print()
    global OldWomanTalk
    global good_people_dict
    global player_name
    print(" — И тебе привет! Как я могу звать тебя?")
    print()
    player_name = input("<?>: ")
    print()
    print(" — Послушай меня,", player_name, ". ")
    sleeping(60_000_000)
    print(" — Ты ведь понимаешь, что рано или поздно всему придёт конец?")
    sleeping(60_000_000)
    print(" — Если так, то это отлично!")
    sleeping(60_000_000)
    print(" — Помни, что лишь чистые и правильные намерения приведут тебя к истинному концу твоего пути...")
    sleeping(60_000_000)
    print(" — Это всё, что мы можем...")
    sleeping(60_000_000)
    good_people_dict["Гардеробщица"] = "Yes"
    OldWomanTalk = True
    past_usefull_talking()


def miss_pair():
    global good_people_dict
    global OldWomanTalk
    global ManTalk
    print(" Вы, абсолютно не торопясь, проходите в гардероб, чтобы сдать вещи.")
    print(" Приятный кофейный аромат, дошедший до вас, манит зайти в «Грушу»")
    print()
    print(" 1 — Пойти за кофе в «Грушу» :)")
    print(" 2 — Пройти мимо столовой :(")
    print(" 3 — Поговорить с гардеробщицой")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        good_people_dict["Гардеробщица"] = "No"
        OldWomanTalk = False
        print()
        coffee_break()
    elif variant == 2:
        OldWomanTalk = False
        ManTalk = False
        good_people_dict["Гардеробщица"] = "No"
        good_people_dict["Бариста"] = "No"
        print()
        print(" Не обратив внимание на приятнейший аромат кофе,")
        print(" вы проходите мимо и идёте ждать окончание пары.")
        break_dialog()
    elif variant == 3:
        print()
        usefull_talking()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        miss_pair()


def university():
    global good_people_dict
    print()
    print(" Вы подходите к ВУЗу и глядите на часы — до начала пары осталось несколько минут")
    print(' "Может прогулять?" — задумались вы.')
    print()
    print(" 1 — Прогулять пару")
    print(" 2 — Пойти на пару")
    print()
    variant = int(input("<?>: "))
    print()
    if variant == 1:
        print()
        miss_pair()
    elif variant == 2:
        good_people_dict["Гардеробщица"] = "No"
        good_people_dict["Бариста"] = "No"
        good_people_dict["Гардеробщица_Номер"] = "No"
        good_people_dict["Бариста_Номер"] = "No"
        print()
        print(" Опоздав, вы заходите в нужную аудиторию,")
        print(" идёте в самый конец и садитесь на последнюю парту.")
        print()
        print(" Пара проходит уныло и скучно, вы уходите на перерыв.")
        break_dialog()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        university()


def metro_step():
    global MoneyAmount
    print()
    print(" Вы доехали до ближайшей станции метро.")
    print(" Спускаясь на эскалаторе, вы лицезрели")
    print(" красоту орнамента стен. Московское метро так красиво!")
    print()
    print(" На станции стоял поезд, двери которого вот-вот начнут закрываться.")
    print(" Есть хороший шанс успеть!")
    print()
    print(" 1 — Бежать к вагону")
    print(" 2 — Спокойно дождаться следующего")
    print()
    variant = int(input("<?>: "))
    print()
    if variant == 1:
        MoneyAmount -= 1945
        print(" Вы побежали к вагону.")
        print(" Вам удается протиснуться между стремительно")
        print(" закрывающимися дверьми. Поезд отправляется.")
        print(" Опустив руку в карман, вы понимаете, что")
        print(" обронили деньги прямо на перроне!")
        print()
        print(" Может, всё-таки, не стоило торопиться?...")
        print()
        print(" *Остаток на счёте*: ", MoneyAmount, " руб.")
        university()
    elif variant == 2:
        print(" Поезд уехал.")
        print(" Спустя несколько минут подъехал новый,")
        print(" вы зашли в него и отправились на «Покру».")
        university()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        metro_step()


def autobus_friend_step():
    global BestEndingPoints
    global good_people_dict
    print()
    print(" Сев на единственное свободное место, вы поднимаете голову и видите,")
    print(" что в метре от вас сидит ваша одногруппница... ")
    print()
    print(" 1 — Окликнуть её")
    print(" 2 — Промолчать")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        BestEndingPoints += 1
        print()
        print(" К сожалению, одногруппница не услышала вас, из-за")
        print(" громкой музыки в своих наушниках. Увы и Ах!")
        metro_step()
    elif variant == 2:
        print()
        print(" Вы продолжили свою поездку в тишине.")
        metro_step()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        autobus_friend_step()


def autobus_step():
    global MoneyAmount
    print()
    print(" Вы вышли на улицу.")
    print(" Ранее хорошее настроение омрачнилось")
    print(" ушедшим за плотные облака солнцем.")
    print()
    print(" Вы подошли к остановке и задумались:")
    print(" На чём же поехать в ВУЗ?")
    print()
    print(" 1 — Такси")
    print(" 2 — Общественный транспорт")
    print(" 3 — Пешком")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        print()
        MoneyAmount -= 2000
        print(" *Остаток на счёте*: ", MoneyAmount, " руб.")
        print()
        print(" Потратив большую часть денег,")
        print(" но ощутив максимальный комфорт, вы добрались места учёбы.")
        university()
    elif variant == 2:
        print()
        MoneyAmount -= 55
        print(" *Остаток на счёте*: ", MoneyAmount, " руб.")
        print()
        print(" Через некоторое время на остановку подъехала «Дубовозка».")
        print(" Вы сели в маршрутку, и отправились в поездку до ближайшего метро.")
        autobus_friend_step()
    elif variant == 3:
        print()
        if isCoatOnYou:
            print()
            print(" Вы пошли пешком...")
            print(" Нерасчищенные снежные сугробы,")
            print(" отсутствие каких-либо ориентиров — всё это тяготит вас...")
            print(' "Может всё-таки на такси?" — задумались вы.')
            print()
            print("1 — Такси")
            print("2 — Пешком")
            print()
            variant_1 = int(input("<?>: "))
            if variant_1 == 1:
                print()
                print(" У вас получилось вызвать такси, и вы отправились в ВУЗ.")
                print(" Вам удалось сэкономить немного денег, но стоило ли оно того?...")
                MoneyAmount -= 1800
                print()
                print(" *Остаток на счёте*: ", MoneyAmount, " руб.")
                university()
            else:
                print()
                print(" Пройдя ещё несколько километров, вы, обессилив, падаете на землю.")
                print(' Попытки встать не увенчались успехом... кажется, Вы мертвы?')
                print(" или просто спите?")
                print()
                sleeping(60_000_000)
                print(" Что же с вами стало?")
                print()
                sleeping(60_000_000)
                print(" Жизнь даёт много вопросов, и катастрофически мало ответов...")
                for _ in range(6):
                    print(".")
                    sleeping(60_000_000)
                print()
                print(" Silly Ending.")
                print()
                sleeping(60_000_000)
                print("P.S. Порой, нам приходится делать то, что не хочется...")
                print()
                sleeping(60_000_000)
                authors()
        else:
            print()
            print("Вы безумны...")
            print()
            sleeping(60_000_000)
            print(" Пройдя несколько километров, вы, обессилив, падаете на землю.")
            print(" Попытки встать не увенчались успехом... кажется, Вы мертвы?")
            print(" или просто спите?")
            print()
            sleeping(60_000_000)
            print(" Что же с вами стало?")
            print()
            sleeping(60_000_000)
            print(" Жизнь даёт много вопросов, и катастрофически мало ответов...")
            for _ in range(6):
                print(".")
                sleeping(60_000_000)
            print()
            print(" Silly Ending.")
            print()
            sleeping(60_000_000)
            print("P.S. Порой, нам приходится делать то, что не хочется...")
            sleeping(60_000_000)
            print()
            authors()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        autobus_step()


def second_step():
    global isCoatOnYou
    print()
    print(" Вы возвращаетесь в комнату и начинаете собираться на учебу.")
    print(" Открыв окно, вы почуствовали дуновение холодного весеннего ветра.")
    print(' "Далеко ещё до лета..." — подумали вы, закрыли окно,')
    print(" и пошли собираться в университет.")
    print()
    print(" 1 — Надеть пальто")
    print(" 2 — Надеть кофту")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        isCoatOnYou = True
        print()
        print(" Отличный выбор! Вам точно будет тепло")
        autobus_step()
    elif variant == 2:
        print()
        isCoatOnYou = False
        print(" Слабоумие и отвага - это точно про Вас!")
        autobus_step()
    elif variant == 1994:
        print()
        print("^_^")
        print()
        sleeping(90_000_000)
        print(" If you’re going to get in trouble for hitting someone, might as well hit them hard.")
        print()
        sleeping(90_000_000)
        print(" @Harry Styles")
        sleeping(90_000_000)
        second_step()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        second_step()


def Breakfast():
    print(" 1 — Завтракать")
    print(" 2 — Поесть в университете")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        print()
        print(" Хлопьев не осталось, но зато вы сыты!")
        print()
        second_step()
    elif variant == 2:
        print()
        print(" Вы отказались от завтрака, и уходите с кухни.")
        second_step()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        Breakfast()


def first_step():
    global BestEndingPoints
    print(" 1 — Пойти в ванную")
    print(" 2 — Пойти на кухню")
    print()
    variant = int(input("<?>: "))
    print()
    if variant == 1:
        BestEndingPoints += 1
        print()
        print(" Вы приняли душ, почистили зубы...")
        print(" Теперь вы сияете!")
        print()
        first_step()
    elif variant == 2:
        print()
        print(" Вы заходите на кухню.")
        print(" На столе с белоснежной скатертью стоит коробка с хлопьями.")
        print(" Вы ощущаете голод, и серьёзно задумываетесь: ")
        print(" Завтракать или нет?")
        print()
        Breakfast()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        first_step()


# #################################################################


def another_line_studing_epilogue():
    print()
    sleeping(60_000_000)
    print(" После приятного обеда, вы продолжили работать.")
    sleeping(60_000_000)
    print(" Время близится к ночи. Вы закрыли большую часть долгов.")
    print(" Вы задумались: лечь спать или проверить соц. сети перед сном?")
    print()
    print(" 1 — Лечь спать сразу")
    print(" 2 — Посидеть в соц. сетях")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        print()
        print(" После сложного домашнего учбеного дня, вы легли спать.")
        for _ in range(5):
            print(".")
            sleeping(60_000_000)
        print()
        print(" OverUsual Ending.")
        print()
        sleeping(60_000_000)
        authors()
    elif variant == 2:
        print()
        print(" Вы проверили социальные сети и пообщались с друзьями. Теперь пора спать.")
        for _ in range(5):
            print(".")
            sleeping(60_000_000)
        print()
        print(" OverUsual Ending.")
        print()
        authors()
    else:
        print()
        print(" Мы все заложники трудного выбора.")
        print()
        another_line_studing_epilogue()


def another_line_studing():
    global MoneyAmount
    print(" Вы начинаете заниматься учебой.")
    sleeping(50_000_000)
    print(" Большое количество долгов ожидает вас. Всё нужно решить.")
    print()
    sleeping(50_000_000)
    print(" Пришло время пообедать. Что хотите покушать?")
    print()
    print(" 1 — Быстрорастворимая лапша")
    print(" 2 — Бизнес-ланч")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        print()
        print(" Вы заказали себе Доширак. Вкусно, но не особо питательно. Немного вредно.")
        MoneyAmount -= 100
        print()
        another_line_studing_epilogue()
    elif variant == 2:
        print()
        print(" Вы заказали себе полноценный обед. Вкусно, питательно, полезно. Дороговато.")
        MoneyAmount -= 1000
        print()
        another_line_studing_epilogue()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        another_line_studing()


def another_line_chill_epilogue():
    print()
    print(" Вы благополучно вернулись домой. Несмотря на острое желание спать,")
    print(" вы задумались над тем, что посидеть в телефоне перед сном.")
    print(" В это же время приходит сообщение от соседа с предложением созвониться по аудио.")
    print()
    print(" 1 — Посидеть в телефоне и лечь спать")
    print(" 2 — Пообщаться с соседом")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        print()
        print(" Вы проверили социальные сети и пообщались с друзьями. Теперь пора спать.")
        for _ in range(5):
            print(".")
            sleeping(60_000_000)
        print()
        print(" Almost a Sincere Ending.")
        print()
        authors()
    elif variant == 2:
        print()
        print(" Эти душевные разговоры... Они так приятны... И необходимы...")
        sleeping(60_000_000)
        print(" Вы отлично поговорили с соседом, и с хорошим настроением легли спать.")
        print()
        for _ in range(5):
            print(".")
            sleeping(60_000_000)
        print()
        print(" Sincere Ending.")
        print()
        sleeping(60_000_000)
        authors()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        another_line_chill_epilogue()


def another_line_going_home_from_tavern():
    global MoneyAmount
    print()
    print(" Душевные разговоры в баре с соседом продлились несколько часов. Но пора домой, бар скоро закрывается.")
    print()
    print(" 1 — Поехать на такси")
    print(" 2 — Поехать на метро")
    print()
    variant = int(input("<?>: "))
    if variant == 1 and MoneyAmount >= 1000:
        MoneyAmount -= 1000
        print()
        print(" Вы отправились домой на такси.")
        print()
        sleeping(60_000_000)
        another_line_chill_epilogue()
    elif variant == 1 and MoneyAmount < 1000:
        MoneyAmount -= 60
        print()
        print(" На такси не хватило денег. Вы с соседом поехали домой на метро. Дорого, но с комфортом!")
        sleeping(60_000_000)
        another_line_chill_epilogue()
    elif variant == 2:
        MoneyAmount -= 60
        print()
        print(" Вы поехали на метро. Сэкономили приличные деньги!")
        sleeping(60_000_000)
        another_line_chill_epilogue()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        another_line_going_home_from_tavern()


def another_line_tavern_step():
    global MoneyAmount
    print()
    print(" Вы пришли в бар.")
    print(" Сосед предложил выпить какой-нибудь напиток.")
    print(" Что будете заказывать?")
    print()
    print(" 1 — Молочный коктейль (450 руб.)")
    print(" 2 — Латте (300 руб.)")
    print(" 3 — Мохито безалкогольный (400 руб.)")
    print(" 4 — Ничего не пить")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        print()
        print(" Вы взяли себе молочный коктейль.")
        MoneyAmount -= 450
        another_line_going_home_from_tavern()
    elif variant == 2:
        print()
        print(" Вы взяли себе латте")
        MoneyAmount -= 300
        another_line_going_home_from_tavern()
    elif variant == 3:
        print()
        print(" Вы взяли себе мохито.")
        MoneyAmount -= 400
        another_line_going_home_from_tavern()
    elif variant == 4:
        print()
        print(" Вы отказались от напитка.")
        another_line_going_home_from_tavern()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        another_line_tavern_step()


def another_line_chill():
    print()
    print(" Вы решили отдохнуть этот день.")
    print(" Ваш сосед в общежитии зовёт вас в бар. Пойдёте?")
    print()
    print(" 1 — Идти в бар")
    print(" 2 — Отказаться")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        print()
        print(" Вы согласились пойти в бар.")
        another_line_tavern_step()
    elif variant == 2:
        print()
        print(" Вы отказались идти в бар.")
        print()
        sleeping(70_000_000)
        print(" Весь свой день вы провели в общажной компании. Было весело!")
        print()
        for _ in range(6):
            print(".")
            sleeping(70_000_000)
        print()
        print(" Friendly Ending.")
        print()
        sleeping(60_000_000)
        authors()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        another_line_chill()


def another_line():
    print()
    print(" Наконец, вы встали с кровати.")
    print(" Чем займёмся?")
    print()
    print(" 1 — Учёба")
    print(" 2 — Отдых")
    print()
    variant = int(input("<?>: "))
    if variant == 1:
        print()
        another_line_studing()
    elif variant == 2:
        print()
        another_line_chill()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        another_line()


# ####################################################################################
def prologue_step():
    print(" 1 — Попробовать снова уснуть")
    print()
    print(" 2 — Посмотреть на часы")
    print()
    print(" 3 — Встать с кровати")
    print()
    print(" 4 — Полежать ещё немного...")
    print()
    variant = int(input("<?>: "))
    print()
    if variant == 1:
        print("Вы серьёзно?")
        for timer in range(6):
            print(".")
            sleeping(60_000_000)
        print()
        print(" Поддавшись сильному желанию спать, вы, спустя некоторое время, уснули.")
        print(" Неизвестно, что было дальше.")
        print(" Вероятнее всего, вы были отчислены из ВУЗа за свою лень и безответственность!")
        print()
        sleeping(90_000_000)
        print(" ...")
        sleeping(90_000_000)
        print()
        print(" Lazy Ending.")
        sleeping(90_000_000)
        print()
        authors()
    elif variant == 2:
        print()
        print(" Вы дотянулись до телефона.")
        print(" Проморгавшись, вы увидели: 8:58")
        sleeping(40_000_000)
        print()
        prologue_step()
    elif variant == 3:
        print()
        print(" Вы встали с кровати.")
        print()
        print(" На улице вылянуло солнышко! День становится веселее!")
        print(" Правда, время уже 9:30... Скоро на пары!")
        print()
        first_step()
    elif variant == 4:
        print()
        print(" Вы решили ещё чуть чуть полежать...")
        sleeping(60_000_000)
        print(" Вы проснулись только через час. Смысла ехать на пары нет — вы точно не успеете на них.")
        print()
        another_line()
    else:
        print()
        print(" Мы все заложники трудного выбора...")
        print()
        prologue_step()


###########################################################
def sleeping(sleep_range):
    for _ in range(sleep_range + 1):
        pass


def authors():
    print("<<<Авторы>>>")
    print("----------------------")
    sleeping(80_000_000)
    print("Сценарий: Алёна Штоппель")
    sleeping(80_000_000)
    print("Техническая часть: Алёна Штоппель")
    sleeping(80_000_000)
    print("Моральная поддержка: n.p. ^_^")
    sleeping(80_000_000)
    print()
    print("Спасибо за игру! Надеюсь, вам понравилось :)")
    print()
    sleeping(90_000_000)
    # print("...The end...")
    game_menu()


def guess_number():
    print()
    print(" Сколько колец у Алёны Штоппель на руке???")
    print()
    variant = int(input("<?>: "))
    while variant != 5:
        print()
        print(" Неверно! ")
        print()
        guess_number()
    print()
    print(" Все верно! Вы хорошо знаете автора!")
    print()
    game_menu()


def game_menu():
    global BestEndingPoints
    print("___One Day in HSE___")
    print("=====================")
    print("-------Играть--------")
    print("-------Авторы--------")
    print("----Угадай число-----")
    print("-------Об игре-------")
    print("---Погладить котика--")
    print("--------Выход--------")
    print("\n")

    player_request = input("<Ввод>:")
    print()

    if player_request in about_game_answers:
        print()
        print("<<<Об игре>>>")
        print()
        print("Текстовый квест о типичном рабочем дне настоящей студентки ВШЭ!")
        print()
        sleeping(80_000_000)
        game_menu()

    elif player_request in author_answers:
        authors()

    elif player_request in guess_number_answers:
        guess_number()

    elif player_request in pet_a_cat_answers:
        BestEndingPoints += 1
        print()
        print("Meeooow <3<3<3")
        print("Вы сделали этот мир счастливее!")
        print()
        print("Маленький Ричи благодарен вам!")
        print()
        sleeping(80_000_000)
        game_menu()
    elif player_request in go_out_answers:
        exit()
    elif player_request in play_answers:
        print()
        print()
        print("Утро.")
        print()
        print(" Вы тяжело открываете глаза, и видите… а что можно увидеть в Дубках того, что ранее было неизвестно?")
        print(" Серые потолки, серая Москва за окном и серые будни… Рутина, одним словом.")
        print()
        prologue_step()

    else:
        print()
        print("А теперь напишите правильно :)")
        sleeping(800999)
        print("\n")
        game_menu()


#####################################################################

cacao_answers = ["Какао", "какао", " Какао", " какао"]
raf_answers = ["Раф", "раф", " Раф", " раф"]
americano_answers = ["Американо", "американо", " Американо", " американо"]

OldWomanTalk = False
ManTalk = False
isCoatOnYou = False
toHelpFriend = False

good_people_dict = {}
coffee_menu = {300: "Какао", 350: "Раф", 200: "Американо"}

MoneyAmount = 2300
BestEndingPoints = 0

player_name = ""

about_game_answers = ["Об игре", " Об игре", "об игре", " об игре"]
author_answers = ["Авторы", " Авторы", "авторы", " авторы"]
pet_a_cat_answers = ["Погладить котика", " Погладить котика", "погладить котика",
                     " погладить котика"]
guess_number_answers = ["Угадай число", "угадай число", " Угадай число", " угадай число"]
go_out_answers = ["Выход", " Выход", "выход", " выход"]
play_answers = ["Играть", " Играть", "играть", " играть"]

################################################################

game_menu()
