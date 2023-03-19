from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging


class ClubEtudiantsScraper:
    def __init__(self, url, email, password, executable_path, log_level=logging.INFO):
        self.url = url
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome(executable_path=executable_path)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

    def __enter__(self):
        self.driver.get(self.url)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jconfirm-scrollpane"))
        )
        btn = self.driver.find_element_by_class_name("btn-default").click()
        self.logger.info(self.driver.title)
        self.driver.find_element_by_class_name("ce-login").click()
        self.driver.implicitly_wait(1)
        self.alert = self.driver.switch_to.window("xtf")

        self.logger.info("Logging in...")
        self.alert.find_elements_by_class_name("form-control")[0].send_keys(self.email)
        self.alert.find_elements_by_class_name("form-control")[1].send_keys(
            self.password
        )
        self.alert.find_element_by_class_name("ce-btn-submit").click()
        self.driver.implicitly_wait(3)
        self.driver.switch_to.window("")
        time.sleep(1)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()

    def scrape(self):
        self.logger.info("Starting scrape...")
        p = self.driver.find_elements_by_xpath("//p/a")
        for t in p:
            self.logger.debug(f"Clicking {t.text}")
            t.click()
            self.driver.find_element_by_class_name("down").click()
            self.driver.back()


if __name__ == "__main__":
    url = "https://clubetudiants.ma/post/cours/-EMI-Exemples-des-anciens-concours"
    email = "email_here"
    password = "pasword_here"
    with ClubEtudiantsScraper(url, email, password, log_level=logging.DEBUG) as scraper:
        scraper.scrape()
