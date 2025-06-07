# Discord Multi Tool

Uma ferramenta multifuncional para gerenciamento de contas do Discord com interface amigável e recursos avançados.

## 🚀 Funcionalidades

- **Gerenciamento de Tokens**
  - Verificação de tokens
  - Informações detalhadas
  - Suporte a múltiplos tokens
  - Backup automático
  - Criptografia de tokens

- **Operações em Servidores**
  - Entrar em servidores
  - Sair de servidores
  - Nuke (deletar canais e cargos)
  - Spam de mensagens

- **Personalização de Perfil**
  - Alterar HypeSquad House
  - Modificar bio
  - Trocar avatar
  - Alterar username

- **Recursos Avançados**
  - Sistema de filas para operações em massa
  - Tratamento automático de erros
  - Retry automático em falhas
  - Logging detalhado
  - Interface personalizável
  - Sistema de proxies rotativos
  - Temas personalizáveis

## 📋 Requisitos

- Python 3.8 ou superior
- Dependências listadas em `requirements.txt`

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/discord-multi-tool.git
cd discord-multi-tool
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o programa:
```bash
python main.py
```

## ⚙️ Configuração

O programa possui um sistema de configuração completo que pode ser acessado através do menu principal:

### Interface
- Personalização de cores
- Barras de progresso
- Animações
- Temas predefinidos (Default, Dark, Light)

### Requisições
- Timeout
- Número de tentativas
- Delay entre tentativas
- Sistema de proxies rotativos
  - Busca automática de proxies
  - Validação de proxies
  - Rotação automática

### Segurança
- Criptografia de tokens
- Intervalo de backup
- Validação de tokens

## 🛠️ Uso

1. **Token Checker**
   - Verifica a validade do token
   - Mostra informações básicas

2. **Token Info**
   - Exibe informações detalhadas da conta
   - Status de verificação
   - Configurações de segurança

3. **Token Joiner**
   - Entra em servidores usando convites
   - Suporte a múltiplos convites

4. **Token Leaver**
   - Sai de servidores específicos
   - Confirmação de segurança

5. **Token Nuker**
   - Deleta canais e cargos
   - Sistema de filas para operações em massa

6. **Token Spammer**
   - Envia mensagens em massa
   - Barra de progresso
   - Controle de delay

7. **HypeSquad**
   - Altera a HypeSquad House
   - Suporte a todas as casas

8. **Bio Changer**
   - Modifica a bio do perfil
   - Validação de conteúdo

9. **Avatar Changer**
   - Altera o avatar
   - Suporte a URLs de imagens

10. **Username Changer**
    - Modifica o username
    - Validação de disponibilidade

## 🔒 Segurança

- Tokens são armazenados de forma segura
- Criptografia opcional
- Backup automático
- Validação rigorosa de entradas
- Proteção contra rate limits
- Sistema de proxies para evitar bloqueios

## 📝 Logs

- Logs detalhados são salvos na pasta `logs`
- Formato: `discord_tool_YYYYMMDD_HHMMSS.log`
- Informações sobre todas as operações
- Erros e exceções

## ⚠️ Aviso

Esta ferramenta é apenas para fins educacionais. O uso indevido pode resultar em banimento da sua conta do Discord.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes. 