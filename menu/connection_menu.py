from ui.ui_elements.label import Label
from ui.ui_elements.button import Button
from ui.ui_elements.entry import Entry
from ui.ui_elements.radioButton import RadioButton
from ui.ui_elements.textBox import TextBox
from ui.ui_elements.switch import Switch


class ConnectionMenu:
    @staticmethod
    def show_label(options: list[dict], master) -> list[dict]:
        labels: list[dict] = []
        for label in range(len(options)):
            item = Label(text=options[label]['Name'], master=master).add_label()
            item.place(x=options[label]['x'], y=options[label]['y'], anchor='center')

            labels.append({"Name": options[label]['Name'],
                           "Item": item,
                           "Place": item.place(x=options[label]['x'], y=options[label]['y'], anchor='center')})

        return labels

    @staticmethod
    def show_button(options: list[dict], master, command: dict) -> list[dict]:
        buttons: list[dict] = []
        for button in range(len(options)):
            item = Button(text=options[button]['Text'],
                          fg_color=options[button]['fg_color'],
                          hover_color=options[button]['hover_color'],
                          command=command[options[button]['Name']],
                          master=master
                          ).add_button()

            buttons.append({"Name": options[button]['Name'],
                            "Item": item,
                            "Place": item.place(x=options[button]['x'], y=options[button]['y'], anchor='center')})

        return buttons

    @staticmethod
    def show_entry(options: list[dict], master) -> list[dict]:
        entries: list[dict] = []
        for entry in range(len(options)):
            item = Entry(master=master).add_entry()

            entries.append({"Name": options[entry]['Name'],
                            "Item": item,
                            "Place": item.place(x=options[entry]['x'], y=options[entry]['y'], anchor='center')})

        return entries

    @staticmethod
    def show_radio_button(options: list[dict], master, command: dict, variable: dict) -> list[dict]:
        radio_buttons: list[dict] = []
        for radio_button in range(len(options)):
            item = RadioButton(text=options[radio_button]['Text'],
                               command=command[options[radio_button]['Command']],
                               variable=variable[options[radio_button]['Variable']],
                               value=options[radio_button]['Value'],
                               master=master
                               ).add_radio_button()

            radio_buttons.append({"Name": options[radio_button]['Name'],
                                  "Item": item,
                                  "Place": item.place(x=options[radio_button]['x'], y=options[radio_button]['y'],
                                                      anchor='center')})

        return radio_buttons

    @staticmethod
    def show_text_box(options: list[dict], master) -> list[dict]:
        text_boxes: list[dict] = []
        for text_box in range(len(options)):
            item = TextBox(master=master).add_text_box()
            text_boxes.append({"Name": options[text_box]['Name'],
                               "Item": item,
                               "Place": item.place(x=options[text_box]['x'], y=options[text_box]['y'],
                                                   anchor='center')})

        return text_boxes

    @staticmethod
    def show_switch(options: list[dict], master: object, variable: dict, command: dict) -> list[dict]:
        switches: list[dict] = []
        for switch in range(len(options)):
            item = Switch(master=master,
                          text=options[switch]['Text'],
                          command=command[options[switch]['Command']],
                          variable=variable[options[switch]['Variable']],
                          state=options[switch]['State'],
                          ).add_switch()

            switches.append({"Name": options[switch]['Name'],
                             "Item": item,
                             "Place": item.place(x=options[switch]['x'], y=options[switch]['y'],
                                                 anchor='center')})

        return switches
