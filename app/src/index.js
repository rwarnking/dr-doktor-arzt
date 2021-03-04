import $ from 'cash-dom'
import axios from 'axios'

window.addEventListener('DOMContentLoaded', () => {

    // book a specific time slot
    $('#appointment-hours').on('click', '.timeslot.time-free', async function() {

        const e = $(this);
        const s = $('.selected-day');

        const hours_html = await axios.post(`/en/appointment/${s.data('year')}/${s.data('month')}/${s.data('day')}/${e.data('slot')}`)
            .catch(() => alert("invalid request"))
            .then(response => response.data)

        if (hours_html) {
            $('#appointment-hours').html(hours_html);
        }
    });


    // load all appointment slots for one day
    $('#appointment-days').on('click', '.dayslot', async function() {

        const e = $(this);
        // unselect previously selected day
        $('.selected-day').removeClass('selected-day');
        // select day
        e.addClass('selected-day');

        const hours_html = await axios.get(`/en/appointment/${e.data('year')}/${e.data('month')}/${e.data('day')}`)
            .catch(() => alert("invalid request"))
            .then(response => response.data)

        if (hours_html) {
            $('#appointment-hours').html(hours_html);
        }
    });


    // load all appointment slots for one day
    $('#appointment-hours').on('click', '.date-prev', async function() {
        const e = $(this);

        const hours_html = await axios.get(`/en/appointment/${e.data('year')}/${e.data('month')}/${e.data('day')}`)
            .catch(() => alert("invalid request"))
            .then(response => response.data)

        if (hours_html) {
            $('#appointment-hours').html(hours_html);
        }
    });


    $('#appointment-hours').on('click', '.date-next', async function() {
        const e = $(this);

        const hours_html = await axios.get(`/en/appointment/${e.data('year')}/${e.data('month')}/${e.data('day')}`)
            .catch(() => alert("invalid request"))
            .then(response => response.data)

        if (hours_html) {
            $('#appointment-hours').html(hours_html);
        }
    });


    $('#appointment-days').on('click', '.date-prev', async function() {
        const e = $(this);

        const days_html = await axios.get(`/en/appointment/${e.data('year')}/${e.data('month')}`)
            .catch(() => alert("invalid request"))
            .then(response => response.data)

        if (days_html) {
            $('#appointment-days').html(days_html);
        }

        const hours_html = await axios.get(`/en/appointment/${e.data('year')}/${e.data('month')}/1`)
            .catch(() => alert("invalid request"))
            .then(response => response.data)

        if (hours_html) {
            $('#appointment-hours').html(hours_html);
        }
    });


    $('#appointment-days').on('click', '.date-next', async function() {
        const e = $(this);

        const days_html = await axios.get(`/en/appointment/${e.data('year')}/${e.data('month')}`)
            .catch(() => alert("invalid request"))
            .then(response => response.data)

        if (days_html) {
            $('#appointment-days').html(days_html);
        }

        const hours_html = await axios.get(`/en/appointment/${e.data('year')}/${e.data('month')}/1`)
            .catch(() => alert("invalid request"))
            .then(response => response.data)

        if (hours_html) {
            $('#appointment-hours').html(hours_html);
        }
    });
});
