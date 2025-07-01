# Manual Completo do Framework NiceGUI (Fornecido pelo Usuário)

Data da Compilação: 2024-07-31 (Conteúdo original fornecido pelo usuário)

## Parte 1: Fundamentos do NiceGUI

### Capítulo 1: Introdução ao NiceGUI

#### 1.1 Visão Geral e Filosofia "Backend-First"

NiceGUI é um framework de interface de usuário (UI) de código aberto, baseado em Python, projetado para simplificar a criação de interfaces gráficas que são executadas em um navegador da web.[1] Ele oferece uma curva de aprendizado suave para iniciantes, ao mesmo tempo que fornece opções de personalização avançada para desenvolvedores experientes, tornando-o adequado para uma vasta gama de projetos, desde scripts simples até aplicações complexas.[2]

O princípio central que orienta o design do NiceGUI é sua filosofia "backend-first". Esta abordagem significa que o framework foi construído para permitir que os desenvolvedores se concentrem exclusivamente na escrita de código Python, enquanto o NiceGUI abstrai e gerencia todos os detalhes complexos do desenvolvimento web, como HTML, CSS e JavaScript.[1] Esta decisão de design é fundamental e define tanto a arquitetura quanto o público-alvo do framework. Ele atrai primariamente desenvolvedores Python — como cientistas de dados, engenheiros de automação, pesquisadores de aprendizado de máquina e entusiastas de IoT — que necessitam de uma interface de usuário funcional e moderna rapidamente, sem a necessidade de adquirir proficiência em tecnologias de front-end como React ou Vue.js. A premissa é que a lógica do backend é a preocupação principal, e a UI serve como uma ferramenta para interagir com essa lógica. Ao lidar com a complexidade do front-end, o NiceGUI se posiciona como uma ponte eficaz entre o mundo do scripting e análise de dados em Python e o mundo das aplicações web interativas.[1]

#### 1.2 Arquitetura do Sistema: FastAPI, Uvicorn, Vue e Quasar

A arquitetura do NiceGUI é uma composição de tecnologias de alto desempenho, escolhidas para garantir performance, extensibilidade e uma experiência de desenvolvimento fluida. A pilha tecnológica subjacente não é apenas um detalhe de implementação, mas uma característica central que define as capacidades do framework.[4]

*   **FastAPI e Uvicorn**: No núcleo do backend, uma aplicação NiceGUI é, essencialmente, uma aplicação FastAPI.[3] O FastAPI é um moderno e rápido framework web para Python, construído sobre o padrão ASGI (Asynchronous Server Gateway Interface). Ele é servido pelo Uvicorn, um servidor ASGI de alta performance. A escolha do FastAPI foi deliberada, visando sua excelente performance, facilidade de uso e suporte nativo para operações assíncronas (`async/await`), o que é crucial para manter a UI responsiva.[4] Uma implicação direta dessa arquitetura é que a integração com uma aplicação FastAPI existente é trivial. Desenvolvedores podem adicionar uma interface NiceGUI a uma API existente ou, inversamente, adicionar rotas de API personalizadas a uma aplicação NiceGUI, aproveitando todo o ecossistema do FastAPI.[2]
*   **Vue.js e Quasar**: Para o front-end, o NiceGUI utiliza o Vue.js, um popular framework JavaScript, e sobre ele, o Quasar Framework.[4] O Quasar fornece uma vasta biblioteca de componentes de UI de alta qualidade, prontos para uso e com um estilo profissional. Isso significa que os desenvolvedores Python têm acesso a elementos como botões, tabelas, diálogos e layouts complexos sem escrever uma única linha de JavaScript. O NiceGUI atua como uma ponte, fornecendo uma API em Python que gera e se comunica com esses componentes Vue/Quasar no navegador. Para desenvolvedores que desejam ir além dos elementos padrão, a documentação do Quasar se torna uma referência valiosa para entender as propriedades (`.props()`) e eventos (`.on()`) disponíveis, permitindo uma personalização profunda.[5]

Essa arquitetura combinada garante não apenas alta performance e uma rica biblioteca de componentes, mas também um caminho claro para a extensibilidade, seja através da integração com rotas FastAPI ou da criação de componentes Vue personalizados.[2]

#### 1.3 Casos de Uso Ideais

O NiceGUI é ideal para uma ampla variedade de aplicações, especialmente aquelas que são interativas e "stateful", onde a comunicação em tempo real entre o front-end e o backend é essencial. A documentação e os exemplos práticos demonstram sua eficácia nos seguintes cenários [2]:

*   Micro-aplicativos Web e Painéis de Controle
*   Projetos de Robótica e IoT
*   Soluções de Casa Inteligente
*   Interfaces para Machine Learning
*   Prototipagem Rápida

O ponto forte do NiceGUI reside em aplicações que dependem de um loop de eventos contínuo (asyncio), atualizações periódicas (`ui.timer`) ou manipulação de eventos em tempo real.[2][4]

### Capítulo 2: Instalação e Primeira Aplicação

#### 2.1 Instalação do Framework

Instale usando pip:[6]
```bash
python3 -m pip install nicegui
```
Disponível também via Docker e conda-forge.[4]

#### 2.2 Estrutura de uma Aplicação Mínima

Código de Exemplo (`main.py`):[4]
```python
from nicegui import ui

# 1. Cria um elemento de texto (label)
ui.label('Hello NiceGUI!')

# 2. Cria um botão que, ao ser clicado, exibe uma notificação
ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))

# 3. Inicia o servidor e a aplicação
ui.run()
```
Estrutura: Importação, Criação de Elementos, Execução (`ui.run()`).[1]

#### 2.3 Executando a Aplicação

Execute com:[6]
```bash
python3 main.py
```
Acesse em `http://localhost:8080`.[4] Possui recarregamento automático por padrão.[4]

## Parte 2: Estrutura e Layout da Aplicação

### Capítulo 3: Páginas e Navegação

#### 3.1 Criando Múltiplas Páginas com `@ui.page`

O decorador `@ui.page` associa uma função Python a uma rota de URL.[2]
```python
from nicegui import ui

@ui.page('/')
def main_page():
    ui.label('Esta é a Página Principal.')
    ui.link('Ir para a página de informações', '/info')

@ui.page('/info')
def info_page():
    ui.label('Esta é a Página de Informações.')
    ui.link('Voltar para a página principal', '/')

ui.run()
```
Se nenhuma função for decorada com `@ui.page('/')`, elementos no escopo global são exibidos na raiz.[8]

#### 3.2 Navegação Programática e Histórico do Navegador

Use o módulo `ui.navigate`:[8]
*   `ui.navigate.to(target, new_tab=False)`
*   `ui.navigate.back()`
*   `ui.navigate.forward()`
*   `ui.navigate.reload()`
*   `ui.navigate.history.push('/new_url')`
*   `ui.navigate.history.replace('/new_url')`

```python
from nicegui import ui

with ui.row():
    ui.button('Voltar', on_click=ui.navigate.back)
    ui.button('Avançar', on_click=ui.navigate.forward)
ui.run()
```

#### 3.3 Layout de Página Padrão: Header, Footer e Drawers

Componentes: `ui.header`, `ui.footer`, `ui.left_drawer`, `ui.right_drawer` criam layouts persistentes para uma página.[9]
```python
from nicegui import ui

@ui.page('/layout_demo')
def page_with_layout():
    with ui.header(elevated=True).style('background-color: #3874c8'):
        ui.label('MEU APP')
    with ui.left_drawer().style('background-color: #d7e3f4'):
        ui.label('Menu Esquerdo')
    ui.label('Conteúdo da Página')
ui.run()
```

### Capítulo 4: Layout Declarativo com Contêineres

#### 4.1 O Paradigma do `with`: Construindo Hierarquias Visuais

A declaração `with` do Python define a estrutura e hierarquia da UI. A indentação reflete o aninhamento.[1]

#### 4.2 Organização com `ui.row` e `ui.column`

Baseados em Flexbox:[10]
*   `ui.row`: Organiza filhos horizontalmente.
*   `ui.column`: Organiza filhos verticalmente.
Aceitam `wrap`, `align_items`.[11]
```python
from nicegui import ui

with ui.row().classes('w-full justify-around'):
    with ui.column():
        ui.label('Col 1, Item 1')
    with ui.column():
        ui.label('Col 2, Item 1')
ui.run()
```

#### 4.3 Layouts em Grade com `ui.grid`

Baseado em CSS Grid Layout.[10] Parâmetros `rows` e `columns` (inteiro ou string CSS).[13]
```python
from nicegui import ui

with ui.grid(columns='auto 1fr').classes('w-full gap-4'):
    ui.label('Nome:')
    ui.input(placeholder='Digite seu nome')
ui.run()
```

#### 4.4 Agrupamento Visual com `ui.card` e `ui.expansion`

*   `ui.card`: Contêiner com bordas, sombra, preenchimento. Seções com `ui.card_section`.[10]
*   `ui.expansion`: Painel dobrável.[3]
```python
from nicegui import ui

with ui.card().classes('w-64'):
    with ui.card_section():
        ui.label('Título do Cartão').classes('text-h6')
    with ui.expansion('Ver detalhes', icon='info'):
        ui.label('Detalhes ocultos.')
ui.run()
```

**Tabela de Propriedades/Classes de Layout Comuns:**

| Propriedade/Método      | Contêineres Aplicáveis | Descrição                                                                 | Valores de Exemplo                                       |
| :---------------------- | :--------------------- | :------------------------------------------------------------------------ | :------------------------------------------------------- |
| `wrap`                  | `ui.row`, `ui.column`  | Controla quebra de linha/coluna.                                          | `True`, `False`                                          |
| `align_items`           | `ui.row`, `ui.column`  | Alinhamento no eixo transversal.                                          | `'start'`, `'center'`, `'end'`, `'stretch'`              |
| `.classes('justify-...')` | `ui.row`, `ui.column`  | Alinhamento no eixo principal.                                            | `'justify-start'`, `'justify-center'`, `'justify-between'` |
| `.classes('items-...')`   | `ui.row`, `ui.column`  | Equivalente a `align_items` (Tailwind).                                 | `'items-start'`, `'items-center'`, `'items-end'`         |
| `.classes('gap-...')`     | `ui.row`, `ui.column`, `ui.grid` | Espaçamento entre filhos.                                               | `'gap-2'`, `'gap-4'`, `'gap-x-8'`, `'gap-y-4'`           |

## Parte 3: Referência Completa de Elementos de UI

### Capítulo 5: O Elemento Base e Métodos Comuns

#### 5.1 `ui.element` e Tags HTML Arbitrárias

`Element` é a classe base.[14] `ui.element('tag_html')` cria elementos HTML arbitrários.[15]
```python
from nicegui import ui

with ui.element('div').classes('p-4 bg-yellow-200 rounded'):
    ui.label('Texto em div personalizado.')
ui.run()
```

#### 5.2 Métodos Universais de Estilização e Manipulação

Métodos compartilhados por todos os elementos:[14]
*   `.classes(add, remove, toggle, replace)`: Preferencial para estilização com Tailwind CSS.[16]
*   `.props(add, remove)`: Interage com propriedades do componente Quasar subjacente.[16]
*   `.style(add, remove, replace)`: Aplica CSS inline (usar com moderação).[16]
*   `.bind_visibility(target_object, target_name, ...)`: Controla visibilidade.[9]
*   `.move(target_container, target_index)`: Move elemento.[14]
*   `.delete()`: Remove elemento.[14]
*   `.clear()`: Remove filhos de um contêiner.[14]

Diretriz de estilização: `classes()` -> `props()` -> `style()`.

### Capítulo 6: Elementos de Texto e Conteúdo

Elementos para exibir texto e conteúdo:[3]
*   `ui.label(text)`
*   `ui.link(text, target, new_tab=False)`
*   `ui.markdown(content, extras=[...])`: Suporta extensões como 'mermaid'.
*   `ui.html(content, tag='div')`
*   `ui.restructured_text(content)`
*   `ui.chat_message(text, name, avatar, sent, stamp)`

```python
from nicegui import ui

ui.label('Label simples.')
ui.link('NiceGUI', 'https://nicegui.io', new_tab=True)
ui.markdown('### Título\n* Item 1')
ui.run()
```

### Capítulo 7: Controles de Entrada do Usuário

Permitem ao usuário fornecer informações. Parâmetros comuns: `label`, `value`, `on_change`.[3]
Recomendado usar `bind_value` para gerenciar estado.

*   **Botões**:[19]
    *   `ui.button(text, on_click, color, icon)`
    *   `ui.button_group()`
    *   `ui.dropdown_button(text, auto_close)`
*   **Entrada de Texto e Números**:
    *   `ui.input(label, placeholder, on_change, validation)`[21]
    *   `ui.textarea()`
    *   `ui.number(label, value, min, max, step, format)`[22]
*   **Seleção**:
    *   `ui.select(options, label, value, on_change, multiple)`[23]
    *   `ui.toggle(options, value)`[19]
    *   `ui.radio(options, value)`[19]
    *   `ui.checkbox(text, value)`
    *   `ui.switch(text, value)`[24]
*   **Outros Controles**:
    *   `ui.slider(min, max, step, value)`
    *   `ui.date(value, on_change)`
    *   `ui.color_picker(on_pick)`
    *   `ui.upload(on_upload)`

Exemplo de Validação:
```python
from nicegui import ui
ui.input('Senha', password=True,
         validation={'Mínimo 8 caracteres': lambda v: len(v) >= 8})
ui.run()
```

### Capítulo 8: Exibição de Dados Tabulares e Estruturados

*   `ui.table(columns, rows, row_key, selection)`: Baseado em Quasar QTable. Simples, para dados tabulares básicos.[25]
*   `ui.aggrid(options, html_columns)`: Baseado em AG Grid. Poderoso, para interatividade complexa, edição, filtragem.[26]
Ambos suportam `.from_pandas(dataframe)`.[25]

**Comparativo `ui.table` vs `ui.aggrid`:**

| Funcionalidade             | `ui.table` (Quasar)                     | `ui.aggrid` (AG Grid)                     |
| :------------------------- | :-------------------------------------- | :---------------------------------------- |
| Simplicidade Configuração  | Alta                                    | Menor (dicionário AG Grid)                |
| Edição In-loco             | Não                                     | Sim                                       |
| Filtragem Coluna          | Limitada                                | Avançada                                  |
| Renderização Células       | Limitada                                | Extensiva (HTML, componentes)             |

### Capítulo 9: Visualização de Dados e Gráficos

Integração com bibliotecas de plotagem. Chamar `.update()` no elemento do gráfico após modificar dados/opções.[30]
*   `ui.line_plot(n, limit, update_every)`: Leve, para dados em tempo real. Método `.push()`.[33]
*   `ui.pyplot()` / `ui.matplotlib()`: Renderiza gráficos Matplotlib.[35]
*   `ui.plotly(figure)`: Gráficos interativos Plotly.[31]
*   `ui.highchart(options, extras=[...])`: Gráficos Highcharts (requer `pip install nicegui[highcharts]`).[27]
*   `ui.echart(options)`: Gráficos Apache ECharts.[39]

Exemplo (Gráfico de Linha em Tempo Real):
```python
import math, time
from datetime import datetime
from nicegui import ui

line_plot = ui.line_plot(n=2, limit=20).with_legend(['sin', 'cos'])
def update_plot():
    now = datetime.now()
    x = now.timestamp()
    line_plot.push([now], [[math.sin(x)], [math.cos(x)]])
ui.timer(0.1, update_plot)
ui.run()
```

### Capítulo 10: Elementos Audiovisuais e de Feedback

*   **Mídia**:
    *   `ui.image(source)`: URL, caminho local, ou `PIL.Image`.
    *   `ui.video(source)`
    *   `ui.audio(source)`[6]
*   **Feedback Visual**:
    *   `ui.notify(message, position, type)`: Notificação toast.[6]
    *   `ui.tooltip(text)`
    *   `ui.spinner(type, size, color)`[27]
    *   `ui.linear_progress(value)`, `ui.circular_progress(value)`[27]
*   **Interações Modais**:
    *   `ui.dialog()`: Caixa de diálogo modal. Usar com `with`. Métodos `.open()`, `.close()`.[6]
    *   `ui.menu()`: Menu suspenso.[6]

Exemplo (Diálogo):
```python
from nicegui import ui

with ui.dialog() as dialog:
    with ui.card():
        ui.label('Você tem certeza?')
        with ui.row():
            ui.button('Sim', on_click=lambda: ui.notify('Confirmado!'))
            ui.button('Não', on_click=dialog.close)
ui.button('Abrir Diálogo', on_click=dialog.open)
ui.run()
```

## Parte 4: Interatividade e Gerenciamento de Estado

### Capítulo 11: Manipulação de Eventos

Baseado no loop de eventos `asyncio`.[1]

#### 11.1 Eventos Padrão e Assíncronos

Parâmetros `on_click`, `on_change`, etc. Suporte a manipuladores `async def`.[40]
```python
import asyncio
from nicegui import ui

async def my_task():
    ui.notify('Tarefa iniciada...')
    await asyncio.sleep(3)
    ui.notify('Tarefa concluída!')
ui.button('Iniciar', on_click=my_task)
ui.run()
```

#### 11.2 O Manipulador de Eventos Genérico `.on()`

`.on(event_type, handler, throttle, args, modifiers)` para qualquer evento JS/Quasar.[5]
`throttle` limita frequência. Consultar documentação Quasar para `event_type`.

#### 11.3 Passando Argumentos de Eventos e Modificadores

Especificar `args` em `.on()` para enviar apenas dados de evento necessários.[5]
Modificadores: `.on('keydown.enter', ...)` ou `.on('event.once', ...)`.[5]

### Capítulo 12: Vinculação de Dados (Data Binding)

Conexão "viva" entre UI e dados Python, automatizando sincronização.[41]

#### 12.1 O Conceito de Vinculação

Evita manipulação manual de UI para refletir/capturar dados.

#### 12.2 Vinculação Bidirecional e Unidirecional

*   **Bidirecional**: `bind_value()`, `bind_visibility()`, etc. UI <=> Modelo.[41]
*   **Unidirecional**: `bind_..._from(modelo)` (Modelo -> UI), `bind_..._to(modelo)` (UI -> Modelo).[41]

```python
from nicegui import ui

class Data: name = "Mundo"
data = Data()
ui.input("Nome").bind_value(data, 'name') # Bidirecional
ui.label().bind_text_from(data, 'name') # Unidirecional (leitura)
ui.run()
```

#### 12.3 Funções de Transformação (`forward`, `backward`)

Transformam valores entre modelo e UI.[41]
*   `backward`: Modelo -> UI.
*   `forward`: UI -> Modelo.
```python
from nicegui import ui
data = {'price': 12.34}
ui.input('Preço').bind_value(data, 'price',
    backward=lambda p: f"R$ {p:.2f}",
    forward=lambda p_str: float(p_str.replace("R$ ", "")))
ui.run()
```

#### 12.4 Vinculando a Diferentes Estruturas de Dados

Atributos de classe, dicionários, `globals()`, `app.storage.user`.[41][42][40]

#### 12.5 Performance da Vinculação: Propriedades Vinculáveis vs. Links Ativos

*   **Propriedades Vinculáveis**: Eficiente, baseado em eventos. Usar `binding.BindableProperty()` ou `@binding.bindable_dataclass` para modelos de dados performáticos.[41]
*   **Links Ativos**: Para objetos Python simples, faz polling (0.1s). Pode ser custoso com muitas vinculações.[41]

```python
from nicegui import ui, binding

@binding.bindable_dataclass
class Demo: number: int = 1
demo = Demo()
ui.slider(min=1, max=10).bind_value(demo, 'number') # Vinculação eficiente
ui.run()
```

### Capítulo 13: Tarefas Assíncronas e Atualizações Periódicas

#### 13.1 Executando Tarefas de Longa Duração

Evitar bloqueio da UI:[40]
*   `run.io_bound(func, *args)`: Para tarefas limitadas por I/O (rede, disco). Executa em thread pool.
*   `run.cpu_bound(func, *args)`: Para tarefas limitadas por CPU (cálculos). Executa em process pool (contorna GIL).
Ambas retornam `Future` (pode ser `await`ed).

```python
import time, requests
from nicegui import run, ui

async def fetch_example():
    response = await run.io_bound(requests.get, 'https://dummyjson.com/products/1')
    ui.notify('Dados da API recebidos!')
ui.button('Buscar API (I/O)', on_click=fetch_example)
ui.run()
```

#### 13.2 Atualizações Agendadas com `ui.timer`

Executa função periodicamente.[6]
`ui.timer(interval, callback, active=True, once=False)`
```python
from datetime import datetime
from nicegui import ui

clock_label = ui.label()
ui.timer(1.0, lambda: clock_label.set_text(f'{datetime.now():%X}'))
ui.run()
```

#### 13.3 Atualizando a UI Explicitamente com `.update()`

Necessário ao manipular estrutura de contêineres ou componentes complexos (gráficos) dinamicamente.[40]
*   `element.update()`
*   `ui.update(*elements)`

## Parte 5: Tópicos Avançados e Implantação

### Capítulo 14: Personalização Avançada e Estilo

`ui.colors(primary, secondary, accent, ...)` define tema de cores global (antes de criar elementos).[6]
```python
from nicegui import ui
ui.colors(primary='#558B2F', accent='#FFCA28')
ui.button('Botão Primário') # Usa cor primária
ui.run()
```
Tailwind CSS ainda é principal para layout/estilo fino.[17] Forçar prioridade com `!`: `.classes('!bg-red-500')`.[44]

### Capítulo 15: Estendendo o NiceGUI

#### 15.1 Modularização

Dividir UI em múltiplos arquivos Python. Importar funções que constroem partes da UI.[2]
Exemplo:
```python
# components/header.py
from nicegui import ui
def create_header():
    with ui.header(): ui.label('Meu App')

# main.py
from nicegui import ui
from components.header import create_header
@ui.page('/')
def index():
    create_header()
    ui.label('Bem-vindo!')
ui.run()
```

#### 15.2 Componentes Personalizados

Criar e integrar componentes Vue personalizados via `ui.element` para necessidades não cobertas.[2]

### Capítulo 16: Implantação (Deployment)

#### 16.1 Configurando `ui.run()` para Produção

Ajustar parâmetros de `ui.run()`:[1]

| Parâmetro        | Descrição                               | Padrão      | Produção Recomendado                        |
| :--------------- | :-------------------------------------- | :---------- | :------------------------------------------ |
| `host`           | IP de vínculo                           | '127.0.0.1' | '0.0.0.0' (em contêiner/VM)               |
| `port`           | Porta de escuta                         | 8080        | 80/443 (proxy) ou outra                     |
| `title`          | Título da página                        | 'NiceGUI'   | Descritivo                                  |
| `favicon`        | Ícone da página                         | None        | Definir                                     |
| `dark`           | Modo de tema                            | False       | None, True, ou False                        |
| `storage_secret` | **CRÍTICO**: Chave para cookie de sessão | None        | **DEFINIR CHAVE SECRETA LONGA E ALEATÓRIA** |
| `reload`         | Recarregamento automático               | True        | `False`                                     |

`storage_secret` é essencial para segurança do `app.storage.user`.[40]

#### 16.2 Empacotamento com Docker

Usar contêineres Docker para implantação robusta.[2]
Exemplo `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python3", "main.py", "--host", "0.0.0.0", "--port", "8080"]
```

#### 16.3 Proxy Reverso (NGINX)

Executar NiceGUI atrás de um proxy reverso (NGINX) para SSL, balanceamento de carga, etc.
Configurar NGINX para encaminhar tráfego HTTP e **WebSocket**. Suporte a WebSocket é essencial.[2]

## Parte 6: Referência Rápida da Documentação de Componentes

Links para a documentação oficial do NiceGUI.[1] (Omitido para brevidade, mas imagine uma tabela aqui como no original)

## Parte 7: Galeria de Exemplos de Código

(Resumos dos exemplos fornecidos no manual original)

#### 7.1 "Olá, Mundo"
Demonstra `ui.label`, `ui.button`, `ui.notify`, `ui.run()`.[6]

#### 7.2 Layout Básico com Linhas e Colunas
Uso de `ui.row` e `ui.column` com `with`.[10]

#### 7.3 Vinculação de Dados Interativa
`ui.slider` vinculado a `ui.label` com `bind_text_from`.[45]

#### 7.4 Gráfico de Linha em Tempo Real
`ui.timer` e `ui.line_plot().push()` para dados dinâmicos.[27]

#### 7.5 Tabela a partir de um DataFrame Pandas
`ui.aggrid.from_pandas(df)`.[26]

#### 7.6 Aplicação Completa: Lista de Tarefas
Usa dataclass, `@ui.refreshable`, vinculação de dados para uma lista de tarefas interativa.[46]

#### 7.7 Aplicação Avançada: Galeria de Imagens Lightbox
Classe Python para componente complexo, `ui.dialog`, `ui.keyboard`, `httpx` para chamadas assíncronas.[47]

---
Referências citadas no manual original (ex: [1], [2], etc.) são mantidas para indicar a origem da informação dentro do texto fornecido.
---
