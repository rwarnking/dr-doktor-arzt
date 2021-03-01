import $ from 'cash-dom'
import axios from 'axios'

window.addEventListener('DOMContentLoaded', () => {
    $('#appointment-hours').on('click', '.timeslot.time-free', async function(event) {

        const e = $(this);
        const success = await axios.post('/de/termine', null, { params: { slot: e.data('slot') }})
            .catch(() => false)
            .then((r) => r.data.success)

        if (success) {
            alert('Okay!');
            e.removeClass('time-free');
            e.addClass('time-taken');
            e.text('Taken')
        } else {
            alert('Nope!');
        }
    });
});
