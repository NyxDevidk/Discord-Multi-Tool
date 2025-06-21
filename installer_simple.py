#!/usr/bin/env python3
"""
Instalador Simplificado do DMS (Discord Management Suite)
Versão 2.0 - Instalador Automático (Sem Atalhos)
"""

import os
import sys
import json
import shutil
import zipfile
import requests
import subprocess
import platform
from pathlib import Path
from datetime import datetime
import urllib.request
from colorama import Fore, init, Style

# Inicializa o colorama
init()

class DMSSimpleInstaller:
    def __init__(self):
        self.app_name = "DMS (Discord Management Suite)"
        self.version = "2.0"
        self.github_repo = "NyxDevidk/Discord-Multi-Tool"
        self.install_dir = None
        self.auto_update = True
        
    def print_banner(self):
        """Exibe o banner do instalador"""
        banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                DMS SIMPLE INSTALLER v{self.version}                ║
║                                                                      ║
║  ██████╗ ███╗   ███╗███████╗    ███████╗██╗   ██╗██╗   ██╗████████╗ ║
║  ██╔══██╗████╗ ████║██╔════╝    ██╔════╝██║   ██║██║   ██║╚══██╔══╝ ║
║  ██║  ██║██╔████╔██║███████╗    ███████╗██║   ██║██║   ██║   ██║    ║
║  ██║  ██║██║╚██╔╝██║╚════██║    ╚════██║██║   ██║██║   ██║   ██║    ║
║  ██████╔╝██║ ╚═╝ ██║███████║    ███████║╚██████╔╝╚██████╔╝   ██║    ║
║  ╚═════╝ ╚═╝     ╚═╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝    ╚═╝    ║
║                                                                      ║
║                    Discord Management Suite                          ║
║                    Desenvolvido por: NYX DEV                        ║
╚══════════════════════════════════════════════════════════════════════╝{Fore.RESET}
"""
        print(banner)
        
    def print_step(self, step, message):
        """Exibe uma etapa do processo de instalação"""
        print(f"\n{Fore.YELLOW}[{step}] {message}{Fore.RESET}")
        
    def print_success(self, message):
        """Exibe uma mensagem de sucesso"""
        print(f"{Fore.GREEN}[✓] {message}{Fore.RESET}")
        
    def print_error(self, message):
        """Exibe uma mensagem de erro"""
        print(f"{Fore.RED}[✗] {message}{Fore.RESET}")
        
    def print_info(self, message):
        """Exibe uma mensagem informativa"""
        print(f"{Fore.CYAN}[ℹ] {message}{Fore.RESET}")
        
    def check_python_version(self):
        """Verifica se a versão do Python é compatível"""
        self.print_step("1", "Verificando versão do Python...")
        
        version = sys.version_info
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            self.print_error(f"Python 3.8+ é necessário. Versão atual: {version.major}.{version.minor}")
            return False
            
        self.print_success(f"Python {version.major}.{version.minor}.{version.micro} detectado")
        return True
        
    def check_internet_connection(self):
        """Verifica a conexão com a internet"""
        self.print_step("2", "Verificando conexão com a internet...")
        
        try:
            response = requests.get("https://api.github.com", timeout=5)
            if response.status_code == 200:
                self.print_success("Conexão com a internet estabelecida")
                return True
        except:
            pass
            
        self.print_error("Sem conexão com a internet")
        return False
        
    def get_install_directory(self):
        """Obtém o diretório de instalação"""
        self.print_step("3", "Configurando diretório de instalação...")
        
        if platform.system() == "Windows":
            default_dir = os.path.join(os.environ.get('PROGRAMFILES', 'C:\\Program Files'), 'DMS')
        else:
            default_dir = os.path.expanduser("~/DMS")
            
        print(f"\n{Fore.CYAN}Diretório padrão: {default_dir}{Fore.RESET}")
        custom_dir = input(f"{Fore.YELLOW}Deseja usar um diretório personalizado? (s/n): {Fore.RESET}")
        
        if custom_dir.lower() == 's':
            custom_path = input(f"{Fore.YELLOW}Digite o caminho: {Fore.RESET}")
            self.install_dir = os.path.abspath(custom_path)
        else:
            self.install_dir = default_dir
            
        # Cria o diretório se não existir
        try:
            os.makedirs(self.install_dir, exist_ok=True)
            self.print_success(f"Diretório configurado: {self.install_dir}")
            return True
        except Exception as e:
            self.print_error(f"Erro ao criar diretório: {str(e)}")
            return False
            
    def download_dependencies(self):
        """Baixa e instala as dependências"""
        self.print_step("4", "Baixando e instalando dependências...")
        
        dependencies = [
            "requests",
            "colorama", 
            "python-dotenv",
            "cryptography",
            "tqdm",
            "pyyaml",
            "aiohttp",
            "beautifulsoup4"
        ]
        
        for dep in dependencies:
            try:
                self.print_info(f"Instalando {dep}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", dep], 
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.print_success(f"{dep} instalado com sucesso")
            except subprocess.CalledProcessError:
                self.print_error(f"Erro ao instalar {dep}")
                return False
                
        return True
        
    def download_program(self):
        """Baixa o programa do GitHub"""
        self.print_step("5", "Baixando programa do GitHub...")
        
        try:
            # URL do arquivo ZIP do repositório
            zip_url = f"https://github.com/{self.github_repo}/archive/refs/heads/main.zip"
            
            self.print_info("Baixando arquivos...")
            response = requests.get(zip_url, stream=True)
            response.raise_for_status()
            
            # Salva o arquivo ZIP
            zip_path = os.path.join(self.install_dir, "dms_temp.zip")
            with open(zip_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    
            # Extrai o arquivo ZIP
            self.print_info("Extraindo arquivos...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.install_dir)
                
            # Remove o arquivo ZIP temporário
            os.remove(zip_path)
            
            # Move os arquivos para o diretório correto
            extracted_dir = os.path.join(self.install_dir, f"Discord-Multi-Tool-main")
            if os.path.exists(extracted_dir):
                # Move todos os arquivos para o diretório principal
                for item in os.listdir(extracted_dir):
                    src = os.path.join(extracted_dir, item)
                    dst = os.path.join(self.install_dir, item)
                    if os.path.isdir(src):
                        shutil.move(src, dst)
                    else:
                        shutil.move(src, dst)
                        
                # Remove o diretório vazio
                shutil.rmtree(extracted_dir)
                
            self.print_success("Programa baixado e extraído com sucesso")
            return True
            
        except Exception as e:
            self.print_error(f"Erro ao baixar programa: {str(e)}")
            return False
            
    def create_config_file(self):
        """Cria arquivo de configuração inicial"""
        self.print_step("6", "Criando configurações iniciais...")
        
        try:
            config = {
                "install_info": {
                    "version": self.version,
                    "install_date": datetime.now().isoformat(),
                    "install_dir": self.install_dir
                },
                "settings": {
                    "auto_update": self.auto_update,
                    "installer_type": "simple"
                }
            }
            
            config_path = os.path.join(self.install_dir, "install_config.json")
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=4)
                
            self.print_success("Configurações criadas com sucesso")
            return True
            
        except Exception as e:
            self.print_error(f"Erro ao criar configurações: {str(e)}")
            return False
            
    def run_post_install_tests(self):
        """Executa testes pós-instalação"""
        self.print_step("7", "Executando testes pós-instalação...")
        
        try:
            # Testa se o programa principal pode ser importado
            main_path = os.path.join(self.install_dir, "main.py")
            if os.path.exists(main_path):
                self.print_success("Arquivo principal encontrado")
            else:
                self.print_error("Arquivo principal não encontrado")
                return False
                
            # Testa se as dependências estão funcionando
            try:
                import requests
                import colorama
                import yaml
                self.print_success("Dependências funcionando corretamente")
            except ImportError as e:
                self.print_error(f"Dependência não encontrada: {str(e)}")
                return False
                
            return True
            
        except Exception as e:
            self.print_error(f"Erro nos testes: {str(e)}")
            return False
            
    def show_installation_summary(self):
        """Mostra um resumo da instalação"""
        print(f"\n{Fore.GREEN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                    INSTALAÇÃO CONCLUÍDA!                    ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        print(f"\n{Fore.CYAN}Resumo da Instalação:{Fore.RESET}")
        print(f"  • Programa: {self.app_name}")
        print(f"  • Versão: {self.version}")
        print(f"  • Diretório: {self.install_dir}")
        print(f"  • Tipo de instalador: Simplificado (sem atalhos)")
        print(f"  • Atualizações automáticas: {'Sim' if self.auto_update else 'Não'}")
        
        print(f"\n{Fore.YELLOW}Próximos Passos:{Fore.RESET}")
        print(f"  1. Execute o programa: python {os.path.join(self.install_dir, 'main.py')}")
        print(f"  2. Configure seu token do Discord")
        print(f"  3. Explore as funcionalidades disponíveis")
        
        print(f"\n{Fore.CYAN}Comandos Úteis:{Fore.RESET}")
        print(f"  • Executar: python {os.path.join(self.install_dir, 'main.py')}")
        print(f"  • Desinstalar: python {os.path.join(self.install_dir, 'uninstaller.py')}")
        
        print(f"\n{Fore.MAGENTA}Nota:{Fore.RESET}")
        print(f"  • Este instalador não criou atalhos automaticamente")
        print(f"  • Para criar atalhos manualmente, use o instalador completo")
        
    def install(self):
        """Executa o processo completo de instalação"""
        self.print_banner()
        
        print(f"{Fore.CYAN}Bem-vindo ao instalador simplificado do {self.app_name}!{Fore.RESET}")
        print(f"{Fore.YELLOW}Este instalador irá configurar o programa em seu sistema.{Fore.RESET}")
        print(f"{Fore.MAGENTA}Versão simplificada - sem criação automática de atalhos{Fore.RESET}")
        
        # Confirmação do usuário
        confirm = input(f"\n{Fore.YELLOW}Deseja continuar com a instalação? (s/n): {Fore.RESET}")
        if confirm.lower() != 's':
            print(f"{Fore.CYAN}Instalação cancelada.{Fore.RESET}")
            return False
            
        # Executa as etapas de instalação
        steps = [
            self.check_python_version,
            self.check_internet_connection,
            self.get_install_directory,
            self.download_dependencies,
            self.download_program,
            self.create_config_file,
            self.run_post_install_tests
        ]
        
        for step in steps:
            if not step():
                self.print_error("Instalação falhou!")
                return False
                
        self.show_installation_summary()
        return True

def main():
    """Função principal"""
    try:
        installer = DMSSimpleInstaller()
        success = installer.install()
        
        if success:
            print(f"\n{Fore.GREEN}🎉 Instalação concluída com sucesso!{Fore.RESET}")
        else:
            print(f"\n{Fore.RED}❌ Instalação falhou!{Fore.RESET}")
            
        input(f"\n{Fore.YELLOW}Pressione ENTER para sair...{Fore.RESET}")
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Instalação cancelada pelo usuário.{Fore.RESET}")
    except Exception as e:
        print(f"\n{Fore.RED}Erro inesperado: {str(e)}{Fore.RESET}")

if __name__ == "__main__":
    main() 