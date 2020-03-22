
 #!/bin/bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar -xvzf geckodriver-v0.26.0-linux64.tar.gz
chmod +x geckodriver 
export PATH=$PATH:$(pwd):/geckodriver


  File "/home/ffm_pc/miniconda3/envs/acoes/lib/python3.8/site-packages/selenium/webdriver/firefox/webdriver.py", line 170, in __init__
    RemoteWebDriver.__init__(
  File "/home/ffm_pc/miniconda3/envs/acoes/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 157, in __init__
    self.start_session(capabilities, browser_profile)
  File "/home/ffm_pc/miniconda3/envs/acoes/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 252, in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
  File "/home/ffm_pc/miniconda3/envs/acoes/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "/home/ffm_pc/miniconda3/envs/acoes/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: invalid argument: can't kill an exited process