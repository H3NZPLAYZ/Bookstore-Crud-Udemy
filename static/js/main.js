let clearForm = () => {
    let form = document.getElementById('book-form');
    document.getElementById('form-errors').replaceChildren();

    form.querySelectorAll('input:not([name="csrfmiddlewaretoken"])').forEach(
        input => input.value = ''
    );

    form.querySelectorAll('select').forEach(
    select => {
        select.selectedIndex = 0;
        select.dispatchEvent(new Event('change'));
    });
}