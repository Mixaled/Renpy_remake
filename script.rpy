define ai = Character('Эйлин', color="#FFFFFF", image="e_image")
define a = Character('Ada', color="#c8ffc8")
define e = Character('Ethan', color="#c8ffc8")
define unk = Character("???", color="#c8ffc8")
define v= Character("Victoria", color="#ffa500")
define t= Character("Tomoko", color="#FF0000")
define tr= Character("Taro", color="#0f0")
define api_gpt = "*INSERT API*"  

image travel = im.FactorScale("travel.png", 1.6)
image unkwn = im.FactorScale("unknown.png", 1.7)
image gg_m = im.FactorScale("m_gg.png", 0.8)
image gg_f = im.FactorScale("f_gg.png", 0.8)
image home_n = im.FactorScale("home.png", 2.0)
image home_m = im.FactorScale("home_m.png", 2.0)
image office = im.FactorScale("office.png", 1.4)
image victoria = im.FactorScale("victoria.png", 0.9)
image tomoko = im.FactorScale("tomoko.png", 0.9)
image coff = im.FactorScale("coffee.png", 3.2)
image taro = im.FactorScale("taro.png", 0.9)

default money = 280995

label start:
    "Вы когда-нибудь задумывались..."
    show screen money_display(money)
    "Кто мы на самом деле?"with dissolve 
    scene travel
    menu:
        "Выбрать мужского персонажа":
            $ character_name = "Ethan"
            $ main = e
            $ ego_ee = 'его'
            $ end_c = ''
            $ bad = 'плохой'
            $ cool = 'крутой'
            $ son = 'Сын'
            $ gender = 'парень'
            jump continue_story

        "Выбрать женского персонажа":
            $ character_name = "Ada"
            $ main = a
            $ end_c = 'а'
            $ ego_ee = 'ее'
            $ bad = 'плохая'
            $ cool = 'крутая'
            $ son = 'Дочь'
            $ gender = 'девушка'
            jump continue_story

label continue_story:
    "Вы [character_name] [gender] 17 лет."
    #show gg
    if character_name == "Ada":
        show gg_f at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    else:
        show gg_m at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    #show gg
    main "Завтра у меня клиент!" with vpunch
    main "Кажется, я уснул[end_c] пока ехал[end_c] в метро" with dissolve 
    show unkwn at Position(xpos = 0.7, xanchor=0.0, ypos=0.55, yanchor=0.5)
    "???" "Можно потише? Ты что тут шумишь?"
    python:
        povname = renpy.input("Что ответить незнакомцу?", length=70)
    main "[povname]" with dissolve 
    python:
        import chatgpt
        apikey = renpy.store.api_gpt
        pol = renpy.store.gender
        messages = [
            {"role": "system", "content": f"Ты незнакомец, которого тревожит {pol} в метро своим вскрикиванием, будь готов к любому ответу"},
            {"role": "assistant", "content": "Можно потише? Ты что тут шумишь?"}
        ]
        user_input = povname
        messages.append(
                {"role": "user", "content": user_input}
            )
        messages = chatgpt.completion(messages,apikey)
        response = messages[-1]["content"]
        unk("[response]")
    "Незнакомый мужчина отошел и сел на свое место, уткнувшись в телефон."
    hide unkwn
    main "Эхх..."
    hide gg_m
    hide gg_f
    "Несмотря на свой юный возраст, [character_name] работает психологом" with dissolve 
    "..."
    jump home

label home:
    scene home_n
    #show gg
    if character_name == "Ada":
        show gg_f at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    else:
        show gg_m at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    #show gg
    main"Сил больше нет, насыщен был день"
    main"Жду не дождусь когда родители купят мне нормальный дом"
    main"Эта коморка меня раздражает, раньше я жил[end_c] в большом доме, пока родители ездили в командировки" with dissolve  
    main"Но вот, я уже месяц живу в этой дыре, как унизительно по отношению ко мне" with dissolve
    main"[character_name] Taylor не обязан[end_c] жить в нищих квартирах" with vpunch
    hide gg_m
    hide gg_f
    "Завтра много работы, пойду спать"
    "{color=#FFA500}Родители [character_name] Taylor - это богатые и успешные предприниматели. Отец, Richard Taylor, является основателем и генеральным директором мировой корпорации в области высоких технологий.{/color}" 
    "{color=#FFA500}А мать, Victoria Taylor, - выдающимся финансовым аналитиком и инвестором.{/color}"
    "{color=#FFA500}Они всегда обеспечивали [character_name] роскошными условиями жизни и не знали бедности. Большие дома, шикарные путешествия и лучшие образовательные возможности - все это было естественной частью их быта.{/color}"
    "{color=#FFA500}Именно поэтому [character_name] не может привыкнуть к жизни в этой маленькой квартире. Это вызывает у н[ego_ee] разочарование и недовольство.{/color}"
    scene home_m
    "Time: 8:40"
    #show gg
    if character_name == "Ada":
        show gg_f at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    else:
        show gg_m at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    #show gg
    "(Телефонный звонок)"
    main"Ало, что звонишь пап?"
    "Richard" "[son], мы избаловали тебя"
    $ money = 0
    show screen money_display(money)
    "Richard" "Осознав это, мы решили лишить тебя денег чтобы подарить возможность стать самостоятельным членом общества"
    main"ЧТО?!" with vpunch
    main"Вы не можете, ваша обязанность меня содержать" with vpunch
    "(Звонок брошен)"
    main"Вы должны..." with dissolve
    main"Черт, надо выкручиваться"
    main"Пойду на работу, там у меня записаны клиенты"
    jump first_day
label first_day:
    scene office
    #show gg
    if character_name == "Ada":
        show gg_f at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    else:
        show gg_m at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    #show gg
    main"Ко мне сегодня придет {color=#FFA500}Виктория Синклер{/color}"
    main"Я читал[end_c] о ней вчера"
    main"32-летний инвестиционный банкир. Несмотря на успешную карьеру, она испытываете тревогу и стресс"
    main"Надо бы узнать об этом подробнее"
    "{color=#FFA500}Во время общения с клиентами нужно набирать очки симпатии{/color}"
    "{color=#FFA500}Если грубить клиентам и плохо общаться, то уровень симпатии будет понижен, что плохо скажется на взаимодействии{/color}"
    "{color=#FFA500}В конце диалога будет дана оценка{/color}"
    show victoria at Position(xpos = 0.7, xanchor=0.0, ypos=0.55, yanchor=0.6)
    v "Привет, [character_name]! Я записана к тебе на прием"
    "{color=#FFA500}Виктория Синклер{/color} довольно высокая женщина"
    "Она села напротив меня"
    python:
        import chatgpt
        import re
        apikey = renpy.store.api_gpt
        name = renpy.store.character_name 
        pol = renpy.store.gender
        rate_dialog = ''
        messages = [
            {"role": "system", "content": f"Ты Виктория Синклер, 32-летний инвестиционного банкира. Несмотря на успешную карьеру, Ты испытываешь тревогу и стресс, которые, по твоему мнению, влияют на принятие решений. Ты намерена обратиться за незаметной психологической помощью, чтобы восстановить свои позиции в мире финансов. Ты обратилась к одному из лучших психологов"},
            {"role": "assistant", "content": f"Привет {name}! Я записана к тебе на прием"},
        ]
        indx = 0
        while indx <= 5:
            user_input = renpy.input("Что сказать Виктории?", length=1000)
            rate_dialog += f'{name}: '+ user_input + '\n'
            main("[user_input]")
            messages.append(
                {"role": "user", "content": user_input + "\nВиктория:"}
            )
            print(messages)
            messages = chatgpt.completion(messages,api_key=apikey)
            response = messages[-1]["content"]
            rate_dialog += f'Victoria: '+ response + '\n'   
            if len(response) < 150 :
                v("[response]")
            else:
                split_into_sentences = []
                split_into_sentences = re.split(r'\.\s|\n\n', response)
    
                for sentence in split_into_sentences:
                    sentence = sentence.strip()
                    v("[sentence]")
            indx+=1
    "{color=#FFA500}Диалог окончен{/color}"
    python:
        import chatgpt
        evaluation_request = [
            {"role": "system", "content": f"Тебе нужно оценить как общался психолог {name} по 5 бальной шкале от 0(очень плохо) до 5(отлично), пожалуйста, напиши только 1 цифру и ничего больше \n {rate_dialog}"},
        ]
        print(evaluation_request)
        evaluation_messages = chatgpt.completion(evaluation_request, api_key=apikey)
        grade = evaluation_messages[-1]["content"]
    "Подсчет оценки закончен"
    "Оценка за этот диалог: {color=#FFA500}[grade]{/color}"
    hide victoria
    if int(grade) == 5:
        $ money = money + 300
        show screen money_display(money)
        "{color=#FFA500}Виктория Синклер{/color} ушла оставив оплату с сверхурочными"
    if int(grade) > 2 and int(grade) <5:
        $ money = money + 200
        show screen money_display(money)
        "{color=#FFA500}Виктория Синклер{/color} ушла оставив оплату"
    else:
        "{color=#FFA500}Виктория Синклер{/color} ушла не оставив оплату"
    show tomoko at Position(xpos = 0.7, xanchor=0.0, ypos=0.55, yanchor=0.6)
    "Как ушла Виктория, так сразу в комнату зашла невысокая девочка"
    show tomoko at Position(xpos = 0.7, xanchor=0.0, ypos=0.55, yanchor=0.6)
    t "П-п-привет!"
    t "Я пришла к вам на прием!"
    python:
        import chatgpt
        import re
        apikey = renpy.store.api_gpt
        name = renpy.store.character_name 
        pol = renpy.store.gender
        rate_dialog = ''
        messages = [
            {"role": "system", "content": f"Ты Томоко Куроки, 17-летняя девушка, страдающая социальным изоляцией и не имеющая друзей. Твоя жизнь полна неловкостей и ситуаций, в которых ты чувствуешь себя неуверенно. Ты решила обратиться за помощью, чтобы научиться лучше общаться с окружающими и наладить социальные отношения."},
            {"role": "assistant", "content": f"П-п-привет, {name}! Я пришла к вам на прием!"}
        ]
        indx = 0
        while indx <= 5:
            user_input = renpy.input("Что ответить Томоко?", length=1000)
            rate_dialog += f'{name}: '+ user_input + '\n'
            main(f"[user_input]")
            messages.append(
                {"role": "user", "content": user_input + "\nТомоко:"}
            )
            print(messages)
            messages = chatgpt.completion(messages, api_key=apikey)
            response = messages[-1]["content"]
            rate_dialog += f'Tomoko: '+ response + '\n'
            if len(response) < 150 :
                t("[response]")
            else:
                split_into_sentences = []
                split_into_sentences = re.split(r'\.\s|\n\n', response)
                for sentence in split_into_sentences:
                    sentence = sentence.strip()
                    t("[sentence]")
            indx+=1
    "{color=#FFA500}Диалог окончен{/color}"
    python:
        import chatgpt
        evaluation_request = [
            {"role": "system", "content": f"Тебе нужно оценить как общался психолог {name} по 5 бальной шкале от 0(очень плохо) до 5(отлично), пожалуйста, напиши только 1 цифру и ничего больше \n {rate_dialog}"},
        ]
        print(evaluation_request)
        evaluation_messages = chatgpt.completion(evaluation_request, api_key=apikey)
        grade = evaluation_messages[-1]["content"]
    python:
        grade = 5
    "Подсчет оценки закончен"
    "Оценка за этот диалог: {color=#FFA500}[grade]{/color}"
    if float(grade) >= 4:
        t"У нас получается так классно общаться"
        t"[character_name], не хотел[end_c] бы ты стать моим другом?"
        menu:
            "Принять дружбу с Томоко":
                $ tomoko_friend = True
                jump tomoko_accepted
            "Отклонить дружбу с Томоко":
                $ tomoko_friend = False
                jump tomoko_declined
    elif float(grade) == 3:
        $ tomoko_friend = False
        $ money = money + 200
        show screen money_display(money)
        "{color=#FF0000}Куроки Томоко{/color} оставила оплату и ушла"
    else:
        $ tomoko_friend = False
        "Видно как у {color=#FF0000}Томоко{/color} потекли слезы от обиды"
        t"Ты [bad]!!" with vpunch
        hide tomoko
        "Томоко выбежала из кабинета и молниеносно выбежала из здания рыдая"
        main"Эй! Ты не заплатила!" with vpunch


label tomoko_declined:
    #show gg
    if character_name == "Ada":
        show gg_f at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    else:
        show gg_m at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    #show gg
    main "Прости, Томоко, но я сейчас занят[end_c] и не могу взять на себя дополнительные обязательства"
    t"Понятно, я понимаю"
    t"Тогда до следующего приема"
    hide tomoko
    $ money = money + 200
    show screen money_display(money)
    "Томоко ушла, оставив оплату"
    main "Я забыл[end_c] позавтракать!" with vpunch
    jump coffee

label tomoko_accepted:
    main"Да, почему бы и нет"
    main"Я буду твоим другом"
    t"..." 
    t"Ура, я нашла себе первого друга" with vpunch
    main"Конечно, это отлично, не хочешь пойти со мной позавтракать?"
    t"Я уже завтракала, но все равно пойду с тобой за компанию" 
    jump coffee_t

label coffee:
    scene coff
    #show gg
    if character_name == "Ada":
        show gg_f at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    else:
        show gg_m at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    #show gg
    if money >= 6:
        "[character_name] заказал[end_c] кофе и круассанчик"
    else:
        main "у меня нет денег на поесть"
    main "Следующий клиент будет {color=#0f0}Таро Исимиси{/color}"
    main "В кратком резюме он описал что ему снятся аномальные сны, которые влияют на реальность без его участия"
    main "Я же не психотерапевт решать подобные проблемы" with vpunch
    jump taro_scene


label coffee_t:
    scene coff
    #show gg
    if character_name == "Ada":
        show gg_f at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    else:
        show gg_m at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    #show gg
    "[character_name] заказал[end_c] кофе и круассанчик"
    show tomoko at Position(xpos = 0.7, xanchor=0.0, ypos=0.55, yanchor=0.6)
    "Томоко заказала просто кофе"
    t"А как ты решил[end_c] стать психологом?"
    main "С детства удавалось понимать людей и мотивы их поступков"
    main "Я просто был[end_c] гением" with vpunch
    t"У тебя же есть образование психолога. Как ты получил[end_c] его?"
    main "Я закончил[end_c] Гарвардский университет 2 года назад"
    main "Бакалавриат психологии с отличием"
    t"Ого, а как ты закончил[end_c] его в таком юном возрасте?" with vpunch
    main "Вытащил[end_c] на интеллекте!"
    main "Окончил[end_c] школу в 11 лет" with dissolve 
    "Не могу же я сказать ей правду о том, что мне все проплатили родители"
    t"Как классно, ты [cool]!" with vpunch
    main "А ты кем планируешь стать?"
    t "Я пока не знаю, но думаю что хочу рисовать мангу!" with dissolve 
    main "Хорошо, Томоко, мне пора к следующему клиенту, классно посидели"
    t"Понимаю, а что насчет оплаты?" 
    main "Можешь не переживать об этом, мы справимся с твоей проблемой, заведешь друзей сколько захочешь и об оплате не беспокойся"
    t"Спасибо, я рада!" with vpunch
    "Томоко ушла"
    hide tomoko
    jump taro_scene

label taro_scene:
    scene office 
    #show gg
    if character_name == "Ada":
        show gg_f at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    else:
        show gg_m at Position(xpos = 0.1, xanchor=0.0, ypos=0.55, yanchor=0.5)
    #show gg
    main "Так, {color=#0f0}Таро Исимиси{/color}, утверждает что обладает удивительным даром видеть сны, предсказывающие будущее и прошлое."
    main"И что этот дар причиняет ему большие трудности в повседневной жизни."
    show taro at Position(xpos = 0.7, xanchor=0.0, ypos=0.55, yanchor=0.6)
    tr "Добрый день, [character_name]! Как я говорил ранее, я вижу аномальные сны"
    python:
        import chatgpt
        apikey = renpy.store.api_gpt
        name = renpy.store.character_name
        rate_dialog = ''
        messages = [
            {"role": "system", "content": f"Ты Таро Исимиси, молодой человек с удивительным даром видеть сны, предсказывающие будущее и прошлое. Этот дар причиняет тебе большие трудности в повседневной жизни. Ты обратился к психологу, чтобы попытаться разобраться с этой способностью и её влиянием на тебя."},
            {"role": "assistant", "content": f"Добрый день, {name}! Как я говорил ранее, я вижу аномальные сны"}
        ]
        
        indx = 0
        while indx <= 5:
            user_input = renpy.input("Что сказать Таро?", length=1000)
            rate_dialog += f'{name}: ' + user_input + '\n'
            main(f"[user_input]")
            messages.append(
                {"role": "user", "content": user_input + "\nТаро:"}
            )
            print(messages)
            messages = chatgpt.completion(messages, api_key=apikey)
            response = messages[-1]["content"]
            rate_dialog += f'Taro: ' + response + '\n'
            
            if len(response) < 150:
                tr("[response]")
            else:
                split_into_sentences = []
                split_into_sentences = re.split(r'\.\s|\n\n', response)
                
                for sentence in split_into_sentences:
                    sentence = sentence.strip()
                    tr("[sentence]")
            indx += 1
    
    "{color=#FFA500}Диалог окончен{/color}"
    python:
        evaluation_request = [
            {"role": "system", "content": f"Тебе нужно оценить, как общался психолог {name} по 5-балльной шкале от 0 (очень плохо) до 5 (отлично). Пожалуйста, напиши только 1 цифру и ничего больше.\n{rate_dialog}"}
        ]
        evaluation_messages = chatgpt.completion(evaluation_request, api_key=apikey)
        grade = evaluation_messages[-1]["content"]
    "Подсчет оценки закончен"
    "Оценка за этот диалог: {color=#FFA500}[grade]{/color}"
    
    if int(grade) == 5:
        hide taro
        $ money = money + 280
        show screen money_display(money)
        "{color=#FFA500}Таро Исимиси{/color} ушел, оставив оплату с бонусами"
    elif int(grade) > 2 and int(grade) < 5:
        hide taro
        $ money = money + 200
        show screen money_display(money)
        "{color=#FFA500}Таро Исимиси{/color} ушел, оставив оплату"
    else:
        taro"Я за такое платить не стану"
        hide taro
    
    
    return

