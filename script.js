document.addEventListener("DOMContentLoaded", () => {
    // --- General Scroll Animations ---
    const scrollObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.fade-in, .fade-in-scroll').forEach(el => {
        scrollObserver.observe(el);
    });

    // --- 3D Grid Canvas Animation ---
    const canvas = document.getElementById('grid-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width, height, grid;
        const speed = 0.00003; // Slower speed

        function init() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
            grid = {
                lines: [],
                lineCount: 80, // Number of lines
                gridSpacing: 50,
                perspective: width * 0.8,
            };

            for (let i = 0; i < grid.lineCount; i++) {
                grid.lines.push({
                    z: i / grid.lineCount * 5,
                    y: 0,
                });
            }
        }

        function draw(time) {
            ctx.clearRect(0, 0, width, height);
            ctx.strokeStyle = 'rgba(0, 255, 255, 0.15)'; // Cyan color with low opacity
            ctx.lineWidth = 1;

            ctx.save();
            ctx.translate(width / 2, height / 2);

            for (let i = 0; i < grid.lineCount; i++) {
                let line = grid.lines[i];
                
                // Animate z-position
                line.z -= speed * 1000;
                if (line.z < 0) {
                    line.z = 5;
                }

                const scale = grid.perspective / (grid.perspective + line.z);
                const x = -width / 2 * scale;
                const y = (i - grid.lineCount / 2) * grid.gridSpacing * scale;
                const w = width * scale;
                
                // Horizontal lines
                ctx.beginPath();
                ctx.moveTo(x, y);
                ctx.lineTo(x + w, y);
                ctx.stroke();
            }

            // Vertical lines (simplified)
            for(let i = 0; i < 10; i++) {
                const x = (i - 5) * 200;
                 ctx.beginPath();
                 ctx.moveTo(x, -height);
                 ctx.lineTo(x, height);
                 ctx.stroke();
            }


            ctx.restore();
            requestAnimationFrame(draw);
        }

        window.addEventListener('resize', init);
        init();
        requestAnimationFrame(draw);
    }
});
