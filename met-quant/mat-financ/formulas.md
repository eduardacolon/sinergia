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