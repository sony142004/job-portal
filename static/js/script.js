document.addEventListener('DOMContentLoaded', () => {
    // Add micro-animations and interactions
    
    // Clear search form
    const btnClear = document.querySelector('.btn-clear');
    if (btnClear) {
        btnClear.addEventListener('click', () => {
            document.querySelectorAll('.search-input').forEach(input => input.value = '');
        });
    }

    // Toggle job card active state
    const jobCards = document.querySelectorAll('.job-card');
    jobCards.forEach(card => {
        card.addEventListener('click', (e) => {
            // Prevent if clicking on save button
            if (e.target.closest('.btn-save')) return;
            
            jobCards.forEach(c => c.classList.remove('active'));
            card.classList.add('active');
            
            // In a real application, clicking a card would fetch the job details
            // through AJAX or a full page reload.
            // For now, we will add brief visual feedback:
            card.style.transform = 'scale(0.98)';
            setTimeout(() => {
                card.style.transform = 'scale(1)';
            }, 150);
        });
    });

    // Animate the detail card entry
    const detailCard = document.querySelector('.job-details-card');
    if (detailCard) {
        detailCard.style.opacity = '0';
        detailCard.style.transform = 'translateY(20px)';
        detailCard.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
        
        requestAnimationFrame(() => {
            setTimeout(() => {
                detailCard.style.opacity = '1';
                detailCard.style.transform = 'translateY(0)';
            }, 100);
        });
    }

    // Interactive filter buttons
    const filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            btn.style.background = '#e5f3ff';
            btn.style.borderColor = '#0062ff';
            setTimeout(() => {
                btn.style.background = '#f9fafb';
                btn.style.borderColor = '#d1d5db';
            }, 200);
        });
    });
});
