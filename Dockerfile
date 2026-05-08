FROM node:20-alpine

# Instalar dependencias del sistema
RUN apk add --no-cache python3 make g++

# Instalar Flowise globalmente
RUN npm install -g flowise

# Crear directorio para la base de datos
RUN mkdir -p /data
WORKDIR /data

# CONFIGURACIÓN PARA RENDER
ENV PORT=3000
ENV HOST=0.0.0.0
ENV DATABASE_PATH=/data

# Exponer el puerto
EXPOSE 3000

# Comando para iniciar
CMD ["flowise", "start"]
