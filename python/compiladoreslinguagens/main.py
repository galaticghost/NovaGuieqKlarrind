import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate
from matplotlib.patches import Patch # Importar Patch para legendas

# =============================================================================
# DADOS GLOBAIS (mantidos no topo para reuso)
# =============================================================================
processadores = [
    # CPUs RISC
    'RISC-V (RV32I)',
    'ARM Cortex-M',
    'ARM Cortex-A78',
    'Apple M2',
    # CPUs CISC
    'Intel i9-14900K',
    'AMD Ryzen 9 7950X',
    # GPUs NVIDIA
    'NVIDIA RTX 4090',
    'NVIDIA RTX 4080',
    'NVIDIA RTX 4070',
    'NVIDIA RTX 4060',
    'NVIDIA RTX 3050',
    # GPUs AMD
    'AMD RX 7900 XTX',
    'AMD RX 7800 XT',
    'AMD RX 7700 XT',
    'AMD RX 7900 XTX OC',
    # GPUs Intel
    'Intel Arc A770'
]

# Dados de tamanho de instrução
tamanho_instrucao = [
    32,     # RISC-V
    32,     # ARM Cortex-M
    32,     # ARM Cortex-A78
    32,     # Apple M2
    64,     # Intel i9 (x86-64)
    64,     # AMD Ryzen (x86-64)
    128,    # RTX 4090 (SIMD width)
    128,    # RTX 4080
    128,    # RTX 4070
    128,    # RTX 4060
    128,    # RTX 3050
    256,    # RX 7900 XTX
    256,    # RX 7800 XT
    256,    # RX 7700 XT
    384,    # RX 7900 XTX OC
    256     # Intel Arc
]

# Tipo de processador (para cores)
cores = []
for proc in processadores:
    if 'RTX' in proc:
        cores.append('lightgreen')
    elif 'RX' in proc:
        cores.append('lightcoral')
    elif 'Arc' in proc:
        cores.append('lightblue')
    elif 'Apple' in proc or 'ARM' in proc or 'RISC' in proc:
        cores.append('lightyellow')
    else:  # CPUs x86
        cores.append('lightgray')

x_pos = np.arange(len(processadores))

# Legenda de cores (centralizada para reuso)
legend_elements = [
    Patch(facecolor='lightyellow', label='CPUs RISC (ARM/Apple/RISC-V)'),
    Patch(facecolor='lightgray', label='CPUs x86 (Intel/AMD)'),
    Patch(facecolor='lightgreen', label='GPUs NVIDIA'),
    Patch(facecolor='lightcoral', label='GPUs AMD'),
    Patch(facecolor='lightblue', label='GPUs Intel')
]

# =============================================================================
# GRÁFICO 1: CPUs vs GPUs - TAMANHO DE INSTRUÇÕES
# =============================================================================
plt.figure(figsize=(12, 7)) # Nova figura
bars = plt.bar(x_pos, tamanho_instrucao, color=cores, alpha=0.8, edgecolor='black')

plt.xlabel('Processador')
plt.ylabel('Largura da Instrução (bits)')
plt.title('CPUs vs GPUs - LARGURA DE INSTRUÇÕES', fontsize=16, fontweight='bold')
plt.xticks(x_pos, processadores, rotation=45, ha='right')
plt.grid(True, alpha=0.3)

# Adicionar valores nas barras
for bar, valor in zip(bars, tamanho_instrucao):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.5, # Ajuste no offset para evitar corte
             f'{valor} bits', ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.legend(handles=legend_elements, loc='upper left')
plt.tight_layout()
plt.show() # Mostra esta figura

# =============================================================================
# GRÁFICO 2: PERFORMANCE COMPARATIVA (TFLOPS)
# =============================================================================
tflops_data = [
    0.0001,  # RISC-V (exemplo: microcontrolador)
    0.0002,  # ARM Cortex-M (exemplo: embarcado)
    0.5,     # ARM Cortex-A78 (exemplo: mobile high-end)
    3.6,     # Apple M2
    2.5,     # Intel i9
    2.8,     # AMD Ryzen
    82.6,    # RTX 4090
    48.7,    # RTX 4080
    29.1,    # RTX 4070
    15.2,    # RTX 4060
    9.1,     # RTX 3050
    61.4,    # RX 7900 XTX
    37.3,    # RX 7800 XT
    35.2,    # RX 7700 XT
    61,      # RX 7900 XTX OC
    17.2     # Intel Arc
]

plt.figure(figsize=(12, 7)) # Nova figura
bars2 = plt.bar(x_pos, tflops_data, color=cores, alpha=0.8, edgecolor='black')
plt.xlabel('Processador')
plt.ylabel('Performance (TFLOPS FP32)')
plt.title('PERFORMANCE DE COMPUTAÇÃO (TFLOPS FP32)', fontsize=16, fontweight='bold')
plt.xticks(x_pos, processadores, rotation=45, ha='right')
plt.yscale('log')  # Escala log para melhor visualização de grandes diferenças
plt.grid(True, alpha=0.3)

# Adicionar valores (apenas para TFLOPS > 1 para evitar poluir)
for i, (proc, tflops) in enumerate(zip(processadores, tflops_data)):
    if tflops >= 1.0: # Ajustado para incluir CPUs high-end
        plt.text(i, tflops, f'{tflops:.1f} TF', ha='center', va='bottom',
                 fontweight='bold', fontsize=8, rotation=45) # Removido +5 offset

plt.legend(handles=legend_elements, loc='upper left')
plt.tight_layout()
plt.show() # Mostra esta figura

# =============================================================================
# GRÁFICO 3: MEMÓRIA E LARGURA DE BARRA
# =============================================================================
memoria_gb = [
    0.016,   # RISC-V (16MB típico, convertido para GB)
    0.064,   # ARM Cortex-M (64MB, convertido para GB)
    16,      # ARM Cortex-A78 (RAM do sistema)
    24,      # Apple M2 (unificada)
    128,     # Intel i9 (DDR5, RAM do sistema)
    128,     # AMD Ryzen (DDR5, RAM do sistema)
    24,      # RTX 4090 (VRAM)
    16,      # RTX 4080 (VRAM)
    12,      # RTX 4070 (VRAM)
    8,       # RTX 4060 (VRAM)
    8,       # RTX 3050 (VRAM)
    24,      # RX 7900 XTX (VRAM)
    16,      # RX 7800 XT (VRAM)
    12,      # RX 7700 XT (VRAM)
    24,      # RX 7900 XTX OC (VRAM)
    16       # Intel Arc (VRAM)
]

largura_barra_bits = [
    32,      # RISC-V
    32,      # ARM Cortex-M
    128,     # ARM Cortex-A78
    256,     # Apple M2
    128,     # Intel i9
    128,     # AMD Ryzen
    384,     # RTX 4090
    256,     # RTX 4080
    192,     # RTX 4070
    128,     # RTX 4060
    128,     # RTX 3050
    384,     # RX 7900 XTX
    256,     # RX 7800 XT
    192,     # RX 7700 XT
    384,     # RX 7900 XTX OC
    256      # Intel Arc
]

plt.figure(figsize=(12, 7)) # Nova figura
largura = 0.35

bars3a = plt.bar(x_pos - largura/2, memoria_gb, largura,
                 label='Memória (GB)', alpha=0.8, color='purple')
bars3b = plt.bar(x_pos + largura/2, largura_barra_bits, largura,
                 label='Largura Barramento (bits)', alpha=0.8, color='orange') # Corrigido label

plt.xlabel('Processador')
plt.ylabel('Memória (GB) / Largura Barramento (bits)')
plt.title('MEMÓRIA vs LARGURA DE BARRAMENTO', fontsize=16, fontweight='bold')
plt.xticks(x_pos, processadores, rotation=45, ha='right')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show() # Mostra esta figura

# =============================================================================
# GRÁFICO 4: EFICIÊNCIA ENERGÉTICA
# =============================================================================
performance_per_watt = [
    500,    # RISC-V (MIPS/W)
    400,    # ARM Cortex-M
    350,    # ARM Cortex-A78
    300,    # Apple M2
    45,     # Intel i9
    50,     # AMD Ryzen
    4.5,    # RTX 4090
    5.2,    # RTX 4080
    6.1,    # RTX 4070
    7.8,    # RTX 4060
    8.5,    # RTX 3050
    3.8,    # RX 7900 XTX
    4.5,    # RX 7800 XT
    5.2,    # RX 7700 XT
    4.0,    # RX 7900 XTX OC
    4.2     # Intel Arc
]

plt.figure(figsize=(12, 7)) # Nova figura
bars4 = plt.bar(x_pos, performance_per_watt, color=cores, alpha=0.8, edgecolor='black')
plt.xlabel('Processador')
plt.ylabel('Performance por Watt (MIPS/W relativo)')
plt.title('EFICIÊNCIA ENERGÉTICA', fontsize=16, fontweight='bold')
plt.xticks(x_pos, processadores, rotation=45, ha='right')
plt.grid(True, alpha=0.3)

# Destacar os mais eficientes
for i, (proc, eff) in enumerate(zip(processadores, performance_per_watt)):
    if eff > 10:  # GPUs geralmente têm < 10, CPUs mais eficientes tem > 10
        plt.text(i, eff + 5, f'{eff:.0f}', ha='center', va='bottom',
                 fontweight='bold', color='green', fontsize=9)

plt.legend(handles=legend_elements, loc='upper left') # Adicionada legenda também aqui
plt.tight_layout()
plt.show() # Mostra esta figura

# =============================================================================
# TABELA COMPARATIVA DETALHADA
# =============================================================================

dados_detalhados = [
    # CPUs RISC
    {
        'Processador': 'RISC-V (RV32I)',
        'Tipo': 'CPU RISC',
        'Arquitetura': 'RV32I',
        'Instrução': '32 bits fixo',
        'Núcleos': '1-4',
        'Memória (GB)': '0.016',
        'TFLOPS': '0.0001',
        'TDP (W)': '1-5',
        'Lançamento': '2019'
    },
    {
        'Processador': 'ARM Cortex-M4',
        'Tipo': 'CPU RISC',
        'Arquitetura': 'ARMv7-M',
        'Instrução': 'Thumb-2 (16/32b)',
        'Núcleos': '1',
        'Memória (GB)': '0.064',
        'TFLOPS': '0.0002',
        'TDP (W)': '0.1-1',
        'Lançamento': '2010'
    },
    {
        'Processador': 'Apple M2',
        'Tipo': 'CPU RISC',
        'Arquitetura': 'ARMv8.5-A',
        'Instrução': 'AArch64 (32b)',
        'Núcleos': '8 (4P+4E)',
        'Memória (GB)': '24',
        'TFLOPS': '3.6',
        'TDP (W)': '15-20',
        'Lançamento': '2022'
    },
    # CPUs x86
    {
        'Processador': 'Intel i9-14900K',
        'Tipo': 'CPU CISC',
        'Arquitetura': 'x86-64',
        'Instrução': 'Variável (1-15B)',
        'Núcleos': '24 (8P+16E)',
        'Memória (GB)': '128',
        'TFLOPS': '2.5',
        'TDP (W)': '125-253',
        'Lançamento': '2023'
    },
    # GPUs NVIDIA
    {
        'Processador': 'NVIDIA RTX 4090',
        'Tipo': 'GPU',
        'Arquitetura': 'Ada Lovelace',
        'Instrução': '128b SIMD',
        'Núcleos': '16384 CUDA',
        'Memória (GB)': '24 GDDR6X',
        'TFLOPS': '82.6',
        'TDP (W)': '450',
        'Lançamento': '2022'
    },
    {
        'Processador': 'NVIDIA RTX 4080',
        'Tipo': 'GPU',
        'Arquitetura': 'Ada Lovelace',
        'Instrução': '128b SIMD',
        'Núcleos': '9728 CUDA',
        'Memória (GB)': '16 GDDR6X',
        'TFLOPS': '48.7',
        'TDP (W)': '320',
        'Lançamento': '2022'
    },
    {
        'Processador': 'NVIDIA RTX 4070',
        'Tipo': 'GPU',
        'Arquitetura': 'Ada Lovelace',
        'Instrução': '128b SIMD',
        'Núcleos': '5888 CUDA',
        'Memória (GB)': '12 GDDR6X',
        'TFLOPS': '29.1',
        'TDP (W)': '200',
        'Lançamento': '2023'
    },
    {
        'Processador': 'NVIDIA RTX 4060',
        'Tipo': 'GPU',
        'Arquitetura': 'Ada Lovelace',
        'Instrução': '128b SIMD',
        'Núcleos': '3072 CUDA',
        'Memória (GB)': '8 GDDR6',
        'TFLOPS': '15.2',
        'TDP (W)': '115',
        'Lançamento': '2023'
    },
    {
        'Processador': 'NVIDIA RTX 3050',
        'Tipo': 'GPU',
        'Arquitetura': 'Ampere',
        'Instrução': '128b SIMD',
        'Núcleos': '2560 CUDA',
        'Memória (GB)': '8 GDDR6',
        'TFLOPS': '9.1',
        'TDP (W)': '130',
        'Lançamento': '2021'
    },
    # GPUs AMD
    {
        'Processador': 'AMD RX 7900 XTX',
        'Tipo': 'GPU',
        'Arquitetura': 'RDNA 3',
        'Instrução': '256b SIMD',
        'Núcleos': '6144 Stream',
        'Memória (GB)': '24 GDDR6',
        'TFLOPS': '61.4',
        'TDP (W)': '355',
        'Lançamento': '2022'
    },
    {
        'Processador': 'AMD RX 7800 XT',
        'Tipo': 'GPU',
        'Arquitetura': 'RDNA 3',
        'Instrução': '256b SIMD',
        'Núcleos': '3840 Stream',
        'Memória (GB)': '16 GDDR6',
        'TFLOPS': '37.3',
        'TDP (W)': '263',
        'Lançamento': '2023'
    },
    {
        'Processador': 'AMD RX 7700 XT',
        'Tipo': 'GPU',
        'Arquitetura': 'RDNA 3',
        'Instrução': '256b SIMD',
        'Núcleos': '3456 Stream',
        'Memória (GB)': '12 GDDR6',
        'TFLOPS': '35.2',
        'TDP (W)': '245',
        'Lançamento': '2023'
    },    
    {
        'Processador': 'AMD RX 7900 XTX OC',
        'Tipo': 'GPU',
        'Arquitetura': 'RDNA 3',
        'Instrução': '256b SIMD',
        'Núcleos': '6144 Stream',
        'Memória (GB)': '24 GDDR6',
        'TFLOPS': '61.4',
        'TDP (W)': '355',
        'Lançamento': '2022'
    },
    # GPUs Intel
    {
        'Processador': 'Intel Arc A770',
        'Tipo': 'GPU',
        'Arquitetura': 'Xe-HPG',
        'Instrução': '256b SIMD',
        'Núcleos': '4096 Xe-cores',
        'Memória (GB)': '16 GDDR6',
        'TFLOPS': '17.2',
        'TDP (W)': '225',
        'Lançamento': '2022'
    }
]

# Criar DataFrame e mostrar tabela
df_detalhado = pd.DataFrame(dados_detalhados)
print("🎯 COMPARAÇÃO DETALHADA: CPUs vs GPUs MODERNAS")
print("=" * 120)
print(tabulate(df_detalhado, headers='keys', tablefmt='grid', showindex=False))

# =============================================================================
# ANÁLISE COMPARATIVA
# =============================================================================

print("\n" + "=" * 80)
print("📈 ANÁLISE COMPARATIVA: CPUs vs GPUs")
print("=" * 80)

print("\n🔍 **OBSERVAÇÕES PRINCIPAIS:**")

print("\n🎯 **DIFERENÇAS ARQUITETURAIS:**")
print("• CPUs: Instruções complexas, poucos núcleos, alta frequência")
print("• GPUs: Instruções SIMD simples, milhares de núcleos, paralelismo massivo")

print("\n⚡ **PERFORMANCE:**")
print("• CPUs: 1-5 TFLOPS (single-thread forte)")
print("• GPUs: 10-80+ TFLOPS (paralelismo massivo)")

print("\n💡 **EFICIÊNCIA:**")
print("• CPUs RISC: 100-500 MIPS/W (extremamente eficientes)")
print("• GPUs: 3-8 MIPS/W (alta performance, menor eficiência)")

print("\n🎮 **USO TÍPICO:**")
print("• CPUs: Tarefas seriais, lógica complexa, sistema operacional")
print("• GPUs: Gráficos, AI, computação científica, processamento paralelo")

print("\n🚀 **EVOLUÇÃO RECENTE:**")
print("• NVIDIA Ada Lovelace: Ray Tracing + DLSS 3")
print("• AMD RDNA 3: Arquitetura chiplet")
print("• Intel Arc: Competição no mercado médio")
print("• Apple M-series: CPU+GPU unificada ARM")