MAIN_WINDOW_STYLE = """
QPushButton{
    background-color: rgb(0, 0, 0);
    color: rgb(0, 255, 0);
}

QLabel{
    color: rgb(0, 255, 0);
}

QWidget#main_window{
    background-color: rgb(0, 0, 0);
}

QPushButton:hover{
    border: 1px solid rgb(0, 255, 0);
}

QPushButton:pressed{
    background-color: rgb(130, 130, 130);
}
"""
ENCRYPT_DIALOG_STYLE = """QPushButton{
    background-color: rgb(0, 0, 0);
    color: rgb(0, 255, 0);
}

QLabel{
    color: rgb(0, 255, 0);
}

QWidget#encrypt_dialog{
    background-color: rgb(0, 0, 0);
}

QPushButton:hover{
    border: 1px solid rgb(0, 255, 0);
}

QPushButton:pressed{
    background-color: rgb(130, 130, 130);
}

QLineEdit{
    background-color: rgb(0, 0, 0);
    border: 1px dashed rgb(255, 255, 255);
    color: rgb(0, 255, 0);
}

QLineEdit:hover{
    border: 1px solid rgb(255, 255, 255);
}
QListWidget{
    color: rgb(0, 255, 0);
    background-color: rgb(0, 0, 0);
    font: 8pt "Segoe Print";
    border: 1px dashed rgb(255, 255, 255);
}
"""

DECRYPT_DIALOG_STYLE = """
QPushButton{
    background-color: rgb(0, 0, 0);
    color: rgb(0, 255, 0);
}




QLabel{
    color: rgb(0, 255, 0);
}


QWidget#decrypt_dialog{
    background-color: rgb(0, 0, 0);
}

QPushButton:hover{
    border: 1px solid rgb(0, 255, 0);
}

QPushButton:pressed{
    background-color: rgb(130, 130, 130);
}

QLineEdit{
    background-color: rgb(0, 0, 0);
    border: 1px dashed rgb(255, 255, 255);
    color: rgb(0, 255, 0);
}

QLineEdit:hover{
    border: 1px solid rgb(255, 255, 255);
}


QListWidget{
    color: rgb(0, 255, 0);
    background-color: rgb(0, 0, 0);
    font: 8pt "Segoe Print";
    border: 1px dashed rgb(255, 255, 255);
}


"""
TEXT_STYLE = "font: 8pt \"Segoe Print\";"
