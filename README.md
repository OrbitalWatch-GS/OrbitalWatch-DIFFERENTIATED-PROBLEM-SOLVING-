# 🛰️ OrbitalWatch – Modelagem Matemática

**Disciplina:** Differentiated Problem Solving  
**Projeto:** Global Solution 2026 | FIAP | Engenharia de Software  

---

## 📄 Documentação da Entrega

🔗 **[CLIQUE AQUI PARA ACESSAR O PDF DO PROJETO](https://docs.google.com/document/d/1X_8GyGPNKpN-kr9EgXLUoC9ziZDoIQWyRiGQqJ8f400/edit?usp=sharing)**

---

## 💻 Sobre o Projeto

O **OrbitalWatch** é uma ferramenta desenvolvida em Python que aplica conceitos de modelagem matemática para analisar e prever cenários relacionados ao acúmulo de lixo espacial na órbita terrestre. O sistema auxilia na tomada de decisão para manobras de satélites e monitoramento de riscos.

### Funcionalidades Principais:

1. **Projeção de Crescimento de Detritos (Função Exponencial)**
   - Calcula e projeta o aumento da quantidade de lixo espacial ao longo dos anos com base em uma taxa de crescimento anual.
   - Gera um gráfico interativo mostrando a evolução ao longo do tempo e limiares críticos.

2. **Probabilidade de Colisão por Distância (Função de 2º Grau)**
   - Modela o risco de impacto (%) com base na distância entre um satélite e um detrito, encontrando o ponto de risco máximo (vértice da parábola).
   - Classifica o risco em níveis (Baixo, Moderado, Alto, Crítico) e gera uma visualização gráfica das zonas de perigo.

3. **Análise de Frota**
   - Simulação rápida do status de múltiplos satélites simultaneamente, emitindo alertas e recomendações de manobra.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3** (Linguagem base)
* **Matplotlib** (Biblioteca para geração de gráficos matemáticos)
* Estruturas de controle de fluxo modernas (`match-case`)

---

## 🚀 Como executar o projeto

Certifique-se de ter o Python instalado em sua máquina.

1. Clone este repositório ou baixe os arquivos.
2. Abra o terminal na pasta do projeto.
3. Instale a biblioteca necessária para os gráficos rodando o comando:
   ```bash
   pip install matplotlib
4. Execute o script principal: 
   ```bash
   python orbitalwatch_math.py

## 👥 Integrantes da Equipe

João Pedro Maschion da Cruz Sá – RM570509
Gustavo Rezende Louro – RM570708
João Pedro Lagonegro Bosco e Silva – RM569444
Lucas Henrique Alves da Silva – RM572216
