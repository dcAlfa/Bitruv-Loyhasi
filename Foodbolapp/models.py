from django.db import models
class Davlat(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Club(models.Model):
    nom = models.CharField(max_length=50)
    rasm = models.FileField(upload_to="Medialar")
    prisident = models.CharField(max_length=30)
    murabbiy = models.CharField(max_length=30, null=True)
    yil = models.DateField(null=True)
    record_tr = models.PositiveSmallIntegerField()
    record_ar = models.PositiveSmallIntegerField()
    davlat = models.ForeignKey(Davlat, on_delete=models.CASCADE, related_name="davlat_clublari")

    def __str__(self):
        return self.nom

class Player(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveSmallIntegerField()
    davlat = models.CharField(max_length=50)
    pazitsiya = models.CharField(max_length=50)
    narx = models.PositiveSmallIntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    cl_from = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="cl_from")
    club_to = models.ForeignKey(Club, on_delete=models.CASCADE)
    t_narx = models.PositiveSmallIntegerField()
    narx = models.PositiveSmallIntegerField()
    mavsum = models.CharField(max_length=50)

    def __str__(self):
        return self.player.ism



