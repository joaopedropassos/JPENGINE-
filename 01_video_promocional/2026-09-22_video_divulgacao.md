# JP Decision Engine — vídeo e divulgação
**Data:** 2026-09-22  
**Produto:** JP Decision Engine (motor plugável de rota intramuros)  
**Dono:** João Pedro Pereira Passos — Palmas/TO  
**Alvos:** Delage (módulo WMS), Automni/AGVS (frota), 3PL e CDs com layout estável  
**CTA único:** 30 minutos **ou** diagnóstico de 2 semanas  
**CTA falado/escrito:** Quero o diagnóstico de duas semanas no mapa de vocês.  
**Restrições:** sem TDA, sem homologia, sem paper, sem “ficar rico”, sem garantia de opex, sem case de opex pago.

**EMBARGO DE PUBLICAÇÃO (2026-09-22):** Agente 3 recomenda não publicar vídeo nem enablement do método até concluir Trilho A (registro de software) e decidir Trilho B. Assets internos e filmagem autorizada: OK. Postagem aberta, comentários públicos e calendário 14d: PAUSADOS. Ver `2026-09-22_storyboard_takes_interno.md`.


---

## Roteiro 90s

Formato vertical 9:16. Narração em tom direto (dono de CD / integrador AMR / gerente de WMS). Duração-alvo: **75–85 s** (cabe em 90 s lida em voz alta).

| Time-code | Texto na tela | Narração |
|-----------|---------------|----------|
| 0:00–0:08 | Rota no papel. Fila no chão. | No corredor do CD, a rota ainda vive no papel, no Excel ou na cabeça de quem conhece o layout. |
| 0:08–0:16 | Pedido sobe. AMR espera. | Quando o volume sobe, a fila trava. O AMR espera. O operador improvisa o próximo passo. |
| 0:16–0:28 | JP Decision Engine · rota intramuros | O JP Decision Engine é um motor plugável de rota intramuros. Ele entra no WMS ou na frota, lê o mapa que você já usa e devolve a próxima rota sem trocar o sistema. |
| 0:28–0:42 | Mapa estável · planner sem recomeçar do zero | O mapa quase não muda. A consulta se repete. A rota continua ótima. O planner para de começar do zero. |
| 0:42–1:02 | Lab v5–v7 · não é case de opex | Em laboratório, na v5, em mil consultas, o JP-Geo ficou cerca de 28% mais rápido e 31% com menos nós que A\* fixo, com 100% de otimalidade. Na v7, em decepção geométrica alta, o Geo cortou até cerca de 73% dos nós frente ao A\*. Isso é prova de laboratório, não case de opex pago. |
| 1:02–1:12 | Delage · Automni · AGVS · 3PL · CD | Para Delage, Automni, AGVS, 3PL e CD com layout estável: mesma lógica. Menos retrabalho na decisão. Mais fluxo no chão. |
| 1:12–1:25 | Diagnóstico de 2 semanas · ou 30 min | Quero o diagnóstico de duas semanas no mapa de vocês. Ou 30 minutos para ver se faz sentido. |

**Narração contínua (colar no teleprompter):**

No corredor do CD, a rota ainda vive no papel, no Excel ou na cabeça de quem conhece o layout. Quando o volume sobe, a fila trava. O AMR espera. O operador improvisa o próximo passo. O JP Decision Engine é um motor plugável de rota intramuros. Ele entra no WMS ou na frota, lê o mapa que você já usa e devolve a próxima rota sem trocar o sistema. O mapa quase não muda. A consulta se repete. A rota continua ótima. O planner para de começar do zero. Em laboratório, na v5, em mil consultas, o JP-Geo ficou cerca de 28% mais rápido e 31% com menos nós que A-estrela fixo, com 100% de otimalidade. Na v7, em decepção geométrica alta, o Geo cortou até cerca de 73% dos nós frente ao A-estrela. Isso é prova de laboratório, não case de opex pago. Para Delage, Automni, AGVS, 3PL e CD com layout estável: mesma lógica. Menos retrabalho na decisão. Mais fluxo no chão. Quero o diagnóstico de duas semanas no mapa de vocês. Ou 30 minutos para ver se faz sentido.

**Checagem de duração:** ~185 palavras ≈ 75–85 s em ritmo B2B calmo (≤ 90 s).

---

## Roteiro 15s

| Time-code | Texto na tela | Narração |
|-----------|---------------|----------|
| 0:00–0:05 | Rota no papel. AMR parado. | Rota no papel. AMR parado. Planner recomeçando do zero no mesmo mapa. |
| 0:05–0:10 | Motor plugável de rota intramuros | JP Decision Engine: motor plugável de rota intramuros. |
| 0:10–0:15 | Diagnóstico de 2 semanas | Quero o diagnóstico de duas semanas no mapa de vocês. |

**Narração contínua:**

Rota no papel. AMR parado. Planner recomeçando do zero no mesmo mapa. JP Decision Engine: motor plugável de rota intramuros. Quero o diagnóstico de duas semanas no mapa de vocês.

---

## Shot-list

Filmável com celular (vertical). Prioridade: chão de CD / planta / tela / face opcional.

| # | Plano | Onde / como | Duração | Notas |
|---|-------|-------------|---------|-------|
| 1 | Corredor de picking / porta-paletes | CD ou planta parceira; caminhada lenta | 4–5 s | Sem placa de cliente se não houver autorização |
| 2 | Mão com papel / tablet / Excel | Mesa de operação | 3 s | Rota “no papel” |
| 3 | AMR ou AGV parado / em espera | Frota ou stock footage autorizado | 3–4 s | Se não tiver robô, use carrinho parado na curva |
| 4 | Operador apontando corredor | Chão | 3 s | Improviso visual |
| 5 | Tela: mapa / layout estável | Notebook ou monitor | 4–5 s | Blur de dados sensíveis |
| 6 | Tela: chamada API (PUT layout / POST plan) | Mock limpo, sem código-fonte | 4 s | Só endpoints e status |
| 7 | Overlay texto: frase autorizada | Pós-produção | 6–8 s | “O mapa quase não muda…” |
| 8 | Card lab v5 / v7 | Pós-produção | 8–10 s | Números autorizados; rótulo **Laboratório** |
| 9 | Logos ou nomes: Delage · Automni · AGVS · 3PL · CD | Pós (texto, sem logo sem permissão) | 4 s | Preferir texto puro |
| 10 | CTA final + contato | Face opcional OU card estático | 6–8 s | Diagnóstico 2 semanas / 30 min |
| 11 | B-roll: empilhadeira / esteira / doca | CD | 3–4 s cada | Reserva para cortes |

**Áudio:** voz seca + ruído baixo de CD (ou silêncio). Sem trilha “startup”.

---

## SRT

Arquivo de legendas da versão longa (`2026-09-22_jpde_90s.srt`):

```srt
1
00:00:00,000 --> 00:00:08,000
No corredor do CD, a rota ainda vive no papel,
no Excel ou na cabeça de quem conhece o layout.

2
00:00:08,000 --> 00:00:16,000
Quando o volume sobe, a fila trava.
O AMR espera. O operador improvisa o próximo passo.

3
00:00:16,000 --> 00:00:28,000
O JP Decision Engine é um motor plugável de rota intramuros.
Ele entra no WMS ou na frota, lê o mapa que você já usa
e devolve a próxima rota sem trocar o sistema.

4
00:00:28,000 --> 00:00:42,000
O mapa quase não muda. A consulta se repete.
A rota continua ótima. O planner para de começar do zero.

5
00:00:42,000 --> 00:00:52,000
Em laboratório, na v5, em mil consultas,
o JP-Geo ficou cerca de 28% mais rápido
e 31% com menos nós que A* fixo, com 100% de otimalidade.

6
00:00:52,000 --> 00:01:02,000
Na v7, em decepção geométrica alta,
o Geo cortou até cerca de 73% dos nós frente ao A*.
Isso é prova de laboratório, não case de opex pago.

7
00:01:02,000 --> 00:01:12,000
Para Delage, Automni, AGVS, 3PL e CD com layout estável:
mesma lógica. Menos retrabalho na decisão. Mais fluxo no chão.

8
00:01:12,000 --> 00:01:25,000
Quero o diagnóstico de duas semanas no mapa de vocês.
Ou 30 minutos para ver se faz sentido.
```

---

## Legendas

### 1) LinkedIn (longo)

No CD brasileiro, a rota intramuros ainda depende demais de papel, Excel e “quem conhece o layout”.

Quando o volume sobe, a fila trava. O AMR espera. O planner recomeça do zero no mesmo mapa.

O **JP Decision Engine** é um motor plugável de rota intramuros: entra no WMS ou na frota, lê o mapa que você já usa e devolve a próxima rota sem trocar o sistema.

Frase de produto: o mapa quase não muda. A consulta se repete. A rota continua ótima. O planner para de começar do zero.

Números de **laboratório** (não são case de opex pago): na v5, em mil consultas, JP-Geo cerca de 28% mais rápido e 31% com menos nós que A\* fixo, com 100% de otimalidade; na v7, até cerca de 73% menos nós em decepção geométrica alta.

Para quem opera Delage, Automni/AGVS, 3PL ou CD com layout estável: conversa objetiva.

CTA: quero o diagnóstico de duas semanas no mapa de vocês — ou 30 minutos para ver se faz sentido.

#WMS #AMR #intralogística #3PL #logística

### 2) Instagram

Rota no papel. AMR parado. Planner recomeçando do zero.

JP Decision Engine = motor plugável de rota intramuros.

Lab (não opex pago): v5 ~28% mais rápido / ~31% menos nós vs A\* fixo, 100% ótimo. v7 até ~73% menos nós.

Quero o diagnóstico de duas semanas no mapa de vocês.

#WMS #AMR #AGV #intralogistica #centrodeDistribuicao

### 3) WhatsApp

João — vídeo curto sobre o JP Decision Engine: motor plugável de rota intramuros (WMS/frota, mapa estável).

Prova de lab v5–v7 (não case de opex). CTA: diagnóstico de 2 semanas no mapa de vocês, ou 30 min.

Posso te mandar o one-pager e marcar o horário?

### 4) X

Planner recomeçando do zero no mesmo mapa do CD.

JP Decision Engine: motor plugável de rota intramuros (WMS / frota AMR).

Lab v5–v7 (não opex pago). CTA: diagnóstico de 2 semanas no mapa de vocês.

### 5) E-mail curto

**Assunto:** Diagnóstico de 2 semanas no mapa do CD  

Bom dia,  

Envio um vídeo curto do **JP Decision Engine**, motor plugável de rota intramuros para WMS e frota AMR/AGV.  

O ponto: mapa estável, consulta repetida, rota ótima — o planner para de começar do zero. Números citados são de laboratório (v5–v7), não case de opex pago.  

Próximo passo: **30 minutos** ou **diagnóstico de 2 semanas no mapa de vocês**.  

Abs,  
João Pedro Pereira Passos  
Palmas/TO

### 6) Comentário em post de AMR/WMS

Boa provocação. No chão, o gargalo costuma ser o planner recomeçando do zero no mesmo layout. Trabalhamos um motor plugável de rota intramuros (JP Decision Engine) para WMS/frota — prova de lab, sem vender case de opex. Se fizer sentido: quero o diagnóstico de duas semanas no mapa de vocês.

---

## Calendário 14d

**CALENDÁRIO PAUSADO pelo embargo** até liberação Trilho A/B. Plano abaixo fica pronto para retomar.

Divulgação **orgânica** apenas. CTA único em todo post: **30 minutos** ou **diagnóstico de 2 semanas**.  
Público: dono de CD, gerente de WMS, integrador AMR/AGV, 3PL.  
Início sugerido: Dia 1 = 2026-09-22 (ajustar se gravar depois).

| Dia | Canal | Peça | Público | CTA |
|-----|-------|------|---------|-----|
| 1 | LinkedIn | Post + vídeo 90s | WMS / CD | Diagnóstico 2 sem. / 30 min |
| 1 | Instagram / Reels | Mesmo 90s (corte) | Operação / automação | Idem |
| 2 | WhatsApp | Envio 1:1 (10 contatos quentes) + legenda WA | Integradores e CDs conhecidos | Idem |
| 3 | LinkedIn | Carrossel: problema → mapa estável → API | Gerente WMS | Idem |
| 4 | X | Gancho 15s + thread curta (lab ≠ opex) | Tech ops | Idem |
| 5 | Comentário | 5 posts AMR/WMS (legenda #6) | Timeline do setor | Idem |
| 6 | LinkedIn | Post “o que não é”: não é WMS, não é AMR, não é roteirizador de rua | Comprador técnico | Idem |
| 7 | Instagram Stories | 3 frames: dor / frase autorizada / CTA | Seguidores B2B | Idem |
| 8 | E-mail | Lista curta (assunto do bloco Legendas) | Delage / Automni / AGVS / 3PL | Idem |
| 9 | LinkedIn | Recorte 15s (gancho) + CTA no primeiro comentário | Alcance amplo | Idem |
| 10 | WhatsApp / grupos setoriais | Só se autorizado pelo admin; senão DM | 3PL / CD | Idem |
| 11 | LinkedIn | FAQ: “tem case de opex pago?” → não; o que oferecemos é diagnóstico | Cético B2B | Idem |
| 12 | Comentário | Mais 5 posts (WMS/AMR) | Timeline | Idem |
| 13 | Instagram + LinkedIn | Bastidor: shot-list / tela API (blur) | Quem curte processo | Idem |
| 14 | LinkedIn + e-mail | Fechamento da quinzena: “ainda dá tempo do diagnóstico de 2 semanas” | Quem engajou e não respondeu | Idem |

**Regra dos 14 dias:** um CTA só. Sem promoção de opex. Sem TDA.

---

## Contas

Contas e hashtags **brasileiras** úteis para descoberta e comentário. **Sem inventar alcance** (seguidores não listados).

### Contas / páginas (empresa ou mídia — verificar handle atual antes de marcar)

1. Delage (WMS / software logístico)  
2. Automni (AMR / automação)  
3. AGVS / players de AGV-AMR no Brasil (página comercial da marca que você já aborda)  
4. Mundo Logística  
5. Tecnologística  
6. Intralogística Brasil / portais de intralogística  
7. Revista Logística  
8. ILOS (inteligência em logística e supply chain)  
9. GS1 Brasil  
10. ABRALOG  
11. Associação / núcleos regionais de logística (ex.: eventos estaduais de CD)  
12. Páginas de eventos: Intermodal, Movimat, Logística & Supply Chain (quando abertas)  
13. Fornecedores de WMS adjacentes ao alvo Delage (só comentar valor, sem ataque)  
14. Integradores de automação de armazém no LinkedIn (busca: “integrador AMR Brasil”)  
15. Perfis de gerentes de CD / WMS que publicam operação real (engajar sem pitch duro)  
16. Comunidades LinkedIn: Logística Brasil, Supply Chain Brasil, Intralogística  
17. Canais YouTube de logística operacional (cortes e comentários sobrios)  
18. Contas de 3PL nacionais que falam de CD e automação  
19. Fabricantes/distribuidores de empilhadeira e AGV com conteúdo de pátio  
20. Seu próprio perfil + página do JP Decision Engine (quando existir) — âncora de CTA

### Hashtags úteis (misturar 3–5 por post)

- `#WMS` `#AMR` `#AGV` `#intralogística` `#intralogistica`  
- `#3PL` `#centrodedistribuicao` `#CD` `#armazém` `#armazem`  
- `#logística` `#logistica` `#supplychain` `#cadeiadesuprimentos`  
- `#automação` `#automacaoindustrial` `#indústria40` (usar com parcimônia)  
- `#picking` `#warehouse` `#operacaologistica`

**Como usar:** comentar valor em posts das contas 1–19; hashtags só no Instagram/LinkedIn; no X, 1–2 no máximo.

---

## Checklist de publicação

- [ ] Vídeo 90s exportado 9:16 + SRT embutido ou arquivo `.srt`  
- [ ] Corte 15s (gancho) exportado  
- [ ] Card lab com rótulo **Laboratório** (números só os autorizados)  
- [ ] Sem TDA / homologia / paper / opex garantido / case pago inventado  
- [ ] CTA único em todos os canais  
- [ ] One-pager anexável no e-mail e no LinkedIn  
- [ ] Lista de 10 contatos WhatsApp (Dia 2) pronta  
- [ ] Handles das contas Delage / Automni / AGVS conferidos no dia do post  
- [ ] Autorização de filmagem no CD (se houver cliente/planta)  
- [ ] Blur de dados na tela de mapa/API  

---

## O que falta filmar

1. Corredor real de CD (plano 1) — **crítico**  
2. AMR/AGV ou proxy (carrinho na curva) — **crítico**  
3. Tela de mapa/layout com blur — **crítico**  
4. Mock limpo PUT `/layout` + POST `/plan` — **crítico**  
5. Face opcional do João (CTA) — opcional  
6. B-roll doca / empilhadeira — reserva  
7. Áudio VO final em ambiente silencioso — **crítico**  
8. Autorização escrita se filmar planta de terceiro  

---

## Verificação pré-entrega

| Item | Status |
|------|--------|
| Números só autorizados (lab v5/v7: 1000 consultas, ~28%, ~31%, 100% otimalidade, ~73% nós) | OK |
| Sem case de opex pago / sem garantia de opex | OK |
| Sem TDA / homologia / paper / “ficar rico” | OK |
| CTA: diagnóstico de 2 semanas / 30 min | OK |
| Narração 90s cabe em ≤ 90 s | OK (~75–85 s) |
| Seções: Roteiro 90s \| Roteiro 15s \| Shot-list \| SRT \| Legendas \| Calendário 14d \| Contas | OK |
