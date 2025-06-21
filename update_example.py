#!/usr/bin/env python3
"""
Exemplo de uso do Sistema de Atualizações do DMS
Este script demonstra como usar as funcionalidades de atualização
"""

import sys
import os
import yaml
from datetime import datetime

# Adiciona o diretório atual ao path para importar as classes
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import UpdateChecker

def load_update_config():
    """Carrega as configurações de atualização"""
    try:
        with open('update_config.yaml', 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print("Arquivo update_config.yaml não encontrado!")
        return None
    except Exception as e:
        print(f"Erro ao carregar configurações: {str(e)}")
        return None

def demo_check_updates():
    """Demonstra a verificação de atualizações"""
    print("=== Demonstração: Verificação de Atualizações ===")
    
    config = load_update_config()
    if not config:
        return
    
    # Cria uma instância do UpdateChecker com configurações personalizadas
    checker = UpdateChecker()
    checker.github_repo = config['update_settings']['github_repo']
    checker.current_version = config['update_settings']['current_version']
    
    print(f"Repositório: {checker.github_repo}")
    print(f"Versão Atual: {checker.current_version}")
    print("Verificando atualizações...")
    
    # Verifica atualizações
    update_info = checker.check_for_updates()
    
    if update_info.get('available'):
        print("\n✅ Nova atualização disponível!")
        print(f"Versão Atual: {update_info['current_version']}")
        print(f"Nova Versão: {update_info['latest_version']}")
        print(f"Data: {update_info['release_date']}")
        print(f"\nNotas de Lançamento:")
        print(update_info['release_notes'][:200] + "..." if len(update_info['release_notes']) > 200 else update_info['release_notes'])
        
        # Simula download
        response = input("\nDeseja baixar a atualização? (s/n): ")
        if response.lower() == 's':
            checker.download_update(update_info['download_url'])
    else:
        if update_info.get('error'):
            print(f"\n❌ Erro: {update_info['error']}")
        else:
            print("\n✅ Você está usando a versão mais recente!")

def demo_changelog():
    """Demonstra o sistema de changelog"""
    print("\n=== Demonstração: Changelog ===")
    
    config = load_update_config()
    if not config:
        return
    
    checker = UpdateChecker()
    checker.github_repo = config['update_settings']['github_repo']
    
    print("Carregando changelog...")
    changelog = checker.get_changelog(limit=3)  # Mostra apenas 3 versões para o exemplo
    
    if changelog:
        print(f"\n📋 Changelog ({len(changelog)} versões):")
        for i, release in enumerate(changelog, 1):
            print(f"\n{i}. Versão {release['version']}")
            print(f"   Título: {release['title']}")
            print(f"   Data: {release['date']}")
            print(f"   URL: {release['url']}")
            
            # Mostra preview das notas
            notes = release['notes']
            if len(notes) > 100:
                notes = notes[:100] + "..."
            print(f"   Notas: {notes}")
            print("   " + "-" * 50)
    else:
        print("❌ Não foi possível carregar o changelog")

def demo_version_comparison():
    """Demonstra a comparação de versões"""
    print("\n=== Demonstração: Comparação de Versões ===")
    
    checker = UpdateChecker()
    
    # Testa diferentes cenários de comparação
    test_cases = [
        ("2.0", "2.1"),
        ("2.1", "2.0"),
        ("2.0", "2.0"),
        ("1.9", "2.0"),
        ("2.0.1", "2.0.2"),
        ("2.0.0", "2.0")
    ]
    
    for v1, v2 in test_cases:
        result = checker._compare_versions(v1, v2)
        if result > 0:
            status = f"{v1} > {v2}"
        elif result < 0:
            status = f"{v1} < {v2}"
        else:
            status = f"{v1} = {v2}"
        
        print(f"Comparando {v1} com {v2}: {status}")

def demo_configuration():
    """Demonstra as configurações do sistema"""
    print("\n=== Demonstração: Configurações ===")
    
    config = load_update_config()
    if not config:
        return
    
    settings = config['update_settings']
    
    print("Configurações atuais:")
    print(f"  Repositório: {settings['github_repo']}")
    print(f"  Versão: {settings['current_version']}")
    print(f"  Verificação Automática: {'Sim' if settings['auto_check'] else 'Não'}")
    print(f"  Intervalo de Verificação: {settings['check_interval']} segundos")
    print(f"  Pasta de Download: {settings['download_path']}")
    print(f"  Backup Antes de Atualizar: {'Sim' if settings['backup_before_update'] else 'Não'}")
    print(f"  Mostrar Notificações: {'Sim' if settings['show_notifications'] else 'Não'}")
    print(f"  Notificar na Inicialização: {'Sim' if settings['notify_on_startup'] else 'Não'}")
    print(f"  Limite do Changelog: {settings['changelog_limit']} versões")
    print(f"  Mostrar Preview: {'Sim' if settings['show_preview'] else 'Não'}")
    print(f"  Usar Proxy para Downloads: {'Sim' if settings['use_proxy_for_downloads'] else 'Não'}")
    print(f"  Timeout de Download: {settings['download_timeout']} segundos")

def main():
    """Função principal do exemplo"""
    print("🚀 Sistema de Atualizações - DMS (Discord Management Suite)")
    print("=" * 60)
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    
    # Executa as demonstrações
    demo_configuration()
    demo_version_comparison()
    demo_check_updates()
    demo_changelog()
    
    print("\n" + "=" * 60)
    print("✅ Demonstração concluída!")
    print("\nPara usar o sistema completo:")
    print("1. Configure seu repositório no update_config.yaml")
    print("2. Execute o programa principal: python main.py")
    print("3. Use as opções 15 e 16 no menu principal")

if __name__ == "__main__":
    main() 