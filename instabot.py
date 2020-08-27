from selenium import webdriver
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from time import sleep, time
from getpass import getpass
username = input('Username: ')
password = getpass('Password: ')

class InstaBot:
    def __init__(self, username, password):

        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/accounts/login/?next=%2F' + username + '%2F&source=desktop_nav')
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element_by_xpath('//button[@type=\"submit\"]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//button[contains(text(), \"Not Now\")]').click()
        self.driver.implicitly_wait(5)

        followers = set(self.get_names(1))
        followings = set(self.get_names(2))
    
        self.driver.quit()
        
        khadoos_peeps = list(set(followings) - set(followers))
        print(str(len(khadoos_peeps)) + ' khadoos people found')
        if len(khadoos_peeps) >= 1:
            for peep in khadoos_peeps:
                print(peep)
        else:
            print('Be Happy!')

    def get_names(self, number):
        self.links = self.driver.find_elements_by_class_name('-nal3')[number].click()
        self.driver.implicitly_wait(2)
        scroll_box = self.driver.find_element_by_class_name('isgrP')
        last_ht, ht = 0, 1
        while ht != last_ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        list_of_elements = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in list_of_elements if name.text != '']
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()

        return names

    


InstaBot(username, password)