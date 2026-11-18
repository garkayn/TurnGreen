from django.contrib import admin

from .models import (
    RecompensaComprada,
    UsuarioLeafpoints,
    mision_completada,
    misiones,
    recompensas,
)


admin.site.register(misiones)
admin.site.register(recompensas)
admin.site.register(mision_completada)
admin.site.register(UsuarioLeafpoints)
admin.site.register(RecompensaComprada)
