#!/usr/bin/env python3
"""
Desinstalador do DMS (Discord Management Suite)
Versão 2.0 - Desinstalador Automático
"""

import os
import sys
import json
import shutil
import platform
from datetime import datetime
from colorama import Fore, init, Style

# Inicializa o colorama
init()

class DMSUninstaller:
    def __init__(self):
        self.app_name = "DMS (Discord Management Suite)"
        self.version = "2.0"
        self.install_dir = None
        self.config_file = None
        
    def print_banner(self):
        """Exibe o banner do desinstalador"""
        banner = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════╗
║                   DMS UNINSTALLER v{self.version}                   ║
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
        """Exibe uma etapa do processo de desinstalação"""
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
        
    def find_installation(self):
        """Encontra a instalação do DMS"""
        self.print_step("1", "Procurando instalação do DMS...")
        
        # Procura em locais comuns
        possible_locations = []
        
        if platform.system() == "Windows":
            possible_locations.extend([
                os.path.join(os.environ.get('PROGRAMFILES', 'C:\\Program Files'), 'DMS'),
                os.path.join(os.environ.get('PROGRAMFILES(X86)', 'C:\\Program Files (x86)'), 'DMS'),
                os.path.expanduser("~/DMS"),
                os.path.expanduser("~/Desktop/DMS"),
                os.path.expanduser("~/Documents/DMS")
            ])
        else:
            possible_locations.extend([
                os.path.expanduser("~/DMS"),
                os.path.expanduser("~/Desktop/DMS"),
                os.path.expanduser("~/Documents/DMS"),
                "/opt/DMS",
                "/usr/local/DMS"
            ])
            
        # Procura pelo arquivo de configuração
        for location in possible_locations:
            config_file = os.path.join(location, "install_config.json")
            if os.path.exists(config_file):
                try:
                    with open(config_file, 'r') as f:
                        config = json.load(f)
                    self.install_dir = location
                    self.config_file = config_file
                    self.print_success(f"Instalação encontrada em: {location}")
                    return True
                except:
                    continue
                    
        # Se não encontrou pelo config, procura pelo main.py
        for location in possible_locations:
            main_file = os.path.join(location, "main.py")
            if os.path.exists(main_file):
                self.install_dir = location
                self.print_success(f"Instalação encontrada em: {location}")
                return True
                
        self.print_error("Nenhuma instalação do DMS foi encontrada")
        return False
        
    def backup_user_data(self):
        """Faz backup dos dados do usuário"""
        self.print_step("2", "Fazendo backup dos dados do usuário...")
        
        try:
            backup_dir = os.path.join(self.install_dir, "backup_" + datetime.now().strftime("%Y%m%d_%H%M%S"))
            os.makedirs(backup_dir, exist_ok=True)
            
            # Lista de arquivos/diretórios para backup
            backup_items = [
                "tokens",
                "logs", 
                "backups",
                "config.yaml",
                "config.json"
            ]
            
            backed_up = []
            for item in backup_items:
                item_path = os.path.join(self.install_dir, item)
                if os.path.exists(item_path):
                    if os.path.isdir(item_path):
                        shutil.copytree(item_path, os.path.join(backup_dir, item))
                    else:
                        shutil.copy2(item_path, backup_dir)
                    backed_up.append(item)
                    
            if backed_up:
                self.print_success(f"Backup criado em: {backup_dir}")
                self.print_info(f"Arquivos salvos: {', '.join(backed_up)}")
            else:
                self.print_info("Nenhum dado do usuário encontrado para backup")
                
            return True
            
        except Exception as e:
            self.print_error(f"Erro ao fazer backup: {str(e)}")
            return False
            
    def remove_shortcuts(self):
        """Remove os atalhos criados"""
        self.print_step("3", "Removendo atalhos...")
        
        try:
            if platform.system() == "Windows":
                self.remove_windows_shortcuts()
            else:
                self.remove_linux_shortcuts()
                
            self.print_success("Atalhos removidos com sucesso")
            return True
            
        except Exception as e:
            self.print_error(f"Erro ao remover atalhos: {str(e)}")
            return False
            
    def remove_windows_shortcuts(self):
        """Remove atalhos no Windows"""
        try:
            import winshell
            
            # Remove atalho da área de trabalho
            desktop = winshell.desktop()
            desktop_shortcut = os.path.join(desktop, "DMS.lnk")
            if os.path.exists(desktop_shortcut):
                os.remove(desktop_shortcut)
                self.print_info("Atalho da área de trabalho removido")
                
            # Remove atalho do menu iniciar
            start_menu = winshell.start_menu()
            start_menu_shortcut = os.path.join(start_menu, "Programs", "DMS")
            if os.path.exists(start_menu_shortcut):
                shutil.rmtree(start_menu_shortcut)
                self.print_info("Atalho do menu iniciar removido")
                
        except ImportError:
            self.print_info("Bibliotecas para atalhos não disponíveis")
        except Exception as e:
            self.print_info(f"Erro ao remover atalhos do Windows: {str(e)}")
            
    def remove_linux_shortcuts(self):
        """Remove atalhos no Linux"""
        try:
            # Remove atalho da área de trabalho
            desktop = os.path.expanduser("~/Desktop")
            desktop_file = os.path.join(desktop, "DMS.desktop")
            if os.path.exists(desktop_file):
                os.remove(desktop_file)
                self.print_info("Atalho da área de trabalho removido")
                
        except Exception as e:
            self.print_info(f"Erro ao remover atalhos do Linux: {str(e)}")
            
    def remove_program_files(self):
        """Remove os arquivos do programa"""
        self.print_step("4", "Removendo arquivos do programa...")
        
        try:
            if os.path.exists(self.install_dir):
                shutil.rmtree(self.install_dir)
                self.print_success("Arquivos do programa removidos com sucesso")
                return True
            else:
                self.print_error("Diretório de instalação não encontrado")
                return False
                
        except Exception as e:
            self.print_error(f"Erro ao remover arquivos: {str(e)}")
            return False
            
    def remove_dependencies(self):
        """Remove as dependências instaladas (opcional)"""
        self.print_step("5", "Removendo dependências...")
        
        remove_deps = input(f"{Fore.YELLOW}Deseja remover as dependências Python? (s/n): {Fore.RESET}")
        
        if remove_deps.lower() == 's':
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
                    self.print_info(f"Removendo {dep}...")
                    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", dep], 
                                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    self.print_success(f"{dep} removido com sucesso")
                except subprocess.CalledProcessError:
                    self.print_info(f"{dep} não estava instalado ou não pôde ser removido")
                    
        else:
            self.print_info("Dependências mantidas no sistema")
            
        return True
        
    def show_uninstallation_summary(self):
        """Mostra um resumo da desinstalação"""
        print(f"\n{Fore.GREEN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                  DESINSTALAÇÃO CONCLUÍDA!                   ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        print(f"\n{Fore.CYAN}Resumo da Desinstalação:{Fore.RESET}")
        print(f"  • Programa: {self.app_name}")
        print(f"  • Versão: {self.version}")
        print(f"  • Diretório removido: {self.install_dir}")
        print(f"  • Atalhos removidos: Sim")
        print(f"  • Backup criado: Sim")
        
        print(f"\n{Fore.YELLOW}Observações:{Fore.RESET}")
        print(f"  • Seus dados foram salvos em backup")
        print(f"  • As dependências Python foram mantidas")
        print(f"  • Para reinstalar, execute: python installer.py")
        
    def uninstall(self):
        """Executa o processo completo de desinstalação"""
        self.print_banner()
        
        print(f"{Fore.RED}⚠️  ATENÇÃO: Esta ação irá remover completamente o {self.app_name}!{Fore.RESET}")
        print(f"{Fore.YELLOW}Certifique-se de que você realmente deseja desinstalar o programa.{Fore.RESET}")
        
        # Confirmação do usuário
        confirm = input(f"\n{Fore.RED}Tem certeza que deseja desinstalar? (digite 'DESINSTALAR' para confirmar): {Fore.RESET}")
        if confirm != "DESINSTALAR":
            print(f"{Fore.CYAN}Desinstalação cancelada.{Fore.RESET}")
            return False
            
        # Executa as etapas de desinstalação
        steps = [
            self.find_installation,
            self.backup_user_data,
            self.remove_shortcuts,
            self.remove_program_files,
            self.remove_dependencies
        ]
        
        for step in steps:
            if not step():
                self.print_error("Desinstalação falhou!")
                return False
                
        self.show_uninstallation_summary()
        return True

def main():
    """Função principal"""
    try:
        uninstaller = DMSUninstaller()
        success = uninstaller.uninstall()
        
        if success:
            print(f"\n{Fore.GREEN}🎉 Desinstalação concluída com sucesso!{Fore.RESET}")
        else:
            print(f"\n{Fore.RED}❌ Desinstalação falhou!{Fore.RESET}")
            
        input(f"\n{Fore.YELLOW}Pressione ENTER para sair...{Fore.RESET}")
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Desinstalação cancelada pelo usuário.{Fore.RESET}")
    except Exception as e:
        print(f"\n{Fore.RED}Erro inesperado: {str(e)}{Fore.RESET}")

if __name__ == "__main__":
    main() 