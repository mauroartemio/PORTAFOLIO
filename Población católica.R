# Cargar los datos desde el archivo CSV
datos <- read.csv(file = "Indicadores20240426133632.csv")
datos2 <- read.csv(file="Indicadores20240426151159.csv")

# Mostrar las primeras filas del conjunto de datos
head(datos)
library(ggplot2)
library(dplyr)
library(hrbrthemes)
datose<-datos[9:15, ]
ggplot(datose, aes(x=Periodos, y=Población)) +
  geom_line() +
  geom_point() +
  theme_ipsum() +
  ggtitle("Pobación con respecto tiempo")

head(datos2)
ggplot(datos2, aes(x=Periodos, y=Población.católica)) +
  geom_line() +
  geom_point() +
  theme_ipsum() +
  ggtitle("Pobación con respecto tiempo")

# Crear el gráfico comparativo
ggplot() +
  geom_line(data = datose, aes(x = Periodos, y = Población, color = "Población")) +
  geom_line(data = datos2, aes(x = Periodos, y = Población.católica, color = "Población Católica")) +
  labs(title = "Comparativo de Población y Población Católica a lo largo del tiempo",
       x = "Periodo",
       y = "Cantidad",
       color = "Variables") +
  theme_minimal()
