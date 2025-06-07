import os
import json
import base64
import msvcrt
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class AuthManager:
    def __init__(self):
        self.auth_file = 'auth.json'
        self.key_file = '.key'
        self.salt = b'DiscordMultiTool'  # Salt fixo para este projeto
        
    def _get_password(self, prompt="Digite a senha: "):
        print(prompt, end='', flush=True)
        password = []
        while True:
            char = msvcrt.getch()
            if char == b'\r':  # Enter
                print()
                break
            elif char == b'\x08':  # Backspace
                if password:
                    password.pop()
                    print('\b \b', end='', flush=True)
            else:
                try:
                    char_str = char.decode('utf-8')
                    password.append(char_str)
                    print('*', end='', flush=True)
                except UnicodeDecodeError:
                    continue
        return ''.join(password)
        
    def _generate_key(self, password):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
        
    def _get_encryption_key(self):
        if not os.path.exists(self.key_file):
            password = self._get_password("Digite uma senha para criptografar o token: ")
            key = self._generate_key(password)
            with open(self.key_file, 'wb') as f:
                f.write(key)
            return key
        else:
            password = self._get_password("Digite a senha para descriptografar o token: ")
            return self._generate_key(password)
            
    def save_token(self, token):
        try:
            key = self._get_encryption_key()
            f = Fernet(key)
            encrypted_token = f.encrypt(token.encode())
            
            auth_data = {
                'token': encrypted_token.decode()
            }
            
            with open(self.auth_file, 'w') as f:
                json.dump(auth_data, f)
                
            return True
        except Exception as e:
            print(f"Erro ao salvar token: {str(e)}")
            return False
            
    def load_token(self):
        try:
            if not os.path.exists(self.auth_file):
                return None
                
            key = self._get_encryption_key()
            f = Fernet(key)
            
            with open(self.auth_file, 'r') as file:
                auth_data = json.load(file)
                
            encrypted_token = auth_data['token'].encode()
            token = f.decrypt(encrypted_token).decode()
            
            return token
        except Exception as e:
            print(f"Erro ao carregar token: {str(e)}")
            return None
            
    def clear_token(self):
        try:
            if os.path.exists(self.auth_file):
                os.remove(self.auth_file)
            if os.path.exists(self.key_file):
                os.remove(self.key_file)
            return True
        except Exception as e:
            print(f"Erro ao limpar token: {str(e)}")
            return False 