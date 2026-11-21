# PrintF 3D Optimizer — cliente público

Este repositório contém apenas o cliente de integração, não o motor privado.

## Exemplo local

```bash
python -m pip install -r requirements.txt
export PRINTF_API_URL=http://127.0.0.1:8000
export PRINTF_API_KEY='chave-de-teste-local'
python scripts/cliente_optimizer.py amostra.stl --printer 'A1 Mini'
```

No PowerShell, use `$env:PRINTF_API_KEY="..."` em vez de `export`.

A versão inicial oferece **diagnóstico de malha STL**, não otimização automática, envio à impressora ou integração pronta com Bambu Studio. Não publique chaves de API ou arquivos de clientes.
