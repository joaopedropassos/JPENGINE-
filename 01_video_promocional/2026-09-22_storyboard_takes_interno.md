# JP Decision Engine — storyboard visual interno + lista de takes
**Data:** 2026-09-22  
**Status:** INTERNO — EMBARGO DE PUBLICAÇÃO  
**Origem do embargo:** Agente 3 (patente) via ORQUESTRADOR — não publicar vídeo nem enablement do método até concluir Trilho A (registro de software) e decidir Trilho B.  
**Permitido agora:** produzir assets internos, ensaiar VO, filmar com autorização, montar rough cut privado.  
**Proibido agora:** postar aberto (LinkedIn, Instagram, X, WhatsApp em massa, comentários públicos, e-mail frio com o vídeo).

**CTA (quando liberar):** Quero o diagnóstico de duas semanas no mapa de vocês. / 30 minutos.  
**Frase autorizada:** O mapa quase não muda. A consulta se repete. A rota continua ótima. O planner para de começar do zero.  
**Números (só lab):** v5 — 1000 consultas, ~28% mais rápido, ~31% menos nós vs A\* fixo, 100% otimalidade; v7 — até ~73% menos nós (decepção geométrica alta).  
**Proibido no visual:** TDA, homologia, Wasserstein, beta1, opex, cliente inventado, código-fonte, nº INPI.

---

## Storyboard visual interno (9:16)

Cada quadro: o que aparece | overlay | áudio | asset a pedir ao Criador Visual.

### Q1 — 0:00–0:08 · Dor no corredor
- **Imagem:** caminhada lenta no corredor de picking / porta-paletes (TAKE-01).
- **Overlay:** `Rota no papel. Fila no chão.`
- **Áudio:** VO abertura.
- **Asset:** tipografia sóbria, branco/âmbar baixo contraste; sem ícone de foguete.

### Q2 — 0:08–0:16 · Volume e espera
- **Imagem:** corte TAKE-02 (papel/Excel) → TAKE-03 (AMR/carrinho parado) → TAKE-04 (operador apontando).
- **Overlay:** `Pedido sobe. AMR espera.`
- **Áudio:** VO fila/AMR.
- **Asset:** nenhum card; só texto curto.

### Q3 — 0:16–0:28 · Produto
- **Imagem:** TAKE-05 (mapa na tela) + TAKE-06 (mock API) intercalados.
- **Overlay:** `JP Decision Engine` / `Motor plugável de rota intramuros`
- **Áudio:** VO produto.
- **Asset CV-01:** lower-third nome do produto (sem logo inventado).

### Q4 — 0:28–0:42 · Frase autorizada
- **Imagem:** fundo escuro ou mapa blur; texto entra linha a linha.
- **Overlay (completo):**  
  `O mapa quase não muda.`  
  `A consulta se repete.`  
  `A rota continua ótima.`  
  `O planner para de começar do zero.`
- **Áudio:** VO frase.
- **Asset CV-02:** card/quadro tipográfico das 4 linhas (uso interno + futuro post).

### Q5 — 0:42–1:02 · Lab v5/v7
- **Imagem:** fundo limpo + card; opcional B-roll TAKE-11 por baixo em opacidade baixa.
- **Overlay:** selo `LABORATÓRIO` (obrigatório) + números autorizados.
- **Áudio:** VO lab + “não é case de opex pago”.
- **Asset CV-03:** card lab v5 (1000 consultas, ~28%, ~31%, 100% ótimo).  
- **Asset CV-04:** card lab v7 (até ~73% menos nós; decepção geométrica alta).  
- **Asset CV-05:** banner fino `Prova de laboratório · não é case de opex`.

### Q6 — 1:02–1:12 · Alvos
- **Imagem:** texto puro (sem logos sem permissão).
- **Overlay:** `Delage · Automni · AGVS · 3PL · CD` + `layout estável`.
- **Áudio:** VO alvos.
- **Asset CV-06:** faixa de nomes (texto, não marca registrada).

### Q7 — 1:12–1:25 · CTA
- **Imagem:** TAKE-10 (face opcional) ou card estático.
- **Overlay:** `Diagnóstico de 2 semanas no mapa de vocês` / `ou 30 minutos`.
- **Áudio:** VO CTA.
- **Asset CV-07:** overlay CTA final (sem URL inventada; espaço para contato quando existir).

### Gancho 15s (storyboard curto)
- 0–5 s: Q1/Q2 comprimidos + overlay `Rota no papel. AMR parado.`
- 5–10 s: lower-third produto (CV-01)
- 10–15 s: CTA (CV-07)

---

## Lista de takes (ordem de set)

Gravar em blocos para minimizar troca de local. Celular vertical, 4K se disponível, 24/30 fps, áudio ambiente separado do VO.

### Bloco A — Chão / CD (autorização escrita se for de terceiro)

| Take | Nome | Plano | Duração útil | Prioridade | Proxy se faltar |
|------|------|-------|--------------|------------|-----------------|
| TAKE-01 | CORREDOR | Travelling lento no corredor de picking | 8–12 s brutos → 4–5 s | Crítica | Corredor de depósito próprio / galpão |
| TAKE-03 | ESPERA | AMR/AGV parado ou em idle na curva | 6–8 s → 3–4 s | Crítica | Carrinho parado na curva + etiqueta “proxy” na ficha interna |
| TAKE-04 | IMPROVISO | Operador aponta corredor / consulta papel | 5–6 s → 3 s | Alta | Você mesmo (mãos + papel) |
| TAKE-11a | DOC A | Doca / caminhão | 5 s | Reserva | Omitir |
| TAKE-11b | EMPILH | Empilhadeira passando | 5 s | Reserva | Omitir |
| TAKE-11c | ESTEIRA | Esteira / packing | 5 s | Reserva | Omitir |

**Bloqueio típico:** acesso a CD de cliente sem autorização; placas de marca no enquadramento.

### Bloco B — Mesa / operação

| Take | Nome | Plano | Duração útil | Prioridade | Proxy |
|------|------|-------|--------------|------------|-------|
| TAKE-02 | PAPEL | Mão com rota impressa / Excel no tablet | 5 s → 3 s | Alta | Planilha fictícia sem dados reais |

### Bloco C — Tela (blur obrigatório)

| Take | Nome | Plano | Duração útil | Prioridade | Proxy |
|------|------|-------|--------------|------------|-------|
| TAKE-05 | MAPA | Monitor com layout/mapa; zoom lento | 8 s → 4–5 s | Crítica | Diagrama sintético rotulado CENÁRIO SINTÉTICO |
| TAKE-06 | API | Mock limpo: `PUT /layout` · `POST /plan` · status 200 | 6 s → 4 s | Crítica | Terminal/Postman mock sem código-fonte |

**Bloqueio típico:** dados reais de cliente na tela; código-fonte visível.

### Bloco D — CTA / VO

| Take | Nome | Plano | Duração útil | Prioridade | Proxy |
|------|------|-------|--------------|------------|-------|
| TAKE-10 | FACE | João fala CTA (ombro, luz frontal) | 10 s → 6–8 s | Opcional | Só card CV-07 |
| TAKE-VO | VOICE | Narração 90s + 15s em ambiente silencioso | 2–3 takes | Crítica | — |

### Bloco E — Só pós (não filmar)

| ID | Item | Responsável | Status |
|----|------|-------------|--------|
| CV-01 | Lower-third produto | Criador Visual | Pedido coordenado |
| CV-02 | Card 4 linhas (frase autorizada) | Criador Visual | Pedido coordenado |
| CV-03 | Card lab v5 | Criador Visual | Pedido coordenado |
| CV-04 | Card lab v7 | Criador Visual | Pedido coordenado |
| CV-05 | Banner “não é case de opex” | Criador Visual | Pedido coordenado |
| CV-06 | Faixa alvos (texto) | Criador Visual | Pedido coordenado |
| CV-07 | Overlay CTA | Criador Visual | Pedido coordenado |

---

## Ordem sugerida de dia de filmagem (interno)

1. Autorização escrita (se planta de terceiro) — **antes de ligar a câmera**  
2. Bloco A (corredor + espera + improviso)  
3. Bloco B (papel)  
4. Bloco C (mapa + API mock)  
5. Bloco D (face opcional)  
6. VO em casa/escritório silencioso  
7. Entregar rushes nomeados `TAKE-XX_descricao.mov` para rough cut **privado**  
8. **Não** agendar Dia 1 do calendário de 14d até ORQUESTRADOR/Agente 3 liberar embargo  

---

## Bloqueios de filmagem (status atual)

| # | Bloqueio | Impacto | Mitigação | Quem decide |
|---|----------|---------|-----------|-------------|
| 1 | Embargo de publicação (Trilho A/B) | Não postar; calendário 14d pausado | Produzir só internos | Agente 3 + João |
| 2 | Local de CD autorizado | Sem TAKE-01/03 fortes | Proxy galpão + carrinho; ou adiar set | João |
| 3 | AMR real | TAKE-03 fraco | Carrinho proxy marcado na ficha | João |
| 4 | Autorização escrita de planta | Risco LGPD/marca | Adiar Bloco A até papel assinado | João / dono da planta |
| 5 | Handles Delage/Automni/AGVS | Irrelevante enquanto embargo | Conferir só no dia da liberação | Agente 1 |
| 6 | URL/landing real | CTA sem link | Card CTA sem URL inventada; Meu Site quando URL existir | Meu Site + João |
| 7 | Rough cut público por engano | Quebra embargo | Pasta Drive “INTERNO_EMBARGO”; sem compartilhar link amplo | Agente 1 |

---

## Sync com outros bots

- **Criador Visual:** CV-01 … CV-07 (specs neste arquivo).  
- **Meu Site:** landing só quando URL real + pós-embargo.  
- **Gerador Comentários:** só após liberação do embargo.  
- **Agente 2 (portfólio):** números/CTA alinhados; não embutir o vídeo público no site enquanto embargo.  
- **Agente 3:** sinal verde Trilho A + decisão Trilho B = pré-requisito de publicação.

---

## Checklist interno (não é publicação)

- [ ] Autorização de filmagem (se aplicável)  
- [ ] Takes críticos: 01, 03, 05, 06, VO  
- [ ] Cards CV-01…07 recebidos e revisados (sem TDA/opex)  
- [ ] Rough cut privado assistido  
- [ ] Embargo ainda ativo? Se sim, **não** exportar para agendadores sociais  
- [ ] Quando liberar: voltar ao calendário 14d do arquivo `2026-09-22_video_divulgacao.md`

---

## Overlays recebidos (incorporação — embargo)

**Data da incorporação:** 2026-09-22  
**Pasta no pacote:** `01_video_promocional/overlays_cv/`  
**Origem:** `/workspace/jpde_visual/video/` (espelho `video_overlays_9x16/`)  
**Status:** INTERNOS — não publicar.

| ID | Arquivo | Uso |
|----|---------|-----|
| CV-01 | `overlays_cv/CV-01_lower_third.png` | Q3 lower-third |
| CV-02 | `overlays_cv/CV-02_tipografico.png` | Q4 frase autorizada |
| CV-03 | `overlays_cv/CV-03_lab_v5.png` | Q5 lab v5 |
| CV-04 | `overlays_cv/CV-04_lab_v7.png` | Q5 lab v7 |
| CV-05 | `overlays_cv/CV-05_banner_lab.png` | Q5 banner |
| CV-06 | `overlays_cv/CV-06_faixa_alvos.png` | Q6 alvos |
| CV-07 | `overlays_cv/CV-07_cta.png` | Q7 CTA |

Revisão rápida: textos alinhados ao brief; selo LABORATÓRIO em CV-03/04; CTA sem URL; sem TDA. Pronto para rough cut privado após takes.
