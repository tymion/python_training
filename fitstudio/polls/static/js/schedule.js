$(document).ready(function() {
    // page is now ready, initialize the calendar...
        resp = $.ajax({
            url: '/polls/ajax/calendar/',
            data: {
                'date': moment(new Date()).format('YYYY-MM-DD')
            },
            dataType: 'json',
            success: function (data) {
                $('#calendar').fullCalendar(data);
            }
        });
        /*
    $('#calendar').fullCalendar({
        locale: 'pl',
        defaultView: 'agendaDay',
        defaultDate: moment(new Date()).format('YYYY-MM-DD'),
        header: {
            left: 'prev,next today',
            center: 'textsad',
            right: 'month,agendaWeek,agendaDay'
        },
        navLinks: true,
        dayClick: function(date, jsEvent, view) {
            console.log('day', date.format());
            console.log('coords', jsEvent.pageX, jsEvent.pageY);
        },
        events: [
            {
                title: 'All Day Event',
                color: 'yellow',
                textColor: 'black',
                start: '2014-06-01'
            },
            {
                id: 999,
                title: 'Repeating Event',
                start: '2014-06-16T16:00:00'
            },
            {
                title: 'Click for Google',
                url: 'http://google.com/',
                start: '2014-06-28',
                end: '2018-01-16T18:30:00Z'
            }
        ]
    })
        */
});
