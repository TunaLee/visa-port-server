# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Class Section
class AlarmModelMixin(models.Model):
    is_expiration_date_alarm = models.BooleanField(_('체류 만기 알람 여부'), default=False)
    is_visit_reservation = models.BooleanField(_('방문 예약 알람 여부'), default=False)

    expiration_date = models.DateTimeField(_('체류 만기 일자'), null=True, blank=True)
    visit_reservation_date = models.DateTimeField(_('방문 예약 일자'), null=True, blank=True)

    class Meta:
        abstract = True

    def pin_club(self, club):
        club_pin, created = ClubPin.objects.get_or_create(user=self, club=club)
        if not created:
            club_pin.is_active = True
            club_pin.save()
        return club_pin

    def update_user_club_pin_count(self):
        self.club_pin_count = self.club_pins.filter(is_active=True).count()
