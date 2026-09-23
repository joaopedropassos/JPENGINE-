# MANIFEST — Figuras técnicas INPI (Etapa 4)

Estilo: desenho técnico P&B; matplotlib; 300 DPI; largura ≈ 16 cm (6,3 in).
Sem logotipo, sem fotos, sem cores de marketing, sem números de patente inventados.

| Arquivo | Legenda sugerida | DPI | Largura |
|---------|------------------|-----|----------|
| `fig01_fluxo_offline.png` | Fluxo offline: layout → grafo → seleção de k landmarks geométricos (FPS) → tabelas de distância / prior estrutural. | 300 | ≈16 cm |
| `fig02_fluxo_online.png` | Fluxo online: consulta O–D → heurística tipo ALT (landmarks) → busca informada → rota; invalidação do prior se o mapa mudar. | 300 | ≈16 cm |
| `fig03_mapa_DG_alto.png` | Esquema de planta com corredor tortuoso; anotação conceitual DG = d_grafo / d_Manhattan. | 300 | ≈16 cm |
| `fig04_amortizacao_consultas.png` | Q* (nº de consultas) vs custo acumulado: curvas conceituais A* fixo vs prior+landmarks (amortização). | 300 | ≈16 cm |
| `fig05_api_blocos.png` | Arquitetura em blocos: Layout \| Grafo \| Prior \| Planner \| Rota. | 300 | ≈16 cm |
| `fig06_admissibilidade.png` | Desigualdade triangular com landmark (origem–landmark–destino) e admissibilidade da heurística. | 300 | ≈16 cm |
| `fig07_checklist_trilho_A.png` | Checklist Trilho A: e-INPI → e-CPF → GRU 730 → hash SHA-512 → e-Software → DV. | 300 | ≈16 cm |
| `fig08_trilhos_AB.png` | Trilhos paralelos: A registro de software (expressão/hash) vs B pedido de invenção IIC (processo/efeito técnico candidato). | 300 | ≈16 cm |
| `fig09_landmarks_FPS.png` | Fig. 3 — Landmarks geométricos (FPS): mesma planta esquemática com k landmarks L1…Lk espalhados (farthest-point sampling). | 300 | ≈16 cm |
| `fig10_expansao_Astar_vs_prior.png` | Fig. 5 — Comparativo qualitativo de expansão: A* heurística fixa (nuvem maior) vs busca com prior de landmarks (nuvem menor); ilustração qualitativa — dados internos v5/v7; não é certificado INPI. | 300 | ≈16 cm |
| `fig11_invalidacao_prior.png` | Fig. 7 — Diagrama de estados: Prior válido → Evento de mudança de layout → Prior inválido → Reexecução offline → Prior válido. | 300 | ≈16 cm |
| `fig12_fronteira_TDA.png` | Fig. 9 — Fronteira do que não se reivindica: nuvem tracejada TDA / homologia / Wasserstein / persistência com carimbo «não essencial — ver nota v6/v7». | 300 | ≈16 cm |

## Observações

- **fig04:** curvas esquemáticas ilustrativas da ideia de amortização; eixos rotulados conceitualmente; não são dados experimentais medidos.
- **fig03:** planta esquemática conceitual; DG anotado apenas como definição (sem valores medidos).
- **fig08:** não inclui número de pedido nem afirmação de deferimento.
- **fig09:** esquema FPS sem pseudocódigo; landmarks geométricos L1…Lk.
- **fig10:** ilustração qualitativa apenas; sem números medidos inventados; rodapé de não-certificação INPI.
- **fig11:** ciclo de invalidação/reexecução do prior quando o layout muda.
- **fig12:** delimita matérias auxiliares (TDA etc.) como não essenciais (nota v6/v7).
- Formato: PNG RGB, linhas pretas sobre fundo branco.
- Gerador das figuras 09–12: `gerar_fig09_12.py` (matplotlib).
