// charts.js
// INSANE HACKER-LEVEL Log Analytics Charts (CONNECTED VERSION)

document.addEventListener("DOMContentLoaded", () => {
    const chartCanvas = document.getElementById("logChart");

    // If dashboard doesn't have chart canvas, exit safely
    if (!chartCanvas) return;

    const ctx = chartCanvas.getContext("2d");

    // Read values injected from backend (Flask → HTML → JS)
    const errorCount   = Number(chartCanvas.dataset.errors || 0);
    const warningCount = Number(chartCanvas.dataset.warnings || 0);
    const infoCount    = Number(chartCanvas.dataset.info || 0);

    // Hacker glow effect
    const glowPlugin = {
        id: "glow",
        beforeDraw(chart) {
            const ctx = chart.ctx;
            ctx.save();
            ctx.shadowColor = "#00ff00";
            ctx.shadowBlur = 20;
            ctx.restore();
        }
    };

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["ERROR", "WARNING", "INFO"],
            datasets: [{
                label: "LOG EVENTS",
                data: [errorCount, warningCount, infoCount],
                backgroundColor: [
                    "rgba(255, 0, 0, 0.85)",     // ERROR
                    "rgba(255, 255, 0, 0.85)",   // WARNING
                    "rgba(0, 255, 255, 0.85)"    // INFO
                ],
                borderColor: "#00ff00",
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            animation: {
                duration: 1200,
                easing: "easeOutQuart"
            },
            plugins: {
                legend: {
                    labels: {
                        color: "#00ff00",
                        font: {
                            family: "Share Tech Mono",
                            size: 14
                        }
                    }
                },
                tooltip: {
                    backgroundColor: "#000",
                    borderColor: "#00ff00",
                    borderWidth: 1,
                    titleColor: "#00ff00",
                    bodyColor: "#00ff00"
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: "#00ff00",
                        font: {
                            family: "Share Tech Mono"
                        }
                    },
                    grid: {
                        color: "rgba(0,255,0,0.15)"
                    }
                },
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: "#00ff00",
                        font: {
                            family: "Share Tech Mono"
                        }
                    },
                    grid: {
                        color: "rgba(0,255,0,0.15)"
                    }
                }
            }
        },
        plugins: [glowPlugin]
    });
});
