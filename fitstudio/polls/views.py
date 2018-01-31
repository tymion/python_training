from django.shortcuts import render
import logging
import datetime

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.template import loader

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.db.models import Q

from .models import WorkHours, ActivityTimeTable, ActivityDone, Category, DayOfTheWeek

from .forms import NameForm, AddCategoryForm, ListCategoryForm, EditCategoryForm
from .forms import AddDayOfTheWeekForm, ListDayOfTheWeekForm, EditDayOfTheWeekForm

logger = logging.getLogger(__name__)

def get_name(request):
    if request.method == "POST":
        logger.error('=============Invalid date value1.')
        form = NameForm(request.POST)
        if form.is_valid():
            logger.error('=============Invalid date value.2')
            return HttpResponseRedirect('/thanks/')
    else:
        logger.error('=============Invalid date value.i3')
        form = NameForm()

    logger.error('=============Invalid date value4.')
    return render(request, 'polls/index.html', {'form': form})

def get_form_response(request, template_str, add_form, list_form, edit_form):
    forms = {
        'add_form': add_form,
        'list_form': list_form
    }
    if edit_form:
        forms.update({'edit_form': edit_form })

    template = loader.get_template(template_str)
    return render(request, template_str, forms)

def unpack_day_of_the_week(packed_day):
    return packed_day[1:-1].split(",", 1)

def time(request):

    add_form = None
    list_form = None
    edit_form = None

    if request.method == "POST":
        button = request.POST["form_button"]

        # adding new category
        if button == "Add":

            add_form = AddDayOfTheWeekForm(request.POST)
            if add_form.is_valid():

                add_form.save()
                messages.info(request, 'Day was added.')
                # redirection prevent from resending post after page refresh
                return HttpResponseRedirect(request.path)

        # day was selected
        elif button == "Edit":

            # edit day
            [ index, day_name ] = unpack_day_of_the_week(request.POST.get('days_list'))
            data = {'edit_day_text': day_name, 'edit_day_index': index}
            edit_form = EditDayOfTheWeekForm(data)
            request.session['original_day_data'] = data

        # delete day
        elif button == "Delete":

            DayOfTheWeek.objects.filter(day_text=day_name).delete()
            messages.info(request, 'Day was deleted.')
            # redirection prevent from resending post after page refresh
            return HttpResponseRedirect(request.path)

        # try to edit category_text
        elif button == "Submit":

            edit_form = EditCategoryForm(request.POST, initial=request.session['original_day_data'])
            logger.error('========has_changed:{0}======== '.format(edit_form.has_changed()))
            if edit_form.has_changed() == False :
                messages.error(request, 'Day name or index value was not changed.')
            # check if changed value don't match with other value in db
            elif (request.session['original_day_text'] != request.POST['edit_day_text'] and DayOfTheWeek.objects.filter(day_text=request.POST['edit_day_text'])) or (request.session['original_day_index'] != request.POST['edit_day_index'] and DayOfTheWeek.objects.filter(index_int=request.POST['edit_day_index'])):
                messages.error(request, 'Day name or value already exists.')
            else:
                data = DayOfTheWeek.objects.get(day_text=request.session['origin_day_text'])
                data.day_text = request.POST['edit_day_text']
                data.index_int = request.POST['edit_day_index']
                data.save()
                messages.info(request, 'Day was changed.')
                return HttpResponseRedirect(request.path)

        else:

            logger.error('Unknown form has send POST request!')
            return HttpResponseBadRequest()

    if add_form is None:
        add_form = AddDayOfTheWeekForm()
    if list_form is None:
        list_form = ListDayOfTheWeekForm()

    return get_form_response(request, 'polls/time.html', add_form, list_form, edit_form)

def category(request):

    add_form = None
    list_form = None
    edit_form = None

    if request.method == "POST" :
        button = request.POST["form_button"]

        # adding new category
        if button == "Add" :

            add_form = AddCategoryForm(request.POST)
            if add_form.is_valid():
                add_form.save()
                messages.info(request, 'Category was added.')
                # redirection prevent from resending post after page refresh
                return HttpResponseRedirect(request.path)

        # edit category
        elif button == "Edit":

            data = Category.objects.get(category_text = request.POST['categories_list'])
            edit_form = EditCategoryForm(instance = data)
            request.session['original_category_text'] = request.POST['categories_list']

        # delete category
        elif button == "Delete":

            Category.objects.filter(category_text = request.POST['categories_list']).delete()
            messages.info(request, 'Category was deleted.')
            # redirection prevent from resending post after page refresh
            return HttpResponseRedirect(request.path)

        # try to edit category_text
        elif button == "Submit":

            instance = Category.objects.get(category_text = request.session['original_category_text'])
            edit_form = EditCategoryForm(request.POST, instance = instance)
            if edit_form.is_valid():
                edit_form.save()
                messages.info(request, 'Category was changed.')
                return HttpResponseRedirect(request.path)

        else:

            logger.error('Unknown form has send POST request!')
            return HttpResponseBadRequest()

    if add_form is None:
        add_form = AddCategoryForm()
    if list_form is None:
        list_form = ListCategoryForm()

    return get_form_response(request, 'polls/category.html', add_form, list_form, edit_form)

def schedule(request):
    template = loader.get_template('polls/schedule.html')
    return render(request, 'polls/schedule.html')

def index(request):
    template = loader.get_template('polls/index.html')
    return render(request, 'polls/index.html')

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
            'is_taken': User.objects.filter(username_iexact=username).exists()
            }
    return JsonResponse(data)

def get_default_work_hours():
    data = {
        'allDaySlot': 'false',
        'axisFormat': 'h:mm A',
        'timeFormat': 'h:mm T',
        'minTime': '08:00:00',
        'maxTime': '23:00:00',
    }
    return data

def get_work_hours(date):

    if date is None:
        logger.error('Invalid date value.')
        return None

    workHours = WorkHours.objects.filter(dateStart_date__lte=date).filter(Q(dateEnd_date__gte=date)
            | Q(dateEnd_date__isnull=True))

    workHour = None
    for val in workHours:
        days_array = val.day_array
        for day in val.day_array.all():
            if day.index_int == date.weekday():
                workHour = val
                break
        if workHour is not None:
            break

    if workHour is None:
        return get_default_work_hours()

    data = {
        'axisFormat': 'h:mm A',
        'timeFormat': 'h:mm T',
        'minTime': workHour.hourStart_time,
        'maxTime': workHour.hourEnd_time,
    }
    return data

def parse_coach_name(coach_key):
    data = coach_key.name_text
    if coach_key.alias_text is not None:
        data += " \"" + coach_key.alias_text + "\" "
    data += coach_key.surname_text
    return data

def parse_date_time(activity, date):
    term = activity.term_key
    data = {
        'start': str(date) + "T" + str(term.timeStart_time) + "Z",
        'end': str(date) + "T" + str(term.timeEnd_time) + "Z"
    }
    return data

def parse_activity(activity, date):
    data = {
        'title': activity.activity_text + "\n" + parse_coach_name(activity.coach_key),
    }
    data.update(parse_date_time(activity, date))
    return data

def parse_activity_done(activityDone):
    activity = activityDone.activity_key
    title = activity.activity_text
    if activity.coachReplacement_key is not None:
        title += "\n" + pars_coach_name(activityDone.coachReplacement_key)
    else:
        title += "\n" + parse_coach_name(activity.coach_key)
    data = {
        'title': title,
    }
    data.update(parse_date_time(activity, date))

    return data

def check_activity(activity, date):
    for day in activity.term_key.day_array.all():
        if day.index_int == date.weekday():
            return True
    return False

def get_events(date):

    if date is None:
        logger.error('Invalid date value.')
        return None

    events_cnt = 0
    parsed_activities = {}
    now = datetime.date.today()
    logger.error('=============Invalid date value.' + str(now))
    if date <= now:
        activities = ActivityDone.objects.filter(date=date)
        for activity in activities:
            parsed_activities.update(parse_activity_done(activity))
            events_cnt += 1

    if date >= now:
        activities = ActivityTimeTable.objects.filter(dateStart_date__lte=date).filter(Q(dateEnd_date__gte=date) | Q(dateEnd_date__isnull=True))
        for activity in activities:
            if check_activity(activity, date) == True:
                parsed_activities.update(parse_activity(activity, date))
                events_cnt += 1
    if events_cnt == 0:
        return None

    events = {
        'events': [
            parsed_activities
        ]
    }
    logger.error('==== Requesting for data from date:' + str(events))
    return events

def get_fullcalendar_data(request):
    date_str = request.GET.get('date', None)
    if date_str is None:
        logger.error('To receive callendar data You need to provide date.')
        raise Http404("Poll does not exist")
    logger.error('==== Requesting for data from date:' + date_str)

    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

    data = {
        'locale': 'pl',
        'defaultView': 'agendaDay',
        'defaultDate': date_str,
        'header': {
            'left': 'prev,next today',
            'center': 'title',
            'right': 'month,agendaWeek,agendaDay'
        },
        'editable': 'false',
    }
    hours = get_work_hours(date)
    logger.error(hours)
    if hours is not None:
        data.update(hours)
    events = get_events(date)
    if events is not None:
        data.update(events)

    return JsonResponse(data)
