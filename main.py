from selenium import webdriver

def main():
	browser = webdriver.Firefox()
	browser.get('https://www2.darkino.io')

if (__name__ == "__main__"):
	main()