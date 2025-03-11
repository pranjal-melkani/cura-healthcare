from base.basedriver import Basedriver

class Homepage(Basedriver):
    MENU_TOGGLE = "//*[@id='menu-toggle']"
    LOGIN_LINK = "//*[text()='Login']"
    LOGOUT_LINK = "//*[text()='Logout']"
    PROFILE_LINK = "//*[text()='Profile']"
    HISTORY_LINK = "//*[text()='History']"
    USERNAME_FIELD = "//*[@id='txt-username']"
    PASSWORD_FIELD = "//*[@id='txt-password']"
    LOGIN_BTN = "//*[@id='btn-login']"
    MAKE_APPT_BTN = "//*[@id='btn-make-appointment']"
    PROFILE_DETAILS= "//*[@id='profile']//h2[text()='Profile']"
    LOGIN_ERR_MSG = "//*[contains(text(), 'Login failed! Please ensure the username and password are valid')]"
    FACILITY_DROPDOWN = "//*[@id='combo_facility']"
    HOSPITAL_READMISSION_CHKBOX = "//*[@id='chk_hospotal_readmission']"
    HEALTHCARE_PROGRAM_RADIO = "//*[@id='radio_program_{}']"
    VISIT_DATE_FIELD = "//*[@id='txt_visit_date']"
    COMMENTS_FIELD = "//*[@id='txt_comment']"
    BOOK_APPT_BTN = "//*[@id='btn-book-appointment']"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self, username, password):
        self.click_on_element(self.MENU_TOGGLE)
        self.click_on_element(self.LOGIN_LINK)
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click_on_element(self.LOGIN_BTN)

    def logout(self):
        self.click_on_element(self.MENU_TOGGLE)
        self.click_on_element(self.LOGOUT_LINK)

    def check_if_successfully_logged_in(self):
        self.click_on_element(self.MENU_TOGGLE)
        self.click_on_element(self.PROFILE_LINK)
        try:
            self.wait_until_element_is_visible(self.PROFILE_DETAILS)
            return True
        except Exception:
            return False

    def check_if_login_error_msg_displayed(self):
        try:
            error_msg = self.wait_until_element_is_visible(self.LOGIN_ERR_MSG)
            if 'text-danger' in error_msg.get_attribute('class'):
                return True
            else:
                return False
        except Exception:
            return False

    def make_appointments(self, username, password, facility, hospital_readmission, healthcare_program, visit_date, comments=None):
        self.login(username, password)
        self.click_on_element(self.MAKE_APPT_BTN)
        self.select_dropdown(self.FACILITY_DROPDOWN, facility)
        checkbox = self.wait_until_element_is_visible(self.HOSPITAL_READMISSION_CHKBOX)
        if hospital_readmission == True and checkbox.is_selected() == False:
            self.click_on_element(self.HOSPITAL_READMISSION_CHKBOX)
        self.click_on_element(self.HEALTHCARE_PROGRAM_RADIO.format(str(healthcare_program).lower()))
        self.send_keys(self.VISIT_DATE_FIELD, visit_date)
        if not comments is None:
            self.send_keys(self.COMMENTS_FIELD, comments)
        self.click_on_element(self.BOOK_APPT_BTN)

    def open_appointment_history(self):
        self.click_on_element(self.MENU_TOGGLE)
        self.click_on_element(self.HISTORY_LINK)











