import os
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def scroll(browser, element):
	position = element.location['y']
	browser.execute_script(f'window.scrollBy(0, {position - 120});')
	sleep(1)

def print_menu(list):
	clear()
	menu = {}
	for i in range(0, len(list)):
		menu.update({i + 1: list[i]})
	for key in menu.keys():
		print(f'{key} -- {menu[key]}')
	try: 
		choosen_option = int(input(' >>> '))
	except:
		raise Exception('Option not valid.')
	if (choosen_option <= 0 or choosen_option > len(list)):
		raise Exception('Option not valid.')
	return (choosen_option)

def filter_qualities(browser):
	i = 1
	browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div').click()
	qualities = []
	base_id = 'choices--tableFiltersqualitevalues-item-choice-'
	full_id = base_id + str(i)
	try:
		while (quality := browser.find_element(By.ID, full_id)):
			i += 1
			qualities.append(quality.get_attribute('innerHTML'))
			full_id = base_id + str(i)
	except:
		pass
	choice = print_menu(qualities)
	browser.find_element(By.ID, f'{base_id}{choice}').click()

def filter_languages(browser):
	i = 1
	browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div/div').click()
	languages = []
	base_id = "choices--tableFilterslanguevalues-item-choice-"
	full_id = base_id + str(i)
	try:
		while (language := browser.find_element(By.ID, full_id)):
			i += 1
			languages.append(language.get_attribute('innerHTML'))
			full_id = base_id + str(i)
	except:
		pass
	choice = print_menu(languages)
	browser.find_element(By.ID, f'{base_id}{choice}').click()

def get_movies(browser):
	clear()
	i = 1
	sizes = []
	links = []
	try:
		while (True):
			size = browser.find_element(By.XPATH, f'/html/body/div[3]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div/div/div/div[3]/table/tbody/tr[{i}]/td[4]/div/div/div/div/span').get_attribute('innerHTML').strip()
			href = browser.find_element(By.XPATH, f'/html/body/div[3]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div/div/div/div[3]/table/tbody/tr[{i}]/td[2]/div/a').get_attribute('href')
			sizes.append(size)
			links.append(href)
			i += 1
	except:
		pass
	choice = print_menu(sizes)
	browser.get(links[choice - 1])

def main():
	clear()
	browser = webdriver.Firefox()
	link = input('Please enter a link: ')
	try:
		browser.get(link)
		sleep(2)
		filter_button = browser.find_element(By.XPATH , '/html/body/div[3]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div[1]/button')
		scroll(browser, filter_button)
		filter_button.click()
		filter_qualities(browser)
		filter_languages(browser)
		sleep(3)
		get_movies(browser)
	except Exception as e:
		print("Error:")
		print(e)
	browser.close()

if (__name__ == "__main__"):
	main()