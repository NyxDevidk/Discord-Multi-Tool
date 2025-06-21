# 🚀 Instalador do DMS (Discord Management Suite)

## Visão Geral

O DMS agora possui um sistema completo de instalação e desinstalação que facilita a distribuição e configuração do programa em qualquer sistema.

## 📁 Arquivos do Sistema de Instalação

### `installer.py`
- **Instalador principal** do DMS
- Baixa automaticamente o programa do GitHub
- Instala todas as dependências necessárias
- Cria atalhos no sistema
- Configura o ambiente automaticamente

### `uninstaller.py`
- **Desinstalador completo** do DMS
- Remove todos os arquivos do programa
- Remove atalhos criados
- Faz backup dos dados do usuário
- Remove dependências (opcional)

## 🛠️ Como Usar

### Instalação

1. **Baixe o instalador:**
   ```bash
   # Clone o repositório ou baixe o installer.py
   git clone https://github.com/NyxDevidk/Discord-Multi-Tool.git
   cd Discord-Multi-Tool
   ```

2. **Execute o instalador:**
   ```bash
   python installer.py
   ```

3. **Siga as instruções na tela:**
   - Confirme a instalação
   - Escolha o diretório de instalação
   - Aguarde o download e instalação

### Desinstalação

1. **Execute o desinstalador:**
   ```bash
   python uninstaller.py
   ```

2. **Confirme a desinstalação:**
   - Digite 'DESINSTALAR' para confirmar
   - Seus dados serão salvos em backup

## 📋 Requisitos do Sistema

### Mínimos
- **Python 3.8+**
- **Conexão com a internet**
- **Permissões de administrador** (recomendado)

### Recomendados
- **Windows 10/11** ou **Linux**
- **2GB RAM**
- **100MB espaço em disco**

## 🔧 Funcionalidades do Instalador

### ✅ Verificações Automáticas
- Versão do Python
- Conexão com a internet
- Permissões de escrita
- Espaço em disco

### 📦 Instalação Completa
- Download automático do GitHub
- Instalação de dependências
- Configuração do ambiente
- Criação de atalhos

### 🎯 Personalização
- Escolha do diretório de instalação
- Configuração de atalhos
- Opções de atualização automática

### 🔒 Segurança
- Verificação de integridade
- Backup automático de dados
- Logs detalhados

## 🎨 Interface do Instalador

### Banner Personalizado
```
╔══════════════════════════════════════════════════════════════╗
║                    DMS INSTALLER v2.0                    ║
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
╚══════════════════════════════════════════════════════════════════════╝
```

### Etapas Visuais
- **Cores diferentes** para cada tipo de mensagem
- **Progresso detalhado** de cada etapa
- **Confirmações** antes de ações importantes
- **Resumo final** da instalação

## 📂 Estrutura de Instalação

Após a instalação, o programa será organizado assim:

```
C:\Program Files\DMS\          # Windows
~/DMS/                         # Linux/Mac
├── main.py                    # Programa principal
├── auth.py                    # Sistema de autenticação
├── config.yaml               # Configurações
├── requirements.txt          # Dependências
├── installer.py              # Instalador
├── uninstaller.py            # Desinstalador
├── install_config.json       # Configuração da instalação
├── tokens/                   # Tokens salvos
├── logs/                     # Logs do programa
├── backups/                  # Backups automáticos
└── web/                      # Arquivos do site
```

## 🔗 Atalhos Criados

### Windows
- **Área de trabalho:** `DMS.lnk`
- **Menu iniciar:** `Programs > DMS > DMS.lnk`

### Linux
- **Área de trabalho:** `DMS.desktop`

## 🚨 Troubleshooting

### Erro: "Python não encontrado"
```bash
# Instale o Python 3.8+ primeiro
# Windows: https://python.org/downloads
# Linux: sudo apt install python3
```

### Erro: "Sem permissão"
```bash
# Execute como administrador
# Windows: Clique direito > Executar como administrador
# Linux: sudo python3 installer.py
```

### Erro: "Sem conexão com a internet"
- Verifique sua conexão
- Configure proxy se necessário
- Tente novamente

### Erro: "Dependência não instalada"
```bash
# Instale manualmente
pip install requests colorama python-dotenv cryptography tqdm pyyaml aiohttp beautifulsoup4
```

## 📝 Logs de Instalação

O instalador cria logs detalhados em:
- **Console:** Mostra progresso em tempo real
- **Arquivo:** `install_log.txt` (se disponível)

## 🔄 Atualizações

### Automáticas
- O programa verifica atualizações automaticamente
- Notifica quando há novas versões
- Permite download direto

### Manuais
```bash
# Reinstale para atualizar
python uninstaller.py
python installer.py
```

## 🛡️ Segurança

### Backup Automático
- Dados do usuário são salvos antes da desinstalação
- Tokens e configurações preservados
- Logs mantidos para análise

### Verificações
- Integridade dos arquivos baixados
- Validação de dependências
- Testes pós-instalação

## 📞 Suporte

Para problemas com a instalação:

1. **Verifique os logs** de erro
2. **Consulte esta documentação**
3. **Abra uma issue** no GitHub
4. **Entre em contato** com a equipe

## 🎯 Próximas Versões

### Planejadas
- [ ] Instalador gráfico (GUI)
- [ ] Instalação silenciosa
- [ ] Atualizações automáticas
- [ ] Múltiplas versões
- [ ] Instalação em rede

### Melhorias
- [ ] Verificação de antivírus
- [ ] Instalação em containers
- [ ] Suporte a mais sistemas
- [ ] Configuração avançada

---

**Desenvolvido por: NYX DEV**  
**Versão: 2.0**  
**Data: 2025** 