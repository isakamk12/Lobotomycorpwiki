document.addEventListener('DOMContentLoaded', () => {
    // Reveal animations on scroll
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                
                // If it contains a meter-fill, animate it
                const meterFill = entry.target.querySelector('.meter-fill');
                if (meterFill && meterFill.dataset.width) {
                    setTimeout(() => {
                        meterFill.style.width = meterFill.dataset.width;
                    }, 400);
                }
            }
        });
    }, { threshold: 0.1 });

    revealElements.forEach(el => revealObserver.observe(el));

    // Dynamic Header Glitch Effect
    const headerTitle = document.querySelector('header h1');
    if (headerTitle) {
        setInterval(() => {
            if (Math.random() > 0.95) {
                headerTitle.style.textShadow = `
                    ${Math.random() * 10}px ${Math.random() * 10}px rgba(255,0,0,0.3),
                    ${Math.random() * -10}px ${Math.random() * -10}px rgba(0,255,255,0.3)
                `;
                setTimeout(() => {
                    headerTitle.style.textShadow = 'none';
                }, 50);
            }
        }, 200);
    }

    // Scroll progress indicator (optional but cool)
    const progressBar = document.createElement('div');
    progressBar.style.position = 'fixed';
    progressBar.style.top = '0';
    progressBar.style.left = '0';
    progressBar.style.height = '2px';
    progressBar.style.background = 'var(--accent-color)';
    progressBar.style.zIndex = '1000';
    progressBar.style.transition = 'width 0.1s';
    document.body.appendChild(progressBar);

    window.addEventListener('scroll', () => {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        progressBar.style.width = scrolled + "%";
    });
});
