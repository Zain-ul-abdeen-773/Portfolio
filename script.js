document.addEventListener('DOMContentLoaded', () => {

    // 1. Perspective Tilt on Hover for Glass Panels (skip project cards — they use hover overlay)
    const panels = document.querySelectorAll('.glass-panel:not(.project-card)');
    
    panels.forEach(panel => {
        panel.addEventListener('mousemove', (e) => {
            const rect = panel.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width - 0.5;
            const y = (e.clientY - rect.top) / rect.height - 0.5;
            panel.style.transform = `perspective(1000px) rotateY(${x * 12}deg) rotateX(${-y * 12}deg) translateZ(20px)`;
        });
        
        panel.addEventListener('mouseleave', () => {
            panel.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg) translateZ(0)';
        });
    });

    // 2. Intersection Observer for Fade Up & Number Counting
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add visible class for fade-up animations
                if (entry.target.classList.contains('anim-fade-up')) {
                    entry.target.classList.add('visible');
                }

                // Handle Number Count Up if data-value
                if (entry.target.classList.contains('data-value') && !entry.target.dataset.counted) {
                    entry.target.dataset.counted = 'true';
                    animateValue(entry.target, 0, parseInt(entry.target.dataset.target), 1500);
                }
                
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.anim-fade-up, .data-value').forEach(el => {
        observer.observe(el);
    });

    // Function to animate numbers counting up
    function animateValue(obj, start, end, duration) {
        if (isNaN(end)) return;
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            obj.innerHTML = Math.floor(progress * (end - start) + start);
            if (progress < 1) {
                window.requestAnimationFrame(step);
            } else {
                obj.innerHTML = end;
            }
        };
        window.requestAnimationFrame(step);
    }

    // 3. Staggered Page Load Anim sequence
    setTimeout(() => {
        document.body.classList.add('loaded');
    }, 200);

});
