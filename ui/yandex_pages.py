from ui.base_app import BasePage
from ui.locators import YandexLocators
from selenium.webdriver import Keys, ActionChains


class YandexDisc(BasePage):

    def open_enter_page(self):
        return self.find_element(YandexLocators.LOCATOR_ENTER_BUTTON, time=2).click()

    def enter_login(self, login):
        login_field = self.find_element(YandexLocators.LOCATOR_INPUT_FIELD_LOGIN)
        login_field.click()
        login_field.send_keys(login)
        return login_field

    def enter_password(self, password):
        password_field = self.find_element(YandexLocators.LOCATOR_INPUT_FIELD_PASSWORD)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    def click_sign_button(self):
        return self.find_element(YandexLocators.LOCATOR_SIGN_BUTTON, time=2).click()

    def open_disc(self):
        self.find_element(YandexLocators.LOCATOR_IMAGE_MENU, time=2).click()
        return self.find_element(YandexLocators.LOCATOR_DISC, time=2).click()

    def create_new_folder(self, folder_name):
        self.find_element(YandexLocators.LOCATOR_CREATE, time=10).click()
        self.find_element(YandexLocators.LOCATOR_CREATE_NEW_FOLDER, time=10).click()
        new_folder_field = self.find_elements(YandexLocators.LOCATOR_NEW_FOLDER_NAME_INPUT)[1]
        new_folder_field.click()
        new_folder_field.send_keys(Keys.CONTROL + "a")
        new_folder_field.send_keys(Keys.DELETE)
        new_folder_field.send_keys(folder_name)
        return self.find_element(YandexLocators.LOCATOR_SAVE_BUTTON, time=10).click()

    def copy_file(self, file_to_copy, folder_name):
        all_list = self.find_elements(YandexLocators.LOCATOR_ITEMS_LIST, time=10)
        item = [q for q in all_list if q.get_attribute("aria-label") == file_to_copy][0]
        action = ActionChains(self.driver)
        action.pause(5).context_click(item).perform()
        self.find_element(YandexLocators.LOCATOR_COPY_BUTTON).click()
        all_list = self.find_elements(YandexLocators.LOCATOR_FOLDERS, time=2)
        item = [q for q in all_list if q.get_attribute("title") == folder_name][0]
        item.click()
        return self.find_element(YandexLocators.LOCATOR_SAVE_BUTTON, time=2).click()

    def open_folder(self, folder_name):
        ActionChains(self.driver).pause(5).perform()
        all_list = self.find_elements(YandexLocators.LOCATOR_ITEMS_LIST, time=2)
        item = [q for q in all_list if q.get_attribute("aria-label") == folder_name][0]
        action = ActionChains(self.driver)
        action.double_click(item).perform()
        return item

    def get_files_list(self):
        all_list = self.find_elements(YandexLocators.LOCATOR_ITEMS_LIST, time=5)
        return [x.get_attribute("aria-label") for x in all_list]

    def logout(self):
        self.find_element(YandexLocators.LOCATOR_USER_IMAGE, time=2).click()
        return self.find_element(YandexLocators.LOCATOR_LOGOUT, time=2).click()

    def logout_from_file(self):
        self.find_element(YandexLocators.LOCATOR_USER_IMAGE, time=2).click()
        return self.find_element(YandexLocators.LOCATOR_LOGOUT_FILE, time=2).click()

    def upload_file(self, path_to_file):
        upload_file = self.find_element(YandexLocators.LOCATOR_UPLOAD_FILE, time=10)
        upload_file.send_keys(path_to_file)
        ActionChains(self.driver).pause(5).perform()
        return upload_file

    def open_file(self, file_name):
        all_list = self.find_elements(YandexLocators.LOCATOR_ITEMS_LIST, time=2)
        item = [q for q in all_list if q.get_attribute("aria-label") == file_name][0]
        action = ActionChains(self.driver)
        action.double_click(item).perform()
        return item

    def get_text_from_file(self):
        ActionChains(self.driver).pause(5).perform()
        all_list = self.find_elements(YandexLocators.LOCATOR_TEXT_LINE, time=2)
        lines = [line.text for line in all_list]
        return lines
