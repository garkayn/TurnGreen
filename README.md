# TurnGreen — hábitos sostenibles con puntos

Aplicación web académica en Django que convierte misiones de sostenibilidad en puntos acumulables. Incluye registro e inicio de sesión, seguimiento de misiones, saldo Leafpoints, canje de recompensas y selección de temas visuales.

## Tecnologías

- Python 3.12 recomendado
- Django 5.1
- SQLite para desarrollo local
- Plantillas HTML y CSS

## Puesta en marcha

```bash
python -m venv .venv
```

Activa el entorno, instala las dependencias, crea la configuración local y prepara la base de datos:

```bash
python -m pip install -r requirements.txt
```

En macOS/Linux:

```bash
cp .env.example .env
```

En PowerShell:

```powershell
Copy-Item .env.example .env
```

Para desarrollo local puedes usar el valor de ejemplo. Antes de desplegar, genera una clave `DJANGO_SECRET_KEY` nueva, establece `DJANGO_DEBUG=false` y limita `DJANGO_ALLOWED_HOSTS` a los dominios de despliegue.

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abre `http://127.0.0.1:8000/admin/` para agregar misiones y recompensas. Para que aparezca el canje del tema acuático, crea una recompensa cuyo título sea exactamente `Tema Acuático`. Luego entra a `http://127.0.0.1:8000/` y registra una cuenta de prueba.

## Decisiones de implementación

- Completar una misión requiere una sesión iniciada y una solicitud POST; una misión ya completada no vuelve a sumar puntos.
- El canje valida el saldo y evita cobrar dos veces la misma recompensa.
- La base SQLite y la clave de desarrollo se mantienen fuera del control de versiones.

Proyecto universitario. Las cuentas y datos originales de desarrollo no se incluyen; crea datos nuevos para una demostración.
