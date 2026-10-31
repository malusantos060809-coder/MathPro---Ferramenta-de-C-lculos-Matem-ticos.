import math


def ler_float(mensagem, positivo=False, estritamente_positivo=False):
    """Lê e valida um número decimal (float) informado pelo usuário."""
    while True:
        try:
            entrada = input(mensagem).replace(",", ".").strip()
            valor = float(entrada)
            if estritamente_positivo and valor <= 0:
                print(">> Erro: O valor deve ser estritamente maior que zero.")
                continue
            if positivo and valor < 0:
                print(">> Erro: O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print(">> Erro: Entrada inválida. Digite um número válido.")


def ler_inteiro(mensagem, positivo=False, estritamente_positivo=False):
    """Lê e valida um número inteiro informado pelo usuário."""
    while True:
        try:
            entrada = input(mensagem).strip()
            valor = int(entrada)
            if estritamente_positivo and valor <= 0:
                print(">> Erro: O valor deve ser estritamente maior que zero.")
                continue
            if positivo and valor < 0:
                print(">> Erro: O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print(">> Erro: Entrada inválida. Digite um número inteiro.")


def pausar():
    """Pausa a execução até o usuário pressionar Enter."""
    input("\nPressione [Enter] para continuar...")


# ==============================================================================
# 1. OPERAÇÕES BÁSICAS
# ==============================================================================

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b


def menu_operacoes_basicas():
    while True:
        print("\n" + "=" * 45)
        print("          OPERAÇÕES BÁSICAS")
        print("=" * 45)
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("0. Voltar ao Menu Principal")
        print("=" * 45)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break
        elif opcao in ["1", "2", "3", "4"]:
            num1 = ler_float("Informe o primeiro número: ")
            num2 = ler_float("Informe o segundo número: ")

            if opcao == "1":
                resultado = somar(num1, num2)
                print(f"\nResultado: {num1:.2f} + {num2:.2f} = {resultado:.2f}")
            elif opcao == "2":
                resultado = subtrair(num1, num2)
                print(f"\nResultado: {num1:.2f} - {num2:.2f} = {resultado:.2f}")
            elif opcao == "3":
                resultado = multiplicar(num1, num2)
                print(f"\nResultado: {num1:.2f} * {num2:.2f} = {resultado:.2f}")
            elif opcao == "4":
                try:
                    resultado = dividir(num1, num2)
                    print(f"\nResultado: {num1:.2f} / {num2:.2f} = {resultado:.2f}")
                except ZeroDivisionError as erro:
                    print(f"\n>> Erro matemático: {erro}")
            pausar()
        else:
            print(">> Opção inválida. Tente novamente.")


# ==============================================================================
# 2. PORCENTAGEM
# ==============================================================================

def calcular_porcentagem_de_valor(porcentagem, valor):
    return (porcentagem / 100) * valor


def calcular_quanto_porcento_representa(parte, total):
    if total == 0:
        raise ZeroDivisionError("O total de referência não pode ser zero.")
    return (parte / total) * 100


def aplicar_aumento_porcentagem(valor, porcentagem):
    return valor * (1 + (porcentagem / 100))


def aplicar_desconto_porcentagem(valor, porcentagem):
    return valor * (1 - (porcentagem / 100))


def menu_porcentagem():
    while True:
        print("\n" + "=" * 45)
        print("             PORCENTAGEM")
        print("=" * 45)
        print("1. Calcular a porcentagem de um valor (ex: X% de Y)")
        print("2. Descobrir quantos % um número representa de outro")
        print("3. Aumentar um valor em determinada porcentagem")
        print("4. Diminuir um valor em determinada porcentagem")
        print("0. Voltar ao Menu Principal")
        print("=" * 45)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break
        elif opcao == "1":
            p = ler_float("Informe a porcentagem (%): ")
            v = ler_float("Informe o valor total: ")
            resultado = calcular_porcentagem_de_valor(p, v)
            print(f"\nResultado: {p:.2f}% de {v:.2f} = {resultado:.2f}")
            pausar()
        elif opcao == "2":
            parte = ler_float("Informe a parte: ")
            total = ler_float("Informe o total de referência: ")
            try:
                resultado = calcular_quanto_porcento_representa(parte, total)
                print(f"\nResultado: {parte:.2f} representa {resultado:.2f}% de {total:.2f}")
            except ZeroDivisionError as erro:
                print(f"\n>> Erro matemático: {erro}")
            pausar()
        elif opcao == "3":
            v = ler_float("Informe o valor inicial: ", positivo=True)
            p = ler_float("Informe a porcentagem de aumento (%): ", positivo=True)
            resultado = aplicar_aumento_porcentagem(v, p)
            diferenca = resultado - v
            print(f"\nAumento: +{diferenca:.2f}")
            print(f"Valor final com aumento de {p:.2f}%: {resultado:.2f}")
            pausar()
        elif opcao == "4":
            v = ler_float("Informe o valor inicial: ", positivo=True)
            p = ler_float("Informe a porcentagem de desconto (%): ", positivo=True)
            resultado = aplicar_desconto_porcentagem(v, p)
            diferenca = v - resultado
            print(f"\nDesconto: -{diferenca:.2f}")
            print(f"Valor final com desconto de {p:.2f}%: {resultado:.2f}")
            pausar()
        else:
            print(">> Opção inválida. Tente novamente.")


# ==============================================================================
# 3. ESCALA E CONVERSÃO DE MEDIDAS
# ==============================================================================

FATORES_PARA_METROS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0
}


def converter_unidade(valor, unidade_origem, unidade_destino):
    if unidade_origem not in FATORES_PARA_METROS or unidade_destino not in FATORES_PARA_METROS:
        raise ValueError("Unidade de medida inválida.")
    valor_em_metros = valor * FATORES_PARA_METROS[unidade_origem]
    return valor_em_metros / FATORES_PARA_METROS[unidade_destino]


def escolher_unidade(mensagem):
    while True:
        print(mensagem)
        print("Opções disponíveis: mm, cm, m, km")
        unidade = input("Digite a unidade: ").strip().lower()
        if unidade in FATORES_PARA_METROS:
            return unidade
        print(">> Unidade não reconhecida. Use mm, cm, m ou km.")


def obter_fator_escala():
    while True:
        print("\nEscolha a escala desejada:")
        print("1. 1:50")
        print("2. 1:100")
        print("3. 1:1000")
        print("4. Outra escala personalizada (1:N)")
        opcao = input("Opção: ").strip()
        if opcao == "1":
            return 50.0
        elif opcao == "2":
            return 100.0
        elif opcao == "3":
            return 1000.0
        elif opcao == "4":
            return ler_float("Informe o valor de N para a escala 1:N: ", estritamente_positivo=True)
        else:
            print(">> Opção inválida.")


def menu_escala():
    while True:
        print("\n" + "=" * 45)
        print("         ESCALA E CONVERSÃO")
        print("=" * 45)
        print("1. Converter Medida Real -> Medida no Desenho/Maquete")
        print("2. Converter Medida no Desenho/Maquete -> Medida Real")
        print("3. Conversor de Unidades (mm, cm, m, km)")
        print("0. Voltar ao Menu Principal")
        print("=" * 45)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break
        elif opcao == "1":
            escala = obter_fator_escala()
            unidade_real = escolher_unidade("\nUnidade da medida real:")
            medida_real = ler_float("Informe o valor da medida real: ", estritamente_positivo=True)
            unidade_desenho = escolher_unidade("\nUnidade desejada para o desenho:")

            # D = R / N (ambos na mesma unidade)
            medida_desenho_mesma_unidade = medida_real / escala
            medida_final = converter_unidade(medida_desenho_mesma_unidade, unidade_real, unidade_desenho)

            print(f"\n--- Resultado da Escala 1:{int(escala) if escala.is_integer() else escala:.2f} ---")
            print(f"Medida Real: {medida_real:.2f} {unidade_real}")
            print(f"Medida no Desenho: {medida_final:.4f} {unidade_desenho} ({medida_final:.2f} {unidade_desenho})")
            pausar()
        elif opcao == "2":
            escala = obter_fator_escala()
            unidade_desenho = escolher_unidade("\nUnidade da medida no desenho:")
            medida_desenho = ler_float("Informe o valor da medida no desenho: ", estritamente_positivo=True)
            unidade_real = escolher_unidade("\nUnidade desejada para a medida real:")

            # R = D * N (ambos na mesma unidade)
            medida_real_mesma_unidade = medida_desenho * escala
            medida_final = converter_unidade(medida_real_mesma_unidade, unidade_desenho, unidade_real)

            print(f"\n--- Resultado da Escala 1:{int(escala) if escala.is_integer() else escala:.2f} ---")
            print(f"Medida no Desenho: {medida_desenho:.2f} {unidade_desenho}")
            print(f"Medida Real: {medida_final:.4f} {unidade_real} ({medida_final:.2f} {unidade_real})")
            pausar()
        elif opcao == "3":
            origem = escolher_unidade("\nUnidade de origem:")
            destino = escolher_unidade("Unidade de destino:")
            valor = ler_float(f"Informe o valor em {origem}: ", positivo=True)
            convertido = converter_unidade(valor, origem, destino)
            print(f"\nResultado: {valor:.4f} {origem} = {convertido:.4f} {destino}")
            pausar()
        else:
            print(">> Opção inválida. Tente novamente.")


# ==============================================================================
# 4. PROBABILIDADE
# ==============================================================================

def calcular_probabilidade(casos_favoraveis, casos_possiveis):
    if casos_possiveis <= 0:
        raise ValueError("O número de casos possíveis deve ser estritamente maior que zero.")
    if casos_favoraveis < 0:
        raise ValueError("O número de casos favoráveis não pode ser negativo.")
    if casos_favoraveis > casos_possiveis:
        raise ValueError("O número de casos favoráveis não pode exceder o total de casos possíveis.")
    
    decimal = casos_favoraveis / casos_possiveis
    porcentagem = decimal * 100
    return decimal, porcentagem


def menu_probabilidade():
    while True:
        print("\n" + "=" * 45)
        print("            PROBABILIDADE SIMPLES")
        print("               P(A) = n(A) / n(S)")
        print("=" * 45)
        print("1. Calcular Probabilidade de um Evento")
        print("0. Voltar ao Menu Principal")
        print("=" * 45)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break
        elif opcao == "1":
            favoraveis = ler_inteiro("Informe o número de casos favoráveis: ", positivo=True)
            possiveis = ler_inteiro("Informe o número total de casos possíveis: ", estritamente_positivo=True)

            try:
                decimal, porcentagem = calcular_probabilidade(favoraveis, possiveis)
                print("\n" + "-" * 35)
                print("       RESULTADO DA PROBABILIDADE")
                print("-" * 35)
                print(f"Fórmula: P(A) = {favoraveis} / {possiveis}")
                print(f"Formato Decimal:     {decimal:.4f} ({decimal:.2f})")
                print(f"Formato Percentual:  {porcentagem:.2f}%")
                print("-" * 35)
            except ValueError as erro:
                print(f"\n>> Erro de validação: {erro}")
            pausar()
        else:
            print(">> Opção inválida. Tente novamente.")


# ==============================================================================
# 5. REGRA DE TRÊS
# ==============================================================================

def regra_de_tres_direta(a, b, c):
    """
    Grandezas diretamente proporcionais:
    A  --->  B
    C  --->  X
    A * X = B * C  ==>  X = (B * C) / A
    """
    if a == 0:
        raise ZeroDivisionError("O valor A não pode ser zero na proporção direta.")
    x = (b * c) / a
    explicacao = (
        f"\nCálculo da Regra de Três Direta:\n"
        f"  Grandeza 1   |   Grandeza 2\n"
        f"      {a:.2f}     --->     {b:.2f}\n"
        f"      {c:.2f}     --->      X\n"
        f"\nEquação: {a:.2f} * X = {b:.2f} * {c:.2f}\n"
        f"X = ({b:.2f} * {c:.2f}) / {a:.2f}\n"
        f"X = {x:.2f}"
    )
    return x, explicacao


def regra_de_tres_inversa(a, b, c):
    """
    Grandezas inversamente proporcionais:
    A  --->  B
    C  --->  X
    C * X = A * B  ==>  X = (A * B) / C
    """
    if c == 0:
        raise ZeroDivisionError("O valor C não pode ser zero na proporção inversa.")
    x = (a * b) / c
    explicacao = (
        f"\nCálculo da Regra de Três Inversa:\n"
        f"  Grandeza 1   |   Grandeza 2\n"
        f"      {a:.2f}     --->     {b:.2f}\n"
        f"      {c:.2f}     --->      X\n"
        f"\nEquação (inversa): {c:.2f} * X = {a:.2f} * {b:.2f}\n"
        f"X = ({a:.2f} * {b:.2f}) / {c:.2f}\n"
        f"X = {x:.2f}"
    )
    return x, explicacao


def menu_regra_de_tres():
    while True:
        print("\n" + "=" * 45)
        print("             REGRA DE TRÊS SIMPLES")
        print("=" * 45)
        print("1. Regra de Três Direta (quando uma grandeza sobe, a outra sobe)")
        print("2. Regra de Três Inversa (quando uma grandeza sobe, a outra desce)")
        print("0. Voltar ao Menu Principal")
        print("=" * 45)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break
        elif opcao in ["1", "2"]:
            print("\nInforme os três valores conhecidos:")
            a = ler_float("Valor A (Grandeza 1 inicial): ")
            b = ler_float("Valor B (Grandeza 2 inicial): ")
            c = ler_float("Valor C (Grandeza 1 final): ")

            try:
                if opcao == "1":
                    resultado, explicacao = regra_de_tres_direta(a, b, c)
                else:
                    resultado, explicacao = regra_de_tres_inversa(a, b, c)

                print(explicacao)
                print(f"\n>> Valor encontrado para X: {resultado:.2f}")
            except ZeroDivisionError as erro:
                print(f"\n>> Erro matemático: {erro}")
            pausar()
        else:
            print(">> Opção inválida. Tente novamente.")


# ==============================================================================
# 6. GEOMETRIA PLANA
# ==============================================================================

def area_quadrado(lado):
    return lado ** 2


def perimetro_quadrado(lado):
    return 4 * lado


def area_retangulo(base, altura):
    return base * altura


def perimetro_retangulo(base, altura):
    return 2 * (base + altura)


def area_perimetro_triangulo(a, b, c):
    """Verifica desigualdade triangular e calcula área (Heron) e perímetro."""
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Os lados informados não formam um triângulo válido.")
    perimetro = a + b + c
    s = perimetro / 2.0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area, perimetro


def area_circulo(raio):
    return math.pi * (raio ** 2)


def perimetro_circulo(raio):
    return 2 * math.pi * raio


def area_perimetro_losango(diagonal_maior, diagonal_menor):
    area = (diagonal_maior * diagonal_menor) / 2
    lado = math.sqrt((diagonal_maior / 2) ** 2 + (diagonal_menor / 2) ** 2)
    perimetro = 4 * lado
    return area, perimetro, lado


def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2


def perimetro_trapezio(base_maior, base_menor, lado1, lado2):
    return base_maior + base_menor + lado1 + lado2


def menu_geometria_plana():
    while True:
        print("\n" + "=" * 45)
        print("          GEOMETRIA PLANA (ÁREA & PERÍMETRO)")
        print("=" * 45)
        print("1. Quadrado")
        print("2. Retângulo")
        print("3. Triângulo")
        print("4. Círculo")
        print("5. Losango")
        print("6. Trapézio")
        print("0. Voltar ao Menu Principal")
        print("=" * 45)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break
        elif opcao == "1":
            l = ler_float("Informe o lado do quadrado (cm/m): ", estritamente_positivo=True)
            print(f"\nÁrea do Quadrado: {area_quadrado(l):.2f} un²")
            print(f"Perímetro do Quadrado: {perimetro_quadrado(l):.2f} un")
            pausar()
        elif opcao == "2":
            b = ler_float("Informe a base do retângulo: ", estritamente_positivo=True)
            h = ler_float("Informe a altura do retângulo: ", estritamente_positivo=True)
            print(f"\nÁrea do Retângulo: {area_retangulo(b, h):.2f} un²")
            print(f"Perímetro do Retângulo: {perimetro_retangulo(b, h):.2f} un")
            pausar()
        elif opcao == "3":
            print("\nInforme os três lados do triângulo:")
            a = ler_float("Lado A: ", estritamente_positivo=True)
            b = ler_float("Lado B: ", estritamente_positivo=True)
            c = ler_float("Lado C: ", estritamente_positivo=True)
            try:
                area, perimetro = area_perimetro_triangulo(a, b, c)
                print(f"\nÁrea do Triângulo (Fórmula de Heron): {area:.2f} un²")
                print(f"Perímetro do Triângulo: {perimetro:.2f} un")
            except ValueError as erro:
                print(f"\n>> Erro geométrico: {erro}")
            pausar()
        elif opcao == "4":
            r = ler_float("Informe o raio do círculo: ", estritamente_positivo=True)
            print(f"\nÁrea do Círculo: {area_circulo(r):.2f} un²")
            print(f"Perímetro (Circunferência): {perimetro_circulo(r):.2f} un")
            pausar()
        elif opcao == "5":
            D = ler_float("Informe a Diagonal Maior (D): ", estritamente_positivo=True)
            d = ler_float("Informe a Diagonal Menor (d): ", estritamente_positivo=True)
            area, perimetro, lado = area_perimetro_losango(D, d)
            print(f"\nLado calculado: {lado:.2f} un")
            print(f"Área do Losango: {area:.2f} un²")
            print(f"Perímetro do Losango: {perimetro:.2f} un")
            pausar()
        elif opcao == "6":
            B = ler_float("Informe a Base Maior (B): ", estritamente_positivo=True)
            b = ler_float("Informe a Base Menor (b): ", estritamente_positivo=True)
            h = ler_float("Informe a Altura (h): ", estritamente_positivo=True)
            l1 = ler_float("Informe o lado lateral 1: ", estritamente_positivo=True)
            l2 = ler_float("Informe o lado lateral 2: ", estritamente_positivo=True)
            area = area_trapezio(B, b, h)
            perimetro = perimetro_trapezio(B, b, l1, l2)
            print(f"\nÁrea do Trapézio: {area:.2f} un²")
            print(f"Perímetro do Trapézio: {perimetro:.2f} un")
            pausar()
        else:
            print(">> Opção inválida. Tente novamente.")


# ==============================================================================
# 7. GEOMETRIA ESPACIAL
# ==============================================================================

def volume_area_cubo(aresta):
    volume = aresta ** 3
    area_total = 6 * (aresta ** 2)
    return volume, area_total


def volume_area_paralelepipedo(a, b, c):
    volume = a * b * c
    area_total = 2 * (a * b + a * c + b * c)
    return volume, area_total


def volume_area_cilindro(raio, altura):
    volume = math.pi * (raio ** 2) * altura
    area_total = 2 * math.pi * raio * (raio + altura)
    return volume, area_total


def volume_area_esfera(raio):
    volume = (4.0 / 3.0) * math.pi * (raio ** 3)
    area_total = 4 * math.pi * (raio ** 2)
    return volume, area_total


def volume_area_cone(raio, altura):
    geratriz = math.sqrt(raio ** 2 + altura ** 2)
    volume = (1.0 / 3.0) * math.pi * (raio ** 2) * altura
    area_total = math.pi * raio * (raio + geratriz)
    return volume, area_total, geratriz


def volume_area_piramide_quadrada(lado_base, altura):
    area_base = lado_base ** 2
    volume = (1.0 / 3.0) * area_base * altura
    apotema_piramide = math.sqrt(altura ** 2 + (lado_base / 2) ** 2)
    area_lateral = 4 * ((lado_base * apotema_piramide) / 2)
    area_total = area_base + area_lateral
    return volume, area_total, apotema_piramide


def menu_geometria_espacial():
    while True:
        print("\n" + "=" * 45)
        print("        GEOMETRIA ESPACIAL (VOLUME & ÁREA)")
        print("=" * 45)
        print("1. Cubo")
        print("2. Paralelepípedo")
        print("3. Cilindro")
        print("4. Esfera")
        print("5. Cone")
        print("6. Pirâmide de Base Quadrada")
        print("0. Voltar ao Menu Principal")
        print("=" * 45)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break
        elif opcao == "1":
            aresta = ler_float("Informe o comprimento da aresta: ", estritamente_positivo=True)
            vol, area = volume_area_cubo(aresta)
            print(f"\nVolume do Cubo: {vol:.2f} un³")
            print(f"Área Total do Cubo: {area:.2f} un²")
            pausar()
        elif opcao == "2":
            a = ler_float("Informe o comprimento (aresta a): ", estritamente_positivo=True)
            b = ler_float("Informe a largura (aresta b): ", estritamente_positivo=True)
            c = ler_float("Informe a altura (aresta c): ", estritamente_positivo=True)
            vol, area = volume_area_paralelepipedo(a, b, c)
            print(f"\nVolume do Paralelepípedo: {vol:.2f} un³")
            print(f"Área Total do Paralelepípedo: {area:.2f} un²")
            pausar()
        elif opcao == "3":
            r = ler_float("Informe o raio da base do cilindro: ", estritamente_positivo=True)
            h = ler_float("Informe a altura do cilindro: ", estritamente_positivo=True)
            vol, area = volume_area_cilindro(r, h)
            print(f"\nVolume do Cilindro: {vol:.2f} un³")
            print(f"Área Total do Cilindro: {area:.2f} un²")
            pausar()
        elif opcao == "4":
            r = ler_float("Informe o raio da esfera: ", estritamente_positivo=True)
            vol, area = volume_area_esfera(r)
            print(f"\nVolume da Esfera: {vol:.2f} un³")
            print(f"Área Superficial Total: {area:.2f} un²")
            pausar()
        elif opcao == "5":
            r = ler_float("Informe o raio da base do cone: ", estritamente_positivo=True)
            h = ler_float("Informe a altura do cone: ", estritamente_positivo=True)
            vol, area, g = volume_area_cone(r, h)
            print(f"\nGeratriz calculada: {g:.2f} un")
            print(f"Volume do Cone: {vol:.2f} un³")
            print(f"Área Total do Cone: {area:.2f} un²")
            pausar()
        elif opcao == "6":
            l = ler_float("Informe o lado da base quadrada: ", estritamente_positivo=True)
            h = ler_float("Informe a altura da pirâmide: ", estritamente_positivo=True)
            vol, area, apotema = volume_area_piramide_quadrada(l, h)
            print(f"\nApótema da pirâmide: {apotema:.2f} un")
            print(f"Volume da Pirâmide: {vol:.2f} un³")
            print(f"Área Total da Pirâmide: {area:.2f} un²")
            pausar()
        else:
            print(">> Opção inválida. Tente novamente.")


# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================

def menu_principal():
    while True:
        print("\n" + "=" * 50)
        print("        CALCULADORA AVANÇADA EM PYTHON")
        print("=" * 50)
        print("1. Operações Básicas (+, -, *, /)")
        print("2. Porcentagem")
        print("3. Escala e Conversão de Medidas")
        print("4. Probabilidade")
        print("5. Regra de Três (Direta e Inversa)")
        print("6. Geometria Plana (Área e Perímetro)")
        print("7. Geometria Espacial (Volume e Área Total)")
        print("0. Sair do Programa")
        print("=" * 50)

        opcao = input("Escolha uma categoria: ").strip()

        if opcao == "0":
            print("\nEncerrando a Calculadora. Até logo!")
            break
        elif opcao == "1":
            menu_operacoes_basicas()
        elif opcao == "2":
            menu_porcentagem()
        elif opcao == "3":
            menu_escala()
        elif opcao == "4":
            menu_probabilidade()
        elif opcao == "5":
            menu_regra_de_tres()
        elif opcao == "6":
            menu_geometria_plana()
        elif opcao == "7":
            menu_geometria_espacial()
        else:
            print(">> Opção inválida. Por favor, escolha um item do menu.")


if __name__ == "__main__":
    menu_principal()