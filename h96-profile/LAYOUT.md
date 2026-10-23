# Perfil visual compacto

O perfil H96 usa os recursos locais do launcher para reduzir o espaço vazio e
manter a tela inicial simples:

| Chave | Valor | Efeito |
|---|---:|---|
| `columns` | `6` | seis atalhos por linha |
| `rows_below_dock` | `1` | uma linha de aplicativos abaixo do dock |
| `dock_top_padding` | `104` | aproxima o dock do cabeçalho |
| `dock_bottom_offset` | `-12` | reduz o espaço abaixo do dock |
| `always_show_names` | `false` | oculta os nomes abaixo dos ícones |
| `grid_bands` | `false` | remove as faixas das fileiras |
| `dock_band` | `false` | remove a faixa externa do dock |
| `library_button` | `true` | coloca **Apps** no cabeçalho |
| `app_library_selection` | `true` | permite mostrar ou ocultar atalhos |
| `ambient_glow` | `false` | evita o brilho colorido de um app no fundo |
| `background_color` | `#1B0B12` | usa vinho profundo quando não há foco |
| `wallpaper` | `false` | não usa imagem de fundo |

A ordem inicial dos atalhos fica em `config.json`. A biblioteca **Apps** continua
permitindo readicionar qualquer aplicativo instalado sem reinstalá-lo.
