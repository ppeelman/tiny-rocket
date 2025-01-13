const reloadButton = document.querySelector('#load-rockets-btn')
const rocketsGrid = document.querySelector('#rockets-grid')

async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}

function createRocketElement(rocket) {
    const rocketElement = document.createElement('article')
    rocketElement.classList.add('rocket')

    rocketElement.innerHTML = `
        <h1 class="rocket__name">${rocket.name}</h1>
        <span class="rocket__description">${rocket.description}</span>
        <section class="rocket__success-rate">
            <label for="fuel">Success rate: ${rocket.success_rate_pct}%</label>
            <meter id="fuel" min="0" max="100" low="33" high="66" optimum="80"
                   value="${rocket.success_rate_pct}"></meter>
        </section>
        `
    return rocketElement
}

function showRockets(rockets) {
    for (const rocket of rockets) {
        const rocketElement = createRocketElement(rocket)
        rocketsGrid.appendChild(rocketElement)
    }
}

function showLoadingState() {
    // Disable reload button
    reloadButton.disabled = true;
    reloadButton.textContent = 'Loading...'

    // Show skeleton loaders in rockets grid
    rocketsGrid.innerHTML = ''
    for (const _ of new Array(6).fill(null)) {
        const skeletonElement = document.createElement('article')
        skeletonElement.classList.add('skeleton', 'rocket-skeleton')
        rocketsGrid.appendChild(skeletonElement)
    }
}

function removeLoadingState() {
    // Restore reload button
    reloadButton.disabled = false;
    reloadButton.textContent = 'Reload ⟳'

    // Replace rockets grid
    rocketsGrid.innerHTML = ''
}

async function main() {
    reloadButton.addEventListener('click', async () => {
        showLoadingState()
        try {
            const response = await fetch('/api/rockets')
            const rockets = await response.json()

            if (!response.ok) {
                alert('Failed to load rockets`')
            }

            // Let's add a bit of artifical delay to simulate network delay and admire the UI :)
            await sleep(1000)

            removeLoadingState()
            showRockets(rockets)
        } catch (err) {
            alert('Failed to load rockets')
        }
    })
}

main();