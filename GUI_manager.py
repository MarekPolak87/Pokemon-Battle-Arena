from tkinter import *
import tkinter
from tkinter import ttk
import pokemon_class, player_class, moves, list_pokemon, random

# creating players as objects of PLAYER class
player_1 = player_class.PLAYER()
player_2 = player_class.PLAYER()

party_size = 0
game_over = False
# attacking_move = ""
crit_ratio = False


def gui_start():
    global user_decision1, printing_console

    # creating main screen and label/entries for user input of team size and player names
    main_screen = tkinter.Tk()
    main_screen.geometry("1000x610")
    main_screen.title("Pokemon Battle Arena")
    main_screen.attributes('-topmost', False)
    lbl1 = Label(main_screen, text="Player 1: ")
    lbl1.place(x=10, y=45)
    user_entry1 = Entry(main_screen, relief=SUNKEN)
    user_entry1.place(x=80, y=45)

    lbl2 = Label(main_screen, text="Player 2: ")
    lbl2.place(x=800, y=45)
    user_entry2 = Entry(main_screen, relief=SUNKEN)
    user_entry2.place(x=870, y=45)

    lbl3 = Label(main_screen, text="How many Pokemons will be in each team? ")
    lbl3.place(x=300, y=85)
    user_entry3 = ttk.Combobox(main_screen, state="readonly", width=4, values=["1", "2", "3", "4", "5", "6"])
    user_entry3.place(x=550, y=85)

# in initial setup, player object instances are created and based on team size, pokemons are randomly chose as well as items
    def initial_setup() :
        global player_1, player_2, party_size
        player_1.name = str(user_entry1)
        player_class.players.append(player_1.name)
        player_1.name = str(user_entry2)
        player_2.turn = False
        player_class.players.append(player_2.name)
        party_size = x
        # choosing pokemons
        for i in range(1, party_size + 1) :
            player_1.choosing_pokemon(list_pokemon.list_of_pokemon[random.randint(0, 150)])
            player_2.choosing_pokemon(list_pokemon.list_of_pokemon[random.randint(0, 150)])
        # choosing items
        for i in range(1, 3) :
            player_1.items.append(random.choice(moves.Status_changers))
            player_2.items.append(random.choice(moves.Status_changers))
            randint = random.randint(0, 5)
            player_1.items.append(moves.Potions[randint])
            randint = random.randint(0, 5)
            player_2.items.append(moves.Potions[randint])
    # switching pokemons status if HP == 0
    def check_if_fainted(pok1, pok2) :
        if pok1.hp <= 0 :
            pok1.status = 12
        elif pok2.hp <= 0 :
            pok2.status = 12

    #function is called from switch pok function and does this: switching pokemon and printing the message, creating
    # all the buttons again so they can be deactivated/activated as
    # I can't use those variables from other functions(need to check it later)
    def validator_pokemon_change(user_decision3) :
        global player_on_turn, player_not_on_turn
        if player_1.turn :
            player_on_turn = player_1
            player_not_on_turn = player_2
        else :
            player_on_turn = player_2
            player_not_on_turn = player_1
        old_pok = getattr(player_on_turn.active_pokemon(), "name")
        player_on_turn.active_pokemon().chosen = False
        player_on_turn.pokemons[user_decision3 - 1].chosen = True
        printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
        printing_console1.place(x=340, y=440)
        btn_ch_pk1 = Button(main_screen, text="Change Pokemon", command=switch_pok, width=15)
        btn_ch_pk1.place(x=30, y=280)
        items1 = Button(main_screen, text="Items", width=15, command=items_viewer)
        items1.place(x=30, y=310)

        btn_ch_pk2 = Button(main_screen, text="Change Pokemon", command=switch_pok, width=15)
        btn_ch_pk2.place(x=850, y=280)
        items2 = Button(main_screen, text="Items", width=15, command=items_viewer)
        items2.place(x=850, y=310)
        btn_show_moves1 = Button(main_screen,
                                 text=f"Moves {getattr(player_1.active_pokemon(), "name")}",
                                 command=move_selector, width=20)
        btn_show_moves1.place(x=180, y=100)
        btn_show_moves2 = Button(main_screen,
                                 text=f"Moves {getattr(player_2.active_pokemon(), "name")}",
                                 command=move_selector, width=20)
        btn_show_moves2.place(x=680, y=100)

        turn_switcher()
        if player_on_turn == player_1 :
            btn_show_moves1["state"] = "active"
            btn_ch_pk1["state"] = "active"
            items1["state"] = "active"
            btn_show_moves2["state"] = "disabled"
            btn_ch_pk2["state"] = "disabled"
            items2["state"] = "disabled"
        elif player_on_turn == player_2 :
            btn_show_moves2["state"] = "active"
            btn_ch_pk2["state"] = "active"
            items2["state"] = "active"
            btn_show_moves1["state"] = "disabled"
            btn_ch_pk1["state"] = "disabled"
            items1["state"] = "disabled"
        printing_console1.insert(END, f"That's enough {old_pok}!\n"
                                      f"Let's go {getattr(player_on_turn.active_pokemon(), "name")}!")

    #creating new Toplevel window and displaying radiobuttons with available items
    def items_viewer() :
        newWindow = Toplevel(main_screen)

        def selection() :
            # global player_1, player_2
            selected = str(radio.get())

            if selected in player_on_turn.items :
                item_usage(selected)
                # if selected == "Revive":
                #     pass
                # else:
                #     turn_switcher()

            confirm_init_settings()
            newWindow.destroy()

        newWindow.title("Items")
        radio = tkinter.StringVar()
        # sets the geometry of toplevel
        newWindow.geometry("250x220")
        if player_1.turn :
            # global player_on_turn, player_not_on_turn
            player_on_turn = str(user_entry1.get())
            player_not_on_turn = player_2
        else :
            player_on_turn = str(user_entry2.get())
            player_not_on_turn = player_1

        label = Label(newWindow, text=f"\n{player_on_turn}'s available items: \n\n")
        label.pack()
        if player_1.turn :
            # global player_on_turn, player_not_on_turn
            player_on_turn = player_1
            player_not_on_turn = player_2
        else :
            player_on_turn = player_2
            player_not_on_turn = player_1

        if len(player_on_turn.items) > 0 :
            for i in range(0, len(player_on_turn.items)) :
                item_1 = Radiobutton(newWindow,
                                     text=f"{player_on_turn.items[i]}",
                                     height=1, width=25, value=f"{player_on_turn.items[i]}", variable=radio,
                                     command=selection, tristatevalue=0)
                item_1.pack(anchor=N)
        else :
            if player_1.turn :
                player_on_turn = str(user_entry1.get())
                player_not_on_turn = player_2
            else :
                player_on_turn = str(user_entry2.get())
                player_not_on_turn = player_1
            no_items_left = Label(newWindow, text=f"No more items available {player_on_turn}!")
            no_items_left.pack(anchor=N)

    #popping up window with pokemns in team as radiobuttons, when pokemon is selected it calls function validattor
    # pokemon change which does the change and then refreshes screen by calling confirm init setting function
    def switch_pok() :
        newWindow = Toplevel(main_screen)

        def selection() :
            selected = radio.get()
            validator_pokemon_change(selected)
            confirm_init_settings()
            # turn_switcher()

            newWindow.destroy()
        newWindow.title("New Window")
        radio = IntVar()
        # sets the geometry of toplevel
        newWindow.geometry("580x250")
        if player_1.turn :
            player_on_turn = player_1
            player_not_on_turn = player_2
        else :
            player_on_turn = player_2
            player_not_on_turn = player_1
        for i in range(1, x+1):
            try:
                player_on_turn.pokemons[i - 1]
            except IndexError:
                pass
            else:
                name = Radiobutton(newWindow,
                                text=f"{(getattr(player_on_turn.pokemons[i-1], "name")).capitalize()} / "
                                  f"{getattr(player_on_turn.pokemons[i-1], "hp")} / "
                                  f"Status: {pokemon_class.statuses[getattr(player_on_turn.pokemons[i-1], "status")]}\n\n"
                                  f"{player_on_turn.pokemons[i-1].move_1["name"]} / " 
                                  f"PP: {player_on_turn.pokemons[i-1].move_1["PP"]} / "
                                  f"{player_on_turn.pokemons[i-1].move_1["move_type"]}\n"
                                  f"{player_on_turn.pokemons[i-1].move_2["name"]} / "
                                  f"PP: {player_on_turn.pokemons[i-1].move_2["PP"]} / "
                                  f"{player_on_turn.pokemons[i-1].move_2["move_type"]}\n"
                                  f"{player_on_turn.pokemons[i-1].move_3["name"]} / "
                                  f"PP: {player_on_turn.pokemons[i-1].move_3["PP"]} / "
                                  f"{player_on_turn.pokemons[i-1].move_3["move_type"]}\n"
                                  f"{player_on_turn.pokemons[i-1].move_4["name"]} / "
                                  f"PP: {player_on_turn.pokemons[i-1].move_4["PP"]} / "
                                  f"{player_on_turn.pokemons[i-1].move_4["move_type"]}\n",
                                background=f"{getattr(player_on_turn.pokemons[i-1], "GUI_color")}",
                                variable= radio,
                                value=i,
                                command=selection)
                if i < 4:
                    name.grid(row=1, column= i)
                else:
                    name.grid(row=2, column=i - 3)

    #creates variables based on user inputs and calls initial setup on first runs (creating players and selecting pokemons and moves)
    #on every other run of this function, it just refreshes the labels and buttons on screen with up to date state
    def confirm_init_settings():
        global x, player_on_turn, player_not_on_turn, party_size
        t1 = int(user_entry3.get())
        x = t1
        pok_count = 1
        y_increment = 100
        if party_size < 1:
            initial_setup()
        else:
            pass
        conf_btn.place_forget()
        lbl3.place_forget()
        user_entry3.place_forget()
        party_size = x
        #creating pokemon labels player 1
        for i in range(1, x + pok_count):
            try:
                player_1.pokemons[i - 1]
            except IndexError:
                pass
            else:
                name1 = Label(main_screen,
                             text=f"{(getattr(player_1.pokemons[i-1], "name")).capitalize()} / "
                                  f"{getattr(player_1.pokemons[i-1], "hp")} / "
                                  f"{pokemon_class.statuses[getattr(player_1.pokemons[i-1], "status")]}",
                             height=2, width=18, background=f"{getattr(player_1.pokemons[i-1], "GUI_color")}",)
                name1.place(x=20, y=0 + y_increment)
                y_increment += 25
                pok_count += 1
        y_increment = 100
        pok_count = 1

        # creating pokemon labels player 2
        for i in range(1, x + pok_count):
            try:
                player_2.pokemons[i - 1]
            except IndexError:
                pass
            else:
                name2 = Label(main_screen,
                             text=f"{(getattr(player_2.pokemons[i - 1], "name")).capitalize()} / "
                                  f"{getattr(player_2.pokemons[i - 1], "hp")} / "
                                  f"{pokemon_class.statuses[getattr(player_2.pokemons[i - 1], "status")]}",
                             height=2, width=18, background=f"{getattr(player_2.pokemons[i - 1], "GUI_color")}")
                name2.place(x=850, y=0 + y_increment)
                y_increment += 25
                pok_count += 1

        btn_ch_pk1 = Button(main_screen, text="Change Pokemon", command=switch_pok, width=15)
        btn_ch_pk1.place(x=30, y=280)
        items1 = Button(main_screen, text="Items", width=15, command=items_viewer)
        items1.place(x=30, y=310)

        btn_ch_pk2 = Button(main_screen, text="Change Pokemon", command=switch_pok, width=15)
        btn_ch_pk2.place(x=850, y=280)
        items2 = Button(main_screen, text="Items",  width=15, command=items_viewer)
        items2.place(x=850, y=310)
        if player_1.turn :
            player_on_turn = player_1
            player_not_on_turn = player_2
        else :
            player_on_turn = player_2
            player_not_on_turn = player_1
        btn_show_moves1 = Button(main_screen,
                                text=f"Moves {getattr(player_1.active_pokemon(), "name")}",
                                command=move_selector, width=20)
        btn_show_moves1.place(x=180, y=100)
        btn_show_moves2 = Button(main_screen,
                                text=f"Moves {getattr(player_2.active_pokemon(), "name")}",
                                command=move_selector, width=20)
        btn_show_moves2.place(x=680, y=100)
        tkinter.img = PhotoImage(file=f"imgs1/{getattr(player_1.active_pokemon(), "name")}.gif")
        picture_label1 = Label(main_screen, width=280, height=280, anchor=NW, image=tkinter.img)
        picture_label1.place(x=180, y=150)
        picture_label1.update()

        hp1_bar = Label(main_screen, width=30, height=1, bg="grey",)
        hp1_bar.place(x=40, y=560)
        hp1_bar.update()

        hp2_bar = Label(main_screen, width=30, height=1, bg="grey")
        hp2_bar.place(x=720, y=560)
        hp2_bar.update()

        p1_hp = int(player_1.active_pokemon().hp / list_pokemon.pokemon_list[player_1.active_pokemon().name]["hp"] * 30)
        p2_hp = int(player_2.active_pokemon().hp / list_pokemon.pokemon_list[player_2.active_pokemon().name]["hp"] * 30)

        color_p1 = "green"
        color_p2 = "green"

        if 17 <= p1_hp < 24:
            color_p1 = "blue"
        elif 10 <= p1_hp < 17:
            color_p1 = "yellow"
        elif 3 <= p1_hp < 10:
            color_p1 = "orange"
        elif p1_hp < 3:
            color_p1 = "red"

        if 17 <= p2_hp < 24:
            color_p2 = "blue"
        elif 10 <= p2_hp < 17:
            color_p2 = "yellow"
        elif 3 <= p2_hp < 10:
            color_p2 = "orange"
        elif p2_hp < 3:
            color_p2 = "red"

        hp1_bar_height = Label(main_screen, width=p1_hp, height=1, bg=color_p1)
        hp1_bar_height.place(x=40, y=560)
        hp1_bar_height.update()

        hp2_bar_height = Label(main_screen, width=p2_hp, height=1, bg=color_p2)
        hp2_bar_height.place(x=720, y=560)
        hp2_bar_height.update()

        tkinter.img2 = PhotoImage(file=f"imgs/{getattr(player_2.active_pokemon(), "name")}.gif")
        picture_label2 = Label(main_screen, width=280, height=280, anchor=NW, image=tkinter.img2)
        picture_label2.place(x=550, y=150)
        picture_label2.update()

        def button_switcher():
            if player_on_turn == player_1:
                btn_show_moves1["state"] = "active"
                btn_ch_pk1["state"] = "active"
                items1["state"] = "active"
                btn_show_moves2["state"] = "disabled"
                btn_ch_pk2["state"] = "disabled"
                items2["state"] = "disabled"
            elif player_on_turn == player_2:
                btn_show_moves2["state"] = "active"
                btn_ch_pk2["state"] = "active"
                items2["state"] = "active"
                btn_show_moves1["state"] = "disabled"
                btn_ch_pk1["state"] = "disabled"
                items1["state"] = "disabled"
        button_switcher()
    # this function is called when Moves button is pressed, it creates Toplevel window with all available moves for
    # active pokemon by selecting radiobutton, it validates whether move has any PP left, when yes, activates main
    # engine function action and when not then calls itself again

    def move_selector() :
        newWindow = Toplevel(main_screen)

        def selection() :
            global player_1, player_2
            selected = str(radio.get())

            if player_on_turn.active_pokemon().move_1["name"] == selected:
                if player_on_turn.active_pokemon().move_1["PP"] > 0:
                    player_on_turn.active_pokemon().move_1["PP"] -= 1
                    action(selected)
                else:
                    newWindow.destroy()
                    move_selector()
            elif player_on_turn.active_pokemon().move_2["name"] == selected:
                if player_on_turn.active_pokemon().move_2["PP"] > 0:
                    player_on_turn.active_pokemon().move_2["PP"] -= 1
                    action(selected)
                else:
                    newWindow.destroy()
                    move_selector()
            elif player_on_turn.active_pokemon().move_3["name"] == selected:
                if player_on_turn.active_pokemon().move_3["PP"] > 0:
                    player_on_turn.active_pokemon().move_3["PP"] -= 1
                    action(selected)
                else :
                    newWindow.destroy()
                    move_selector()
            elif player_on_turn.active_pokemon().move_4["name"] == selected:
                if player_on_turn.active_pokemon().move_4["PP"] > 0:
                    player_on_turn.active_pokemon().move_4["PP"] -= 1
                    action(selected)
                else :
                    newWindow.destroy()
                    move_selector()
            confirm_init_settings()
            newWindow.destroy()

        newWindow.title("Moves")
        radio = tkinter.StringVar()
        # sets the geometry of toplevel
        newWindow.geometry("250x220")
        if player_1.turn :
            global player_on_turn, player_not_on_turn
            player_on_turn = player_1
            player_not_on_turn = player_2
        else :
            player_on_turn = player_2
            player_not_on_turn = player_1

        m1 = player_on_turn.active_pokemon().move_1["name"]
        m2 = player_on_turn.active_pokemon().move_2["name"]
        m3 = player_on_turn.active_pokemon().move_3["name"]
        m4 = player_on_turn.active_pokemon().move_4["name"]

        label = Label(newWindow, text=f"\n{player_on_turn.active_pokemon().name} available moves: \n\n")
        label.pack()
        if (player_on_turn.active_pokemon().move_1["PP"] > 0 or player_on_turn.active_pokemon().move_2["PP"] > 0 or
                player_on_turn.active_pokemon().move_3["PP"] > 0) or player_on_turn.active_pokemon().move_4["PP"] > 0:
            move_1 = Radiobutton(newWindow,
                         text=f"{player_on_turn.active_pokemon().move_1["name"]} / " 
                              f"PP: {player_on_turn.active_pokemon().move_1["PP"]} / "
                              f"{player_on_turn.active_pokemon().move_1["move_type"]}",
                        height=1, width=25, value=m1, variable= radio, command=selection, tristatevalue=0)
            move_1.pack(anchor=N)
            move_2 = Radiobutton(newWindow,
                           text=f"{player_on_turn.active_pokemon().move_2["name"]} / "
                                f"PP: {player_on_turn.active_pokemon().move_2["PP"]} / "
                                f"{player_on_turn.active_pokemon().move_2["move_type"]}",
                           height=1, width=25, value=m2, variable= radio, command=selection, tristatevalue=0)
            move_2.pack(anchor=N)
            move_3 = Radiobutton(newWindow,
                           text=f"{player_on_turn.active_pokemon().move_3["name"]} / "
                                f"PP: {player_on_turn.active_pokemon().move_3["PP"]} / "
                                f"{player_on_turn.active_pokemon().move_3["move_type"]}",
                           height=1, width=25, value=m3, variable= radio, command=selection, tristatevalue=0)
            move_3.pack(anchor=N)
            move_4 = Radiobutton(newWindow,
                           text=f"{player_on_turn.active_pokemon().move_4["name"]} / "
                                f"PP: {player_on_turn.active_pokemon().move_4["PP"]} / "
                                f"{player_on_turn.active_pokemon().move_4["move_type"]}",
                           height=1, width=25, value=m4, variable= radio, command=selection, tristatevalue=0)
            move_4.pack(anchor=N)
        else:
            no_PP_left = Radiobutton(newWindow,
                           text=f"{moves.moves_g1["Struggle"]["name"]} / "
                                f"PP: {moves.moves_g1["Struggle"]["PP"]} / "
                                f"{moves.moves_g1["Struggle"]["move_type"]}",
                           height=1, width=25, value=m4, variable= radio, command=selection, tristatevalue=0)
            no_PP_left.pack(anchor=N)

    def turn_switcher() :
        if player_1.turn :
            player_1.turn = False
            player_2.turn = True
        else :
            player_1.turn = True
            player_2.turn = False

    #this function is called from itemviewr when user selects radiobutton, it decides whether the item is some kind of
    # potion or status changer and acts accordingly. In case of revive it popps another window with fainted pokemons
    # which can be revived.
    def item_usage(item):
        global player_on_turn, player_not_on_turn
        if player_1.turn :
            player_on_turn = player_1
            player_not_on_turn = player_2
        else :
            player_on_turn = player_2
            player_not_on_turn = player_1
        pok1 = player_on_turn.active_pokemon()
        printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
        printing_console1.place(x=340, y=440)


        if item in moves.ITEMS["Status changers"]:
            if pok1.status == moves.ITEMS["Status changers"][item]:
                pok1.status = 1
                printing_console1.insert(END, f"{getattr(pok1, "name")} is healthy again!")
                player_on_turn.items.remove(item)
                confirm_init_settings()
                turn_switcher()
            else:
                if item == "Revive" :
                    revival = tkinter.Toplevel(main_screen)
                    revival.title("Revival")
                    revival.attributes('-topmost', True)
                    revival.geometry("250x220")
                    rev_label = Label(revival, text="Which Pokemon would you like to revive?")
                    rev_label.pack()
                    radio = tkinter.StringVar()

                    def revival_pok(pok) :
                        for i in player_on_turn.pokemons:
                            if i.name == pok:
                                i.status = 1
                                i.hp = int(list_pokemon.pokemon_list[i.name]["hp"] / 2)
                                player_on_turn.items.remove(item)
                                revival.destroy()
                                printing_console1.insert(END, f"{i.name} was revived with half of its original HP!")
                                turn_switcher()
                                confirm_init_settings()

                    def selection_revival() :
                        to_be_revived = str(radio.get())
                        revival_pok(to_be_revived)

                    for i in player_on_turn.pokemons :
                        if i.status == 12 :
                            new_label = Radiobutton(revival,
                                                    text=f"{i.name} / "
                                                         f"{i.hp} / "
                                                         f"{pokemon_class.statuses[i.status]}",
                                                    height=1, width=25,
                                                    value=i.name,
                                                    variable=radio, command=selection_revival,
                                                    tristatevalue=0)
                            new_label.pack(anchor=N)
                else:
                    printing_console1.insert(END, f"This item has no effect now.")
        elif item in moves.Potions :
                print("OK1")
                potion_screen = tkinter.Toplevel(main_screen)
                potion_screen.title("Potion")
                potion_screen.attributes('-topmost', True)
                potion_screen.geometry("250x220")
                potion_label = Label(potion_screen, text="Which Pokemon should drink that potion?")
                potion_label.pack()
                radio = tkinter.StringVar()

                def drinking_potion(pok) :
                    for i in player_on_turn.pokemons :
                        if i.name == pok :
                            i.hp += moves.ITEMS["Potions"][moves.Potions.index(item)][item]
                            player_on_turn.items.remove(item)
                            potion_screen.destroy()
                            if i.hp > list_pokemon.pokemon_list[pok1.name]["hp"] :
                                i.hp = list_pokemon.pokemon_list[pok1.name]["hp"]
                            printing_console1.insert(END, f"{i.name} health rose to {i.hp}!")
                            turn_switcher()
                            confirm_init_settings()

                def selection_potion() :
                    to_be_healed = str(radio.get())
                    drinking_potion(to_be_healed)

                for i in player_on_turn.pokemons :
                    new_label = Radiobutton(potion_screen,
                                            text=f"{i.name} / "
                                                 f"{i.hp} / "
                                                 f"{pokemon_class.statuses[i.status]}",
                                            height=1, width=25,
                                            value=i.name,
                                            variable=radio, command=selection_potion,
                                            tristatevalue=0)
                    new_label.pack(anchor=N)








            # for key1 in moves.ITEMS["Potions"] :
            #     for key in key1 :
            #         if key == item:
            #             pok1.hp += moves.ITEMS["Potions"][moves.ITEMS["Potions"].index(key1)][item]
            #             player_on_turn.items.remove(item)
            #         else:
            #             pass
            #
            # if pok1.hp > list_pokemon.pokemon_list[pok1.name]["hp"]:
            #     pok1.hp = list_pokemon.pokemon_list[pok1.name]["hp"]
            # printing_console1.insert(END, f"{getattr(pok1, "name")} health rose to {pok1.hp}!")

    #action is a main engine function, defines behavior of moves aligned to groups, battle mechanics and game over conditions
    def action(move) :
        global player_on_turn, player_not_on_turn
        if player_1.turn :
            player_on_turn = player_1
            player_not_on_turn = player_2
        else :
            player_on_turn = player_2
            player_not_on_turn = player_1
        pok1 = player_on_turn.active_pokemon()
        pok2 = player_not_on_turn.active_pokemon()
        #defines behavior of moves (in file moves) which are decreasing opponent accuracy by 1 stage

        def OPP_ACC_dec_1(add_checker) :
            pok1.status = 1
            if add_checker == 2:
                printing_console1.insert(END, f"{getattr(pok2, "name")}'s accuracy fell.")
                pok2.accuracy -= 1
            else:
                pok2.accuracy -= 1
                printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok2, "name")}'s accuracy fell.")

        # defines behavior of moves (in file moves) which are decreasing opponent attack by 1 stage
        def OPP_ATT_dec_1(add_checker) :
            pok1.status = 1
            if pok2.attack[1] > -6:
                pok2.attack[1] -= 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok2, "name")}'s attack fell.")
                else:
                    printing_console1.insert(END,f"{getattr(pok2, "name")}'s attack fell.")
            else:
                printing_console1.insert(END, "Nothing happened.")

        def OPP_CONFUSION() :
            pok1.status = 1
            if random.randint(1, 101) < 80 :
                pok2.status = 8
                printing_console1.insert(END,f"{getattr(pok2, "name")} became confused.")
            else:
                printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")

        # defines behavior of moves (in file moves) which are decreasing opponent defense by 1 stage
        def OPP_DEF_dec_1(add_checker) :
            pok1.status = 1
            if pok2.defense[1] > -6 :
                pok2.defense[1] -= 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok2, "name")}'s defense fell.")
                else:
                    printing_console1.insert(END,f"{getattr(pok2, "name")}'s defense fell.")
            else:
                printing_console1.insert(END, "Nothing happened.")

        # defines behavior of moves (in file moves) which are decreasing opponent defense by 2 stages
        def OPP_DEF_dec_2(add_checker) :
            pok1.status = 1
            if pok2.defense[1] > -5 :
                pok2.defense[1] -= 2
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok2, "name")}'s defense greatly fell.")
                else:
                    printing_console1.insert(END,f"{getattr(pok2, "name")}'s defense greatly fell.")
            elif pok2.defense[1] == -5:
                pok2.defense[1] -= 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                              f"{getattr(pok2, "name")}'s defense fell.")
                else:
                    printing_console1.insert(END,f"{getattr(pok2, "name")}'s defense fell.")
            else:
                printing_console1.insert(END, "Nothing happened.")

        def OPP_PARLYZ() :
            pok1.status = 1
            if random.randint(1, 101) < 80 :
                if pok2.type1 == "electric" or pok2.type2 == "electric":
                    printing_console1.insert(END, f"It has no effect on {getattr(pok2, "name")}.\n")
                else:
                    pok2.status = 3
                    printing_console1.insert(END, f"{getattr(pok2, "name")} paralyzed.\n"
                                                  f"It may not attack.")
            else:
                printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")

        def OPP_POISON() :
            pok1.status = 1
            if random.randint(1, 101) < 80 :
                if pok2.type1 == "poison" or pok2.type2 == "poison" :
                    printing_console1.insert(END, f"It has no effect on {getattr(pok2, "name")}.\n")
                else:
                    pok2.status = 7
                    printing_console1.insert(END, f"{getattr(pok2, "name")} poisoned.\n")
            else:
                printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")

        def OPP_SLEEP() :
            pok1.status = 1
            if random.randint(1,2) == 2:
                if pok2.status != 2:
                    pok2.status = 2
                    printing_console1.insert(END, f"{getattr(pok2, "name")} fell asleep.\n")
                else:
                    printing_console1.insert(END, f"{getattr(pok2, "name")} is already sleeping.\n"
                                                  f"Nothing happened.")
            else:
                printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")

        # defines behavior of moves (in file moves) which are increasing user attack by 1 stage
        def US_ATT1(add_checker) :
            pok1.status = 1
            if pok1.attack[1] < 6:
                pok1.attack[1] += 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok1, "name")}'s attack rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s attack rose.")
            else:
                printing_console1.insert(END, "Nothing happened.")

        # defines behavior of moves (in file moves) which are increasing user attack by 2 stages
        def US_ATT2(add_checker) :
            pok1.status = 1
            if pok1.attack[1] < 5:
                pok1.attack[1] += 2
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok1, "name")}'s attack greatly rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s attack greatly rose.")
            elif pok1.attack[1] == 5:
                pok1.attack[1] += 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                              f"{getattr(pok1, "name")}'s attack rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s attack rose.")
            else:
                printing_console1.insert(END, "Nothing happened.")


        # defines behavior of moves (in file moves) which are increasing user defense by 1 stage
        def US_DEF1(add_checker) :
            pok1.status = 1
            if pok1.defense[1] < 6:
                pok1.defense[1] += 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok1, "name")}'s defense rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s defense rose.")
            else:
                printing_console1.insert(END, "Nothing happened.")

        # defines behavior of moves (in file moves) which are increasing user defense by 2 stages
        def US_DEF2(add_checker) :
            pok1.status = 1
            if pok1.defense[1] < 5:
                pok1.defense[1] += 2
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok1, "name")}'s defense greatly rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s defense greatly rose.")
            elif pok1.defense[1] == 5:
                pok1.defense[1] += 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                              f"{getattr(pok1, "name")}'s defense rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s defense rose.")
            else :
                printing_console1.insert(END, "Nothing happened.")

        # defines behavior of moves (in file moves) which are increasing user evasion by 1 stage
        def US_EVAS1(add_checker) :
            pok1.status = 1
            if pok1.evasion < 6:
                pok1.evasion += 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok1, "name")}'s evasion rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s evasion rose.")
            else:
                printing_console1.insert(END, "Nothing happened.")

        # defines behavior of moves (in file moves) which are increasing user evasion by 2 stages
        def US_EVAS2(add_checker) :
            pok1.status = 1
            if pok1.evasion < 5:
                pok1.evasion += 2
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok1, "name")}'s evasion greatly rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s evasion greatly rose.")
            elif pok1.evasion == 5 :
                pok1.evasion += 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                              f"{getattr(pok1, "name")}'s evasion rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s evasion rose.")
            else :
                printing_console1.insert(END, "Nothing happened.")

        # defines behavior of moves (in file moves) which are increasing user special defense by 2 stages
        def US_SPCDEF2(add_checker) :
            pok1.status = 1
            if pok1.spec_def[1] < 5:
                pok1.spec_def[1] += 2
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok1, "name")}'s special defense greatly rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s special defense greatly rose.")
            elif pok1.spec_def[1] == 5 :
                pok1.spec_def[1] += 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                              f"{getattr(pok1, "name")}'s special defense rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s special defense rose.")
            else :
                printing_console1.insert(END, "Nothing happened.")

        # defines behavior of moves (in file moves) which are increasing user speed by 2 stages
        def US_SPEED2(add_checker) :
            pok1.status = 1
            if pok1.speed[1] < 6:
                pok1.speed[1] += 2
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok1, "name")}'s speed greatly rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s speed greatly rose.")
            elif pok1.speed[1] == 5:
                pok1.speed[1] += 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                              f"{getattr(pok1, "name")}'s speed rose.")
                else:
                    printing_console1.insert(END,f"{getattr(pok1, "name")}'s speed rose.")
            else:
                printing_console1.insert(END, "Nothing happened.")

        def OPP_BURN() :
            pok1.status = 1
            if random.randint(1, 101) < 80 :
                if pok2.type1 == "fire" or pok2.type2 == "fire" :
                    printing_console1.insert(END, f"It has no effect on {getattr(pok2, "name")}.\n")
                else:
                    pok2.status = 6
                    printing_console1.insert(END, f"{getattr(pok2, "name")} burned.\n")

            else:
                printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")

        def OPP_FLINCH() :
            pok1.status = 1
            if random.randint(1, 101) < 80 :
                pok2.status = 4
                printing_console1.insert(END, f"{getattr(pok2, "name")} flinched.\n")
            else:
                printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")


        def OPP_Freeze() :
            pok1.status = 1
            if random.randint(1, 101) < 80 :
                if pok2.type1 == "ice" or pok2.type2 == "ice" :
                    printing_console1.insert(END, f"It has no effect on {getattr(pok2, "name")}.\n")
                else:
                    pok2.status = 5
                    printing_console1.insert(END, f"{getattr(pok2, "name")} frozen.\n")
            else :
                printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")

        # defines behavior of moves (in file moves) which are decreasing opponent special defense by 1 stage
        def OPP_Specdef_dec_1(add_checker) :
            pok1.status = 1
            if pok2.spec_def[1] > -6:
                pok2.spec_def[1] -= 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok2, "name")}'s special defense fell.")
                else:
                    printing_console1.insert(END,f"{getattr(pok2, "name")}'s special defense fell.")
            else:
                printing_console1.insert(END, "Nothing happened.")

        def OPP_Speed_dec_1(add_checker) :
            pok1.status = 1
            if pok2.speed[1] > -6:
                pok2.speed[1] -= 1
                if add_checker != 2:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                          f"{getattr(pok2, "name")}'s speed fell.")
                else:
                    printing_console1.insert(END,f"{getattr(pok2, "name")}'s speed fell.")
            else:
                printing_console1.insert(END, "Nothing happened.")

        # calling all the above defined move groups
        def call_all_move_groups(add_checker) :
            if move in moves.OPP_ACC_dec_1 :
                OPP_ACC_dec_1(add_checker)
            elif move in moves.OPP_ATT_dec_1 :
                OPP_ATT_dec_1(add_checker)
            elif move in moves.OPP_CONFUSION :
                OPP_CONFUSION()
            elif move in moves.OPP_DEF_dec_1 :
                OPP_DEF_dec_1(add_checker)
            elif move in moves.OPP_DEF_dec_2 :
                OPP_DEF_dec_2(add_checker)
            elif move in moves.OPP_PARLYZ :
                OPP_PARLYZ()
            elif move in moves.OPP_POISON :
                OPP_POISON()
            elif move in moves.OPP_SLEEP :
                OPP_SLEEP()
            elif move in moves.US_ATT1 :
                US_ATT1(add_checker)
            elif move in moves.US_ATT2 :
                US_ATT2(add_checker)
            elif move in moves.US_DEF1 :
                US_DEF1(add_checker)
            elif move in moves.US_DEF2 :
                US_DEF2(add_checker)
            elif move in moves.US_EVAS1 :
                US_EVAS1(add_checker)
            elif move in moves.US_EVAS2 :
                US_EVAS2(add_checker)
            elif move in moves.US_SPCDEF2 :
                US_SPCDEF2(add_checker)
            elif move in moves.US_SPEED2 :
                US_SPEED2(add_checker)
            elif move in moves.OPP_BURN :
                OPP_BURN()
            elif move in moves.OPP_FLINCH :
                OPP_FLINCH()
            elif move in moves.OPP_Freeze :
                OPP_Freeze()
            elif move in moves.OPP_Specdef_dec_1 :
                OPP_Specdef_dec_1(add_checker)
            elif move in moves.OPP_Speed_dec_1 :
                OPP_Speed_dec_1(add_checker)


        #returns boolean for critical hit used in damage calculation formula
        def critical_hit_check(pok1, move):
            global crit_ratio
            benchmark = random.randint(1,256)
            if move in moves.US_CRITICAL:
                if int(pok1.speed[0] / 2) * 8 > benchmark :
                    crit_ratio = True
                    return crit_ratio
                else :
                    crit_ratio = False
                    return crit_ratio
            else:
                if int(pok1.speed[0] / 2) > benchmark:
                    crit_ratio = True
                    return crit_ratio
                else:
                    crit_ratio = False
                    return crit_ratio
        #returns coeficient for effectivity (move type against pokemon type) used later in damage formula
        def effectivity_checker(move, pok2):
            if str(moves.moves_g1[move]["move_type"]+"_"+ str(pok2.type1.upper())) in moves.no_effect:
                return 0
            elif str(moves.moves_g1[move]["move_type"]+"_"+ str(pok2.type1.upper())) in moves.not_very_effective:
                return 0.5
            elif str(moves.moves_g1[move]["move_type"]+"_"+ str(pok2.type1.upper())) in moves.super_effective:
                return 2
            else:
                return 1

#check whether pok status is paralyzed, asleep, poisoned, frozen, confused, burned or poisoned, if yes, switches turn and hit pokemon,
        # if it heals it does the selected move
        if 2 <= pok1.status <= 8:
            heal_checker = random.randint(1,5)
            if heal_checker == 1 or heal_checker == 2:
                printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
                printing_console1.place(x=340, y=440)
                if 5 <= pok1.status <= 8:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} is {pokemon_class.statuses[pok1.status]}.\n"
                                                  f"{getattr(pok1, "name")} suffers from being {pokemon_class.statuses[pok1.status]}")
                    pok1.hp -= int(1 / 16 * list_pokemon.pokemon_list[getattr(pok1, "name")]["hp"])
                    printing_console1.insert(END, f"\n{getattr(pok1, "name")}'s HP changed to: {pok1.hp}")
                    check_if_fainted(pok1, pok2)
                    turn_switcher()
                else:
                    printing_console1.insert(END, f"{getattr(pok1, "name")} is {pokemon_class.statuses[pok1.status]}.\n"
                                                  f"It can not attack.")
                    turn_switcher()
            else:
                if moves.moves_g1[move]["category"] == "status" :
                    printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
                    printing_console1.place(x=340, y=440)

                    if move in moves.OPP_ACC_dec_1 :
                        printing_console1.insert(END,f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_ACC_dec_1(1)
                    elif move in moves.OPP_ATT_dec_1 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_ATT_dec_1(1)
                    elif move in moves.OPP_CONFUSION :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_CONFUSION()
                    elif move in moves.OPP_DEF_dec_1 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_DEF_dec_1(1)
                    elif move in moves.OPP_DEF_dec_2 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_DEF_dec_2(1)
                    elif move in moves.OPP_PARLYZ :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_PARLYZ()
                    elif move in moves.OPP_POISON :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_POISON()
                    elif move in moves.OPP_SLEEP :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_SLEEP()
                    elif move in moves.US_ATT1 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        US_ATT1(1)
                    elif move in moves.US_ATT2 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        US_ATT2(1)
                    elif move in moves.US_DEF1 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        US_DEF1(1)
                    elif move in moves.US_DEF2 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        US_DEF2(1)
                    elif move in moves.US_EVAS1 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        US_EVAS1(1)
                    elif move in moves.US_EVAS2 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        US_EVAS2(1)
                    elif move in moves.US_SPCDEF2 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        US_SPCDEF2(1)
                    elif move in moves.US_SPEED2 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        US_SPEED2(1)
                    elif move in moves.OPP_BURN :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_BURN()
                    elif move in moves.OPP_FLINCH :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_FLINCH()
                    elif move in moves.OPP_Freeze :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_Freeze()
                    elif move in moves.OPP_Specdef_dec_1 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_Specdef_dec_1(1)
                    elif move in moves.OPP_Speed_dec_1 :
                        printing_console1.insert(END,
                                                 f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n")
                        OPP_Speed_dec_1(1)
                elif moves.moves_g1[move]["category"] == "physical" :
                    accuracy_check = random.randint(1, 101)
                    printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
                    printing_console1.place(x=340, y=440)
                    if critical_hit_check(pok1, move):
                        if (moves.moves_g1[move]["accuracy"] * pokemon_class.stat_changes_multipliers[pok1.accuracy] *
                                pokemon_class.stat_changes_multipliers[pok2.evasion * -1] > accuracy_check) :
                            damage = int((((2 * 50 / 5 + 2) * (pok1.attack[0] * pokemon_class.stat_changes_multipliers[
                                pok1.attack[1]]) * moves.moves_g1[move]["power"] / (pok2.defense[0] *
                                pokemon_class.stat_changes_multipliers[pok2.defense[1]])) / 50) + 2)
                            if move in moves.MULTI_HITTER:
                                repeater = random.randint(2,5)
                                for i in range(1, repeater + 1):
                                    pok2.hp -= (damage * 1.5) * effectivity_checker(move, pok2)
                                    if pok2.hp < 0 :
                                        pok2.hp = 0
                                    printing_console1.insert(END,
                                                             f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n"
                                                             f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}\n"
                                                             f"Critical hit!")
                                    if effectivity_checker(move, pok2) == 0 :
                                        printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                                    elif effectivity_checker(move, pok2) == 0.5 :
                                        printing_console1.insert(END, f"\nIt's not very effective.")
                                        printing_console1.insert(END,
                                                                 f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                    elif effectivity_checker(move, pok2) == 2 :
                                        printing_console1.insert(END, f"\nIt's super effective.")
                                        printing_console1.insert(END,
                                                                 f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                    else :
                                        printing_console1.insert(END,
                                                                 f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                    check_if_fainted(pok1, pok2)
                            else:
                                pok2.hp -= (damage * 1.5) * effectivity_checker(move, pok2)
                                if pok2.hp < 0 :
                                    pok2.hp = 0
                                printing_console1.insert(END, f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n"
                                                              f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}\n"
                                                              f"Critical hit!")
                                if effectivity_checker(move, pok2) == 0:
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                                elif effectivity_checker(move, pok2) == 0.5:
                                    printing_console1.insert(END, f"\nIt's not very effective.")
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                elif effectivity_checker(move, pok2) == 2:
                                    printing_console1.insert(END, f"\nIt's super effective.")
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                else:
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                check_if_fainted(pok1, pok2)
                            if pok2.hp != 0:
                                call_all_move_groups(2)

                    elif not crit_ratio:
                        if (moves.moves_g1[move]["accuracy"] * pokemon_class.stat_changes_multipliers[pok1.accuracy] *
                                pokemon_class.stat_changes_multipliers[pok2.evasion * -1] > accuracy_check) :
                            damage = int(
                                (((2 * 50 / 5 + 2) * (
                                        pok1.attack[0] * pokemon_class.stat_changes_multipliers[pok1.attack[1]]) *
                                  moves.moves_g1[move]["power"] / (pok2.defense[0] *
                                                                   pokemon_class.stat_changes_multipliers[
                                                                       pok2.defense[1]])) / 50) + 2)
                            if move in moves.MULTI_HITTER:
                                repeater = random.randint(2,5)
                                for i in range(1, repeater + 1):
                                    pok2.hp -= int(damage * effectivity_checker(move, pok2))
                                    if pok2.hp < 0 :
                                        pok2.hp = 0
                                    printing_console1.insert(END,
                                                             f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n"
                                                             f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}")
                                    if effectivity_checker(move, pok2) == 0 :
                                        printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                                    elif effectivity_checker(move, pok2) == 0.5 :
                                        printing_console1.insert(END, f"\nIt's not very effective.")
                                        printing_console1.insert(END,
                                                                 f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                    elif effectivity_checker(move, pok2) == 2 :
                                        printing_console1.insert(END, f"\nIt's super effective.")
                                        printing_console1.insert(END,
                                                                 f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                    else :
                                        printing_console1.insert(END,
                                                                 f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")

                                    check_if_fainted(pok1, pok2)
                            else:
                                pok2.hp -= int(damage * effectivity_checker(move, pok2))
                                if pok2.hp < 0 :
                                    pok2.hp = 0
                                printing_console1.insert(END,
                                                         f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n"
                                                         f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}")
                                if effectivity_checker(move, pok2) == 0:
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                                elif effectivity_checker(move, pok2) == 0.5:
                                    printing_console1.insert(END, f"\nIt's not very effective.")
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                elif effectivity_checker(move, pok2) == 2:
                                    printing_console1.insert(END, f"\nIt's super effective.")
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                else:
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")

                                check_if_fainted(pok1, pok2)
                            if pok2.hp != 0 :
                                call_all_move_groups(2)
                    else :
                        printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")
                        check_if_fainted(pok1, pok2)
                        pok1.status = 1
                elif moves.moves_g1[move]["category"] == "special" :
                    accuracy_check = random.randint(1, 101)
                    printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
                    printing_console1.place(x=340, y=440)
                    if critical_hit_check(pok1, move):
                        if (moves.moves_g1[move]["accuracy"] * pokemon_class.stat_changes_multipliers[pok1.accuracy] *
                                (pokemon_class.stat_changes_multipliers[pok2.evasion * -1]) > accuracy_check) :
                            damage = int(
                                (((2 * 50 / 5 + 2) * (
                                            pok1.spec_att[0] * pokemon_class.stat_changes_multipliers[pok1.spec_att[1]]) *
                                  moves.moves_g1[move]["power"] / (pok2.spec_def[0] *
                                                                   pokemon_class.stat_changes_multipliers[
                                                                       pok2.spec_def[1]])) / 50) + 2)
                            if move in moves.MULTI_HITTER:
                                repeater = random.randint(2,5)
                                for i in range(1, repeater + 1):
                                    pok2.hp -= int(damage * 1.5) * effectivity_checker(move, pok2)
                                    if pok2.hp < 0 :
                                        pok2.hp = 0
                                    printing_console1.insert(END,
                                                             f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n"
                                                             f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}"
                                                             f"Critical hit!")
                                    if effectivity_checker(move, pok2) == 0 :
                                        printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                                    elif effectivity_checker(move, pok2) == 0.5 :
                                        printing_console1.insert(END, f"\nIt's not very effective.")
                                        printing_console1.insert(END,
                                                                 f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                    elif effectivity_checker(move, pok2) == 2 :
                                        printing_console1.insert(END, f"\nIt's super effective.")
                                        printing_console1.insert(END,
                                                                 f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                    else :
                                        printing_console1.insert(END,
                                                                 f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                    check_if_fainted(pok1, pok2)
                            else:
                                pok2.hp -= int(damage * 1.5) * effectivity_checker(move, pok2)
                                if pok2.hp < 0 :
                                    pok2.hp = 0
                                printing_console1.insert(END,
                                                         f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n"
                                                         f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}"
                                                         f"Critical hit!")
                                if effectivity_checker(move, pok2) == 0:
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                                elif effectivity_checker(move, pok2) == 0.5:
                                    printing_console1.insert(END, f"\nIt's not very effective.")
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                elif effectivity_checker(move, pok2) == 2:
                                    printing_console1.insert(END, f"\nIt's super effective.")
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                else:
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                check_if_fainted(pok1, pok2)
                            if pok2.hp != 0 :
                                call_all_move_groups(2)
                    elif not crit_ratio:
                        if (moves.moves_g1[move]["accuracy"] * pokemon_class.stat_changes_multipliers[pok1.accuracy] *
                                (pokemon_class.stat_changes_multipliers[pok2.evasion * -1]) > accuracy_check) :
                            damage = int(
                                (((2 * 50 / 5 + 2) * (
                                            pok1.spec_att[0] * pokemon_class.stat_changes_multipliers[pok1.spec_att[1]]) *
                                  moves.moves_g1[move]["power"] / (pok2.spec_def[0] *
                                                                   pokemon_class.stat_changes_multipliers[
                                                                       pok2.spec_def[1]])) / 50) + 2)
                            if move in moves.MULTI_HITTER:
                                repeater = random.randint(2,5)
                                for i in range(1, repeater + 1):
                                    pok2.hp -= int(damage * effectivity_checker(move, pok2))
                                    if pok2.hp < 0 :
                                        pok2.hp = 0
                                    printing_console1.insert(END,
                                                             f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n"
                                                             f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}")
                                    if effectivity_checker(move, pok2) == 0 :
                                        printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                                    elif effectivity_checker(move, pok2) == 0.5 :
                                        printing_console1.insert(END, f"It's not very effective.")
                                        printing_console1.insert(END,
                                                                 f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                    elif effectivity_checker(move, pok2) == 2 :
                                        printing_console1.insert(END, f"It's not very effective.")
                                        printing_console1.insert(END,
                                                                 f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                    else :
                                        printing_console1.insert(END,
                                                                 f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                    check_if_fainted(pok1, pok2)
                            else:
                                pok2.hp -= int(damage * effectivity_checker(move, pok2))
                                if pok2.hp < 0 :
                                    pok2.hp = 0
                                printing_console1.insert(END,
                                                         f"{getattr(pok1, "name")} is not {pokemon_class.statuses[pok1.status]} anymore.\n"
                                                         f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}")
                                if effectivity_checker(move, pok2) == 0:
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                                elif effectivity_checker(move, pok2) == 0.5:
                                    printing_console1.insert(END, f"It's not very effective.")
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                elif effectivity_checker(move, pok2) == 2:
                                    printing_console1.insert(END, f"It's not very effective.")
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                else:
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                check_if_fainted(pok1, pok2)
                            pok1.status = 1
                            if pok2.hp != 0 :
                                call_all_move_groups(2)
                    else :
                        printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")
                        check_if_fainted(pok1, pok2)
                        pok1.status = 1
                check_if_fainted(pok1, pok2)
                turn_switcher()

# pokemon in OK status - does the damage or status change according move
        elif pok1.status == 1:
            if moves.moves_g1[move]["category"] == "status" :
                printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
                printing_console1.place(x=340, y=440)
                call_all_move_groups(2)

            elif moves.moves_g1[move]["category"] == "physical" :
                accuracy_check = random.randint(1,101)
                printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
                printing_console1.place(x=340, y=440)
                if critical_hit_check(pok1,move):
                    if (moves.moves_g1[move]["accuracy"] * pokemon_class.stat_changes_multipliers[pok1.accuracy] *
                            pokemon_class.stat_changes_multipliers[pok2.evasion * -1] > accuracy_check):
                        damage = int(
                            (((2 * 50 / 5 + 2) * (pok1.attack[0]*pokemon_class.stat_changes_multipliers[pok1.attack[1]]) *
                              moves.moves_g1[move]["power"] / (pok2.defense[0] *
                                pokemon_class.stat_changes_multipliers[pok2.defense[1]])) / 50) + 2)
                        if move in moves.MULTI_HITTER :
                            repeater = random.randint(2, 5)
                            for i in range(1, repeater + 1) :
                                pok2.hp -= int(damage * 1.5) * effectivity_checker(move, pok2)
                                if pok2.hp < 0 :
                                    pok2.hp = 0
                                printing_console1.insert(END,
                                                         f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                                         f"Critical hit!")
                                if effectivity_checker(move, pok2) == 0 :
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                                elif effectivity_checker(move, pok2) == 0.5 :
                                    printing_console1.insert(END, f"It's not very effective.")
                                    printing_console1.insert(END,
                                                             f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                elif effectivity_checker(move, pok2) == 2 :
                                    printing_console1.insert(END, f"It's super effective.")
                                    printing_console1.insert(END,
                                                             f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                else :
                                    printing_console1.insert(END,
                                                             f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                check_if_fainted(pok1, pok2)
                        else:
                            pok2.hp -= int(damage * 1.5) * effectivity_checker(move, pok2)
                            if pok2.hp < 0 :
                                pok2.hp = 0
                            printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n"
                                                          f"Critical hit!")
                            if effectivity_checker(move, pok2) == 0 :
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                            elif effectivity_checker(move, pok2) == 0.5 :
                                printing_console1.insert(END, f"It's not very effective.")
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                            elif effectivity_checker(move, pok2) == 2 :
                                printing_console1.insert(END, f"It's super effective.")
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                            else :
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                            check_if_fainted(pok1, pok2)
                        if pok2.hp != 0 :
                            call_all_move_groups(2)
                    else :
                        printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")
                        check_if_fainted(pok1, pok2)
                elif not crit_ratio:
                    if (moves.moves_g1[move]["accuracy"] * pokemon_class.stat_changes_multipliers[pok1.accuracy] *
                            pokemon_class.stat_changes_multipliers[pok2.evasion * -1] > accuracy_check) :
                        damage = int(
                            (((2 * 50 / 5 + 2) * (
                                        pok1.attack[0] * pokemon_class.stat_changes_multipliers[pok1.attack[1]]) *
                              moves.moves_g1[move]["power"] / (pok2.defense[0] *
                                                               pokemon_class.stat_changes_multipliers[
                                                                   pok2.defense[1]])) / 50) + 2)
                        if move in moves.MULTI_HITTER :
                            repeater = random.randint(2, 5)
                            for i in range(1, repeater + 1) :
                                pok2.hp -= int(damage * effectivity_checker(move, pok2))
                                if pok2.hp < 0 :
                                    pok2.hp = 0
                                printing_console1.insert(END,
                                                         f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n")
                                if effectivity_checker(move, pok2) == 0:
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                                elif effectivity_checker(move, pok2) == 0.5 :
                                    printing_console1.insert(END, f"It's not very effective.")
                                    printing_console1.insert(END,
                                                             f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                elif effectivity_checker(move, pok2) == 2:
                                    printing_console1.insert(END, f"It's super effective.")
                                    printing_console1.insert(END,
                                                             f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                else :
                                    printing_console1.insert(END,
                                                             f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                check_if_fainted(pok1, pok2)
                        else:
                            pok2.hp -= int(damage * effectivity_checker(move, pok2))
                            if pok2.hp < 0:
                                pok2.hp = 0
                            printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n")
                            if effectivity_checker(move, pok2) == 0 :
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                            elif effectivity_checker(move, pok2) == 0.5 :
                                printing_console1.insert(END, f"It's not very effective.")
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                            elif effectivity_checker(move, pok2) == 2 :
                                printing_console1.insert(END, f"It's super effective.")
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                            else:
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                            check_if_fainted(pok1, pok2)
                        if pok2.hp != 0 :
                            call_all_move_groups(2)
                    else:
                        printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")
                        check_if_fainted(pok1, pok2)
            elif moves.moves_g1[move]["category"] == "special" :
                accuracy_check = random.randint(1, 101)
                printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
                printing_console1.place(x=340, y=440)
                if critical_hit_check(pok1, move):
                    if (moves.moves_g1[move]["accuracy"] * pokemon_class.stat_changes_multipliers[pok1.accuracy] *
                            pokemon_class.stat_changes_multipliers[pok2.evasion * -1] > accuracy_check) :
                        damage = int(
                            (((2 * 50 / 5 + 2) * (pok1.spec_att[0] * pokemon_class.stat_changes_multipliers[pok1.spec_att[1]]) *
                              moves.moves_g1[move]["power"] / (pok2.spec_def[0] *
                                pokemon_class.stat_changes_multipliers[pok2.spec_def[1]])) / 50) + 2)
                        if move in moves.MULTI_HITTER :
                            repeater = random.randint(2, 5)
                            for i in range(1, repeater + 1) :
                                pok2.hp -= int(damage * 1.5) * effectivity_checker(move, pok2)
                                if pok2.hp < 0 :
                                    pok2.hp = 0
                                printing_console1 = Text(main_screen, width=48, height=7, font="Helvetica")
                                printing_console1.place(x=340, y=440)
                                printing_console1.insert(END,
                                                         f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n")
                                if effectivity_checker(move, pok2) == 0 :
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                                elif effectivity_checker(move, pok2) == 0.5 :
                                    printing_console1.insert(END, f"It's not very effective.")
                                    printing_console1.insert(END,
                                                             f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                elif effectivity_checker(move, pok2) == 2 :
                                    printing_console1.insert(END, f"It's super effective.")
                                    printing_console1.insert(END,
                                                             f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                else :
                                    printing_console1.insert(END,
                                                             f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                        else:
                            pok2.hp -= int(damage * 1.5) * effectivity_checker(move, pok2)
                            if pok2.hp < 0 :
                                pok2.hp = 0
                            printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
                            printing_console1.place(x=340, y=440)
                            printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n")
                            if effectivity_checker(move, pok2) == 0 :
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                            elif effectivity_checker(move, pok2) == 0.5 :
                                printing_console1.insert(END, f"It's not very effective.")
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                            elif effectivity_checker(move, pok2) == 2 :
                                printing_console1.insert(END, f"It's super effective.")
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                            else :
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                        if pok2.hp != 0 :
                            call_all_move_groups(2)
                    else :
                        printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")
                        check_if_fainted(pok1, pok2)
                elif not crit_ratio:
                    if (moves.moves_g1[move]["accuracy"] * pokemon_class.stat_changes_multipliers[pok1.accuracy] *
                            pokemon_class.stat_changes_multipliers[pok2.evasion * -1] > accuracy_check) :
                        damage = int(
                            (((2 * 50 / 5 + 2) * (
                                        pok1.spec_att[0] * pokemon_class.stat_changes_multipliers[pok1.spec_att[1]]) *
                              moves.moves_g1[move]["power"] / (pok2.spec_def[0] *
                                                               pokemon_class.stat_changes_multipliers[
                                                                   pok2.spec_def[1]])) / 50) + 2)
                        if move in moves.MULTI_HITTER :
                            repeater = random.randint(2, 5)
                            for i in range(1, repeater + 1) :
                                pok2.hp -= int(damage * effectivity_checker(move, pok2))
                                if pok2.hp < 0 :
                                    pok2.hp = 0
                                printing_console1 = Text(main_screen, width=48, height=7, font="Helvetica")
                                printing_console1.place(x=340, y=440)
                                printing_console1.insert(END,
                                                         f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n")
                                if effectivity_checker(move, pok2) == 0 :
                                    printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                                elif effectivity_checker(move, pok2) == 0.5 :
                                    printing_console1.insert(END, f"It's not very effective.")
                                    printing_console1.insert(END,
                                                             f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                elif effectivity_checker(move, pok2) == 2 :
                                    printing_console1.insert(END, f"It's super effective.")
                                    printing_console1.insert(END,
                                                             f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                                else :
                                    printing_console1.insert(END,
                                                             f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                        else:
                            pok2.hp -= int(damage * effectivity_checker(move, pok2))
                            if pok2.hp < 0 :
                                pok2.hp = 0
                            printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
                            printing_console1.place(x=340, y=440)
                            printing_console1.insert(END, f"{getattr(pok1, "name")} used {moves.moves_g1[move]["name"]}.\n")
                            if effectivity_checker(move, pok2) == 0 :
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}is not affected.")
                            elif effectivity_checker(move, pok2) == 0.5 :
                                printing_console1.insert(END, f"It's not very effective.")
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                            elif effectivity_checker(move, pok2) == 2 :
                                printing_console1.insert(END, f"It's super effective.")
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                            else :
                                printing_console1.insert(END, f"\n{getattr(pok2, "name")}'s HP changed to: {pok2.hp}\n")
                        if pok2.hp != 0 :
                            call_all_move_groups(2)
                    else :
                        printing_console1.insert(END, f"{getattr(pok1, "name")} missed.\n")
                        check_if_fainted(pok1, pok2)
            check_if_fainted(pok1, pok2)
            turn_switcher()
        # refresh after changes
        confirm_init_settings()
        # check whether there are any not fainted pokemon left in team 1, if not pop up window with game over appears
        healthy_pokemons = 0
        for i in player_1.pokemons :
            if i.status != 12 :
                healthy_pokemons += 1
        if healthy_pokemons == 0 :
            printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
            printing_console1.place(x=340, y=440)
            printing_console1.insert(END, (f"{str(user_entry1.get())} is out of usable Pokemons!\n"
                  f"{str(user_entry1.get())} lost!"))
            tkinter.img3 = PhotoImage(file=f"imgs/game_over.gif")
            newWindow1 = Toplevel(main_screen)
            newWindow1.geometry("405x290")
            picture_label2 = Label(newWindow1, width=540, height=308, anchor=NW, image=tkinter.img3)
            picture_label2.place(x=0, y=0)
            name = Label(newWindow1,
                         text=f"You LOST {str(user_entry1.get())}!\n", bg="red"
                         )
            name.place(x=150, y=20)
            name.lift()
            newWindow1.attributes("-topmost", True)

            def end() :
                main_screen.destroy()

            go_btn = Button(newWindow1, text="GAME OVER", command=end, height=1, width=20)
            go_btn.pack()
        # check whether there are any not fainted pokemon left in team 2, if not pop up window with game over appears
        healthy_pokemons = 0
        for i in player_2.pokemons :
            if i.status != 12 :
                healthy_pokemons += 1
        if healthy_pokemons == 0 :
            printing_console1 = Text(main_screen, width=35, height=8, font= "Helvetica")
            printing_console1.place(x=340, y=440)
            printing_console1.insert(END, (f"{str(user_entry2.get())} is out of usable Pokemons!\n"
                                           f"{str(user_entry2.get())} lost!"))
            tkinter.img3 = PhotoImage(file=f"imgs/game_over.gif")
            newWindow1 = Toplevel(main_screen)
            newWindow1.geometry("405x290")
            picture_label2 = Label(newWindow1, width=540, height=308, anchor=NW, image=tkinter.img3)
            picture_label2.place(x=0, y=0)
            name = Label(newWindow1,
                         text=f"You LOST {str(user_entry2.get())}!\n", bg="red"
                         )
            name.place(x= 150, y= 20)
            name.lift()
            newWindow1.attributes("-topmost", True)

            def end():
                main_screen.destroy()
            go_btn = Button(newWindow1, text="GAME OVER", command=end, height=1, width=20, bg="red")
            go_btn.place(x= 110, y= 50)
            go_btn.lift()

    conf_btn = Button(main_screen, text="Confirm initial settings", command=confirm_init_settings)
    conf_btn.place(x=420, y=40)

    main_screen.mainloop()

