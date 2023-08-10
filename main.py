from selenium import webdriver
from selenium.webdriver.common.by import By

def get_qualities(browser):
	i = 1
	qualities = []
	base_id = 'choices--tableFiltersqualitevalues-item-choice-'
	try:
		full_id = base_id + str(i)
		while (quality := browser.find_element(By.ID, full_id)):
			i += 1
			qualities.append((full_id, quality.get_attribute('innerHTML')))
			full_id = base_id + str(i)
	except:
		pass
	return (qualities)

def get_languages(browser):
	i = 1
	languages = []
	base_id = "choices--tableFilterslanguevalues-item-choice-"
	try:
		full_id = base_id + str(i)
		while (language := browser.find_element(By.ID, full_id)):
			i += 1
			languages.append((full_id, language.get_attribute('innerHTML')))
			full_id = base_id + str(i)
	except:
		pass
	return (languages)

def main():
	link = input('Please enter a link: ')
	browser = webdriver.Firefox()
	try:
		browser.get(link)
		qualities = get_qualities(browser)
		languages = get_languages(browser)
		print(qualities)
		print(languages)
	except Exception as e:
		print("Error:")
		print(e)
	browser.close()

if (__name__ == "__main__"):
	main()