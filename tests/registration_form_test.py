from pages.registration_form_page import RegistrationFormPage


def test_registration_form(student):
    form_page = RegistrationFormPage()

    form_page.fill_form(student).should_have_submitted(student)
