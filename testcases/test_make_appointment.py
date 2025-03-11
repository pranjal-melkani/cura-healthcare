from pages.homepage import Homepage
from pages.appointmentpage import Appointmentpage
import time, pytest

class Test_MakeAppointment:
    def test_make_appointment(self, driver):
        username = "John Doe"
        password = "ThisIsNotAPassword"
        facility = "Tokyo CURA Healthcare Center"
        hospital_readmission = True
        healthcare_program = "medicaid"
        visit_date = "10/03/2025"
        comments = "This is a test comment"

        hp = Homepage(driver)
        hp.make_appointments(username,password,facility,hospital_readmission,healthcare_program, visit_date, comments)
        ap = Appointmentpage(driver)
        ap.goto_homepage()

    def test_appointment_history(self, driver):
        facility = "Tokyo CURA Healthcare Center"
        hospital_readmission = True
        healthcare_program = "medicaid"
        visit_date = "10/03/2025"
        comments = "This is a test comment"

        hp = Homepage(driver)
        hp.open_appointment_history()
        
