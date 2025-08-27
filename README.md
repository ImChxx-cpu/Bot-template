# Bot Template

Un bot de Discord modular desarrollado con discord.py que incluye comandos generales y de moderación.

## 🚀 Instalación

### Prerrequisitos
- Python 3.12 o anterior (recomendado para compatibilidad)
- Una aplicación de Discord creada en [Discord Developer Portal](https://discord.com/developers/applications)

### Configuración

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/ImChxx-cpu/Bot-template.git
   cd Bot-template
   ```

2. **Crea un entorno virtual:**
   ```bash
   python -m venv env
   
   # Windows
   env\Scripts\activate
   
   # Linux/Mac
   source env/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno:**
   
   Crea un archivo `.env` en la carpeta `config/`:
   ```
   config/.env
   ```
   
   Con el siguiente contenido:
   ```env
   DISCORD_TOKEN=tu_token_aqui
   BOT_PREFIX=t!
   GUILD_ID=tu_guild_id_aqui
   ```

   **⚠️ IMPORTANTE:** Nunca compartas tu token de Discord. Si accidentalmente lo subes a Git, regenera inmediatamente un nuevo token en el Developer Portal.

## 🤖 Uso

Ejecuta el bot:
```bash
python main.py
```

## 📁 Estructura del Proyecto

```
Bot-template/
├── config/
│   ├── .env              # Variables de entorno (NO incluir en Git)
│   └── settings.py       # Configuración del bot
├── commands/
│   ├── general.py        # Comandos generales
│   └── moderation.py     # Comandos de moderación
├── models/               # Modelos de datos
├── services/             # Servicios del bot
├── utils/                # Utilidades
├── main.py              # Archivo principal
└── requirements.txt     # Dependencias
```

## 🔧 Características

- **Comandos Slash:** Sistema moderno de comandos de Discord
- **Sistema Modular:** Comandos organizados en categorías
- **Configuración Flexible:** Variables de entorno para fácil despliegue
- **Logging:** Sistema de logging integrado

## 👨‍💻 Desarrollo

Desarrollado por **Jesús Jara S.**

## 📝 Notas

- El archivo `.env` está incluido en `.gitignore` por seguridad
- Para Python 3.13+, se incluye `audioop-lts` para compatibilidad con discord.py
- Los comandos slash se sincronizan automáticamente al iniciar el bot