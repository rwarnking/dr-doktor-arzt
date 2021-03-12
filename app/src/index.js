import $ from 'cash-dom'
import axios from 'axios'


window.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#appointmentModal').addEventListener('show.bs.modal', function(event) {
        const button = event.relatedTarget;
        let t = $('#appointmentText');
        t.text(button.getAttribute('data-complete'));
        t.data("slot", button.getAttribute('data-slot'));
    })

    // book a specific time slot
    $('#appointmentForm').on('submit', async function(event) {

        event.preventDefault();

        const t = $('#appointmentText');
        const s = $('.selected-day');

        const slot = Number.parseInt(t.data('slot'));
        const fname = $('#firstName').val();
        const lname = $('#lastName').val();
        const id = $('#insuranceID').val();
        const requestData = {
            slot: slot,
            day: Number.parseInt(s.data('day')),
            month: Number.parseInt(s.data('month')),
            year: Number.parseInt(s.data('year')),
            firstName: fname,
            lastName: lname,
            insuranceID: id
        };

        const hours_html = await axios.post(`/en/appointment/register`, requestData)
            .catch((error) => {
                alert(error.response ? error.response.data : 'An error occured');
                return false;
            })
            .then(response => response.data)

        if (hours_html) {
            $('#appointmentForm button[data-bs-dismiss]').trigger('click');
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
        const prev = e.data('day');

        const hours_html = await axios.get(`/en/appointment/${e.data('year')}/${e.data('month')}/${prev}`)
            .catch(() => alert("invalid request"))
            .then(response => response.data)

        if (hours_html) {
            $('#appointment-hours').html(hours_html);
            $('.selected-day').removeClass('selected-day');
            $(`.dayslot[data-day="${prev}"]`).addClass('selected-day');
        }
    });


    $('#appointment-hours').on('click', '.date-next', async function() {
        const e = $(this);
        const next = e.data('day');

        const hours_html = await axios.get(`/en/appointment/${e.data('year')}/${e.data('month')}/${next}`)
            .catch(() => alert("invalid request"))
            .then(response => response.data)

        if (hours_html) {
            $('#appointment-hours').html(hours_html);
            $('.selected-day').removeClass('selected-day');
            $(`.dayslot[data-day="${next}"]`).addClass('selected-day');
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
