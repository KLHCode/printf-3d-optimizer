---
name: printf-3d-optimizer
description: Conector público para diagnóstico de STL pela API privada PrintF, com orientação de validação de impressão e comparação A/B.
---

# PrintF 3D Optimizer — skill pública

Quando o usuário enviar uma peça, identifique o objetivo, a categoria (figura orgânica ou peça dimensional), a impressora, o bico, o material e o defeito prioritário.

1. Peça autorização antes de transferir STLs de terceiros ou de clientes ao serviço remoto.
2. Execute `scripts/cliente_optimizer.py arquivo.stl --printer "A1"` (ou `"A1 Mini"`), com `PRINTF_API_URL` e `PRINTF_API_KEY` configuradas. A ferramenta atualmente **somente diagnostica** a malha.
3. Leia o JSON retornado, distinguindo medições reais de campos ainda não avaliados.
4. Para figuras, recomende inspeção de rosto, dedos, suportes e costura; para peças funcionais, exija cotas, folgas por lado e gabaritos de encaixe.
5. Proponha um teste A/B preservando cópia A original e registrando tempo, gramas e acabamento.
6. Nunca afirme que o STL foi corrigido, que o fatiador foi operado ou que a impressão foi enviada sem evidência de execução. Sempre obtenha confirmação antes de imprimir.

O motor de otimização, futuras edições de geometria e integrações CAD são mantidos em infraestrutura privada.
