import requests
import hashlib
import json

class BreachChecker:
    def __init__(self):
        self.haveibeenpwned_api = "https://haveibeenpwned.com/api/v3/breachedaccount/"
        self.headers = {
            'hibp-api-key': 'VOTRE_API_KEY',
            'user-agent': 'Mozilla/5.0'
        }
    
    def check(self, email):
        breaches = []
        
        # HaveIBeenPwned
        try:
            response = requests.get(
                f"{self.haveibeenpwned_api}{email}",
                headers=self.headers
            )
            if response.status_code == 200:
                breaches.extend(response.json())
        except:
            pass
        
        # DeHashed API
        try:
            # Implementation similaire avec DeHashed
            pass
        except:
            pass
        
        return breaches
    
    def check_password(self, password):
        # K-anonymity HaveIBeenPwned
        sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix = sha1[:5]
        suffix = sha1[5:]
        
        try:
            response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
            for line in response.text.splitlines():
                if line.startswith(suffix):
                    return int(line.split(':')[1])
        except:
            pass
        return 0
