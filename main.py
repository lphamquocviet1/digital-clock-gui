import sys

from PyQt6.QtCore import QDate, QTime, QTimer, Qt
from PyQt6.QtGui import QColor, QFont, QFontDatabase
from PyQt6.QtWidgets import (QApplication,QFrame,QGraphicsDropShadowEffect,QHBoxLayout,QLabel,QMainWindow,QPushButton,QVBoxLayout,QWidget,)


class ClockWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.use_24_hour_time = True
        self.setWindowTitle("My Clock")
        self.setMinimumSize(700, 430)
        self.resize(820, 480)

        self.build_window()
        self.set_theme()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_current_time)
        self.timer.start(500)
        self.show_current_time()

    def build_window(self):
        page = QWidget()
        page.setObjectName("page")
        page_layout = QVBoxLayout(page)
        page_layout.setContentsMargins(48, 42, 48, 42)

        clock_card = QFrame()
        clock_card.setObjectName("clockCard")

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(45)
        shadow.setOffset(0, 15)
        shadow.setColor(QColor(0, 0, 0, 110))
        clock_card.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout(clock_card)
        card_layout.setContentsMargins(48, 38, 48, 40)
        card_layout.setSpacing(0)

        header = QHBoxLayout()

        brand = QLabel("MOMENT")
        brand.setObjectName("brand")

        live_area = QHBoxLayout()
        live_area.setSpacing(8)

        live_dot = QLabel("●")
        live_dot.setObjectName("liveDot")

        live_text = QLabel("LOCAL TIME")
        live_text.setObjectName("liveText")

        live_area.addWidget(live_dot)
        live_area.addWidget(live_text)

        header.addWidget(brand)
        header.addStretch()
        header.addLayout(live_area)

        self.day_label = QLabel()
        self.day_label.setObjectName("dayLabel")

        time_row = QHBoxLayout()
        time_row.setSpacing(14)

        self.main_time_label = QLabel()
        self.main_time_label.setObjectName("mainTime")

        self.seconds_label = QLabel()
        self.seconds_label.setObjectName("seconds")
        self.seconds_label.setAlignment(
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft
        )

        self.period_label = QLabel()
        self.period_label.setObjectName("period")
        self.period_label.setAlignment(
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft
        )

        time_row.addWidget(self.main_time_label)
        time_row.addWidget(self.seconds_label)
        time_row.addWidget(self.period_label)
        time_row.addStretch()

        footer = QHBoxLayout()
        footer.setContentsMargins(0, 24, 0, 0)

        self.date_label = QLabel()
        self.date_label.setObjectName("dateLabel")

        self.format_button = QPushButton("Switch to 12-hour")
        self.format_button.setObjectName("formatButton")
        self.format_button.setAccessibleName("Switch to 12-hour time")
        self.format_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.format_button.clicked.connect(self.change_time_format)

        footer.addWidget(self.date_label)
        footer.addStretch()
        footer.addWidget(self.format_button)

        card_layout.addLayout(header)
        card_layout.addStretch()
        card_layout.addWidget(self.day_label)
        card_layout.addSpacing(8)
        card_layout.addLayout(time_row)
        card_layout.addStretch()
        card_layout.addLayout(footer)

        page_layout.addWidget(clock_card)
        self.setCentralWidget(page)

    def set_theme(self):
        clock_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        clock_font.setPointSize(78)
        clock_font.setWeight(QFont.Weight.Medium)
        self.main_time_label.setFont(clock_font)

        self.setStyleSheet(
            """
            QMainWindow, QWidget#page {
                background: #111318;
                color: #f7f3ea;
            }

            QLabel {
                background: transparent;
            }

            QFrame#clockCard {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #252936,
                    stop: 0.55 #1d202a,
                    stop: 1 #181a22
                );
                border: 1px solid #353a49;
                border-radius: 28px;
            }

            QLabel#brand {
                color: #f0b35a;
                font-size: 13px;
                font-weight: 800;
                letter-spacing: 5px;
            }

            QLabel#liveDot {
                color: #75d69c;
                font-size: 11px;
            }

            QLabel#liveText {
                color: #8e95a5;
                font-size: 11px;
                font-weight: 700;
                letter-spacing: 2px;
            }

            QLabel#dayLabel {
                color: #a4aaba;
                font-size: 16px;
                font-weight: 600;
                letter-spacing: 2px;
            }

            QLabel#mainTime {
                color: #fffaf0;
            }

            QLabel#seconds {
                color: #f0b35a;
                font-size: 30px;
                font-weight: 700;
                padding-bottom: 17px;
            }

            QLabel#period {
                color: #8e95a5;
                font-size: 16px;
                font-weight: 700;
                padding-bottom: 20px;
            }

            QLabel#dateLabel {
                color: #c7cbd4;
                font-size: 15px;
            }

            QPushButton#formatButton {
                background: #2b303d;
                color: #d8dbe2;
                border: 1px solid #3d4352;
                border-radius: 14px;
                padding: 9px 16px;
                font-size: 11px;
                font-weight: 800;
                letter-spacing: 1px;
            }

            QPushButton#formatButton:hover {
                background: #f0b35a;
                border-color: #f0b35a;
                color: #1a1c22;
            }

            QPushButton#formatButton:pressed {
                background: #d99a44;
            }
            """
        )

    def show_current_time(self):
        now = QTime.currentTime()
        today = QDate.currentDate()

        if self.use_24_hour_time:
            time_text = now.toString("HH:mm")
            period = ""
        else:
            hour = now.hour() % 12 or 12
            time_text = f"{hour:02d}:{now.minute():02d}"
            period = "AM" if now.hour() < 12 else "PM"

        self.main_time_label.setText(time_text)
        self.seconds_label.setText(now.toString("ss"))
        self.period_label.setText(period)
        self.day_label.setText(today.toString("dddd").upper())
        self.date_label.setText(today.toString("MMMM d  •  yyyy"))

    def change_time_format(self):
        self.use_24_hour_time = not self.use_24_hour_time

        next_format = "12-hour" if self.use_24_hour_time else "24-hour"
        self.format_button.setText(f"Switch to {next_format}")
        self.format_button.setAccessibleName(f"Switch to {next_format} time")
        self.show_current_time()


def main():
    app = QApplication(sys.argv)
    window = ClockWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
