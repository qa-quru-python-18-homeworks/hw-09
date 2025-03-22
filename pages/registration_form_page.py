from datetime import datetime

from selene import have, be, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from models.student import StudentSubmittedView


class RegistrationFormPage:
    def fill_form(self, student):
        self.__open_page() \
            .__set_first_name(student.first_name) \
            .__set_last_name(student.last_name) \
            .__set_email(student.email) \
            .__select_gender(student.gender) \
            .__set_mobile_number(student.mobile_number) \
            .__set_birth_date(student.birth_date) \
            .__add_subjects(student.subjects) \
            .__select_hobbies(student.hobbies) \
            .__upload_picture(student.picture) \
            .__set_current_address(student.address) \
            .__set_state(student.state) \
            .__set_city(student.city) \
            .__submit()
        return self

    def __open_page(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def __set_first_name(self, value):
        s('#firstName').type(value)
        return self

    def __set_last_name(self, value):
        s('#lastName').type(value)
        return self

    def __set_email(self, value):
        s('#userEmail').type(value)
        return self

    def __select_gender(self, gender):
        gender_map = {
            'Male': 'label[for="gender-radio-1"]',
            'Female': 'label[for="gender-radio-2"]',
            'Other': 'label[for="gender-radio-3"]'
        }
        s(gender_map[gender]).click()
        return self

    def __set_mobile_number(self, value):
        s('#userNumber').type(value)
        return self

    def __set_birth_date(self, birth_date):
        date_obj = datetime.strptime(birth_date, "%d %B %Y")
        day, month, year = date_obj.day, date_obj.month - 1, date_obj.year

        s('#dateOfBirthInput').click()
        s('.react-datepicker__month-select').element(f'option[value="{month}"]').click()
        s('.react-datepicker__year-select').element(f'option[value="{year}"]').click()
        day_str = f'{day:02d}'
        s(f'.react-datepicker__day--0{day_str}:not(.react-datepicker__day--outside-month)').click()
        return self

    def __add_subjects(self, subjects):
        for subject in subjects:
            s('#subjectsInput').type(subject).press_enter()
        return self

    def __select_hobbies(self, hobbies):
        hobby_map = {
            'Sports': 'label[for="hobbies-checkbox-1"]',
            'Reading': 'label[for="hobbies-checkbox-2"]',
            'Music': 'label[for="hobbies-checkbox-3"]'
        }
        for hobby in hobbies:
            s(hobby_map[hobby]).click()
        return self

    def __upload_picture(self, file_path):
        s('#uploadPicture').send_keys(file_path)
        return self

    def __set_current_address(self, value):
        s('#currentAddress').type(value)
        return self

    def __set_state(self, state_name):
        s('#state').click()
        s('#react-select-3-input').type(state_name).press_enter()
        return self

    def __set_city(self, city_name):
        s('#city').click()
        s('#react-select-4-input').type(city_name).press_enter()
        return self

    def __submit(self):
        s('#submit').click()
        return self

    def __close_modal(self):
        s('#closeLargeModal').perform(command.js.click)
        return self

    def should_have_submitted(self, student):
        student_submitted_view = StudentSubmittedView(student)

        s('.modal-content').should(be.visible)
        s('table tbody tr:nth-of-type(1) td:nth-of-type(2)').should(have.text(student_submitted_view.name))
        s('table tbody tr:nth-of-type(2) td:nth-of-type(2)').should(have.text(student_submitted_view.email))
        s('table tbody tr:nth-of-type(3) td:nth-of-type(2)').should(have.text(student_submitted_view.gender))
        s('table tbody tr:nth-of-type(4) td:nth-of-type(2)').should(have.text(student_submitted_view.mobile_number))
        s('table tbody tr:nth-of-type(5) td:nth-of-type(2)').should(have.text(student_submitted_view.birth_date))
        s('table tbody tr:nth-of-type(6) td:nth-of-type(2)').should(have.text(student_submitted_view.subjects))
        s('table tbody tr:nth-of-type(7) td:nth-of-type(2)').should(have.text(student_submitted_view.hobbies))
        s('table tbody tr:nth-of-type(8) td:nth-of-type(2)').should(have.text(student_submitted_view.picture))
        s('table tbody tr:nth-of-type(9) td:nth-of-type(2)').should(have.text(student_submitted_view.address))
        s('table tbody tr:nth-of-type(10) td:nth-of-type(2)').should(have.text(student_submitted_view.state_and_city))
        self.__close_modal()
