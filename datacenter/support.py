from django.utils.timezone import localtime


def get_duration(visit):
    return ((visit.leaved_at if visit.leaved_at else localtime()) - visit.entered_at)


def is_visit_long(visit, minutes=60):
    return get_duration(visit).seconds >= minutes * 60


def format_duration(duration):
    sec = duration.seconds
    hours = sec // 3600
    sec = sec - (hours * 3600)
    minutes = sec // 60

    return "{:02}:{:02}".format(int(hours), int(minutes))
