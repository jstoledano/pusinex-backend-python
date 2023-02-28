from django.db import models
from django.contrib.auth.models import User

CAT_TIPO = (
    (1, 'URBANO CONCENTRADO'),
    (2, 'URBANO(A)'),
    (3, 'MIXTO'),
    (4, 'RURAL'),
    (5, 'RURAL DISPERSO')
)

CAT_CABECERA = (
    (1, 'CAPITAL DEL ESTADO'),
    (2, 'CABECERA DISTRITAL'),
    (3, 'CABECERA MUNICIPAL'),
    (4, 'CABECERA SECCIONAL')
)


class Entidad(models.Model):
    entidad = models.PositiveSmallIntegerField()
    nombre = models.TextField()

    class Meta:
        verbose_name_plural = 'Entidades'

    def __str__(self):
        return f'{self.entidad:02} {self.nombre}'


class Distrito(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    distrito = models.PositiveSmallIntegerField()
    cabecera = models.TextField()

    def __str__(self):
        return f'{self.entidad.entidad:02}-{self.distrito:02}'

    def get_distrito(self):
        return self.distrito


class Municipio(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    municipio = models.PositiveSmallIntegerField()
    nombre = models.TextField()

    class Meta:
        verbose_name_plural = 'Municipios'
        ordering = ['municipio', ]

    def __str__(self):
        return f'{self.municipio:03} {self.nombre}'


class Seccion(models.Model):
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    seccion = models.PositiveSmallIntegerField()
    tipo = models.PositiveSmallIntegerField(choices=CAT_TIPO)

    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'

    def __str__(self):
        return f'{self.distrito.distrito:02} {self.municipio.municipio:03} {self.seccion:04}'


class Localidad(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    localidad = models.PositiveSmallIntegerField()
    nombre = models.TextField(max_length=150)
    tipo = models.PositiveSmallIntegerField(choices=CAT_TIPO)
    cabecera = models.PositiveSmallIntegerField(choices=CAT_CABECERA, null=True)

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        ordering = ['municipio__municipio', 'localidad', ]

    def __str__(self):
        return f'{self.municipio.municipio:03} {self.localidad:04} {self.nombre}'


class Pusinex(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'PUSINEX'
        verbose_name_plural = 'PUSINEXs'
        ordering = ['seccion__distrito__distrito', 'seccion__seccion', 'localidad__localidad', ]

    def __str__(self):
        return f'{self.seccion.seccion:04} {self.localidad.localidad:04} {self.localidad.nombre}'


# Función para subir archivos
def pusinex_file(p, file):
    import os.path
    ext = file.split('.')[-1]
    orig = 'pusinex'
    distrito = p.pusinex.seccion.distrito.distrito
    seccion = p.pusinex.seccion.seccion
    localidad = p.pusinex.localidad.localidad
    nombre = f'29{distrito:02}{seccion:04}-{localidad:04}_rev{p.f_act:%Y%m%d}.{ext}'
    ruta = os.path.join(orig, f'{distrito:02}', nombre)
    return ruta


class Revision(models.Model):
    pusinex = models.ForeignKey(Pusinex, on_delete=models.CASCADE)
    f_act = models.DateField()
    hojas = models.PositiveSmallIntegerField()
    observaciones = models.TextField(blank=True, null=True)
    archivo = models.FileField(upload_to=pusinex_file, blank=True, null=True)

    # Trazabilidad
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        d = self.pusinex.seccion.distrito.distrito
        s = self.pusinex.seccion.seccion
        loc = self.pusinex.localidad.localidad
        return f'29{d:02}{s:04}-{loc:04}_rev{self.f_act:%Y%m%d}'

    class Meta:
        get_latest_by = "f_act"
