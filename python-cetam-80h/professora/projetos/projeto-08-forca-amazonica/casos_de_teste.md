# Casos de teste para correção – Projeto 8

| **Entrada / situação** | **Resultado esperado** |
| --- | --- |
| Rodada 1 (tambaqui): t, x, t, “12”, “ab”, a, m, b, q, u, i | “x” erra (1 vida perdida); “t” repetida: aviso sem perder vida; “12” e “ab” inválidas; vitória com 5 vidas = **35 pontos** |
| Rodada 2 (pirarucu): z, x, w, k, j, h | Seis erros: derrota, revela PIRARUCU, **0 ponto** |
| Rodada 3 (tucunare): t, u, c, n, a, r, e | Vitória sem erros (6 vidas) = **40 pontos** |
| Placar ao final | 3 rodadas; 2 vitórias; **75 pontos** |
| `montar_exibicao("tambaqui", ["t", "a"])` | `t a _ _ a _ _ _` |
| `venceu("cupuacu", ["c", "u", "p", "a"])` | `True` |
| Rodada 7 | Volta à palavra da rodada 1 (tambaqui) |
