from . import utils
from time import sleep
import random
import json


def get_user_information(users, driver=None, headless=True):
    """ get user information if the "from_account" argument is specified """

    driver = utils.init_driver(headless=headless)

    users_info = {}
    sleep(10)
    for i, user in enumerate(users):

        log_user_page(user, driver)

        if user is not None:
            try:
                following = driver.find_element_by_xpath(
                    '//a[contains(@href,"/following")]/span[1]/span[1]').text
                followers = driver.find_element_by_xpath(
                    '//a[contains(@href,"/followers")]/span[1]/span[1]').text
            except Exception as e:
                following = ""
                followers = ""
            try:
                website = driver.find_element_by_xpath('//a[contains(@data-testid,"UserUrl")]').text
            except Exception as e:
                website = ""
            try:
                desc = driver.find_element_by_xpath('//div[contains(@data-testid,"UserDescription")]').text
            except Exception as e:
                desc = ""
            try:
                join_date = driver.find_element_by_xpath('//span[contains(@data-testid,"UserJoinDate")]').text
            except Exception as e:
                join_date = ""
            try:
                birthday = driver.find_element_by_xpath('//span[contains(@data-testid,"UserBirthdate")]').text
            except Exception as e:
                birthday = ""            
            try:
                location = driver.find_element_by_xpath('//span[contains(@data-testid,"UserLocation")]').text
            except Exception as e:
                location = ""
            try:
                professional = driver.find_element_by_xpath('//span[contains(@data-testid,"UserProfessionalCategory")]').text
            except Exception as e:
                professional = ""      
            try:
                name = driver.find_element_by_xpath('//h2[contains(@role,"heading")]').text
            except Exception as e:
                name = "" 
            try:
                tweets = driver.find_element_by_xpath('//h2[contains(@role,"heading")]/following-sibling::div').text
            except Exception as e:
                tweets = ""                 
                 
            # try:
            #     join_date = driver.find_element_by_xpath(
            #         '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[3]').text
            #     birthday = driver.find_element_by_xpath(
            #         '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[2]').text
            #     location = driver.find_element_by_xpath(
            #         '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[1]').text
            # except Exception as e:
            #     try:
            #         join_date = driver.find_element_by_xpath(
            #             '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[2]').text
            #         span1 = driver.find_element_by_xpath(
            #             '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[1]').text
            #         if hasNumbers(span1):
            #             birthday = span1
            #             location = ""
            #         else:
            #             location = span1
            #             birthday = ""
            #     except Exception as e:
            #         try:
            #             join_date = driver.find_element_by_xpath(
            #                 '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[1]').text
            #             birthday = ""
            #             location = ""
            #         except Exception as e:
            #             join_date = ""
            #             birthday = ""
            #             location = ""
            users_info[user] = [name,following, followers, tweets ,join_date, birthday, location,professional, website, desc,]

            if i == len(users) - 1:
                driver.close()
                return users_info
        else:
            print("You must specify the user")
            continue


def log_user_page(user, driver, headless=True):
    sleep(random.uniform(1, 2))
    driver.get('https://twitter.com/' + user)
    sleep(random.uniform(1, 2))


def get_users_followers(users, env, verbose=1, headless=True, wait=2, limit=float('inf'), file_path=None):
    followers = utils.get_users_follow(users, headless, env, "followers", verbose, wait=wait, limit=limit)

    if file_path == None:
        file_path = 'outputs/' + str(users[0]) + '_' + str(users[-1]) + '_' + 'followers.json'
    else:
        file_path = file_path + str(users[0]) + '_' + str(users[-1]) + '_' + 'followers.json'
    with open(file_path, 'w') as f:
        json.dump(followers, f)
        print(f"file saved in {file_path}")
    return followers


def get_users_following(users, env, verbose=1, headless=True, wait=2, limit=float('inf'), file_path=None):
    following = utils.get_users_follow(users, headless, env, "following", verbose, wait=wait, limit=limit)

    if file_path == None:
        file_path = 'outputs/' + str(users[0]) + '_' + str(users[-1]) + '_' + 'following.json'
    else:
        file_path = file_path + str(users[0]) + '_' + str(users[-1]) + '_' + 'following.json'
    with open(file_path, 'w') as f:
        json.dump(following, f)
        print(f"file saved in {file_path}")
    return following


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
