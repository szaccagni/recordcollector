const nav = document.querySelector('.nav-right')

document.addEventListener('DOMContentLoaded', function() {
    if (nav) activeNavItem()
})

function activeNavItem() {
    const navItems = nav.querySelectorAll('a')
    navItems.forEach(item => {
        const color = item.dataset.color
        if (item.dataset.activeLink === item.id) item.style.borderBottom = `3px solid ${color}`
    })
}