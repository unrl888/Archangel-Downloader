def get_style():
    style = """
        QPushButton {
        background-color:rgba(0, 0, 0, 0.31);       /* Цвет фона */
        color:rgb(146, 146, 146);
        font-weight: bold;                    /* Цвет текста */
        border-radius: 15px;             /* Скругление углов */
        padding: 8px 16px;               /* Внутренние отступы */
            font-size: 18px;
        }
        QPushButton:hover {
        background-color: rgba(0, 0, 0, 50)     /* При наведении */

        }
        QPushButton:pressed {
        background-color: None;       /* При клике */

        }   


        QLineEdit {
        background-color: rgba(255, 255, 255, 0.2); /* Прозрачный белый */
        color: rgb(196, 196, 196);
        border: 1px solid #969696;
        border-radius: 10px;
        padding: 5px 10px;
        font-size: 14px;
        }

        QLabel {
        color: rgb(172, 172, 172);
        font-size: 14px;
        font-weight: bold;
        }
        QWidget {
        background-color: rgba(255, 255, 255, 0);  /* Прозрачный тёмный фон */

        }

        QLabel {
        background-color: transparent;
        }
        """
    return style