from base.basedriver import Basedriver

class Appointmentpage(Basedriver):
    FACILITY_DETAILS = "//*[@id='facility']"
    HOSPITAL_READMISSION_DETAILS = "//*[@id='hospital_readmission']"
    HEALTHCARE_PROGRAM = "//*[@id='program']"
    VISIT_DATE_DETAILS = "//*[@id='visit_date']"
    COMMENTS_DETAILS = "//*[@id='comment']"
    GO_TO_HOMEPAGE_BTN = "//*[text()='Go to Homepage']"

    def __init__(self, driver):
        super().__init__(driver)

    def goto_homepage(self):
        self.click_on_element(self.GO_TO_HOMEPAGE_BTN)

    def confirm_appointment_details(self, facility, hospital_readmission, healthcare_program, visit_date, comment=None):
        facility_details = self.wait_until_element_is_visible(self.FACILITY_DETAILS)
        hospital_readmission_details = self.wait_until_element_is_visible(self.HOSPITAL_READMISSION_DETAILS)
        healthcare_program_details = self.wait_until_element_is_visible(self.HEALTHCARE_PROGRAM)
        visit_date_details = self.wait_until_element_is_visible(self.VISIT_DATE_DETAILS)
        comment_details = self.wait_until_element_is_visible(self.COMMENTS_DETAILS)

        assert facility_details.text == facility
        if hospital_readmission == True:
            assert hospital_readmission_details.text == "Yes"
        else:
            assert hospital_readmission_details.text== "No"
        assert healthcare_program_details.text.lower() == str(healthcare_program).lower()
        assert visit_date_details.text == visit_date
        if not comment is None:
            assert comment_details.text == comment
        self.goto_homepage()


