from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.support import get_duration, format_duration


def storage_information_view(request):

    non_closed_visits = []

    visits_not_leaved = Visit.objects.filter(leaved_at=None)
    for visit_not_leaved in visits_not_leaved:
        non_closed_visits.append({
            'who_entered': visit_not_leaved.passcard,
            'entered_at': visit_not_leaved.entered_at,
            'duration':  format_duration(get_duration(visit_not_leaved))
            })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
