# Sistema de Atualizações - DMS (Discord Management Suite)

## Visão Geral

O DMS agora inclui um sistema completo de atualizações automáticas que verifica novas versões no GitHub e permite aos usuários baixar e instalar atualizações facilmente.

## Funcionalidades

### 1. Verificação Automática de Atualizações
- Verifica automaticamente por novas versões na inicialização
- Compara versões usando semântica de versionamento
- Notifica o usuário quando há atualizações disponíveis

### 2. Changelog Completo
- Mostra histórico de todas as versões
- Exibe notas de lançamento detalhadas
- Inclui links para releases no GitHub

### 3. Sistema de Download
- Download automático de atualizações
- Backup automático antes da instalação
- Suporte a proxies para downloads

## Configuração

### Arquivo `update_config.yaml`

```yaml
update_settings:
  github_repo: "seu-usuario/seu-repositorio"
  current_version: "2.0"
  auto_check: true
  check_interval: 3600
  download_path: "./downloads"
  backup_before_update: true
  show_notifications: true
  notify_on_startup: true
  changelog_limit: 10
  show_preview: true
  use_proxy_for_downloads: false
  download_timeout: 300
```

### Configurações Explicadas

- **github_repo**: Seu repositório no GitHub (formato: usuario/repositorio)
- **current_version**: Versão atual do programa
- **auto_check**: Verifica automaticamente por atualizações
- **check_interval**: Intervalo entre verificações (em segundos)
- **download_path**: Pasta onde as atualizações serão baixadas
- **backup_before_update**: Cria backup antes de atualizar
- **show_notifications**: Mostra notificações de atualização
- **notify_on_startup**: Notifica na inicialização
- **changelog_limit**: Número máximo de versões no changelog
- **show_preview**: Mostra preview das notas de lançamento
- **use_proxy_for_downloads**: Usa proxies para downloads
- **download_timeout**: Timeout para downloads (em segundos)

## Como Usar

### Verificar Atualizações Manualmente
1. No menu principal, selecione a opção `[15] Verificar Updates`
2. O sistema verificará se há novas versões disponíveis
3. Se houver atualização, você pode baixá-la

### Ver Changelog
1. No menu principal, selecione a opção `[16] Changelog`
2. O sistema mostrará o histórico de versões
3. Cada versão inclui notas de lançamento e link para o GitHub

### Verificação Automática
- O sistema verifica automaticamente por atualizações na inicialização
- Se houver uma nova versão, você será notificado
- Use a opção manual para mais detalhes

## Estrutura de Releases no GitHub

Para que o sistema funcione corretamente, suas releases no GitHub devem seguir este formato:

### Tags de Versão
- Use tags semânticas (ex: v2.0, v2.1, v2.1.1)
- Formato recomendado: `vX.Y.Z`

### Título da Release
- Nome descritivo da versão
- Ex: "Versão 2.0 - Novas Funcionalidades"

### Notas de Lançamento
- Descrição detalhada das mudanças
- Lista de funcionalidades novas
- Correções de bugs
- Melhorias de performance

### Assets
- Arquivo executável ou instalador
- Arquivos de configuração atualizados
- Documentação da versão

## Exemplo de Release no GitHub

```markdown
# Versão 2.0 - Sistema de Atualizações

## Novas Funcionalidades
- Sistema completo de atualizações automáticas
- Verificação de novas versões
- Changelog detalhado
- Download automático de atualizações

## Melhorias
- Interface mais responsiva
- Melhor tratamento de erros
- Logs mais detalhados

## Correções
- Corrigido problema de validação de tokens
- Melhorada estabilidade do sistema de proxies

## Instalação
1. Baixe o arquivo `dms_v2.0.exe`
2. Execute o instalador
3. Siga as instruções na tela
```

## Troubleshooting

### Erro ao Verificar Atualizações
- Verifique se o repositório está correto no `update_config.yaml`
- Confirme se há releases públicas no GitHub
- Verifique sua conexão com a internet

### Erro no Download
- Verifique se o arquivo de release existe no GitHub
- Confirme se o caminho de download é válido
- Verifique permissões de escrita na pasta de downloads

### Changelog Não Carrega
- Verifique se há releases no repositório
- Confirme se as releases têm notas de lançamento
- Verifique a conexão com a API do GitHub

## Desenvolvimento

### Adicionando Novas Funcionalidades
1. Atualize a versão no `update_config.yaml`
2. Crie uma nova release no GitHub
3. Adicione notas de lançamento detalhadas
4. Teste o sistema de atualização

### Personalizando o Sistema
- Modifique a classe `UpdateChecker` para adicionar funcionalidades
- Ajuste as configurações no `update_config.yaml`
- Personalize as mensagens e interface

## Suporte

Para suporte ou dúvidas sobre o sistema de atualizações:
- Abra uma issue no GitHub
- Consulte a documentação
- Entre em contato com a equipe de desenvolvimento 