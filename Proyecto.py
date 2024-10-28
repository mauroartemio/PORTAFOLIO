import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from scipy.stats import beta,norm



df=pd.read_csv("/Users/maurosotelo/Downloads/SuperMarketData.csv")


sales=np.array(df["Sales"])*19.88

max_sales=max(sales)
min_sales=min(sales)
sales_norm=1/(max_sales-min_sales)*sales

a,b,_,_=beta.fit(sales)

print(a,b)

mu_norm= a/(a+b)

var_norm=(a*b)/((a+b)**2*(a+b+1))
desv_norm=np.sqrt(var_norm)

mu=(max_sales-min_sales)*mu_norm
var=(max_sales-min_sales)**2*var_norm
sigma=np.sqrt(var)

#-------Salarios----
fact=1.15

sal_cajeros=258.25
num_cajeros=20
dias_t=20

tot_sal_caj=sal_cajeros*num_cajeros*dias_t*fact

sal_conserjes=5000
num_conserjes=16
tot_sal_conserj=sal_conserjes*num_conserjes*fact

gerente=21634*fact

sub_gerente=9341*fact
num_subgerente=5
tot_sal_sub=sub_gerente*num_subgerente*fact

sal_almacenista=262.13
almacenista=30
tot_sal_alm=sal_almacenista*almacenista*dias_t*fact

g_pasillo=264.65
num_pasillos=22
tot_sal_pasillo=g_pasillo*num_pasillos*dias_t*fact

nomina_tot=tot_sal_caj+tot_sal_conserj+tot_sal_sub+tot_sal_alm+tot_sal_pasillo

print(nomina_tot)
gasto_inter=120*2000*14*1.981*30
gasto_base=120*2000*6*1.072*30
gasto_punta=120*2000*4*1.072*30
gasto_luz=gasto_inter+gasto_base+gasto_punta
print(gasto_luz)
gasto_prod=150000000
gasto_agua=0.85*30*4000
gastos_tot=gasto_luz+nomina_tot+gasto_agua+gasto_prod
ingreso=gastos_tot+1500000
print(gastos_tot)
omega=norm.ppf(0.99)
a_=mu**2
b_=-2*mu*ingreso-omega**2-sigma**2
c_=ingreso**2
N1=(-b_+np.sqrt(b_**2-4*a_*c_))/(2*a_)
N2=(-b_-np.sqrt(b_**2-4*a_*c_))/(2*a_)


print(N1)
print(N2)

if(ingreso/N1-mu>0):
    n=N1
else:
    N=N2

porc_pob=21/160000
print(porc_pob)

poblacion_total = 40000

frecuencia_semanal = 0.681 * poblacion_total
frecuencia_diaria = 0.198 * poblacion_total
frecuencia_cada_dos_semanas = 0.098 * poblacion_total
frecuencia_mensual = 0.023 * poblacion_total


preferencia_entre_semana = 0.742 * poblacion_total
preferencia_fin_semana = (1 - 0.742) * poblacion_total


porc_pob1 = 21 / poblacion_total
print(porc_pob1)

ratings = df["Rating"]

plt.figure(figsize=(10, 6))
plt.hist(ratings, bins=20, alpha=0.7, color='blue', density=True)
plt.title("Distribución de Ratings")
plt.xlabel("Rating")
plt.ylabel("Densidad")

x = np.linspace(min(ratings), max(ratings), 100)
mu_ratings = ratings.mean()
sigma_ratings = ratings.std()
plt.plot(x, norm.pdf(x, mu_ratings, sigma_ratings), color='red', label='Aproximación Normal')
plt.legend()
plt.show()

n = len(ratings)
mu_sample = mu_ratings
sigma_sample = sigma_ratings / np.sqrt(n)
p_rating_8_5 = 1 - norm.cdf(8.5, loc=mu_sample, scale=sigma_sample)
