# Site da Discord Multi Tool

Este é o site oficial da Discord Multi Tool, uma ferramenta multifuncional para gerenciamento de contas do Discord.

## 🎨 Design

O site foi desenvolvido com um design moderno e responsivo, utilizando:

- HTML5
- CSS3 (com variáveis CSS e Flexbox/Grid)
- JavaScript (ES6+)
- Font Awesome para ícones
- Google Fonts (Poppins)

## 🚀 Funcionalidades

- Design responsivo para todos os dispositivos
- Menu mobile com animação
- Scroll suave
- Animações de elementos ao scroll
- Tema claro/escuro
- Efeitos de hover
- Otimizado para performance

## 📦 Estrutura de Arquivos

```
web/
├── index.html          # Página principal
├── css/
│   └── style.css      # Estilos do site
├── js/
│   └── main.js        # JavaScript
└── images/            # Imagens do site
```

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/discord-multi-tool.git
cd discord-multi-tool/web
```

2. Abra o arquivo `index.html` em seu navegador ou use um servidor local:
```bash
# Usando Python
python -m http.server 8000

# Usando Node.js
npx serve
```

## 🎯 Personalização

### Cores
As cores podem ser facilmente alteradas editando as variáveis CSS no arquivo `style.css`:

```css
:root {
    --primary-color: #5865F2;
    --secondary-color: #2C2F33;
    --accent-color: #7289DA;
    /* ... outras cores ... */
}
```

### Fontes
Para alterar as fontes, modifique o link do Google Fonts no `index.html` e atualize a variável `--font-family` no CSS.

### Imagens
Substitua as imagens na pasta `images/` mantendo os mesmos nomes de arquivo ou atualize os caminhos no HTML.

## 📱 Responsividade

O site é totalmente responsivo e se adapta a diferentes tamanhos de tela:

- Desktop (> 1200px)
- Tablet (768px - 1199px)
- Mobile (< 767px)

## 🔧 Manutenção

### Adicionar Novas Seções
1. Crie a estrutura HTML na seção desejada
2. Adicione os estilos CSS correspondentes
3. Se necessário, adicione interatividade com JavaScript

### Atualizar Conteúdo
1. Edite o texto no arquivo `index.html`
2. Atualize as imagens na pasta `images/`
3. Ajuste os estilos no `style.css` se necessário

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia o arquivo `CONTRIBUTING.md` para detalhes sobre nosso código de conduta e o processo para enviar pull requests.

## 📞 Suporte

Para suporte, entre em contato através de:

- Discord: [Link do servidor]
- Email: contato@discordtool.com
- GitHub: [Issues do repositório] 