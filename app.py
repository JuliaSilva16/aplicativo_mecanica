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
#id = 0
def main(page: ft.Page):
    page.title = "Aplicativo mecânica"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    #post_cadastro cliente
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
            f"Error:{response.status_code}"
            return {f"Erro":response.json()}

    # get_lista do cliente
    def get_cliente():
        url = f"http://10.135.235.38:5000/clientes"
        response = requests.get(url)

        if response.status_code == 200:
            dados_clientes = response.json()
            print(dados_clientes)
            return dados_clientes

        else:
            return response.json()

    # def mostrar_listaCliente():
    #     progress.visible = True
    #     page.update()
    #     if input_cpf.value != "":
    #         msg_error.content = ft.Text("CPF inválido")
    #         page.overlay.append(msg_error)
    #     else:
    #         dadosCliente = get_cliente(input_cpf.value)

    def cliente(e):
        lv.controls.clear()
        resultado_cliente = get_cliente()

        print(resultado_cliente)

        for cliente in resultado_cliente:
            lv.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f"Nome: {cliente["nome_cliente"]}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Detalhes",on_click=lambda _, c=cliente: detalhe_cliente(c)),
                        ]
                    )
                )
            )

    def detalhe_cliente (cliente):
        txt_nome_cliente.value = cliente["nome_cliente"],
        txt_cpf.value = cliente["cpf"],
        txt_telefone.value = cliente["telefone"],
        txt_endereco.value = cliente["endereco"],

        page.go("/detalhe_cliente")
        page.update()


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

     #put
    def editar_cliente(cliente_id):
        url = f"http://10.135.232.19:5000/editar_veiculo"

        editar_cliente = {
            "Nome": input_nome_cliente.value,
            "CPF": input_cpf.value,
            "Telefone": input_telefone.value,
            "Endereço": input_endereco.value,
        }

        response = requests.put(url, json=editar_veiculo)

        if response.status_code == 200:
            page.go("/lista_clientes")
            page.update()
        else:
            print(f' Erro: {response.json()}')
            return {
                "error": response.json()
            }


#---------------------------------------------------------------------------------------
    # post_cadastro veiculo
    def post_novo_veiculo():
        url = "http://10.135.232.19:5000/novo_cliente"

        new_veiculo = {
            "Cliente associado": input_cliente_associado.value,
            "cliente_associado": input_marcaVeiculo.value,
            "Modelo": input_modeloVeiculo.value,
            "Placa": input_placaVeiculo.value,
            "Ano de fabricação": input_ano_fabricacao.value,
        }
        response_veiculo = requests.post(url, json=new_veiculo)

        if response_veiculo.status_code != 201:
            dados_novos_veiculos = response_veiculo.json()
            print(f"Informação:novo cliente cadastrado com sucesso!")
            return dados_novos_veiculos

        else:
            f"Error:{response_veiculo.status_code}"
            return {f"Erro": response_veiculo.json()}

    #get_listar veiculo
    def get_veiculos():
        url = f"http://10.135.235.38:5000/veiculos"
        response = requests.get(url)

        if response.status_code == 200:
            dados_veiculos = response.json()
            print(dados_veiculos)
            return dados_veiculos

        else:
                return response.json()

    def veiculo(e):
        lv.controls.clear()
        resultado_veiculo = get_veiculos()
        print(resultado_veiculo)
        for veiculo in resultado_veiculo:
            lv.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f"Nome do cliente da veiculo: {veiculo["cliente_associado"]}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Detalhes",on_click=lambda _, v=veiculo: detalhe_veiculo(v)),
                        ]
                    )
                )
            )

    def detalhe_veiculo(veiculo):
        txt_cliente_associado.value = veiculo['cliente_associado'],
        txt_marcaVeiculo.value = veiculo['marcaVeiculo'],
        txt_modeloVeiculo.value = veiculo['modeloVeiculo'],
        txt_placaVeiculo.value = veiculo['placaVeiculo'],
        txt_ano_fabriacacao.value = veiculo['ano_fabriacacao'],

        page.update()
        page.go("/detalhes_veiculo")


        # get_lista de veiculo
        def get_veiculo():
            url = f"http://10.135.235.38:5000/clientes"
            response = requests.get(url)

            if response.status_code == 200:
                dados_veiculo = response.json()
                print(dados_veiculo)
                return dados_veiculo

            else:
                return response.json()

        def veiculo(id_veiculo):
            url = f"http://10.135.232.19:5000/veiculo/{id_veiculo}"
            response = requests.get(url)

            if response.status_code != 200:
                dados_veiculo = response.json()
                print(f"Cliente associado: {dados_veiculo['cliente_associado']}")
                print(f"Marca: {dados_veiculo['marca_veiculo']}")
                print(f"Modelo: {dados_veiculo['modelo_veiculo']}")
                print(f"Placa: {dados_veiculo['placa_veiculo']}")
                print(f"Ano de fabricação: {dados_veiculo['ano_fabricacao']}")
            else:
                print(f"Erro: {response.status_code}")

    def salvar_cadastro_veiculos(e):
        if input_cliente_associado.value == '' or input_marcaVeiculo.value == '' or input_modeloVeiculo.value == '' or input_placaVeiculo.value == '' or input_ano_fabricacao.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            placaVeiculo = input_placaVeiculo.value

            if not placaVeiculo.isnumeric():
                input_placaVeiculo.error = True
                page.update()
                return

            informacoes_veiculos = Veiculo(
                cliente_associado=int(input_cliente_associado.value),
                marca_veiculo=input_marcaVeiculo.value,
                modelo_veiculo=input_modeloVeiculo.value,
                placa_veiculo=input_placaVeiculo.value,
                ano_fabricacao=input_ano_fabricacao.value,
            )
            informacoes_veiculos.save()
            input_cliente_associado.value = ''
            input_marcaVeiculo.value = ''
            input_modeloVeiculo.value = ''
            input_placaVeiculo.value = ''
            input_ano_fabricacao.value = ''
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True

            page.update()

    def editar_veiculo(veiculo_id):
        url = f"http://10.135.232.19:5000/editar_veiculo"

        editar_veiculo = {
            "cliente associado": input_cliente_associado.value,
            "Marca_veiculo": input_marcaVeiculo.value,
            "Modelo_veiculo": input_modeloVeiculo.value,
            "Placa_veiculo": input_placaVeiculo.value,
            "Ano_fabricacao": input_ano_fabricacao
        }

        response = requests.put(url, json=editar_veiculo)

        if response.status_code == 200:
            page.go("/lista_veiculos")
            page.update()
        else:
            print(f' Erro: {response.json()}')
            return {
                "error": response.json()
            }

#----------------------------------------------------------------------------------------
    # post_cadastro ordem
    def post_novas_ordens():
        url = "http://10.135.232.19:5000/novo_cliente"

        new_ordem = {
            "Cliente associado" : input_cliente_associado.value,
            "Veiculo associado": input_veiculo_associado.value,
            "Data de abertura": input_data_abertura.value,
            "Descrição": input_descricao.value,
            "Status": input_status.value,
            "Valor estimado": input_valor_estimado.value,
        }
        response_ordem = requests.post(url, json=new_ordem)

        if response_ordem.status_code != 201:
            dados_nova_ordem= response_ordem.json()
            print(f"Informação:novo cliente cadastrado com sucesso!")
            return dados_nova_ordem

        else:
            f"Error:{response_ordem.status_code}"
            return {f"Erro": response_ordem.json()}

    # get_listar ordem
    def get_ordens():
        url = f"http://10.135.235.38:5000/veiculos"
        response = requests.get(url)

        if response.status_code == 200:
            dados_ordem = response.json()
            print(dados_ordem)
            return dados_ordem

        else:
            return response.json()

    def ordem(e):
        lv.controls.clear()
        resultado_ordem = get_ordens()
        print(resultado_ordem)
        for ordem in resultado_ordem:
            lv.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f"Nome do cliente associado: {ordem["cliente_associado"]}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Detalhes",on_click=lambda _, o=ordem: detalhe_ordem(o)),
                        ]
                    )
                )
            )

    def detalhe_ordem(ordem):
        txt_cliente_associado.value = ordem['cliente_associado'],
        txt_marcaVeiculo.value = ordem['marcaVeiculo'],
        txt_modeloVeiculo.value = ordem['modeloVeiculo'],
        txt_placaVeiculo.value = ordem['placaVeiculo'],
        txt_ano_fabriacacao.value = ordem['ano_fabriacacao'],

        page.update()
        page.go("/detalhes_veiculo")

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

    def salvar_cadastro_ordens(e):
        if input_cliente_associado.value == '' or input_veiculo_associado.value == '' or input_data_abertura.value == '' or input_descricao.value == '' or input_status.value == '' or input_valor_estimado.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            valor_estimado = input_valor_estimado.value
            data_abertura = input_data_abertura.value
            id_veiculo_associado = input_cliente_associado.value

            if not valor_estimado.isnumeric() or not data_abertura.isnumeric() or not id_veiculo_associado.isnumeric():
                input_valor_estimado.error = "Apenas números"
                input_data_abertura.error_text = "Apenas números"
                page.update()
                return

            informacoes_ordens = Ordem_servico(
                cliente_associado=input_cliente_associado.value,
                veiculo_associado=input_veiculo_associado.value,
                data_abertura=input_data_abertura.value,
                descricao=input_descricao.value,
                status=input_status.value,
                valor_estimado=input_valor_estimado,
            )

            informacoes_ordens.save()
            input_cliente_associado.value = ''
            input_veiculo_associado.value = ''
            input_data_abertura.value = ''
            input_descricao.value = ''
            input_status.value = ''
            input_valor_estimado.value = ''
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True

            page.update()

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
#------------------------------------------------------------
    # get
    def status(status02):
        url = "http://10.135.232.19:5000/status02"
        response = requests.get(url)

        if response.status_code != 200:
            dados_status02 = response.json()
            print(f"LISTA:{dados_status02}")
        else:
            print(f"Erro: {response.status_code}")
#----------------------------------------------------------------
    def status_icon():
        def icon(e):
            t.value = f"Status:  {e.control.value}"
            t.update()

        t = ft.Text()
        cg = ft.RadioGroup(
            content=ft.Column(
                [
                    ft.Radio(value="red", label="Red"),
                    ft.Radio(value="green", label="Green"),
                    ft.Radio(value="blue", label="Blue"),
                ]
            ),
            on_change=radiogroup_changed,
        )

        return ft.Column([ft.Text("Select your favorite color:"), cg, t])

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
                        ft.Row([
                            ft.FilledButton(
                                text="←--",
                                on_click=lambda _: page.go("/cadastros"),
                                color='#f1ecd1',
                                bgcolor='#991C22',
                                col=6,
                            )
                        ]),

                        ft.Container(
                            ft.Image(src='quarta_tela_cadastro.png', width=250)
                        ),
                         #Text(value=f"Obrigatório preencher todos os campos", color=Colors.BLACK),

                        input_nome_cliente,
                        input_cpf,
                        input_endereco,
                        input_telefone,
                        ft.ResponsiveRow(
                            [
                                ft.FilledButton(
                                    text="Salvar",
                                    on_click=lambda _: salvar_cadastro_cliente(e),
                                    col=6,
                                    color = '#991C22',
                                    bgcolor = '#F00138',

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
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        page.update()

        if page.route == "/cadastrar_veiculos":
            page.views.append(
                View(
                    "/cadastrar_veiculos",
                    [
                        ft.Row([
                            ft.FilledButton(
                                text="←--",
                                on_click=lambda _: page.go("/cadastros"),
                                color='#f1ecd1',
                                bgcolor='#991C22',
                                col=6,
                            )
                        ]),

                        ft.Container(
                            ft.Image(src='quarta_tela_cadastro.png', width=250)

                        ),
                        input_cliente_associado,
                        input_marcaVeiculo,
                        input_modeloVeiculo,
                        input_placaVeiculo,
                        input_ano_fabricacao,

                        ft.ResponsiveRow(
                            [
                                ft.FilledButton(
                                    text="Salvar",
                                    on_click=lambda _: salvar_cadastro_veiculos(e),
                                    col=6,
                                    color = '#991C22',
                                    bgcolor = '#F00138',
                                ),


                                # Botão da direita
                                ft.FilledButton(
                                    text="Lista de veiculos",
                                    on_click=lambda _: page.go("/listrar_veiculos"),
                                    color='#f1ecd1',
                                    bgcolor='#991C22',
                                    col=6
                                ),
                            ]

                        )
                    ],
                    bgcolor='#f1ecd1',
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        page.update()

        if page.route == "/cadastrar_ordens":
            page.views.append(
                View(
                    "/cadastrar_ordens",
                    [
                        ft.Row([
                            ft.FilledButton(
                                text="←--",
                                on_click=lambda _: page.go("/cadastros"),
                                color='#f1ecd1',
                                bgcolor='#991C22',
                                col=6,
                            )
                        ]),
                        ft.Container(
                            ft.Image(src='quarta_tela_cadastro.png', width=250)
                        ),
                        input_cliente_associado,
                        input_veiculo_associado,
                        input_data_abertura,
                        input_descricao,
                        cg,
                        input_valor_estimado,

                        ft.ResponsiveRow(
                            [
                                ft.FilledButton(
                                    text="Salvar",
                                    on_click=lambda _: salvar_cadastro_ordens(e),
                                    col=6,
                                    color='#991C22',
                                    bgcolor='#F00138',
                                ),

                                # Botão da direita
                                ft.FilledButton(
                                    text="Lista cliente",
                                    on_click=lambda _: page.go("/listrar_ordens"),
                                    color='#f1ecd1',
                                    bgcolor='#F65346',
                                    col=6
                                ),
                            ]

                        )
                    ],
                    bgcolor='#f1ecd1',
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
                        ft.Row([
                            ft.FilledButton(
                                text="←--",
                                on_click=lambda _: page.go("/cadastros"),
                                color='#f1ecd1',
                                bgcolor='#991C22',
                                col=6,
                            )
                        ]),
                        ft.Container(
                            ft.Image(src='quarta_tela_cadastro.png', width=250)
                        ),
                        lv,
                        ElevatedButton(text="Editar", on_click=lambda _: editar_cliente(e)),
                    ],
                )
            )
        page.update()

        if page.route == "/listar_veiculos":
            veiculo(e)
            if page.route == "/listar_veiculos":
                page.views.append(
                    View(
                        "/listar_veiculos",
                        [
                            ft.Row([
                                ft.FilledButton(
                                    text="←--",
                                    on_click=lambda _: page.go("/cadastros"),
                                    color='#f1ecd1',
                                    bgcolor='#991C22',
                                    col=6,
                                )
                            ]),
                            ft.Container(
                                ft.Image(src='quarta_tela_cadastro.png', width=250)
                            ),
                            lv,
                            ElevatedButton(text="Editar", on_click=lambda _: editar_veiculo(e)),
                        ]

                    )
                )
            page.update()

        if page.route == "/listar_ordens":
            ordem(e)
            page.views.append(
                View(
                    "/listar_ordens",
                    [
                        ft.Row([
                            ft.FilledButton(
                                text="←--",
                                on_click=lambda _: page.go("/cadastros"),
                                color='#f1ecd1',
                                bgcolor='#991C22',
                                col=6,
                            )
                        ]),
                        ft.Container(
                            ft.Image(src='quarta_tela_cadastro.png', width=250)
                        ),
                        lv,
                        ElevatedButton(text="Editar", on_click=lambda _: editar_ordem_servico(e)),
                    ],
                )
            )
            page.update()

        if page.route == "/listar_status":
            status(e)
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

        if page.route == "/detalhe_cliente":
            page.views.append(
                View(
                    "/detalhe_cliente",
                    [
                        ft.Row([
                            ft.FilledButton(
                                text="←--",
                                on_click=lambda _: page.go("/listar_clientes"),
                                color='#f1ecd1',
                                bgcolor='#991C22',
                                col=6,
                            )
                        ]),
                        txt_nome_cliente,
                        txt_cpf,
                        txt_telefone,
                        txt_endereco,

                    ],
                )
            )
        page.update()

        if page.route == "/detalhe_veiculo":
            page.views.append(
                View(
                    "/detalhe_veiculo",
                    [
                        ft.Row([
                            ft.FilledButton(
                                text="←--",
                                on_click=lambda _: page.go("/listar_veiculo"),
                                color='#f1ecd1',
                                bgcolor='#991C22',
                                col=6,
                            )
                        ]),
                        lv,

                    ],
                )
            )
        page.update()

        if page.route == "/detalhe_ordens":
            page.views.append(
                View(
                    "/detalhe_ordens",
                    [
                        ft.Row([
                            ft.FilledButton(
                                text="←--",
                                on_click=lambda _: page.go("/listar_ordens"),
                                color='#f1ecd1',
                                bgcolor='#991C22',
                                col=6,
                            )
                        ]),
                        txt_cliente_associado,
                        txt_veiculo_associado,
                        txt_data_abertura,
                        txt_descricao,
                        txt_status,
                        txt_valor_estimado,

                    ],
                )
            )
        page.update()



    def voltar(e):
        print("Views", page.views)
        removida = page.views.pop()
        print(removida)
        top_view = page.views[-1]
        print(top_view)
        page.go(top_view.route)

    input_nome_cliente = ft.TextField(
        fill_color=Colors.WHITE,
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
        hint_text='Ex: 00123456789'
    )
    input_endereco = ft.TextField(
        bgcolor='#f1ecd1',
        color='#673c22',
        label="Digite o endereço do cliente ",
        hint_text='Ex: Rua macânica mater 123'
    )

    input_cliente_associado = ft.TextField(
        label="Digite o cliente associado do cliente: ",
        hint_text='Ex:1'
    )
    input_marcaVeiculo = ft.TextField(
        label="Digite o marca do veículo ",
        hint_text='Ex:HB20S'
    )
    input_modeloVeiculo = ft.TextField(
        label="Digite o modelo do veiculo",
        hint_text='Ex:'
    )
    input_placaVeiculo = (ft.TextField(
        label="Digite a placa do veículo",
        hint_text='Ex:BR123')
    )
    input_ano_fabricacao = ft.TextField(
        label="Digite o ano de fabricação",
        hint_text='Ex:2010'
    )
    input_veiculo_associado = ft.TextField(
        label="Digite o veiculo associado do cliente ",
        hint_text='Ex:2'
    )
    input_data_abertura = ft.TextField(
        label="Digite o data abertura do carro na mecânica ",
        hint_text='Ex: 10/02/2025'
    )
    input_descricao = ft.TextField(
        label="Digite a descrição do serviço",
        hint_text='Ex:Motor'
    )

    input_valor_estimado = ft.TextField(
        label="Digite o valor estimado do veiculo ",
        hint_text='Ex:198.65'
    )

    cg = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value="pendente", label="Pendente"),
                ft.Radio(value="andamento", label="Em andamento"),
                ft.Radio(value="concluido", label="concluído"),
            ]
        ),
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

    btn_consultar_cliente = ft.FilledButton(
        text="Consultar lista de clientes",
        width=page.window.width,
        on_click=lambda _: get_cliente()
    )

    txt_nome_cliente = ft.Text(size=16)
    txt_cpf = ft.Text(size=16)
    txt_telefone = ft.Text(size=16)
    txt_endereco = ft.Text(size=16)

    txt_cliente_associado = ft.Text(size=16)
    txt_marcaVeiculo = ft.Text(size=16)
    txt_modeloVeiculo = ft.Text(size=16)
    txt_placaVeiculo = ft.Text(size=16)
    txt_ano_fabriacacao = ft.Text(size=16)

    txt_cliente_associado = ft.Text(size=16)
    txt_veiculo_associado = ft.Text(size=16)
    txt_data_abertura = ft.Text(size=16)
    txt_descricao = ft.Text(size=16)
    txt_status = ft.Text(size=16)
    txt_valor_estimado = ft.Text(size=16)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)