/**
 * video-hover.js
 * Handles play/pause on hover for blog cards and other video elements.
 */

document.addEventListener('DOMContentLoaded', function() {
    const blogCards = document.querySelectorAll('.blog-meta-one');

    blogCards.forEach(card => {
        const video = card.querySelector('video');
        
        if (video) {
            // Ensure the video is paused initially (redundancy)
            video.pause();

            card.addEventListener('mouseenter', () => {
                // Only try to play if paused
                if (video.paused) {
                    video.play().catch(error => {
                        // Suppress AbortError which occurs when mouse leaves before play starts
                        if (error.name !== 'AbortError') {
                            console.warn("Video playback failed:", error);
                        }
                    });
                }
            });

            card.addEventListener('mouseleave', () => {
                // Pause if playing
                if (!video.paused) {
                    video.pause();
                }
            });
        }
    });
});
