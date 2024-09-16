import webbrowser as wb

def workauto():
    
    Chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    URLS = ["https://www.youtube.com",
            "https://github.com",
            "https://aws.amazon.com/console/",
            "https://www.jenkins.io/",
            "https://slack.com/",
            "https://app.terraform.io/"]  # Change the URLs according to ur needs 

    for url in URLS:
        # The 'get' method retrieves the browser and 'open' opens the URL
        wb.get(Chrome_path).open(url)

workauto()
