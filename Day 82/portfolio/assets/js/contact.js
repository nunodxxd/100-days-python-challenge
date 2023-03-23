(function () {
    emailjs.init("pmB4RMVixlIjuHogu");
    })();
// send emails to emailjs
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    // these IDs from the previous steps
    emailjs.sendForm('service_v1mg06q', 'template_uknxvtx', this)
        .then(function() {
            console.log('SUCCESS!');
        }, function(error) {
            console.log('FAILED...', error);
        });
});
