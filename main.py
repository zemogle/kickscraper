import requests
import bs4 as BeautifulSoup
import settings

def main(project_id, project_name):
    url = "https://www.kickstarter.com/projects/%s/%s".format(project_id, project_name)
    return

if __name__ == '__main__':
    main(settings.PROJECT_ID, settings.PROJECT_NAME)
