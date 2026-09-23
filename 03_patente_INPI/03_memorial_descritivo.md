# RASCUNHO DE TRABALHO — SEM VALOR DE PROTOCOLO

# 03 — Memorial descritivo (rascunho) | ETAPA 2

**Atenção:** texto para revisão por agente PI. Não protocolar neste estado.  
**Inventor:** João Pedro Pereira Passos (PF), Palmas/TO. Cotitularidade institucional: PENDENTE de verificação contratual (UFT / Rede BIONORTE / UNITINS).

---

## 1. Título (provisório)

Processo de planejamento de caminhos em grafo de layout espacial estável com pré-processamento offline de landmarks geométricos e consultas origem–destino online por busca informada admissível.

## 2. Campo técnico

A invenção candidata situa-se no campo técnico de **sistemas de planejamento de rotas em ambientes industriais** (armazéns, pátios, plantas), implementados em computador, em que um mapa espacial relativamente estável é modelado como grafo e múltiplas consultas origem–destino (O-D) devem ser respondidas com caminhos de custo mínimo (ou custo admissivelmente ótimo), sob restrições de tempo de resposta e de expansão de estados de busca.

Aplicações típicas (não limitativas): apoio a roteamento em corredores de picking; apoio a gestores de frota de veículos/AMR em planta; pré-cálculo auxiliar a WMS — **sem** reivindicar o WMS em si.

## 3. Estado da técnica (referências nominadas)

Sem prejuízo de busca completa (ver `06_protocolo_busca_anterioridade.md`), listam-se referências nominadas do estado da técnica:

1. **Dijkstra** — algoritmo clássico de caminhos mínimos em grafos com pesos não negativos.  
2. **A*** — busca informada com heurística admissível (Hart, Nilsson, Raphael — literatura clássica).  
3. **Busca bidirecional** — expansão simultânea/alternada a partir de origem e destino.  
4. **ALT / landmarks** — A* com landmarks e desigualdade triangular; ver documento de patente verificável **US7603229B2** (Goldberg; Harrelson) e pedido publicado **US20090228198A1** (seleção de landmarks; Goldberg; Werneck).  
5. **Jump Point Search (JPS)** — Harabor & Grastien (literatura); aplicação a grades; documento de patente específico: **PENDENTE DE BUSCA**.  
6. **Contraction hierarchies (CH)** — Geisberger et al. (literatura); documento verificável correlato de roteamento com CH: **US9175972B2** / **EP2757504B1**.  
7. **Portais / corredores / abstrações espaciais** — técnicas de redução de grafo por regiões e portas; documento de patente específico: **PENDENTE DE BUSCA**.  
8. **Picking / WMS** — sistemas de gerenciamento de armazém e otimização de rotas de coleta; documento de patente específico: **PENDENTE DE BUSCA**.  
9. **Gestores de frota AMR / AGV** — roteamento multiagente em planta; documento de patente específico: **PENDENTE DE BUSCA** (ex.: famílias de multi-robot routing — a completar pelo inventor/agente).  
10. Heurísticas geométricas (Manhattan, Euclidean, octile) em mapas de grade — literatura padrão de pathfinding.

**Documento de patente:** só citar número se verificável; caso contrário manter **PENDENTE DE BUSCA**.

## 4. Problema técnico

Em layouts industriais estáveis, consultas O-D repetidas sobre o mesmo mapa, resolvidas por A* com heurística geométrica fixa (ex. Manhattan), tendem a expandir número elevado de estados, especialmente quando a razão DG = d_grafo / d_Manhattan cresce (corredores longos, obstáculos, desvios).  
Pré-processamentos clássicos (ALT genérico, CH, JPS) existem, porém a combinação operacional offline/online voltada a **mapa industrial estável**, com **landmarks geométricos** (ex. FPS), **tabelas de distância reutilizáveis** e **política de invalidação do prior** quando o layout muda, e com evidência interna de redução de nós/tempo **mantendo otimalidade**, constitui o foco do memorial — sujeito a exame de novidade e atividade inventiva.

## 5. Proposta (nível memorial — sem detalhe reprodutível de seletor topológico)

### 5.1 Fase offline
- Obter representação do layout como grafo (nós/arestas com custos).  
- Calcular **prior estrutural** associado ao mapa.  
- Selecionar conjunto de **landmarks geométricos** (exemplo de família: farthest-point sampling — FPS).  
- Pré-computar **tabelas de distância** entre nós (ou subconjunto relevante) e landmarks.  
- Persistir o prior para reuso.

### 5.2 Fase online
- Receber consulta O-D.  
- Executar busca informada do tipo **ALT** (ou equivalente admissível baseado em landmarks + desigualdade triangular).  
- Garantir, nos termos da heurística adotada, **admissibilidade** → otimalidade do caminho retornado (conforme teoria clássica e testes internos).  
- Reutilizar o prior enquanto o mapa for válido.

### 5.3 Invalidação
- Se o layout mudar materialmente, invalidar o prior e recomputar offline.

### 5.4 O que deliberadamente NÃO se descreve aqui com detalhe reprodutível
- Algoritmo completo de **seletor topológico** baseado em homologia / Wasserstein / persistência.  
Motivo: (i) não essencial às independentes; (ii) v6/v7 não demonstraram superioridade sobre geométrica; (iii) preservar opção de segredo / dependente opcional.

## 6. Vantagens alegadas (amarradas a evidência)

| Alegação | Base | Status |
|----------|------|--------|
| 100% otimalidade em 1000 consultas (v5) | Teste interno inventor | Informado pelo inventor — **não** é exame INPI |
| Variante geométrica reduziu nós e tempo vs A* fixo (v5) | Teste interno | Informado |
| Em DG alto, landmarks geométricos vencem A* (v7) | Teste interno | Informado |
| Seleção por geradores topológicos não superou FPS (v7) | Teste interno | Informado — **desaconselha** ênfase TDA |
| Variar só beta1 (stretch ~1) sem vantagem topológica (v6) | Teste interno | Informado |
| Superioridade em planta real de cliente específico | — | **NÃO MEDIDO** / não alegar |
| Redução de opex / honorários / ROI comercial | — | **NÃO** usar como efeito técnico |

**Efeito técnico candidato (não deferido):** menos estados expandidos e/ou menor tempo em consultas repetidas no mesmo mapa, com ótimo intacto nos testes internos.

## 7. Descrição sumária das figuras

Ver `05_resumo_e_figuras.md` (Figuras 1–N: fluxo offline/online; mapa DG alto; amortização; API sem código). Linhas pretas; sem foto de cliente; sem logo.

## 8. Aplicação industrial

O processo candidato aplica-se a ambientes industriais reais (armazém, pátio, planta) nos quais o layout espacial permanece estável por períodos suficientes para amortizar o pré-processamento offline ao longo de um lote de consultas Q*.

## Observações ao agente PI

- Risco art. 10 I / 10 V elevado se claims colapsarem para «shortest path + landmarks».  
- Risco de obviedade frente a **US7603229B2** e literatura ALT.  
- Homologia: no máximo dependente opcional com nota v6/v7.  
- Completar estado da técnica com busca executada (arquivo 06).
