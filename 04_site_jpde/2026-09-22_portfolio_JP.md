# JP Decision Engine

**Portfólio técnico-comercial · uma página / PDF**  
**Data do documento:** 2026-09-22  
**Produto:** motor plugável de rota intramuros  
**Dono técnico:** João Pedro Pereira Passos — Palmas/TO  
**Público:** product manager de WMS · CEO / liderança de frota AMR  

> **Laboratório ≠ operação.** Os números deste documento vêm de provas de laboratório (v5 e v7). Não são case de opex pago, não garantem economia de metros nem de turno, e não substituem medição no mapa do cliente.

---

## 1. Capa e uma frase

### JP Decision Engine
Motor plugável de rota intramuros para WMS e frota AMR.

**Uma frase**

O mapa quase não muda. A consulta se repete. A rota continua ótima. O planner para de começar do zero.

**Subtítulo de capa (opcional, uma linha)**

Entra no sistema que você já opera, lê o layout estável e devolve a próxima rota — sem trocar o WMS nem a frota.

**Marcadores de capa (texto puro; sem logo inventado)**

- Nome do produto: JP Decision Engine  
- Posição: rota intramuros · plugável  
- Escopo: laboratório v5–v7 documentado · operação sob diagnóstico/piloto  
- Contato: João Pedro Pereira Passos · Palmas/TO · `joaopedro.passos@mail.uft.edu.br`  

*Não há neste documento: logo oficial, CNPJ, marca registrada, domínio público no ar nem URL comercial ativa.*

---

## 2. Problema

No corredor do CD, a rota intramuros ainda vive no papel, no Excel ou na cabeça de quem conhece o layout.

Quando o volume sobe:

- a fila trava no chão;
- o AMR espera a próxima decisão;
- o operador improvisa o próximo passo;
- o planner recomeça do zero **no mesmo mapa** que quase não mudou.

Para o product manager de WMS, isso aparece como módulo de roteamento frágil, integração cara e retrabalho a cada onda. Para o CEO de AMR, aparece como frota ociosa, fila na curva e confiança baixa na decisão automática.

O problema não é “falta de sistema”. O problema é **recomputar do zero uma decisão que o layout estável já permitiria reaproveitar** — com otimalidade e previsibilidade.

---

## 3. Solução em três blocos

O JP Decision Engine é um **motor de decisão de rota intramuros**, não um WMS e não um robô. Ele se encaixa em três modos de uso.

### 3.1 Offline — prova no mapa estático

- Recebe um layout estável (planta / grafo / mapa que o time já usa).
- Roda consultas de rota em bancada (laboratório ou sandbox do integrador).
- Compara planner de referência (ex.: A\* com heurística fixa) com o motor JP-Geo.
- Entrega relatório de nós expandido, tempo de consulta e otimalidade — **sempre rotulado como laboratório** quando a fonte for v5/v7.

**Para quem:** PM de WMS validando módulo; time de AMR validando planner antes de plug na frota.

### 3.2 Online — decisão na onda / na missão

- O mapa permanece o mesmo entre consultas repetidas.
- O motor devolve a próxima rota sem forçar o planner a recomeçar do zero a cada pedido.
- Opera ao lado do WMS ou do orquestrador de frota: quem manda no inventário e no robô continua sendo o sistema do cliente.

**Para quem:** operação com layout estável, ondas repetidas, corredores conhecidos.

### 3.3 API — encaixe sem trocar o stack

Dois endpoints de contrato (núcleo comercial):

| Método | Recurso | Papel |
|--------|---------|--------|
| `PUT` | `/layout` | Publica / atualiza o mapa intramuros que o motor deve conhecer |
| `POST` | `/plan` | Solicita a rota / plano a partir de origem, destino e restrições do turno |

Fluxo típico: o integrador envia o layout uma vez (ou quando o mapa muda de verdade) via `PUT /layout`; a cada missão ou picking path, chama `POST /plan` e consome a resposta no WMS ou no fleet manager.

**O que a API não é:** substituto de inventário, de WCS, de telemetria do robô ou de roteirização de rua.

---

## 4. Prova — tabela honesta (laboratório v5 e v7)

**Fonte:** provas de laboratório JP-Geo, versões **v5** e **v7** (números alinhados ao pacote de divulgação 2026-09-22).  
**Baseline:** A\* com heurística fixa.  
**Leitura correta:** métricas de **busca** (tempo relativo, nós, otimalidade).  

### Aviso obrigatório

> **Números de nós e milissegundos não são economia de metros nem de turno.**  
> Redução de nós ou ganho de tempo de consulta em laboratório **não** implica, por si, menos metros andados, menos opex, menos horas de mão de obra ou ROI de turno. Qualquer extrapolação operacional exige medição no mapa e no fluxo do cliente (diagnóstico / piloto).

### Tabela — o que a prova diz (e só o que ela diz)

| Versão | Condição | Métrica | Resultado (lab) | O que **não** afirma |
|--------|----------|---------|-----------------|----------------------|
| **v5** | 1.000 consultas | Tempo vs A\* fixo | JP-Geo cerca de **28% mais rápido** (v5) | Economia de metros ou de turno |
| **v5** | 1.000 consultas | Nós expandidos vs A\* fixo | cerca de **31% menos nós** (v5) | Menos opex pago em CD real |
| **v5** | 1.000 consultas | Otimalidade | **100%** de otimalidade (v5) | Garantia de SLA operacional |
| **v7** | Decepção geométrica alta | Nós vs A\* | Geo cortou até cerca de **73% dos nós** (v7) | Case de opex pago / ROI contratado |

### Como usar esta tabela com comprador técnico

1. Dizê-la em voz alta como **prova de laboratório**.  
2. Separar da conversa de preço e de piloto.  
3. No diagnóstico de duas semanas, repetir a medição **no mapa deles** — aí sim fala-se de operação.

---

## 5. O que não é

Checklist curto para PM de WMS e CEO de AMR:

| Não é | Por quê |
|-------|---------|
| **WMS** | Não gerencia inventário, onda, packing nem billing. Encaixa-se *no* WMS. |
| **AMR / frota** | Não é hardware, firmware nem fleet manager. Entrega decisão de rota para quem já opera a frota. |
| **Roteirizador de rua** | Domínio é **intramuros** (corredor, picking, layout de CD), não malha urbana nem última milha. |
| **TDA (e adjacências de pesquisa pura)** | Fora do **núcleo comercial**. Não é diferencial de venda deste portfólio; não entra em pitch, pricing nem CTA. |

Também **não** vendemos neste documento: garantia de opex, case de opex pago, patente como argumento comercial, paper como prova de chão, nem “ficar rico com automação”.

---

## 6. Ofertas e próximo passo

Três ofertas comerciais claras. Preços em faixa (BRL). Escopo fino no kickoff.

| Oferta | Duração | Faixa | O que entrega | Próximo passo típico |
|--------|---------|-------|---------------|----------------------|
| **Diagnóstico** | 2 semanas | R$ 8 mil – R$ 15 mil | Mapa de vocês no motor; leitura honesta lab × operação; go/no-go para piloto | Kickoff com layout + 1–2 fluxos críticos |
| **Piloto** | 90 dias | R$ 25 mil – R$ 60 mil | `PUT /layout` + `POST /plan` no ambiente acordado; métricas combinadas; decisão de licença | Contrato de piloto com critérios de sucesso |
| **Licença por site** | mensal | R$ 3 mil – R$ 12 mil / mês / site | Uso contínuo do motor no site licenciado | Após piloto aprovado |

### CTA único (alinhar a site, PDF e conversa)

**Quero o diagnóstico de duas semanas no mapa de vocês.**  
Alternativa leve: **30 minutos** para ver se faz sentido.

Contato comercial/técnico do fundador: `joaopedro.passos@mail.uft.edu.br` · Palmas/TO.

---

## 7. Mini bio (sem inflar títulos)

**João Pedro Pereira Passos** constrói o JP Decision Engine em Palmas/TO: motor de rota intramuros pensado para encaixar em WMS e frota AMR sem trocar o stack do cliente.

Atua também na formação acadêmica (UFT / Rede BIONORTE; docência em Palmas/TO). Neste portfólio comercial, a credencial que importa é **capacidade de provar em laboratório (v5–v7) e de medir no mapa do comprador** — não cargo de C-level inventado, não CNPJ decorativo, não marca registrada.

ORCID (referência acadêmica, se o leitor quiser): `0000-0001-7181-4587`.

---

## 8. CENARIO SINTETICO

> **Rótulo obrigatório:** isto é um **CENARIO SINTETICO**.  
> **Não é cliente.** Não é case. Não é opex pago. Não use como prova de operação.

**CENARIO SINTETICO — CD regional com layout estável e frota AMR em rampa**

- **Persona A:** product manager de WMS que precisa modular rota intramuros sem reescrever o core.  
- **Persona B:** CEO de empresa de AMR que perde ciclo com planner recomeçando do zero no mesmo mapa.  
- **Situação:** corredores fixos, ondas repetidas, mapa que muda pouco entre turnos.  
- **Dor:** fila na curva; operador improvisando; integração “custom” a cada fornecedor.  
- **Uso do motor:** `PUT /layout` no mapa sintético; `POST /plan` por missão; comparação interna com A\* fixo **no mesmo mapa sintético**.  
- **Leitura permitida:** se os números de lab (v5/v7) se repetirem *naquele* mapa, abre-se conversa de diagnóstico real — ainda sem afirmar metros ou turno.  
- **Leitura proibida:** transformar este parágrafo em “cliente X economizou Y%”.

---

## 9. Especificação visual

Para site one-pager e PDF. Sem logo inventado: use **wordmark tipográfico** “JP Decision Engine” até existir marca oficial.

### 9.1 Princípios

- Tom B2B seco (CD / WMS / AMR), sem estética “startup neon”.  
- Hierarquia: problema → solução → prova lab → o que não é → oferta → CTA.  
- Todo card de número leva o selo **Laboratório (v5)** ou **Laboratório (v7)**.  
- O aviso de nós/ms aparece **junto** da tabela, não no rodapé escondido.

### 9.2 Paleta sugerida (neutra; ajustável)

| Papel | Hex | Uso |
|-------|-----|-----|
| Fundo | `#F7F4EC` | Página / PDF |
| Texto | `#141C2B` | Corpo |
| Painel / capa | `#1B2A41` | Faixa de capa |
| Acento | `#C8A024` | CTA e selos “Laboratório” |
| Branco card | `#FFFFFF` | Blocos de oferta e tabela |

*Paleta de referência tipográfica/institucional já usada em materiais do autor; não constitui identidade oficial do produto.*

### 9.3 Tipografia

- Títulos: sans geométrica legível (ex.: Inter / Source Sans) · peso 600–700.  
- Corpo: 16–18 px web / 11–12 pt PDF.  
- Código / endpoints: mono (`PUT /layout`, `POST /plan`).

### 9.4 Layout one-pager (web)

1. Hero: frase + CTA diagnóstico.  
2. Problema (2 colunas: WMS | AMR).  
3. Três cards: Offline · Online · API.  
4. Tabela lab + aviso obrigatório.  
5. “O que não é” em quatro chips.  
6. Ofertas em três colunas + CTA.  
7. Mini bio + CENARIO SINTETICO em box com borda tracejada.  
8. Rodapé: e-mail · Palmas/TO · data do doc · *sem URL inventada*.

### 9.5 Layout PDF (A4)

- Margens ≥ 1,5 cm.  
- Capa em 1/3 da primeira página; resto em seções numeradas iguais a este Markdown.  
- Quebra de página **antes** da tabela lab, para o aviso não ficar órfão.  
- Marca d’água leve opcional: `LABORATÓRIO — NÃO É OPEX`.

### 9.6 Assets a **não** inventar

- Logo vetorial, ícone de app, mock de domínio `.com.br` no ar, CNPJ, selo “patente”, print de dashboard de cliente real sem autorização.

---

## 10. Índice de arquivos e README de montagem

### 10.1 Índice (pacote portfólio)

| Arquivo | Função |
|---------|--------|
| `02_portfolio/2026-09-22_portfolio_JP.md` | **Este documento** — fonte master (site + PDF) |
| `01_video_promocional/2026-09-22_video_divulgacao.md` | Roteiros, legendas, calendário; números lab alinhados |
| `01_video_promocional/2026-09-22_jpde_90s.srt` | Legendas do vídeo 90s |
| `02_portfolio/README_montagem.md` | Passo a passo de publicação (abaixo, seção 10.2) |
| *(a criar)* `02_portfolio/assets/` | Wordmark, prints de API mock, diagramas — só com material real |
| *(a criar)* export PDF / HTML | Gerados a partir deste Markdown |

### 10.2 README de montagem

```text
README — montagem do portfólio JP Decision Engine
=================================================

1. Fonte da verdade
   - Edite apenas 2026-09-22_portfolio_JP.md (ou a data nova).
   - Números de prova: só os da tabela v5/v7 deste arquivo
     (alinhados a 01_video_promocional/).

2. Site de uma página
   - Converter o Markdown para HTML estático (Pandoc, 11ty, ou
     gerador que você já usa).
   - Manter a ordem das seções 1→8 no hero→rodapé.
   - CTA fixo: diagnóstico de 2 semanas / 30 minutos.
   - Não publicar URL comercial inventada; use domínio real
     quando existir.

3. PDF
   - Exportar A4 a partir do mesmo Markdown.
   - Garantir aviso de nós/ms na mesma página da tabela.
   - Rodapé: data + “Laboratório ≠ operação”.

4. Checagem pré-publicação
   [ ] Todo número cita v5 ou v7
   [ ] TDA não aparece como diferencial de venda
   [ ] CENARIO SINTETICO rotulado (nunca como cliente)
   [ ] Sem logo/CNPJ/marca/URL inventados
   [ ] Lab separado de operação
   [ ] Aviso: nós/ms ≠ metros ≠ turno

5. Alinhamento com vídeo
   - Mesma frase de capa, mesmos números, mesmo CTA
     que 01_video_promocional/2026-09-22_video_divulgacao.md.
```

### 10.3 Verificação deste arquivo

| Regra | Status |
|-------|--------|
| Arquivo em `02_portfolio/2026-09-22_portfolio_JP.md` | OK |
| Capa + uma frase | OK |
| Problema | OK |
| Solução offline / online / API (`PUT /layout`, `POST /plan`) | OK |
| Tabela honesta v5 e v7; todo número cita v5 ou v7 | OK |
| O que não é: WMS, AMR, roteirizador de rua, TDA | OK |
| TDA **fora** do diferencial de venda | OK |
| Ofertas (diagnóstico / piloto / licença) + próximo passo | OK |
| Mini bio sem títulos inflados | OK |
| CENARIO SINTETICO rotulado; nunca como cliente | OK |
| Especificação visual | OK |
| Índice + README de montagem | OK |
| Sem logo, CNPJ, marca registrada, URL no ar inventados | OK |
| Laboratório ≠ operação | OK |
| Aviso: nós e ms ≠ metros ≠ turno | OK |

---

*Fim do portfólio master · 2026-09-22 · João Pedro Pereira Passos · JP Decision Engine*
