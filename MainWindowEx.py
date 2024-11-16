import math

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from MainWindow import Ui_MainWindow

class MainWindowEx(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Kết nối các nút với các hàm xử lý
        self.ui.button_calculate.clicked.connect(self.calculate_monthly_payment)
        self.ui.button_clear.clicked.connect(self.clear_fields)
        self.ui.button_exit.clicked.connect(self.close_application)

    def calculate_monthly_payment(self):
        try:
            #Lấy các giá trị nhập từ giao diện
            loan_amount = float(self.ui.lineEdit_loan_amount.text())
            annual_interest_rate = float(self.ui.lineEdit_interest_rate.text()) / 100   #Chuyển từ phần trăm sang số thập phân
            loan_duration_years = int(self.ui.lineEdit_loan_duration.text())

            #Tính toán lãi suất hàng tháng và số kỳ hạn
            monthly_interest_rate = annual_interest_rate / 12
            total_payments = loan_duration_years * 12

            #Công thức tính khoản thanh toán hàng tháng
            monthly_payment = (loan_amount * monthly_interest_rate) / (1-math.pow((1 + monthly_interest_rate), -total_payments))

            #Hiện thị kết quả lên giao diện
            self.ui.label_result.setText(f"Khoản thanh toán hàng tháng: {monthly_payment:,.2f} VNĐ")
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập các giá trị hợp lệ cho tất cả các trường.")

    def clear_fields(self):
        #Xóa nội dung các ô nhập và nhận kết quả
        self.ui.lineEdit_loan_amount.clear()
        self.ui.lineEdit_interest_rate.clear()
        self.ui.lineEdit_loan_duration.clear()
        self.ui.label_result.setText("Kết quả sẽ hiện thị tại đây.")

    def close_application(self):
        self.close()
