from page.main_page import MainPage


class TestAccount:
    def setup_class(self):
        self.main_page = MainPage()

    def test_login_by_password(self):
        self.main_page.profile_page().login_by_password('15600534760', '12345678') == "xxx"

    def test_login_by_password_fail(self):
        assert self.main_page \
            .profile_page() \
            .login_by_password_fail('15600534760', '12345678') == '失败'

    def test_login_by_code_fail(self):
        assert self.main_page \
            .profile_page() \
            .login_by_verify_code_fail('15600534760', '1234') == '验证码已过期'
