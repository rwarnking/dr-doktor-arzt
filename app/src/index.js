import $ from 'cash-dom'
import axios from 'axios'

window.addEventListener('DOMContentLoaded', () => {

    // book a specific time slot
    $('#appointment-hours').on('click', '.timeslot.time-free', async function() {

        const e = $(this);
        const s = $('.selected-day');

        const html = await axios.post(`/en/appointment/${s.data('year')}/${s.data('month')}/${s.data('day')}/${e.data('slot')}`)
            .catch(() => alert("invalid request"))
            .then(response => response.data)

        if (html) {
            $('#appointment-hours').html(html);
        }
    });

    // load all appointment slots for one day
    $('#appointment-days').on('click', '.dayslot', async function() {

        const e = $(this);
        // unselect previously selected day
        $('.selected-day').removeClass('selected-day');
        // select day
        e.addClass('selected-day');

        const html = await axios.get(`/en/appointment/${e.data('year')}/${e.data('month')}/${e.data('day')}`)
            .catch(() => alert("invalid request"))
            .then(response => response.data)

        if (html) {
            $('#appointment-hours').html(html);
        }
    });

    // $('#appointment-month').on('click', '.monthsdays', async function() {

    //     const e = $(this);

    //     $('.selected-month').removeClass('selected-month');
    //     // select month
    //     e.addClass('selected-month');

    //     const html = await axios.get(`/en/appointment/${e.data('year')}/${e.data('month')}`)
    //         .catch(() => alert("invalid request"))
    //         .then(response => response.data)

    //     if (html) {
    //         $('#appointment-days').html(html);
    //     }
    // });
});
