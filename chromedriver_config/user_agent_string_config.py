import random

user_agent_options = {
    "platforms": [
        "Windows NT 10.0; Win64; x64",
        "Windows NT 6.1; Win64; x64",
        "Macintosh; Intel Mac OS X 10_15_7",
        "Macintosh; Intel Mac OS X 11_2_3",
        "X11; Linux x86_64",
        "X11; Linux i686",
        "Windows NT 6.3; Win64; x64",
        "Windows NT 6.2; Win64; x64",
        "Macintosh; Intel Mac OS X 10_14_6"
    ],
    "webkit_versions": [
        "537.36", 
        "537.35", 
        "537.34",
        "537.31",
        "537.32",
        "537.33",
        "534.57.2",
        "534.30",
        "537.22"
    ],
    "browsers": [
        "Chrome/91.0.4472.124",
        "Chrome/92.0.4515.107",
        "Chrome/90.0.4430.85",
        "Chrome/89.0.4389.90",
        "Firefox/89.0",
        "Firefox/88.0",
        "Firefox/87.0",
        "Edge/90.0.818.62",
        "Edge/91.0.864.41",
        "Opera/77.0.4054.60"
    ],
    "safari_versions": [
        "Safari/537.36",
        "Safari/537.35",
        "Safari/537.34",
        "Safari/534.57.2",
        "Safari/534.30",
        "Safari/537.31",
        "Safari/537.22"
    ]
}


def generate_user_agent_string():
    platform = random.choice(user_agent_options["platforms"])
    webkit_version = random.choice(user_agent_options["webkit_versions"])
    browser = random.choice(user_agent_options["browsers"])
    safari_version = random.choice(user_agent_options["safari_versions"])
    
    user_agent_string = f"user-agent=Mozilla/5.0 ({platform}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {browser} {safari_version}"
    return user_agent_string