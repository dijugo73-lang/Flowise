FROM node:20-alpine

# Instalar dependencias del sistema necesarias
RUN apk add --no-cache python3 make g++

# Instalar Flowise globalmente
RUN npm install -g flowise

# Crear y configurar el directorio de trabajo
RUN mkdir -p /data
WORKDIR /data

# CONFIGURACIÓN CRÍTICA PARA CLOUD
# Forzamos a que Flowise escuche en todas las interfaces (0.0.0.0) 
# y use el puerto que Render le asigne
ENV PORT=3000
ENV HOST=0.0.0.0
ENV DATABASE_PATH=/data

# Exponer el puerto para el health check de Render
EXPOSE 3000

# Iniciar Flowise
CMD ["flowise", "start"]
