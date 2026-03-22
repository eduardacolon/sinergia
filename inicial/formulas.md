# CAP1:
# 1.1 - Juros Simples : 

FV = PV + J  
J = PV * i * n  
FV = PV * (1 + i * n)                    
PV = FV / (1 + i * n)                 
i = (FV / PV - 1) * (1 / n)  
n = (FV / PV - 1) * (1 / i)  

# 1.2 - Juros Compostos

FV = PV * (1 + i)^n  
PV = FV / (1 + i)^n  
i = (FV / PV)^(1/n) - 1  
n = log(FV / PV) / log(1 + i)  

## 1.2.1 - Conversão de taxa

I = (1 + i)^n - 1  
i = (1 + I)^(1/n) - 1  

# 1.3 - Taxa Nominal

i = j / k  

## 1.3.1 - Taxa over (taxa por dia útil)

i = (1 + taxa_over / 30)^(30/du) - 1  

## 1.3.2 - Taxa over anual efetiva

taxa_a.a = [(1 + taxa_over/100)^(252) - 1] * 100  

## 1.3.3 - Taxa efetiva mensal

(1 + i) = (1 + i_r) * (1 + i_inf)  

# 1.4 - Séries periódicas uniformes

## 1.4.1 - Séries uniformes – valor presente

PV = PMT * [1 - (1 + i)^(-n)] / i  
PMT = PV / {[1 - (1 + i)^(-n)] / i}  

## 1.4.2 - Séries uniformes – valor futuro (montante)

FV = PMT * [(1 + i)^n - 1] / i  
PMT = FV / {[(1 + i)^n - 1] / i}  

## 1.4.3 - Perpetuidade

R = P * i  
P = R / i  
P = R / (i - c)  

Sendo: R = renda; c = taxa de crescimento.

# 1.5 - Sistemas de amortização

## 1.5.1 - SAC 

Amortização:
A = PV / n  

Juros:
J = SD * i  

Parcela:
PMT = A + J  

Saldo Devedor:
SD = PV - (A * k)  

## 1.5.2 - Price

Parcela (PMT):
PMT = PV * [i * (1 + i)^n] / [(1 + i)^n - 1]  

Juros:
J = SD * i  

Amortização:
A = PMT - J  

Saldo Devedor:
SD_novo = SD_anterior - A  

## 1.5.3 - SPV (pré/pós)

## 1.5.3.1 - SPV PÓS

FV = PMT * [(1 + i)^n - 1] / i  
PV = PMT * [1 - (1 + i)^(-n)] / i  

## 1.5.3.2 - SPV PRÉ

FV = PMT * [(1 + i)^n - 1] / i * (1 + i)  
PV = PMT * [1 - (1 + i)^(-n)] / i * (1 + i)

# 2.6 - Gráfico de Dispersão

Tipos de relação entre variáveis:

(a) Correlação positiva → variáveis crescem juntas  
(b) Correlação negativa → uma sobe enquanto a outra desce  
(c) Não correlacionadas → sem relação aparente  

---

## 2.7 - Covariância

A covariância mede como duas variáveis (X e Y) variam juntas.

- σXY > 0 → relação positiva  
- σXY < 0 → relação negativa  
- σXY = 0 → sem relação  

---

### 2.7.1 - Fórmulas

Covariância populacional:

σXY = Σ[(Xi - μX) * (Yi - μY)] / N  

Covariância amostral:

SXY = Σ[(Xi - X̄) * (Yi - Ȳ)] / (n - 1)  

Sendo:  
σXY = covariância populacional  
SXY = covariância amostral  

---

## 2.7.2 - Observação importante

As unidades da covariância podem variar, pois dependem das unidades de X e Y.  

---

## 2.8 - Correlação

A correlação mede a **força e direção da relação linear** entre duas variáveis.

---

### 2.8.1 - Fórmulas

Correlação populacional:

ρ = σXY / (σX * σY)  

Correlação amostral:

r = SXY / (S * SY)  

Sendo:  
ρ = correlação populacional  
r = correlação amostral  

---

## 2.8.2 - Intervalo de valores

-1 ≤ r ≤ +1  

---

## 2.8.3 - Interpretação

- r ≈ +1 → forte correlação positiva  
- r ≈ -1 → forte correlação negativa  
- r ≈ 0 → ausência de correlação  

---

## 2.9 - Aplicação em Finanças

- Análise de relação entre ativos  
- Diversificação de carteira  
- Avaliação de risco conjunto  
- Identificação de dependência entre variáveis  

---

## 2.10 - Interpretação Geral

- Covariância → indica direção da relação  
- Correlação → indica direção + intensidade  
- Correlação é padronizada (mais utilizada)  
