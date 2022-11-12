document.addEventListener('DOMContentLoaded', () => {
    let arrayInputMask = []

    django.jQuery('.version-field').each(function (index, element) {
        let versionMask = new IMask(
            element,
            {
                mask: /^[0-9]{0,2}.?[0-9]{0,2}.?[0-9]{0,3}$/
            });
        arrayInputMask.push(versionMask);
    });
})