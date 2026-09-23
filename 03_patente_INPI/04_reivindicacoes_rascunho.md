# RASCUNHO DE TRABALHO — SEM VALOR DE PROTOCOLO

# 04 — Reivindicações (rascunho) | ETAPA 3

Prefixo obrigatório em cada claim: **[RASCUNHO]**. Forma: «caracterizado por».  
**Não protocolar** sem revisão de agente PI.

---

## Estratégia do redator (obrigatória)

Um examinador pode argumentar que a matéria é **ALT clássico + FPS (ou amostragem geométrica equivalente) aplicada a mapa de armazém**.  
O **Trilho B** só se sustenta se for isolado e documentado um **delta não óbvio** além dessa combinação (e além do estado da técnica nominado).  
Se **não** houver delta documentado → **Trilho B em alto risco**.  
**Ato desta semana = Trilho A** (registro de software). Manter estas claims como rascunho interno até decisão fundamentada.

---

### [RASCUNHO] 1. (Independente — PROCESSO / MÉTODO IIC)

Processo implementado em computador para planejamento de caminhos em grafo derivado de layout espacial estável de ambiente industrial, **caracterizado por** compreender:  
(a) uma fase offline de construção de um prior estrutural do referido grafo, incluindo seleção de landmarks geométricos e pré-computação de tabelas de distância associadas aos ditos landmarks;  
(b) uma fase online de atendimento a consultas origem–destino mediante busca informada que utiliza o referido prior para obter estimativas admissíveis de custo residual; e  
(c) reuso do referido prior em múltiplas consultas enquanto o layout permanecer válido.

- **Suporte memorial:** seções 5.1–5.3.  
- **Risco art. 10:** médio–alto (método de grafo / software); depende da redação ligada a layout industrial e efeito técnico.  
- **Risco obviedade vs ALT clássico:** **alto** — núcleo próximo de ALT + landmarks.

### [RASCUNHO] 2. (Independente opcional — SISTEMA)

Sistema de planejamento de rotas em layout industrial, compreendendo pelo menos um processador e memória com instruções, **caracterizado por** o processador ser configurado para executar a fase offline e a fase online do processo da reivindicação 1, persistindo o prior estrutural em memória não transitória enquanto o mapa for válido.

- **Suporte memorial:** seções 5 e 8.  
- **Risco art. 10:** médio (sistema); evitar reivindicar «programa em si».  
- **Risco obviedade:** alto, acoplado à claim 1.

### [RASCUNHO] 3. (Dependente — número k de landmarks)

Processo de acordo com a reivindicação 1, **caracterizado por** o número k de landmarks geométricos ser selecionado em função do tamanho do grafo e de um orçamento de memória de pré-processamento.

- **Suporte:** §5.1.  
- **Risco art. 10:** baixo adicional.  
- **Risco obviedade:** médio (escolha de k é rotineira em ALT).

### [RASCUNHO] 4. (Dependente — FPS)

Processo de acordo com a reivindicação 1 ou 3, **caracterizado por** os landmarks geométricos serem obtidos por amostragem do tipo farthest-point sampling (FPS) sobre coordenadas ou métrica geométrica do layout.

- **Suporte:** §5.1; evidência v7 (FPS não superado por geradores topológicos).  
- **Risco art. 10:** baixo adicional.  
- **Risco obviedade vs ALT clássico:** **alto** — FPS/geométrico é combinação esperada.

### [RASCUNHO] 5. (Dependente — ALT / desigualdade triangular)

Processo de acordo com qualquer uma das reivindicações 1, 3 ou 4, **caracterizado por** a busca informada online ser do tipo ALT, utilizando desigualdades triangulares entre nó corrente, destino e landmarks para compor heurística admissível.

- **Suporte:** §5.2; estado da técnica US7603229B2.  
- **Risco art. 10:** médio–alto.  
- **Risco obviedade:** **muito alto** — ALT é estado da técnica documentado.

### [RASCUNHO] 6. (Dependente — invalidação do prior)

Processo de acordo com a reivindicação 1, **caracterizado por** invalidar o prior estrutural e recomputar a fase offline quando for detectada alteração material do layout espacial.

- **Suporte:** §5.3.  
- **Risco art. 10:** baixo–médio.  
- **Risco obviedade:** médio (invalidação de cache/pré-processamento é previsível).

### [RASCUNHO] 7. (Dependente — lote de consultas)

Processo de acordo com a reivindicação 1, **caracterizado por** amortizar o custo da fase offline ao longo de um lote de Q* consultas origem–destino sobre o mesmo mapa válido.

- **Suporte:** §8; figura de amortização.  
- **Risco art. 10:** baixo adicional.  
- **Risco obviedade:** médio.

### [RASCUNHO] 8. (Dependente — função de custo)

Processo de acordo com a reivindicação 1, **caracterizado por** o custo de aresta do grafo representar distância de corredor, tempo de travessia ou combinação ponderada definida para o ambiente industrial.

- **Suporte:** §2 e §5.  
- **Risco art. 10:** baixo.  
- **Risco obviedade:** baixo–médio.

### [RASCUNHO] 9. (Dependente — mapas DG alto)

Processo de acordo com a reivindicação 1 ou 5, **caracterizado por** ser aplicado a mapas em que a razão DG = d_grafo / d_Manhattan é elevada, condição na qual, segundo testes internos (v7), landmarks geométricos reduziram expansão face a A* com heurística Manhattan fixa.

- **Suporte:** §6 (v7).  
- **Risco art. 10:** médio (depende de não virar só resultado matemático).  
- **Risco obviedade:** médio–alto; formulação ajuda a delimitar domínio, não garante inventividade.

### [RASCUNHO] 10. (Dependente — otimalidade / admissibilidade)

Processo de acordo com a reivindicação 5, **caracterizado por** a heurística utilizada na fase online ser admissível, de modo a preservar otimalidade do caminho retornado, conforme verificado em bateria interna de 1000 consultas (v5) com 100% de otimalidade.

- **Suporte:** §6 (v5).  
- **Risco art. 10:** médio.  
- **Risco obviedade:** alto (admissibilidade é propriedade clássica de A*/ALT).

### [RASCUNHO] 11. (Dependente — persistência do prior)

Sistema de acordo com a reivindicação 2, **caracterizado por** armazenar as tabelas de distância e a lista de landmarks em estrutura persistente indexada ao identificador do mapa.

- **Suporte:** §5.1.  
- **Risco art. 10:** baixo.  
- **Risco obviedade:** médio.

### [RASCUNHO] 12. (Dependente — sinalização de reprocessamento)

Sistema de acordo com a reivindicação 2 ou 11, **caracterizado por** emitir sinal de reprocessamento offline quando um módulo de monitoração de layout indicar mudança de topologia de corredores ou obstáculos.

- **Suporte:** §5.3.  
- **Risco art. 10:** baixo–médio.  
- **Risco obviedade:** médio.

### [RASCUNHO] 13. (Dependente opcional — TDA) — NO MÁXIMO UMA

Processo de acordo com a reivindicação 1, **caracterizado por** opcionalmente empregar descritor derivado de análise topológica de dados (TDA) na seleção auxiliar de landmarks, **ressalvado** que testes internos v6 e v7 **não** demonstraram superioridade dessa via sobre seleção geométrica tipo FPS.

- **Suporte:** §5.4; §6 (v6/v7).  
- **Risco art. 10:** alto (método matemático / abstrato).  
- **Risco obviedade / falta de vantagem:** **alto** — incluir só se agente PI julgar útil como fallback; **não** elevar a independente.

### [RASCUNHO] 14. (Dependente — ambiente armazém/pátio/planta)

Processo de acordo com a reivindicação 1, **caracterizado por** o layout espacial estável corresponder a mapa de armazém, pátio logístico ou planta industrial com corredores e obstáculos.

- **Suporte:** §2.  
- **Risco art. 10:** ajuda delimitação de aplicação industrial.  
- **Risco obviedade:** não elimina obviedade de ALT+FPS.

---

**Contagem:** 14 claims (2 independentes + 12 dependentes, sendo 1 TDA opcional).  
**Recomendação:** para depósito futuro de Trilho B, considerar cortar claim 13 e fortalecer evidência de delta além de ALT+FPS; caso contrário, **não depositar** Trilho B.
