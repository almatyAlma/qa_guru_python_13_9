from pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()

    (
        registration_page.fill_first_name("Alma")
        .fill_second_name("Bekbergenova")
        .fill_email("test@test.com")
        .select_gender("Male")
        .fill_phone_number("1234567890")
        .fill_date_of_birth("July", "1991", "02")
        .fill_subjects("QA")
        .fill_hobbies("Sports")
        .upload_picture("orig.jpg")
        .fill_current_address("Abay")
        .fill_state("Haryana")
        .fill_city("Karnal")
        .submit_form()
    )

    registration_page.should_registered_user_info_with(
        "Alma Bekbergenova",
        "test@test.com",
        "Male",
        "1234567890",
        "02 July,1991",
        "Economics",
        "Sports",
        "orig.jpg",
        "Abay",
        "Haryana Karnal",
    )