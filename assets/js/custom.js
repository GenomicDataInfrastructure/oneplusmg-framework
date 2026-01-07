// Meal definitions
const meals = {
    morning: {
        title: 'Before birth',
        description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
    },
    lunch: {
        title: 'Childhood',
        description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
    },
    dinner: {
        title: 'Adulthood',
        description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
    }
};

const foodItems = document.querySelectorAll('.topic-item');
const mealTabs = document.querySelectorAll('.topic-tab');
//const infoBox = document.getElementById('infoBox');

let currentMeal = 'morning';

function updateActiveMeal(meal) {
    currentMeal = meal;

    // Update tabs
    mealTabs.forEach(tab => {
        if (tab.dataset.meal === meal) {
            tab.classList.add('active');
        } else {
            tab.classList.remove('active');
        }
    });

    // Update food items visibility
    foodItems.forEach(item => {
        if (item.dataset.meal === meal) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });

    // Update info box
    const mealInfo = meals[meal];
/*     infoBox.innerHTML = `
        <div class="card-body text-center">
            <h3 class="card-title text-primary mb-3">${mealInfo.title}</h3>
            <p class="card-text text-muted">${mealInfo.description}</p>
        </div>
    `; */
}

// Meal tab click handlers
mealTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const meal = tab.dataset.meal;
        updateActiveMeal(meal);
    });
});

// Initialize with morning meal
updateActiveMeal('morning');