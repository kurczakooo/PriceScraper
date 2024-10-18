from .user_agent_string_config import generate_user_agent_string
from selenium.webdriver.chrome.options import Options

user_agent_string = generate_user_agent_string()
user_agent_string_override_command = user_agent_string.split('=')[1]

chrome_options = Options()
# Headless mode
chrome_options.add_argument("--headless")
# Disable a feature which may tell the browser that it's being controlled by automation software
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# Disable sandbox for headless mode
chrome_options.add_argument("--no-sandbox")
# Disable gpu acceleration, since we're using headless mode
chrome_options.add_argument("--disable-gpu")
# Disable webgl so it's not trying to access the GPU for rendering
chrome_options.add_argument('--disable-webgl')
# Disable an infobar informing the browser that it's being controlled by automation software
chrome_options.add_argument("--disable-infobars")
# Overcome limited resource problems
chrome_options.add_argument("--disable-dev-shm-usage")
# Set a custom user agent string that mimics a normal desktop user 
# (it's telling the browser the user uses Mozilla on windows 10 with a speciic webKit and KHTML engine, Chrome ver.91, and a ver. of Webkit to render for Safari)
chrome_options.add_argument(user_agent_string)