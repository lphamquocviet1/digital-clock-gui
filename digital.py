import sys

from PyQt6.QtCore import QDate, QTime, QTimer, Qt
from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QVBoxLayout, QWidget,
)


class ClockWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.use_24_hour_time = True
        self.setWindowTitle("My Clock")
        self.setMinimumSize(520, 280)
        self.resize(580, 320)

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
        page_layout.setContentsMargins(32, 28, 32, 28)
        page_layout.setSpacing(16)

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

        page_layout.addStretch()
        page_layout.addLayout(time_row)
        page_layout.addLayout(footer)
        page_layout.addStretch()
        self.setCentralWidget(page)

    def set_theme(self):
        clock_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        clock_font.setPointSize(64)
        self.main_time_label.setFont(clock_font)

        self.setStyleSheet(
            """
            QMainWindow, QWidget#page {
                background: #222222;
                color: #eeeeee;
            }
            QLabel {
                background: transparent;
                color: #eeeeee;
            }
            QLabel#seconds {
                color: #aaaaaa;
                font-size: 24px;
                padding-bottom: 12px;
            }
            QLabel#period {
                color: #aaaaaa;
                font-size: 16px;
                padding-bottom: 14px;
            }
            QLabel#dateLabel {
                color: #bbbbbb;
                font-size: 14px;
            }
            QPushButton#formatButton {
                background: #333333;
                color: #eeeeee;
                border: 1px solid #666666;
                border-radius: 4px;
                padding: 7px 10px;
            }
            QPushButton#formatButton:hover {
                background: #444444;
            }
            QPushButton#formatButton:pressed {
                background: #292929;
            }
            QPushButton#formatButton:focus {
                border: 2px solid #eeeeee;
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
        self.date_label.setText(today.toString("ddd, MMM d, yyyy"))

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
