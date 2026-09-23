# RASCUNHO DE TRABALHO — SEM VALOR DE PROTOCOLO

# 06 — Protocolo de busca de anterioridade | ETAPA 5

**Data de elaboração deste protocolo:** 2026-09-22 (America/Araguaina, UTC-3).  
**Executante desta rodada:** redator técnico (buscas parciais via bases públicas).  
**Completar:** inventor e/ou agente PI credenciado.

## Classes IPC/CPC candidatas (hipótese — a validar no exame)

- G06Q 10/04 — forecasting or optimisation  
- G06Q 10/08 — logistics  
- G01C 21/20 — instruments for performing navigational calculations  
- Correlatas possíveis: G05D 1/00 (controle de veículos terrestres), G06F 17/00 / G06F 16/00 (estruturas de dados — verificar CPC vigente), G01C 21/34  

**Status:** hipótese de classificação; **PENDENTE** de confirmação pelo agente na estratégia de depósito.

## Consultas PT / EN (lista de trabalho)

1. planejamento de caminhos OR path planning armazém OR warehouse  
2. A* landmarks ALT "triangle inequality"  
3. farthest point sampling landmarks shortest path  
4. jump point search warehouse AGV OR AMR  
5. contraction hierarchies routing  
6. portal corridor graph abstraction pathfinding  
7. WMS picking route optimization patent  
8. frota AMR roteamento planta industrial  
9. "shortest path" landmarks Goldberg Harrelson  
10. busca informada admissível layout industrial  
11. DG ratio graph distance Manhattan heuristic  
12. offline preprocessing online query path warehouse  
13. bidirectional A* warehouse robot  
14. geometric landmarks FPS pathfinding  
15. hierarchical pathfinding industrial plant  
16. "route planning" "contraction hierarchies" Geisberger  
17. planejamento rotas corredores obstáculos grafo  
18. multi-agent pathfinding warehouse patent  
19. heurística admissível consultas origem destino  
20. invalidação pré-processamento mapa layout  
21. "selecting landmarks" shortest path  
22. path planning "stable layout" OR "static map" industrial  
23. JPS "jump point" grid warehouse  
24. portal-based pathfinding OR "entrance points" map abstraction  
25. INPI pathfinding OR "caminho mínimo" programa computador (literatura BR)

## Tabela de resultados

| Consulta | Base | Data | Documentos (número) | Relevância | Status |
|----------|------|------|---------------------|------------|--------|
| ALT landmarks shortest path / Goldberg Harrelson | Google Patents | 2026-09-22 | **US7603229B2** | Alta — ALT com landmarks e desigualdade triangular | Verificado (página Google Patents) |
| Selecting landmarks shortest path | Google Patents | 2026-09-22 | **US20090228198A1** | Alta — seleção de landmarks para A*/ALT | Verificado |
| Contraction hierarchies / Geisberger route planning | Google Patents | 2026-09-22 | **US9175972B2**; **EP2757504B1** | Alta–média — CH em roteamento; contexto trânsito, não armazém | Verificado |
| Customizable route planning / landmarks mentions | Google Patents | 2026-09-22 | **US20130231862A1** (família CRP; menciona A*+landmarks no background) | Média — background ALT | Verificado como publicação; checar concessão na família |
| Hub label / landmarks background | Google Patents | 2026-09-22 | **US20120250535A1** | Média — background A*+landmarks | Verificado como publicação |
| JPS warehouse / Jump Point Search patent | Google Patents / Espacenet | 2026-09-22 | — | Potencial alta | **PENDENTE DE EXECUÇÃO PELO INVENTOR OU PELO AGENTE** |
| Portal/corridor pathfinding patents | Espacenet | 2026-09-22 | — | Média–alta | **PENDENTE DE EXECUÇÃO PELO INVENTOR OU PELO AGENTE** |
| WMS picking route optimization | Espacenet / Google Patents | 2026-09-22 | — | Média | **PENDENTE DE EXECUÇÃO PELO INVENTOR OU PELO AGENTE** |
| AMR/AGV multi-robot warehouse routing | Google Patents | 2026-09-22 | — | Média–alta | **PENDENTE DE EXECUÇÃO PELO INVENTOR OU PELO AGENTE** (não inventar número) |
| Busca BR: caminho mínimo / armazém / AMR | INPI BuscaWeb / base patentes BR | 2026-09-22 | — | A definir | **PENDENTE DE EXECUÇÃO PELO INVENTOR OU PELO AGENTE** |
| FPS + ALT warehouse | Google Patents | 2026-09-22 | — | Crítica para óbvio | **PENDENTE DE EXECUÇÃO PELO INVENTOR OU PELO AGENTE** |
| Literatura: Dijkstra; A*; JPS (Harabor); CH (Geisberger) | NPL | 2026-09-22 | N/A (NPL) | Alta | Listada no memorial; completar bibliografia |
| Consultas 1, 10, 11, 12, 14, 17, 19, 20, 22 (PT/EN restantes) | Espacenet + Google Patents + INPI | — | — | — | **PENDENTE DE EXECUÇÃO PELO INVENTOR OU PELO AGENTE** |
| Consultas 7, 8, 18, 23, 24, 25 | Espacenet + INPI | — | — | — | **PENDENTE DE EXECUÇÃO PELO INVENTOR OU PELO AGENTE** |

**Regra aplicada:** nenhum número foi inventado. Apenas documentos com número conferido em fonte pública nesta rodada foram preenchidos.

## Interpretação provisória (não é parecer de patenteabilidade)

A existência de **US7603229B2** e **US20090228198A1** torna especialmente arriscada qualquer reivindicação que se reduza a ALT + seleção de landmarks (inclusive geométrica).  
CH (**US9175972B2**) reforça o campo congestionado de pré-processamento offline + consulta online.  
Para Trilho B, a busca deve focar no **delta** (se houver) além de ALT+FPS em layout industrial — hoje **não isolado de forma convincente** neste dossiê.

## Próximos passos de busca (inventor / agente)

1. Rodar as 25 consultas em Espacenet (Worldwide) + Google Patents + BuscaWeb INPI.  
2. Exportar lista de famílias (WO/EP/US/BR) com datas de prioridade.  
3. Incluir NPL: Goldberg & Harrelson (MSR-TR-2004-24); Harabor & Grastien (JPS); Geisberger et al. (CH).  
4. Atualizar esta tabela **somente** com números verificáveis.
