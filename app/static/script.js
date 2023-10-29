window.onload = () => {
    const $ = document.querySelector.bind(document)

    const queryString = window.location.search
    const parameters = new URLSearchParams(queryString)
    const tab = parameters.get('tab')

    if (tab) {
        $(`.tab.${tab}`).classList.add('active')
    } else {
        $('.tab.encrypt').classList.add('active')
    }

    $('.tabs').childNodes.forEach(tab => {
        tab.addEventListener('click', () => {
            const urlParams = new URLSearchParams(window.location.search)
            urlParams.set('tab', tab.innerHTML.toLowerCase())
            window.location.search = urlParams
        })
    })
}
