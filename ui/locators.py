from selenium.webdriver.common.by import By


class YandexLocators:
    LOCATOR_ENTER_BUTTON = (By.CLASS_NAME, "headline__personal-enter")
    LOCATOR_INPUT_FIELD_LOGIN = (By.ID, "passp-field-login")
    LOCATOR_INPUT_FIELD_PASSWORD = (By.ID, "passp-field-passwd")
    LOCATOR_SIGN_BUTTON = (By.ID, "passp:sign-in")
    LOCATOR_IMAGE_MENU = (By.CLASS_NAME, "avatar__image-wrapper")
    LOCATOR_DISC = (By.CLASS_NAME, "usermenu-redesign__disk")
    LOCATOR_CREATE = (By.CSS_SELECTOR, ".LeftColumn .Button2_view_raised")
    LOCATOR_CREATE_NEW_FOLDER = (By.CLASS_NAME, "file-icon_dir_plus")
    LOCATOR_NEW_FOLDER_NAME_INPUT = (By.CLASS_NAME, "Textinput-Control")
    LOCATOR_SAVE_BUTTON = (By.CLASS_NAME, "confirmation-dialog__button_submit")
    LOCATOR_ITEMS_LIST = (By.CLASS_NAME, "listing-item__title")
    LOCATOR_COPY_BUTTON = (By.CLASS_NAME, "resources-actions-popup__action_type_copy")
    LOCATOR_FOLDERS = (By.CLASS_NAME, "b-tree__name")
    LOCATOR_ITEMS_FOLDER = (By.CLASS_NAME, "listing__items")
    LOCATOR_USER_IMAGE = (By.CLASS_NAME, "user-pic__image")
    LOCATOR_LOGOUT = (By.CLASS_NAME, "legouser__menu-item_action_exit")
    LOCATOR_LOGOUT_FILE = (By.CLASS_NAME, "user2__menu-item_action_exit")
    LOCATOR_TEXT_LINE = (By.CLASS_NAME, "mg1")
    LOCATOR_UPLOAD_FILE = (By.CLASS_NAME, "upload-button__attach")
