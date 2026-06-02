# ============================================================
#   OrbitalWatch – Modelagem Matemática
#   Disciplina: Differentiated Problem Solving
#   Global Solution 2026 | FIAP | Engenharia de Software
#
#   Integrantes:
#   João Pedro Maschion da Cruz Sá – RM570509
#   Gustavo Rezende Louro – RM570708
#   João Pedro Lagonegro Bosco e Silva – RM569444
#   Lucas Henrique Alves da Silva – RM572216
# ============================================================

import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def crescimento_detritos(t):
    """
    Função Exponencial: modela o crescimento de detritos orbitais.

    D(t) = 28.000 * (1,07)^t

    Onde:
      D(t) = quantidade de detritos no ano t
      28.000 = quantidade inicial (base: dados NASA 2024)
      1,07   = taxa de crescimento de 7% ao ano
      t      = anos a partir de 2024

    Domínio: t >= 0 (anos futuros)
    Comportamento: crescente, pois base > 1
    """
    D0 = 28000       # detritos rastreados em 2024 (valor inicial)
    taxa = 1.07      # crescimento de 7% ao ano
    return D0 * (taxa ** t)


def probabilidade_colisao(d):
    """
    Função de 2º Grau: modela a probabilidade de colisão (%)
    em função da distância do detrito ao satélite (em km).

    P(d) = -0,004 * d² + 2 * d

    Onde:
      P(d) = probabilidade de colisão (%)
      d    = distância do detrito ao satélite (km)

    Vértice (ponto de máximo risco):
      d_v = -b / (2a) = -2 / (2 * -0,004) = 250 km
      P_v = 250% → normalizado para escala 0-100%

    Domínio relevante: 0 < d < 500 km
    Raízes: d = 0 e d = 500 (onde o risco é zero)
    Comportamento: parábola com concavidade negativa (a < 0)
                   risco máximo na distância de 250 km do cone de impacto
    """
    # Forma canônica com vértice em (250, 100):
    # P(d) = -(100/250²) · (d - 250)² + 100
    # Expandida: P(d) = -0,0016d² + 0,8d
    a = -0.0016
    resultado = a * (d - 250) ** 2 + 100
    return max(0.0, min(100.0, resultado))


def classificar_risco(prob):
    """
    Classifica o nível de risco com base na probabilidade de colisão.
    Usa match-case, estrutura ensinada em aula.
    """
    faixa = 0
    if prob >= 75:
        faixa = 4
    elif prob >= 50:
        faixa = 3
    elif prob >= 25:
        faixa = 2
    elif prob > 0:
        faixa = 1

    match faixa:
        case 4:
            return "🔴 CRÍTICO"
        case 3:
            return "🟠 ALTO"
        case 2:
            return "🟡 MODERADO"
        case 1:
            return "🟢 BAIXO"
        case _:
            return "⚪ SEGURO"


def calcular_projecao_detritos(anos):
    """
    Recebe uma lista de anos e retorna uma lista com
    a projeção de detritos para cada ano.
    """
    projecoes = []
    for t in anos:
        valor = crescimento_detritos(t)
        projecoes.append(round(valor))
    return projecoes


def calcular_risco_por_distancias(distancias):
    """
    Recebe uma lista de distâncias (km) e retorna
    uma lista com a probabilidade de colisão de cada uma.
    """
    riscos = []
    for d in distancias:
        p = probabilidade_colisao(d)
        riscos.append(round(p, 2))
    return riscos



# GRÁFICO 1 – FUNÇÃO EXPONENCIAL (Crescimento de Detritos)

def gerar_grafico_exponencial():
    anos_t = list(range(0, 31))          # t de 0 a 30 anos
    anos_labels = [2024 + t for t in anos_t]
    detritos = calcular_projecao_detritos(anos_t)

    pontos_destaque_t = [0, 5, 10, 20, 30]
    pontos_destaque_x = [2024 + t for t in pontos_destaque_t]
    pontos_destaque_y = [crescimento_detritos(t) for t in pontos_destaque_t]

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor("#0a1628")
    ax.set_facecolor("#050d1a")

    # curva principal
    ax.plot(anos_labels, detritos,
            color="#00d4ff", linewidth=2.5, label="D(t) = 28.000 · (1,07)^t")

    # área sob a curva
    ax.fill_between(anos_labels, detritos, alpha=0.12, color="#00d4ff")

    # pontos de destaque
    ax.scatter(pontos_destaque_x, pontos_destaque_y,
               color="#ff4040", s=70, zorder=5)
    for x, y in zip(pontos_destaque_x, pontos_destaque_y):
        ax.annotate(f"{y:,.0f}",
                    xy=(x, y),
                    xytext=(8, 10),
                    textcoords="offset points",
                    color="#ffffff",
                    fontsize=8.5,
                    fontweight="bold")

    # linha de alerta (100.000 detritos)
    ax.axhline(y=100000, color="#ffaa00", linestyle="--",
               linewidth=1.2, alpha=0.7, label="Limiar crítico: 100.000 detritos")

    # formatação
    ax.set_title("Projeção de Crescimento de Detritos Orbitais (2024–2054)\n"
                 "Modelo: Função Exponencial  D(t) = 28.000 · (1,07)^t",
                 color="white", fontsize=13, pad=15)
    ax.set_xlabel("Ano", color="#c8d8f0", fontsize=11)
    ax.set_ylabel("Quantidade de Detritos Rastreados", color="#c8d8f0", fontsize=11)
    ax.tick_params(colors="#c8d8f0")
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{int(v):,}"))
    for spine in ax.spines.values():
        spine.set_edgecolor("#1a3a6b")
    ax.grid(color="#1a3a6b", linestyle="--", linewidth=0.6, alpha=0.5)
    ax.legend(facecolor="#0a1628", edgecolor="#2e6db4",
              labelcolor="white", fontsize=10)

    # anotação da fórmula
    ax.text(0.02, 0.93,
            "D(t) = 28.000 · (1,07)^t\nBase > 1  →  Função Crescente",
            transform=ax.transAxes,
            color="#00d4ff", fontsize=9,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#0a1628",
                      edgecolor="#2e6db4", alpha=0.85))

    plt.tight_layout()
    plt.savefig("grafico_exponencial.png", dpi=150,
                bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    print("  ✅ Gráfico 1 gerado: grafico_exponencial.png")


# GRÁFICO 2 – FUNÇÃO DE 2º GRAU (Probabilidade de Colisão)

def gerar_grafico_2grau():
    distancias = [d for d in range(0, 501, 5)]
    probabilidades = calcular_risco_por_distancias(distancias)

    # vértice: d = -b/(2a) = -2/(2*-0.004) = 250 km
    d_vertice = 250
    p_vertice = probabilidade_colisao(d_vertice)

    # zonas de risco (cores de fundo)
    zonas = [
        (0,   125, "#ff404018"),   # crítico
        (125, 250, "#ffaa0018"),   # alto
        (250, 375, "#ffaa0018"),   # alto (simétrico)
        (375, 500, "#00aa0018"),   # baixo
    ]

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor("#0a1628")
    ax.set_facecolor("#050d1a")

    # zonas coloridas
    ax.axvspan(0,   125, alpha=0.15, color="#ff4040", label="Zona Crítica (>75%)")
    ax.axvspan(125, 375, alpha=0.08, color="#ffaa00", label="Zona de Atenção (25–75%)")
    ax.axvspan(375, 500, alpha=0.08, color="#00aa00", label="Zona Segura (<25%)")

    # curva
    ax.plot(distancias, probabilidades,
            color="#00d4ff", linewidth=2.5,
            label="P(d) = -0,0016d² + 0,8d")

    # vértice
    ax.scatter([d_vertice], [p_vertice],
               color="#ff4040", s=100, zorder=6)
    ax.annotate(f"Vértice\n({d_vertice} km, {p_vertice:.1f}%)",
                xy=(d_vertice, p_vertice),
                xytext=(-90, -40),
                textcoords="offset points",
                color="#ff4040",
                fontsize=9,
                fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#ff4040"))

    # linha de alerta 1:10.000 (limiar do OrbitalWatch)
    ax.axhline(y=50, color="#ffaa00", linestyle="--",
               linewidth=1.2, alpha=0.8,
               label="Limiar de alerta OrbitalWatch (P ≥ 50%)")

    # formatação
    ax.set_title("Probabilidade de Colisão em Função da Distância\n"
                 "Modelo: Função de 2º Grau  P(d) = -0,0016d² + 0,8d",
                 color="white", fontsize=13, pad=15)
    ax.set_xlabel("Distância do Detrito ao Satélite (km)", color="#c8d8f0", fontsize=11)
    ax.set_ylabel("Probabilidade de Colisão (%)", color="#c8d8f0", fontsize=11)
    ax.set_xlim(0, 500)
    ax.set_ylim(0, 110)
    ax.tick_params(colors="#c8d8f0")
    for spine in ax.spines.values():
        spine.set_edgecolor("#1a3a6b")
    ax.grid(color="#1a3a6b", linestyle="--", linewidth=0.6, alpha=0.5)
    ax.legend(facecolor="#0a1628", edgecolor="#2e6db4",
              labelcolor="white", fontsize=9, loc="upper right")

    # fórmula
    ax.text(0.02, 0.93,
            "P(d) = -0,0016d² + 0,8d\na < 0  →  Concavidade para baixo\n"
            "Vértice = ponto de máximo risco",
            transform=ax.transAxes,
            color="#00d4ff", fontsize=9,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#0a1628",
                      edgecolor="#2e6db4", alpha=0.85))

    plt.tight_layout()
    plt.savefig("grafico_2grau.png", dpi=150,
                bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    print("  ✅ Gráfico 2 gerado: grafico_2grau.png")


# MENU PRINCIPAL

def exibir_cabecalho():
    print("=" * 60)
    print("        🛰️  OrbitalWatch – Modelagem Matemática")
    print("        Differentiated Problem Solving | FIAP 2026")
    print("=" * 60)
    print()


def menu_exponencial():
    print("\n── FUNÇÃO EXPONENCIAL: Crescimento de Detritos ──")
    print("   D(t) = 28.000 · (1,07)^t\n")

    # entrada do usuário
    while True:
        entrada = input("   Digite o número de anos a projetar (ex: 10): ").strip()
        if entrada.isdigit() and int(entrada) > 0:
            anos_futuro = int(entrada)
            break
        print("   ⚠ Por favor, digite um número inteiro positivo.")

    print()
    print(f"   {'Ano':<10} {'t':<8} {'Detritos estimados':>20}")
    print("   " + "-" * 40)

    # lista de anos para calcular
    lista_t = list(range(0, anos_futuro + 1))
    projecoes = calcular_projecao_detritos(lista_t)

    for t, valor in zip(lista_t, projecoes):
        ano = 2024 + t
        print(f"   {ano:<10} {t:<8} {valor:>20,.0f}")

    # análise
    print()
    crescimento_total = projecoes[-1] - projecoes[0]
    fator = projecoes[-1] / projecoes[0]
    print(f"   📊 Crescimento total: {crescimento_total:,.0f} detritos")
    print(f"   📊 O número de detritos será {fator:.1f}x maior em {anos_futuro} anos")
    print()
    gerar_grafico_exponencial()


def menu_2grau():
    print("\n── FUNÇÃO DE 2º GRAU: Probabilidade de Colisão ──")
    print("   P(d) = -0,004d² + 2d")
    print("   Domínio: 0 a 500 km | Vértice: 250 km\n")

    # entrada: lista de distâncias
    print("   Digite distâncias separadas por vírgula (ex: 50,150,250,400):")
    while True:
        entrada = input("   Distâncias (km): ").strip()
        try:
            distancias_input = [float(x.strip()) for x in entrada.split(",")]
            if all(0 <= d <= 500 for d in distancias_input):
                break
            print("   ⚠ Distâncias devem estar entre 0 e 500 km.")
        except ValueError:
            print("   ⚠ Formato inválido. Use números separados por vírgula.")

    print()
    print(f"   {'Distância (km)':<18} {'Probabilidade (%)':<20} {'Classificação'}")
    print("   " + "-" * 55)

    for d in distancias_input:
        p = probabilidade_colisao(d)
        risco = classificar_risco(p)
        print(f"   {d:<18.1f} {p:<20.2f} {risco}")

    print()
    # vértice
    print("   📐 Análise do Vértice (ponto de máximo risco):")
    print("      d_v = -b / (2a) = -0,8 / (2 × -0,0016) = 250 km")
    print(f"      P(250) = {probabilidade_colisao(250):.1f}%  →  {classificar_risco(100)}")
    print()
    print("   📐 Raízes da parábola (P = 0):")
    print("      -0,004d² + 2d = 0")
    print("      d(-0,004d + 2) = 0")
    print("      d₁ = 0 km  |  d₂ = 500 km")
    print()
    gerar_grafico_2grau()


def menu_consulta_rapida():
    print("\n── CONSULTA RÁPIDA: Avaliação de Risco por Distância ──\n")

    while True:
        entrada = input("   Digite a distância do detrito (km, entre 0 e 500): ").strip()
        try:
            d = float(entrada)
            if 0 <= d <= 500:
                break
            print("   ⚠ Distância deve estar entre 0 e 500 km.")
        except ValueError:
            print("   ⚠ Digite um número válido.")

    p = probabilidade_colisao(d)
    risco = classificar_risco(p)

    print()
    print("   ┌─────────────────────────────────────────┐")
    print(f"   │  Distância:      {d:.1f} km")
    print(f"   │  P(d):           {p:.2f}%")
    print(f"   │  Classificação:  {risco}")

    # recomendação com match-case
    match risco:
        case "🔴 CRÍTICO":
            rec = "Acionar protocolo de manobra imediatamente."
        case "🟠 ALTO":
            rec = "Monitorar com frequência aumentada. Preparar manobra."
        case "🟡 MODERADO":
            rec = "Manter monitoramento padrão. Calcular janela de desvio."
        case "🟢 BAIXO":
            rec = "Risco dentro dos parâmetros. Monitoramento normal."
        case _:
            rec = "Órbita limpa. Nenhuma ação necessária."

    print(f"   │  Recomendação:   {rec}")
    print("   └─────────────────────────────────────────┘")
    print()


def menu_projecao_frota():
    print("\n── PROJEÇÃO DE RISCO PARA FROTA DE SATÉLITES ──\n")

    # lista de satélites com distâncias simuladas
    frota = [
        ("SAT-ORBITAL-01", 80),
        ("SAT-ORBITAL-02", 210),
        ("SAT-ORBITAL-03", 340),
        ("SAT-ORBITAL-04", 450),
        ("SAT-ORBITAL-05", 120),
    ]

    print(f"   {'Satélite':<20} {'Distância (km)':<18} {'Risco (%)':<14} {'Status'}")
    print("   " + "-" * 65)

    criticos = []
    for nome, distancia in frota:
        p = probabilidade_colisao(distancia)
        status = classificar_risco(p)
        print(f"   {nome:<20} {distancia:<18} {p:<14.2f} {status}")
        if p >= 50:
            criticos.append(nome)

    print()
    if criticos:
        print(f"   ⚠ Satélites em situação crítica ou alta: {len(criticos)}")
        for s in criticos:
            print(f"      → {s}: manobra de desvio recomendada")
    else:
        print("   ✅ Todos os satélites da frota estão em zona segura.")
    print()


def main():
    exibir_cabecalho()

    while True:
        print("  Escolha uma opção:")
        print("  [1] Projeção de crescimento de detritos (Função Exponencial)")
        print("  [2] Probabilidade de colisão por distância (Função de 2º Grau)")
        print("  [3] Consulta rápida: avaliação de risco de um detrito")
        print("  [4] Análise de risco da frota de satélites")
        print("  [0] Sair")
        print()

        opcao = input("  Digite a opção desejada: ").strip()

        match opcao:
            case "1":
                menu_exponencial()
            case "2":
                menu_2grau()
            case "3":
                menu_consulta_rapida()
            case "4":
                menu_projecao_frota()
            case "0":
                print()
                print("  Encerrando OrbitalWatch. Até logo! 🛰️")
                print("=" * 60)
                break
            case _:
                print("  ⚠ Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
