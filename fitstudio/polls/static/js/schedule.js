$(document).ready(function() {
    // page is now ready, initialize the calendar...
    $('#calendar').fullCalendar({
        /*
        $.ajax({
            url: '/ajax/calendar/',
            data: {
                'username': username
            },
            dataType: 'json',
            success: function (data) {
                if (data.is_taken) {
                    alert("A user with this username already exists.");
                }
            }
        });
        */
        locale: 'pl',
        defaultView: 'agendaDay',
        defaultDate: '2018-01-16',
        header: {
            left: 'prev,next today',
            center: 'Plan zajęć',
            right: 'month,agendaWeek,agendaDay'
        },
        editable: false,
        events: [
            {
                title: 'Salsa',
                color: 'yellow',
                textColor: 'black',
                start: '2018-01-16T17:15:00Z',
                end: '2018-01-16T18:30:00Z'
            },
            {
                title: 'Bachata',
                color: 'white',
                textColor: 'black',
                start: '2018-01-16T18:30:00Z',
                end: '2018-01-16T19:45:00Z'
            }
        ]


        /*
        defaultView: 'agendaDay',
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        defaultDate: '2014-06-12',
        editable: true,
        events: [
            {
                title: 'All Day Event',
                start: '2014-06-01'
            },
            {
                title: 'Long Event',
                start: '2014-06-07',
                end: '2014-06-10'
            },
            {
                id: 999,
                title: 'Repeating Event',
                start: '2014-06-09T16:00:00'
            },
            {
                id: 999,
                title: 'Repeating Event',
                start: '2014-06-16T16:00:00'
            },
            {
                title: 'Meeting',
                start: '2014-06-12T10:30:00',
                end: '2014-06-12T12:30:00'
            },
            {
                title: 'Lunch',
                start: '2014-06-12T12:00:00'
            },
            {
                title: 'Birthday Party',
                start: '2014-06-13T07:00:00'
            },
            {
                title: 'Click for Google',
                url: 'http://google.com/',
                start: '2014-06-28'
            }
        ]
        */
    })
});
