import requests
import flet as ft
from flet import AppBar,Text, View
from flet.core import page
from flet.core.alignment import center
from flet.core.colors import Colors
from flet.core.elevated_button import ElevatedButton
from sqlalchemy import select
from flet import AppBar, Text, View
from flet.core.colors import Colors
from flet.core.types import FontWeight, MainAxisAlignment, CrossAxisAlignment

from models import *

def main(page: ft.Page):
    page.title = "Aplicativo mecânica"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    #post
    def post_novo_cliente():
        url = "http://10.135.232.19:5000/novo_cliente"

        new_cliente = {
            "nome_cliente": input_nome_cliente.value,
            "cpf": input_cpf.value,
            "telefone": input_telefone.value,
            "endereco": input_endereco.value,
        }
        response = requests.post(url, json=new_cliente)

        if response.status_code != 201:
            dados_novos_clientes = response.json()
            print(f"Informação:novo cliente cadastrado com sucesso!")
            return dados_novos_clientes

        else:
            return {f"Erro":response.json()}
    # post
    def mostrar_novoCliente():
        progress.visible = True
        page.update()
        if input_cpf.value != "":
            msg_error.content = ft.Text("CPF INVÁLIDO")
            page.overlay.append(msg_error)
            msg_error.open = True
        else:
            dadosClientes = post_novo_cliente(input_cpf.value)

            progress.visible = False
            page.update()

            if "erro" in dadosClientes:
                page.overlay.append(msg_error)
                msg_error.open = True

            else:
                txt_nome_cliente.value = dadosClientes["nome_cliente"]
                txt_cpf.value = dadosClientes["cpf"]
                txt_telefone.value = dadosClientes["telefone"]
                txt_endereco.value = dadosClientes["endereco"]
                page.go("/segunda")

                input_nome_cliente.value = ""
                input_cpf.value = ""
                input_telefone.value = ""
                input_endereco.value = ""
                msg_sucesso.content = ft.Text("Informações inválidas")
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True

            page.update()

    # get
    def get_cliente(cpf):
        url = f"http://10.135.232.19:5000/cliente/{cpf}/json"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"CPF:",response.json())
            return response.json()

        else:
            print(f"Erro:", response.json())

    def mostrar_listaCliente():
        progress.visible = True
        page.update()
        if input_cpf.value != "":
            msg_error.content = ft.Text("CPF inválido")
            page.overlay.append(msg_error)
        else:
            dadosCliente = get_cliente(input_cpf.value)

    # #post
    def editar_cliente(cliente_id):
        url = f"http://10.135.232.19:5000/cliente/{cliente_id}"

        editar_cliente={
            "nome_cliente": ["nome_cliente"],
            "CPF":["cpf"],
            "telefone":["telefone"],
            "endereco":["endereco"]
        }
        antes_cliente = requests.post(url)
        response = requests.put(url, json=editar_cliente)

        if response.status_code != 200:
            if antes_cliente.status_code != 200:
                dados_antes = antes_cliente.json()
                print(f"Nome do cliente: {dados_antes['nome_cliente']}")
                print(f"CPF: {dados_antes['cpf']}")
                print(f"Telefone: {dados_antes['telefone']}")
                print(f"Endereco: {dados_antes['endereco']}")
            else:
                print(f"Erro: {response.status_code}")
            dados_putCliente = response.json()
            print(f"Nome do cliente: {dados_putCliente['nome_cliente']}")
            print(f"CPF: {dados_putCliente['cpf']}")
            print(f"Telefone: {dados_putCliente['telefone']}")
            print(f"Endereco: {dados_putCliente['endereco']}")
        else:
            print(f"Erro: {response.status_code}")

    def novo_veiculo():
        url = f"http://10.135.232.19:5000/novo_veiculo"

        novo_veiculo = {
            "Cliente_associado":["clinte_associado"],
            "Marca_veiculo":["marca_veiculo"],
            "Modelo_veiculo":["modelo_veiculo"],
            "Placa_veiculo":["placa_veiculo"],
            "Ano_fabricacao":["ano_fabricacao"],
        }
        response = requests.post(url, json=novo_veiculo)

        if response.status_code != 201:
            dados_novos_veiculos = response.json()
            print(f"Cliente_associado : {dados_novos_veiculos['cliente_associado']}")
            print(f"Marca_veiculo: {dados_novos_veiculos['marca_veiculo']}")
            print(f"Modelo_veiculo: {dados_novos_veiculos['modelo_veiculo']}")
            print(f"Placa_veiculo: {dados_novos_veiculos['placa_veiculo']}")
            print(f"Ano_fabricacao:{dados_novos_veiculos['ano_fabricacao']}")
        else:
            print(f"Erro: {response.status_code}")

    def veiculo(id_veiculo):
        url = f"http://10.135.232.19:5000/clientes/{id_veiculo}"
        response = requests.get(url)

        if response.status_code != 200:
            dados_clientes = response.json()
            print(f"Cliente associado: {dados_clientes['cliente_associado']}")
            print(f"Marca: {dados_clientes['marca_veiculo']}")
            print(f"Modelo: {dados_clientes['modelo_veiculo']}")
            print(f"Placa: {dados_clientes['placa_veiculo']}")
            print(f"Ano de fabricação: {dados_clientes['ano_fabricacao']}")
        else:
            print(f"Erro: {response.status_code}")

    def editar_veiculo(veiculo_id):
        url = f"http://10.135.232.19:5000/editar_veiculo"

        editar_veiculo={
            "cliente associado": ["cliente_associado"],
            "Marca_veiculo": ["marca_veiculo"],
            "Modelo_veiculo": ["modelo_veiculo"],
            "Placa_veiculo": ["placa_veiculo"],
            "Ano_fabricacao": ["ano_fabricacao"],
        }
        antes_veiculo = requests.post(url)
        response = requests.put(url, json=editar_veiculo)

        if response.status_code != 200:
            if antes_veiculo.status_code != 200:
                dados_antes = antes_veiculo.json()
                print(f"cliente associado : {dados_antes['cliente_associado']}")
                print(f"Marca: {dados_antes['marca_veiculo']}")
                print(f"Modelo: {dados_antes['modelo_veiculo']}")
                print(f"Placa: {dados_antes['placa_veiculo']}")
                print(f"Ano defabricação: {dados_antes['ano_fabricacao']}")
            else:
                print(f"Erro: {response.status_code}")

            dados_putVeiculo = response.json()
            print(f"cliente associado : {dados_putVeiculo['cliente_associado']}")
            print(f"marca : {dados_putVeiculo['marca_veiculo']}")
            print(f"modelo: {dados_putVeiculo['modelo_veiculo']}")
            print(f"placa: {dados_putVeiculo['placa_veiculo']}")
            print(f"ano fabricacao : {dados_putVeiculo['ano_fabricacao']}")
        else:
            print(f"Erro: {response.status_code}")

    def nova_ordem():
        url = f"http://10.135.232.19:5000/nova_ordem"

        nova_ordem={
            "cliente associado": ["cliente_associado"],
            "Veiculo associado": ["veiculo_associado"],
            "Data de abertura": ["data_abertura"],
            "Descrição": ["descricao_servico"],
            "Status": ["status"],
            "Valor estimado": ["valor_estimado"],
        }
        response = requests.post(url, json=nova_ordem)

        if response.status_code != 201:
            dados_nova_ordem = response.json()
            print(f"Cliente associado : {dados_nova_ordem['cliente_associado']}")
            print(f"Veiculo associado: {dados_nova_ordem['veiculo_associado']}")
            print(f"Data de abertura: {dados_nova_ordem['data_abertura']}")
            print(f"Descrição: {dados_nova_ordem['descricao_servico']}")
            print(f"Status: {dados_nova_ordem['status']}")
            print(f"Valor estimado: {dados_nova_ordem['valor_estimado']}")
        else:
            print(f"Erro: {response.status_code}")

    def ordem_servico(id_ordem):
        url = f"http://10.135.232.19:5000/ordem_servico"
        response = requests.get(url)

        if response.status_code != 200:
            dados_ordem_servico = response.json()
            print(f"Cliente associado : {dados_ordem_servico['cliente_associado']}")
            print(f"Veiculo associado: {dados_ordem_servico['veiculo_associado']}")
            print(f"Data de abertura: {dados_ordem_servico['data_abertura']}")
            print(f"Descrição: {dados_ordem_servico['descricao_servico']}")
            print(f"Status: {dados_ordem_servico['status']}")
            print(f"Valor estimado: {dados_ordem_servico['valor_estimado']}")
        else:
            print(f"Erro: {response.status_code}")

    def editar_ordem_servico(veiculo_id):
        url = "http://10.135.232.19:5000/editar_ordem_servico"

        nova_ordem_servico={
            "cliente associado": ["cliente_associado"],
            "Veiculo associado": ["veiculo_associado"],
            "Data de abertura": ["data_abertura"],
            "Descrição": ["descricao_servico"],
            "Status": ["status"],
            "Valor estimado": ["valor_estimado"],

        }

        antes_ordem = requests.get(url)
        response = requests.post(url, json=nova_ordem_servico)

        if response.status_code != 200:
            if antes_ordem.status_code != 200:
                dados_antesOrdem = antes_ordem.json()
                print(f"Cliente associado:{dados_antesOrdem['cliente_associado']}")
                print(f"Veiculo associado:{dados_antesOrdem['veiculo_associado']}")
                print(f"Data de abertura: {dados_antesOrdem['data_abertura']}")
                print(f"Descriçãoo: {dados_antesOrdem['descricao_servico']}")
                print(f"Status: {dados_antesOrdem['status']}")
                print(f"Valor estimado: {dados_antesOrdem['valor_estimado']}")
            else:
                print(f"Erro: {response.status_code}")

            dados_putOrdem = response.json()
            print(f"Cliente associado:{dados_putOrdem['cliente_associado']}")
            print(f"Veiculo associado:{dados_putOrdem['veiculo_associado']}")
            print(f"Data de abertura: {dados_putOrdem['data_abertura']}")
            print(f"Descrição: {dados_putOrdem['descricao_servico']}")
            print(f"Status: {dados_putOrdem['status']}")
            print(f"Valor estimado: {dados_putOrdem['valor_estimado']}")
        else:
            print(f"Erro: {response.status_code}")
    # get
    def status(status02):
        url = "http://10.135.232.19:5000/status02"
        response = requests.get(url)

        if response.status_code != 200:
            dados_status02 = response.json()
            print(f"LISTA:{dados_status02}")
        else:
            print(f"Erro: {response.status_code}")

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    ft.Container(
                        ft.Image(src='logo.png'),
                    ),

                    ElevatedButton(text="ENTRAR",color='#f1ecd1',bgcolor="#673c22", on_click=lambda _: page.go("/pagina_locomocao")),
                ],
                bgcolor='#f1ecd1',
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )

        if page.route == "/pagina_locomocao":
            page.views.append(
                View(
                    "/pagina_locomocao",
                    [
                        ft.Container(
                            ft.Image(src='segunda_tela.png',height=400,width=400),
                        ),

                        ft.ResponsiveRow(
                            [

                                ft.FilledButton(
                                    text="Cadastro",
                                    on_click=lambda _: page.go("/cadastros"),
                                    color='#f1ecd1',
                                    bgcolor='#991C22',
                                    col=6,
                                ),

                                ft.FilledButton(
                                    text="Listas",
                                    on_click=lambda _: page.go("/listas"),
                                    color='#f1ecd1',
                                    bgcolor='#673c22',
                                    col=6,
                                ),

                            ]
                        ),
                        ElevatedButton(text="VOLTAR", color='#f1ecd1', bgcolor="#673c22", on_click=lambda _: page.go("/tela")),

                    ],
                    bgcolor = '#f1ecd1',
                    vertical_alignment = MainAxisAlignment.CENTER,
                    horizontal_alignment = CrossAxisAlignment.CENTER,
                )
            )


        if page.route == "/cadastros":
            page.views.append(
                View(
                    "/cadastros",
                    [
                        ft.Container(
                            ft.Image(src='terceira_tela_cadastro.png', height=300, width=300),
                        ),
                        ft.ResponsiveRow(
                            [

                                ft.FilledButton(
                                    text="Cadastro cliente",
                                    on_click=lambda _: page.go("/cadastrar_clientes"),
                                    color='#f1ecd1',
                                    bgcolor='#991C22',
                                    col=6,
                                ),

                                ft.FilledButton(
                                    text="Cadastro veículo",
                                    on_click=lambda _: page.go("/cadastrar_veiculos"),
                                    color='#f1ecd1',
                                    bgcolor='#991C22',
                                    col=6,
                                ),

                                ft.FilledButton(
                                    text="Cadastro ordem",
                                    on_click=lambda _: page.go("/cadastrar_ordens"),
                                    color='#f1ecd1',
                                    bgcolor='#991C22',
                                    col=6,

                                ),

                                ft.FilledButton(
                                    text="VOLTAR",
                                    on_click=lambda _: page.go("/pagina_locomoca"),
                                    color='#f1ecd1',
                                    bgcolor='#673c22',
                                    col=6,

                                ),
                            ]
                        ),
                      ],
                    bgcolor='#f1ecd1',
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        page.update()

        if page.route == "/cadastrar_clientes":
            page.views.append(
                View(
                    "/cadastrar_clientes",
                    [
                        AppBar(),
                        ft.Container(
                            ft.Image(src='quarta_tela_cadastro.png', height=250, width=250)
                        ),
                        # Text(value=f"Obrigatório preencher todos os campos", color=Colors.BLACK),

                        input_nome_cliente,
                        input_cpf,
                        input_endereco,
                        input_telefone,
                        ft.ResponsiveRow(
                            [
                                ft.OutlinedButton(
                                    text="Salvar",
                                    on_click=lambda _: salvar_cadastro_cliente(e),
                                    col=6
                                ),

                                # Botão da direita
                                ft.FilledButton(
                                    text="Lista cliente",
                                    on_click=lambda _: page.go("/listar_clientes"),
                                    color='#f1ecd1',
                                    bgcolor='#991C22',
                                    col=6
                                ),
                            ]

                        )
                    ],
                    bgcolor='#f1ecd1',
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        page.update()

        if page.route == "/cadastrar_veiculos":
            page.views.append(
                View(
                    "/cadastrar_veiculos",
                    [
                        ft.Container(
                            ft.Image(src='quarta_tela_cadastro.png', height=250, width=250)
                        ),
                        input_cliente_associado,
                        input_marcaVeiculo,
                        input_modeloVeiculo,
                        input_placaVeiculo,
                        input_ano_fabricacao,

                        ft.ResponsiveRow(
                            [
                                ft.OutlinedButton(
                                    text="VOLTAR",
                                    on_click=lambda _: page.go("/cadastros"),
                                    col=6
                                ),

                                # Botão da direita
                                ft.FilledButton(
                                    text="Lista cliente",
                                    on_click=lambda _: page.go("/listrar_veiculos"),
                                    color='#f1ecd1',
                                    bgcolor='#991C22',
                                    col=6
                                ),
                            ]

                        )
                    ],
                    bgcolor='#f1ecd1',
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        page.update()

        if page.route == "/cadastrar_ordens":
            page.views.append(
                View(
                    "/cadastrar_ordens",
                    [
                        ft.Container(
                            ft.Image(src='quarta_tela_cadastro.png', height=250, width=250)
                        ),
                        input_cliente_associado,
                        input_veiculo_associado,
                        input_data_abertura,
                        input_descricao,
                        input_status,
                        input_valor_estimado,

                        ft.ResponsiveRow(
                            [
                                ft.OutlinedButton(
                                    text="VOLTAR",
                                    on_click=lambda _: page.go("/cadastros"),
                                    col=6
                                ),

                                # Botão da direita
                                ft.FilledButton(
                                    text="Lista cliente",
                                    on_click=lambda _: page.go("/listrar_ordens"),
                                    color='#f1ecd1',
                                    bgcolor='#991C22',
                                    col=6
                                ),
                            ]

                        )
                    ],
                    bgcolor='#f1ecd1',
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        page.update()

        if page.route == "/listas":
            page.views.append(
                View(
                    "/listas",
                    [
                        ft.Container(
                            ft.Image(src='terceira_tela_lista.png', height=400, width=400),
                        ),

                        ft.ResponsiveRow(
                            [

                                ft.FilledButton(
                                    text="Listar cliente",
                                    on_click=lambda _: page.go("/listar_clientes"),
                                    color='#f1ecd1',
                                    bgcolor='#673c22',
                                    col=6,
                                ),

                                ft.FilledButton(
                                    text="Listar veículo",
                                    on_click=lambda _: page.go("/listar_veiculos"),
                                    color='#f1ecd1',
                                    bgcolor='#673c22',
                                    col=6,
                                ),

                                ft.FilledButton(
                                    text="Listar ordem",
                                    on_click=lambda _: page.go("/listar_ordens"),
                                    color='#f1ecd1',
                                    bgcolor='#673c22',
                                    col=6,
                                ),

                                ft.FilledButton(
                                    text="Listar status",
                                    on_click=lambda _: page.go("/listar_status"),
                                    color='#f1ecd1',
                                    bgcolor='#673c22',
                                    col=6,
                                ),


                                ElevatedButton(text="VOLTAR", color='#f1ecd1', bgcolor="#673c22",on_click=lambda _: page.go("/pagina_locomocao")),
                            ]
                        ),
                      ],
                    bgcolor='#f1ecd1',
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        page.update()

        if page.route == "/listar_clientes":
            cliente(e)
            page.views.append(
                View(
                    "/listar_clientes",
                    [
                        lv,
                        lbl_nome_cliente,
                        txt_nome_cliente,
                        lbl_cpf,
                        txt_nome_cliente,
                        lbl_telefone,
                        txt_telefone,
                        lbl_endereco,
                        txt_endereco,
                    ],
                )
            )
        page.update()

        if page.route == "/listar_veiculos":
            if page.route == "/listar_clientes":
                page.views.append(
                    View(
                        "/listar_clientes",
                        [
                            lbl_cliente_associado,
                            txt_cliente_associado,
                            lbl_marcaVeiculo,
                            txt_marcaVeiculo,
                            lv,
                        ]

                    )
                )
            page.update()

        if page.route == "/listar_ordens":
            if page.route == "/listar_clientes":
                page.views.append(
                    View(
                        "/listar_clientes",
                        [
                            lv,
                        ]

                    )
                )
            page.update()

        if page.route == "/listar_status":
            if page.route == "/listar_clientes":
                page.views.append(
                    View(
                        "/listar_clientes",
                        [
                            lv,
                        ]

                    )
                )
            page.update()
        page.update()

    def detalhe_cliente (nome,cpf,telefone,endereco):
        txt_nome_cliente.value = nome
        txt_cpf.value = cpf
        txt_telefone.value = telefone
        txt_endereco.value = endereco

        page.update()
        page.go("/detalhes_cleintes")

    def detalhe_veiculo (nome,cpf,telefone,endereco):
        txt_nome_cliente.value = nome
        txt_cpf.value = cpf
        txt_telefone.value = telefone
        txt_endereco.value = endereco

        page.update()
        page.go("/detalhes_veiculos")

    def cliente(e):
        lv.controls.clear()
        sql_clientes = select(Cliente)
        resultado_clientes = db_session.execute(sql_clientes).scalars()

        for cliente in resultado_clientes:
            lv.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f"Nome: {cliente.nome}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Detalhes",on_click=lambda _, c=cliente: detalhe_cliente(c.nome,c.cpf,c.telefone,c.endereco)),
                        ]
                    )
                )
            )

    def salvar_cadastro_cliente(e):
        if input_nome_cliente.value == '' or input_cpf.value == '' or input_telefone.value == '' or input_endereco.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            cpf = input_cpf.value
            telefone = input_telefone.value

            if not cpf.isnumeric() or not telefone.isnumeric():
                input_cpf.error = True
                input_telefone.error_text = "Apenas números"
                page.update()
                return

            informacoes_clientes = Cliente(
                nome_cliente=input_nome_cliente.value,
                cpf=input_cpf.value,
                telefone=input_telefone.value,
                endereco=input_endereco.value,
            )
            informacoes_clientes.save()
            input_nome_cliente.value = ''
            input_cpf.value = ''
            input_telefone.value = ''
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True

            page.update()


    def voltar(e):
        print("Views", page.views)
        removida = page.views.pop()
        print(removida)
        top_view = page.views[-1]
        print(top_view)
        page.go(top_view.route)

    input_nome_cliente = ft.TextField(
        bgcolor='#f1ecd1',
        color='#673c22',
        label="Digite o nome do cliente ",
        hint_text='Ex:Júlia Rafaela '
    )

    input_cpf = ft.TextField(
        bgcolor='#f1ecd1',
        color='#673c22',
        label="Digite o cpf do cliente ",
        hint_text='Ex: 01234567890'
    )

    input_telefone = ft.TextField(
        bgcolor='#f1ecd1',
        color='#673c22',
        label="Digite o telefone do cliente ",
        hint_text='Ex: 00 123456789'
    )

    input_endereco = ft.TextField(
        bgcolor='#f1ecd1',
        color='#673c22',
        label="Digite o endereço do cliente ",
        hint_text='Ex: Rua macânica mater 123'
    )
    input_cliente_associado = ft.TextField(
        label="Digite o cliente associado do cliente: ",
        hint_text='Ex:'
    )
    input_marcaVeiculo = ft.TextField(
        label="Digite o marca do veículo ",
        hint_text='Ex:'
    )
    input_modeloVeiculo = ft.TextField(
        label="Digite o modelo do veiculo",
        hint_text='Ex:'
    )
    input_placaVeiculo = (ft.TextField(
        label="Digite a placa do veículo",
        hint_text='Ex:')
    )
    input_ano_fabricacao = ft.TextField(
        label="Digite o ano de fabricação",
        hint_text='Ex:'
    )
    input_veiculo_associado = ft.TextField(
        label="Digite o veiculo associado do cliente ",
        hint_text='Ex:'
    )
    input_data_abertura = ft.TextField(
        label="Digite o data abertura do carro na mecânica ",
        hint_text='Ex:'
    )
    input_descricao = ft.TextField(
        label="Digite a descrição do serviço",
        hint_text='Ex:'
    )
    input_status = ft.TextField(
        label="Digite o status do veiculo ",
        hint_text='Ex:'
    )
    input_valor_estimado = ft.TextField(
        label="Digite o valor estimado do veiculo ",
        hint_text='Ex:'
    )

    progress = ft.ProgressRing(visible=False)

    lv = ft.ListView(
        height=500
    )

    msg_sucesso = ft.SnackBar(
        content=ft.Text("Salvo com sucesso!"),
        bgcolor=Colors.GREEN
    )

    msg_error = ft.SnackBar(
        content=ft.Text("Não pode estar vazio!"),
        bgcolor=Colors.RED
    )

    input_cpf = ft.TextField(
        label="CPF",
        hint_text="Ex: 12345678910"
    )

    btn_consultar_cliente = ft.FilledButton(
        text="Consultar lista de clientes",
        width=page.window.width,
        on_click=lambda _: mostrar_listaCliente()
    )

    txt_nome_cliente = ft.Text(size=16)
    lbl_nome_cliente = ft.Text(value="Nome cliente:", size=18, weight=FontWeight.BOLD)
    txt_cpf = ft.Text(size=16)
    lbl_cpf = ft.Text(value="CPF:", size=18, weight=FontWeight.BOLD)
    txt_telefone = ft.Text(size=16)
    lbl_telefone = ft.Text(value="Telefone:", size=18, weight=FontWeight.BOLD)
    txt_endereco = ft.Text(size=16)
    lbl_endereco = ft.Text(value="Endereço:", size=18, weight=FontWeight.BOLD)

    txt_cliente_associado = ft.Text(size=16)
    lbl_cliente_associado = ft.Text(value="Cliente associado:", size=18, weight=FontWeight.BOLD)
    txt_marcaVeiculo = ft.Text(size=16)
    lbl_marcaVeiculo = ft.Text(value="Marca do veiculo:", size=18, weight=FontWeight.BOLD)
    txt_modeloVeiculo = ft.Text(size=16)
    lbl_modeloVeiculo = ft.Text(value="Modelo do veiculo:", size=18, weight=FontWeight.BOLD)
    txt_placaVeiculo = ft.Text(size=16)
    lbl_placaVeiculo = ft.Text(value="Placa do veiculo:", size=18, weight=FontWeight.BOLD)
    txt_ano_fabriacacao = ft.Text(size=16)
    lbl_ano_fabricacao = ft.Text(value="Anod e fabricação:", size=18, weight=FontWeight.BOLD)



    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)