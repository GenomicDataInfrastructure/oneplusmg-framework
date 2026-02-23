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


// Add this script before the closing </body> tag
document.addEventListener('DOMContentLoaded', function() {
    // Function to highlight and fade
    function highlightElement() {
        const hash = window.location.hash;
        if (hash) {
            const target = document.querySelector(hash);
            if (target) {
                // Remove any existing highlights
                document.querySelectorAll('.highlight-fade').forEach(el => {
                    el.classList.remove('highlight-fade');
                });
                
                // Add highlight class
                target.classList.add('highlight-fade');
                
                // Remove highlight after animation completes (2 seconds)
                setTimeout(() => {
                    target.classList.remove('highlight-fade');
                }, 2000);
            }
        }
    }
    
    // Trigger on hash change (when clicking a link)
    window.addEventListener('hashchange', highlightElement);
    
    // Trigger on page load if hash exists
    if (window.location.hash) {
        setTimeout(highlightElement, 100); // Small delay to ensure scroll completes
    }
});

//accordion

document.querySelectorAll('details').forEach(detail => {
    const summary = detail.querySelector('summary');
    const body = detail.querySelector('.accordion-body');

    summary.addEventListener('click', e => {
      e.preventDefault();
      const isOpen = detail.hasAttribute('open');

      // Close all open panels smoothly
      document.querySelectorAll('details[open]').forEach(openDetail => {
        const openBody = openDetail.querySelector('.accordion-body');
        openBody.style.height = openBody.scrollHeight + 'px';
        requestAnimationFrame(() => {
          openBody.style.height = '0px';
          openBody.style.opacity = '0';
        });
        openBody.addEventListener('transitionend', () => {
          openDetail.removeAttribute('open');
        }, { once: true });
      });

      // Open clicked panel if it was closed
      if (!isOpen) {
        detail.setAttribute('open', '');
        const targetHeight = body.scrollHeight + 'px';
        body.style.height = targetHeight;
        body.style.opacity = '1';
        body.addEventListener('transitionend', () => {
          body.style.height = 'auto';
        }, { once: true });
      }
    });
  });


  //scroll through content
  const links = document.querySelectorAll('.spy-link');
  const sections = document.querySelectorAll('.page-content section');

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        links.forEach(link => link.classList.remove('active'));
        const active = document.querySelector(`.spy-link[href="#${entry.target.id}"]`);
        if (active) active.classList.add('active');
      }
    });
  }, { rootMargin: '0px 0px -70% 0px' });

  sections.forEach(sec => observer.observe(sec));

  //Tabbed content

  const buttons = document.querySelectorAll('.tab-btn');
  const panels = document.querySelectorAll('.tab-panel');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.classList.remove('active'));
      panels.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      document.getElementById('tab-' + btn.dataset.tab).classList.add('active');
    });
  });
