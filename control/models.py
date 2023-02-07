from django.db import models

# Create your models here.

ENTIDAD = (
    (29, 'TLAXCALA'),
)

DISTRITO = (
    (1, 'APIZACO'),
    (2, 'TLAXCALA DE XICOHTENCATL'),
    (3, 'ZACATELCO')
)

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
        return f'{self.entidad.entidad:02}-{self.distrito}'


class Municipio(models.Model):
    entidad = models.PositiveSmallIntegerField(choices=ENTIDAD)
    municipio = models.PositiveSmallIntegerField()
    nombre = models.TextField()

    class Meta:
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return f'{self.municipio:03} {self.nombre}'


class Seccion(models.Model):
    distrito = models.PositiveSmallIntegerField(choices=DISTRITO)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    seccion = models.PositiveSmallIntegerField()
    tipo = models.PositiveSmallIntegerField(choices=CAT_TIPO)

    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'

    def __str__(self):
        return f'{self.distrito:02} {self.municipio.municipio:03} {self.seccion:04}'


class Localidad(models.Model):
    localidad = models.PositiveSmallIntegerField()
    nombre = models.TextField(max_length=150)
    tipo = models.PositiveSmallIntegerField(choices=CAT_TIPO)
    cabecera = models.PositiveSmallIntegerField(choices=CAT_CABECERA, null=True)

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return f'{self.localidad:04} {self.nombre}'


class Pusinex(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'PUSINEX'
        verbose_name_plural = 'PUSINEXs'
        get_latest_by = 'f_actual'

    def __str__(self):
        return f'{self.seccion.seccion:04} {self.localidad.localidad:04} {self.localidad.nombre} ({self.f_actual})'


class Revision(models.Model):
    pusinex = models.ForeignKey(Pusinex, on_delete=models.CASCADE)
    f_act = models.DateField()
    hojas = models.PositiveSmallIntegerField()
    observaciones = models.TextField()
    archivo = models.FileField()