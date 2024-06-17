from pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()

    (
        registration_page.fill_first_name("Test")
        .fill_second_name("Testov")
        .fill_email("test@test.com")
        .select_gender("test")
        .fill_phone_number("1234567890")
        .fill_date_of_birth("July", "1988", "02")
        .fill_subjects("Computer Science")
        .fill_hobbies("Sing")
        .upload_picture("orig.jpg")
        .fill_current_address("test test")
        .fill_state("test")
        .fill_city("test")
        .submit_form()
    )

    registration_page.should_registered_user_info_with(
        "Test Testov",
        "test@test.com",
        "test",
        "1234567890",
        "02 July,1988",
        "test test",
        "Sing",
        "orig.jpg",
        "test test",
        "test test",
    )