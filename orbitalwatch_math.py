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


def crescimento_detritos(t):
    """
    Função Exponencial CRESCENTE: modela o crescimento de detritos orbitais.

    D(t) = 40.000 * (1,07)^t

    Onde:
      D(t) = quantidade de objetos rastreados no ano t
      40.000 = quantidade inicial (base: ESA Space Environment Report 2025)
      1,07   = taxa de crescimento de 7% ao ano
      t      = anos a partir de 2025

    Domínio: t >= 0 (anos futuros)
    Imagem: D(t) >= 40.000
    Comportamento: CRESCENTE, pois a base (1,07) é maior que 1.
    """
    D0 = 40000       # objetos rastreados em 2025 (valor inicial - ESA 2025)
    taxa = 1.07      # crescimento de 7% ao ano
    return D0 * (taxa ** t)


def probabilidade_colisao(d):
    """
    Função Exponencial DECRESCENTE: modela a probabilidade de colisão (%)
    em função da distância (km) entre o detrito e o satélite.

    P(d) = 100 * e^(-d / 80)

    Onde:
      P(d) = probabilidade (índice) de colisão, de 0% a 100%
      d    = distância do detrito ao satélite (km)
      80   = constante que controla a velocidade de queda do risco

    Interpretação física (por que é decrescente):
      - Quanto MENOR a distância, MAIOR o risco. Em d = 0 (contato
        iminente) o risco é máximo: P(0) = 100%.
      - Quanto MAIOR a distância, MENOR o risco, tendendo a zero.

    Domínio: d >= 0 (distância não pode ser negativa)
    Imagem: 0 < P(d) <= 100
    Comportamento: DECRESCENTE em todo o domínio.
    Assíntota horizontal: P(d) -> 0 quando d -> infinito
                          (o risco tende a zero, mas nunca é exatamente zero).
    """
    K = 80.0
    return 100 * math.exp(-d / K)


def classificar_risco(prob):
    """
    Classifica o nível de risco com base na probabilidade de colisão.
    Usa if-elif-else para definir a faixa e match-case para a etiqueta.
    """
    if prob >= 75:
        faixa = 4
    elif prob >= 50:
        faixa = 3
    elif prob >= 25:
        faixa = 2
    elif prob > 0:
        faixa = 1
    else:
        faixa = 0

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
    """Recebe uma lista de anos e retorna a projeção de detritos para cada um."""
    projecoes = []
    for t in anos:
        valor = crescimento_detritos(t)
        projecoes.append(round(valor))
    return projecoes


def calcular_risco_por_distancias(distancias):
    """Recebe uma lista de distâncias (km) e retorna a probabilidade de cada uma."""
    riscos = []
    for d in distancias:
        p = probabilidade_colisao(d)
        riscos.append(round(p, 2))
    return riscos


# ============================================================
# GRÁFICO 1 – FUNÇÃO EXPONENCIAL CRESCENTE (Crescimento de Detritos)
# ============================================================

def gerar_grafico_exponencial():
    anos_t = list(range(0, 31))          # t de 0 a 30 anos
    anos_labels = [2025 + t for t in anos_t]
    detritos = calcular_projecao_detritos(anos_t)

    pontos_destaque_t = [0, 5, 10, 20, 30]
    pontos_destaque_x = [2025 + t for t in pontos_destaque_t]
    pontos_destaque_y = [crescimento_detritos(t) for t in pontos_destaque_t]

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor("#0a1628")
    ax.set_facecolor("#050d1a")

    ax.plot(anos_labels, detritos,
            color="#00d4ff", linewidth=2.5, label="D(t) = 40.000 · (1,07)^t")
    ax.fill_between(anos_labels, detritos, alpha=0.12, color="#00d4ff")

    ax.scatter(pontos_destaque_x, pontos_destaque_y,
               color="#ff4040", s=70, zorder=5)
    for x, y in zip(pontos_destaque_x, pontos_destaque_y):
        ax.annotate(f"{y:,.0f}", xy=(x, y), xytext=(8, 10),
                    textcoords="offset points", color="#ffffff",
                    fontsize=8.5, fontweight="bold")

    ax.set_title("Projeção de Crescimento de Objetos Rastreados (2025–2055)\n"
                 "Modelo: Função Exponencial Crescente  D(t) = 40.000 · (1,07)^t",
                 color="white", fontsize=13, pad=15)
    ax.set_xlabel("Ano", color="#c8d8f0", fontsize=11)
    ax.set_ylabel("Quantidade de Objetos Rastreados", color="#c8d8f0", fontsize=11)
    ax.tick_params(colors="#c8d8f0")
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{int(v):,}"))
    for spine in ax.spines.values():
        spine.set_edgecolor("#1a3a6b")
    ax.grid(color="#1a3a6b", linestyle="--", linewidth=0.6, alpha=0.5)
    ax.legend(facecolor="#0a1628", edgecolor="#2e6db4", labelcolor="white", fontsize=10)

    ax.text(0.02, 0.93,
            "D(t) = 40.000 · (1,07)^t\nBase > 1  →  Função Crescente",
            transform=ax.transAxes, color="#00d4ff", fontsize=9,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#0a1628",
                      edgecolor="#2e6db4", alpha=0.85))

    plt.tight_layout()
    plt.savefig("grafico_exponencial_crescente.png", dpi=150,
                bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    print("  ✅ Gráfico 1 gerado: grafico_exponencial_crescente.png")


# ============================================================
# GRÁFICO 2 – FUNÇÃO EXPONENCIAL DECRESCENTE (Risco x Distância)
# ============================================================

def gerar_grafico_risco():
    distancias = [d for d in range(0, 401, 5)]
    probabilidades = calcular_risco_por_distancias(distancias)

    # distância de "meia-risco": onde P cai à metade -> d = 80 * ln(2)
    d_meia = 80 * math.log(2)

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor("#0a1628")
    ax.set_facecolor("#050d1a")

    # faixas de risco coloridas (apenas referência visual)
    ax.axhspan(75, 100, alpha=0.12, color="#ff4040", label="Zona Crítica (≥ 75%)")
    ax.axhspan(25, 75, alpha=0.08, color="#ffaa00", label="Zona de Atenção (25–75%)")
    ax.axhspan(0, 25, alpha=0.08, color="#00aa00", label="Zona Segura (< 25%)")

    ax.plot(distancias, probabilidades,
            color="#00d4ff", linewidth=2.5, label="P(d) = 100 · e^(-d/80)")

    # ponto de meia-risco
    ax.scatter([d_meia], [50], color="#ff4040", s=90, zorder=6)
    ax.annotate(f"Meia-risco\n(d ≈ {d_meia:.1f} km, 50%)",
                xy=(d_meia, 50), xytext=(40, 30),
                textcoords="offset points", color="#ff4040",
                fontsize=9, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#ff4040"))

    ax.set_title("Probabilidade de Colisão em Função da Distância\n"
                 "Modelo: Função Exponencial Decrescente  P(d) = 100 · e^(-d/80)",
                 color="white", fontsize=13, pad=15)
    ax.set_xlabel("Distância do Detrito ao Satélite (km)", color="#c8d8f0", fontsize=11)
    ax.set_ylabel("Probabilidade de Colisão (%)", color="#c8d8f0", fontsize=11)
    ax.set_xlim(0, 400)
    ax.set_ylim(0, 105)
    ax.tick_params(colors="#c8d8f0")
    for spine in ax.spines.values():
        spine.set_edgecolor("#1a3a6b")
    ax.grid(color="#1a3a6b", linestyle="--", linewidth=0.6, alpha=0.5)
    ax.legend(facecolor="#0a1628", edgecolor="#2e6db4", labelcolor="white",
              fontsize=9, loc="upper right")

    ax.text(0.40, 0.80,
            "P(d) = 100 · e^(-d/80)\nDecrescente  →  risco cai com a distância\n"
            "P(0) = 100%  |  P(d) → 0 quando d → ∞",
            transform=ax.transAxes, color="#00d4ff", fontsize=9,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#0a1628",
                      edgecolor="#2e6db4", alpha=0.85))

    plt.tight_layout()
    plt.savefig("grafico_risco_exponencial.png", dpi=150,
                bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    print("  ✅ Gráfico 2 gerado: grafico_risco_exponencial.png")


# ============================================================
# MENU PRINCIPAL
# ============================================================

def exibir_cabecalho():
    print("=" * 60)
    print("        🛰️  OrbitalWatch – Modelagem Matemática")
    print("        Differentiated Problem Solving | FIAP 2026")
    print("=" * 60)
    print()


def menu_exponencial():
    print("\n── FUNÇÃO EXPONENCIAL CRESCENTE: Crescimento de Detritos ──")
    print("   D(t) = 40.000 · (1,07)^t\n")

    while True:
        entrada = input("   Digite o número de anos a projetar (ex: 10): ").strip()
        if entrada.isdigit() and int(entrada) > 0:
            anos_futuro = int(entrada)
            break
        print("   ⚠ Por favor, digite um número inteiro positivo.")

    print()
    print(f"   {'Ano':<10} {'t':<8} {'Detritos estimados':>20}")
    print("   " + "-" * 40)

    lista_t = list(range(0, anos_futuro + 1))
    projecoes = calcular_projecao_detritos(lista_t)

    for t, valor in zip(lista_t, projecoes):
        ano = 2025 + t
        print(f"   {ano:<10} {t:<8} {valor:>20,.0f}")

    print()
    crescimento_total = projecoes[-1] - projecoes[0]
    fator = projecoes[-1] / projecoes[0]
    print(f"   📊 Crescimento total: {crescimento_total:,.0f} detritos")
    print(f"   📊 O número de detritos será {fator:.1f}x maior em {anos_futuro} anos")
    print()
    gerar_grafico_exponencial()


def menu_risco_distancia():
    print("\n── FUNÇÃO EXPONENCIAL DECRESCENTE: Risco de Colisão ──")
    print("   P(d) = 100 · e^(-d/80)")
    print("   Quanto menor a distância, maior o risco.\n")

    print("   Digite distâncias separadas por vírgula (ex: 15,50,120,300):")
    while True:
        entrada = input("   Distâncias (km): ").strip()
        try:
            distancias_input = [float(x.strip()) for x in entrada.split(",")]
            if all(d >= 0 for d in distancias_input):
                break
            print("   ⚠ As distâncias não podem ser negativas.")
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
    print("   📐 Análise da função P(d) = 100 · e^(-d/80):")
    print("      • Domínio: d ≥ 0 (distância não pode ser negativa)")
    print("      • Imagem: 0 < P(d) ≤ 100")
    print("      • Comportamento: DECRESCENTE em todo o domínio")
    print(f"      • P(0) = {probabilidade_colisao(0):.1f}%  → risco máximo no contato iminente")
    print("      • Assíntota horizontal: P(d) → 0 quando d → ∞")
    d_meia = 80 * math.log(2)
    print(f"      • Distância de meia-risco: d = 80·ln(2) ≈ {d_meia:.1f} km (risco cai à metade)")
    print()
    gerar_grafico_risco()


def menu_consulta_rapida():
    print("\n── CONSULTA RÁPIDA: Avaliação de Risco por Distância ──\n")

    while True:
        entrada = input("   Digite a distância do detrito (km): ").strip()
        try:
            d = float(entrada)
            if d >= 0:
                break
            print("   ⚠ A distância não pode ser negativa.")
        except ValueError:
            print("   ⚠ Digite um número válido.")

    p = probabilidade_colisao(d)
    risco = classificar_risco(p)

    print()
    print("   ┌─────────────────────────────────────────┐")
    print(f"   │  Distância:      {d:.1f} km")
    print(f"   │  P(d):           {p:.2f}%")
    print(f"   │  Classificação:  {risco}")

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
    print("\n── ANÁLISE DE RISCO PARA FROTA DE SATÉLITES ──\n")

    # frota de exemplo com distâncias que cobrem todos os níveis de risco
    frota = [
        ("SAT-ORBITAL-01", 15),
        ("SAT-ORBITAL-02", 50),
        ("SAT-ORBITAL-03", 95),
        ("SAT-ORBITAL-04", 160),
        ("SAT-ORBITAL-05", 280),
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
        print(f"   ⚠ Satélites em situação ALTA ou CRÍTICA: {len(criticos)}")
        for s in criticos:
            print(f"      → {s}: manobra de desvio recomendada")
    else:
        print("   ✅ Todos os satélites da frota estão em zona segura.")
    print()


def main():
    exibir_cabecalho()

    while True:
        print("  Escolha uma opção:")
        print("  [1] Projeção de crescimento de detritos (Exponencial Crescente)")
        print("  [2] Risco de colisão por distância (Exponencial Decrescente)")
        print("  [3] Consulta rápida: avaliação de risco de um detrito")
        print("  [4] Análise de risco da frota de satélites")
        print("  [0] Sair")
        print()

        opcao = input("  Digite a opção desejada: ").strip()

        match opcao:
            case "1":
                menu_exponencial()
            case "2":
                menu_risco_distancia()
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
