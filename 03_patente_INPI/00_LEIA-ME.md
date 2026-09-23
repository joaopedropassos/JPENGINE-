# RASCUNHO DE TRABALHO — SEM VALOR DE PROTOCOLO

# 00 — LEIA-ME | Dossiê de trabalho PI (INPI) — processo candidato IIC / registro de software

**Inventor (PF):** João Pedro Pereira Passos — Palmas/TO.  
**Afiliação acadêmica informada:** UFT / Rede BIONORTE; leciona UNITINS.  
**Flag de cotitularidade institucional:** o inventor deve verificar contrato, estatuto, política de PI e eventuais cláusulas de cessão **ANTES** de protocolar qualquer pedido.  
**Objeto candidato:** processo IIC de planejamento de caminhos em grafo de layout espacial estático/estável (armazém / pátio / planta), com fase offline (prior estrutural + landmarks geométricos, ex. FPS + tabelas de distância) e fase online (consultas O-D com busca informada tipo ALT, admissibilidade e otimalidade nos testes internos).

## Propósito deste dossiê

Conjunto de **rascunhos técnicos** para revisão por **agente da propriedade industrial credenciado**.  
Este material **não** constitui protocolo no INPI, **não** gera prioridade oficial, **não** substitui parecer jurídico e **não** autoriza depósito sem revisão profissional.

## Índice dos nove arquivos

| Arquivo | Etapa | Conteúdo |
|---------|-------|----------|
| `00_LEIA-ME.md` | — | Índice, avisos, conclusão estratégica |
| `01_enquadramento_LPI.md` | 0 | Trilho A vs B; arts. 10 I e 10 V; efeito técnico |
| `02_trilho_A_registro_software.md` | 1 | Checklist operacional e-Software |
| `03_memorial_descritivo.md` | 2 | Memorial (rascunho) — seções 1–8 |
| `04_reivindicacoes_rascunho.md` | 3 | Claims [RASCUNHO] + estratégia |
| `05_resumo_e_figuras.md` | 4 | Resumo 150–250 palavras + figuras |
| `06_protocolo_busca_anterioridade.md` | 5 | Protocolo de busca PT/EN |
| `07_divulgacao_previa_e_graca.md` | 6 | Linha do tempo / Art. 12 LPI |
| `08_segredo_versus_deposito.md` | 7 | Segredo industrial vs depósito |
| `09_atos_da_semana.md` | 8 | Cinco atos da semana |

## Aviso de não-protocolo

Nenhuma peça deste dossiê deve ser enviada ao e-INPI / e-Software / e-Patentes sem revisão e assinatura sob responsabilidade de agente PI (quando aplicável) e do inventor.  
**Não anexar código-fonte** a este dossiê. Hash e ZIP de fonte ficam sob custódia do inventor até o protocolo do Trilho A.

## Conclusão estratégica honesta

1. **Trilho A agora (registro de programa de computador):** caminho operacional de baixo atrito relativo, protege a **expressão** do código (hash), validade da ordem de ~50 anos (Convenção de Berna), **não** cobre ideia, processo, API nem marca.  
2. **Trilho B (pedido de patente IIC):** **alto risco** se o delta inventivo documentável reduzir-se a **ALT + FPS** (ou equivalente geométrico óbvio) em layout de armazém. O estado da técnica clássico (Dijkstra, A*, ALT/landmarks, JPS, contraction hierarchies, portais/corredores, WMS/picking, gestores de frota AMR) é denso.  
3. Homologia / Wasserstein / persistência: **não essenciais** nas independentes; no máximo 1 dependente opcional, com nota de que v6/v7 **não** demonstraram superioridade topológica sobre geométrica.  
4. Divulgações (paper interno, one-pager, e-mails Delage/Automni, vídeo futuro): tratar como **possível divulgação prévia**; Art. 12 LPI = **hipótese a datar**, não certeza.

**Recomendação do redator para a semana:** executar Trilho A; manter Trilho B sob embargo até isolamento documental de delta não óbvio **além** de ALT+FPS, com evidência experimental amarrada (v5/v7) e revisão de agente PI.

---

## Cadeia de verificação (redator técnico — entrega)

| # | Item | Sim/Não | Comentário |
|---|------|---------|------------|
| 1 | Foram inventados números de patente, protocolo INPI ou prioridade unionista? | **NÃO** | Números de documento só quando verificáveis (ex.: US7603229B2, US20090228198A1, US9175972B2, EP2757504B1). Demais: PENDENTE DE EXECUÇÃO. |
| 2 | Foram inventados titulares, datas de divulgação, honorários de agente, opex, cliente ou patente deferida? | **NÃO** | Titularidade institucional e datas de divulgação marcadas como PENDENTE. Custo citado: apenas faixa oficial INPI GRU 730 (R$ 210,00), a confirmar na tabela vigente. |
| 3 | Cabeçalho obrigatório presente em cada peça? | **SIM** | «RASCUNHO DE TRABALHO — SEM VALOR DE PROTOCOLO» em todas as nove peças. |
| 4 | Foi afirmada patente deferida, prioridade oficial ou certeza de incidência do Art. 12 LPI? | **NÃO** | Art. 12 tratado como hipótese a datar. Nenhum protocolo, prioridade ou deferimento inventado. |
| 5 | Dados oficiais de registro de software alinhados a fontes gov.br (e-Software, e-CPF ICP-Brasil, GRU 730, hash, 10 dias)? | **SIM** | Referências: Guia Básico, FAQ Programas de Computador, Portaria INPI/PR nº 10/2025 / tabela 20_dez_25. |
| 6 | Portaria INPI/PR nº 411/2020 (Diretrizes IIC) citada somente após confirmação em fonte oficial? | **SIM** | Confirmada via gov.br (Portaria/INPI/PR nº 411, de 23/12/2020; vigência 01/01/2021). Nota: nomenclatura oficial é INPI/PR, não «DIRPA nº 411». |
| 7 | Seletor topológico / TDA descritos de modo reprodutível nas independentes? | **NÃO** | Núcleo reivindicado: offline/online + landmarks geométricos + reuso do prior. Homologia/Wasserstein/persistência no máximo em 1 dependente opcional, com nota v6/v7. |
| 8 | Conclusão honesta sobre risco ALT+FPS e Trilho B? | **SIM** | Se o delta inventivo documentado reduzir-se a ALT clássico + FPS em mapa de armazém, Trilho B (patente IIC) é de **alto risco**. Ato desta semana: **Trilho A** (registro de software). Trilho B só se isolar delta não óbvio documentado além de ALT+FPS. |

