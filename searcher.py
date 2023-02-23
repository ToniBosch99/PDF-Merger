import os
import PySimpleGUI as sg
from PLUS_ICO import PLUS_ICO

def add_pdf(i = 2):
    name = f'-INPUT{i}-'
    return [[sg.Input(key=name), sg.FilesBrowse()]]


def create_layout():
    input_pdf_layout = [
        [sg.Text('Select PDFs to be merged')],
        [sg.Input(key='-INPUT1-'), sg.FilesBrowse(), sg.Button(enable_events=True, image_data=PLUS_ICO, key="-ADD-")],
        [sg.Input(key='-INPUT2-'), sg.FilesBrowse()]

    ]

    output_pdf_layout = [
        [sg.Text('Select folder where the merged PDF is going to be stored')],
        [sg.Input(key='-OUTPUT-FOLDER-'), sg.FolderBrowse()],
        [sg.Text('Write the name of the PDF')],
        [sg.Input(key='-OUTPUT-NAME-')],
    ]

    layout = [
        [sg.Column(input_pdf_layout, key='-in_lay-'), sg.VerticalSeparator(), sg.Column(output_pdf_layout)],
        [sg.Button('Merge')]
    ]
    return layout


def open_window():
    sg.theme("DarkBlue3")
    sg.set_options(font=("Courier New", 12))
    i = 3

    layout = create_layout()
    window = sg.Window('PDF merger', layout, finalize=True)

    while True:

        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == '-ADD-':
            window.extend_layout(window['-in_lay-'], add_pdf(i))

        elif event == 'Merge':
            pdf_list = [fr'{values[i]}' for i in values.keys() if i.startswith('-INPUT')]
            out_folder = values['-OUTPUT-FOLDER-'] 
            out_name = values['-OUTPUT-NAME-'] + '.pdf'
            out_path = os.path.join(out_folder, out_name)
            return pdf_list, out_path
        
        

    window.close()
    


