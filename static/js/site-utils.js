$(function () {
    "use strict";

    // ------------------------ Blog Slider
    if ($(".vjs-blog-slider").length) {
        $('.vjs-blog-slider').slick({
            dots: false,
            arrows: false,
            autoplay: true,
            autoplaySpeed: 5000,
            slidesToShow: 2,
            slidesToScroll: 1,
            responsive: [
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 2
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 1
                    }
                }
            ]
        });
    }
});

// ============================================================
// Vijayalakshmi Group - Global Site Utilities
// (Accessibility, Translation, and Persisted Settings)
// ============================================================

// Mode Logic (Light/Dark)
function vjsSetMode(mode) {
    if (mode === 'dark') {
        document.body.classList.add('vjs-dark-mode');
        localStorage.setItem('vjs-theme-mode', 'dark');
    } else {
        document.body.classList.remove('vjs-dark-mode');
        localStorage.setItem('vjs-theme-mode', 'light');
    }
}

// Font Size Logic
function vjsSetFontSize(size) {
    document.documentElement.classList.remove('vjs-font-small', 'vjs-font-normal', 'vjs-font-large');
    document.documentElement.classList.add('vjs-font-' + size);
    localStorage.setItem('vjs-font-size', size);
}

// Reset Settings
function vjsResetSettings() {
    vjsSetMode('light');
    vjsSetFontSize('normal');
    localStorage.clear();
}

// Google Translate Initialization
function googleTranslateElementInit() {
    new google.translate.TranslateElement({
        pageLanguage: 'en',
        includedLanguages: 'hi,ta,kn,te,ml,en',
        layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
        autoDisplay: false
    }, 'google_translate_element');
}

// Function to trigger translation
function vjsTranslate(langCode) {
    console.log("Attempting translation to:", langCode);
    const googleSelect = document.querySelector('select.goog-te-combo');
    
    if (googleSelect) {
        googleSelect.value = langCode;
        googleSelect.dispatchEvent(new Event('change'));
        localStorage.setItem('vjs-selected-lang', langCode);
        
        // Update Label
        const labels = { 'en': 'ENG', 'hi': 'HIN', 'ta': 'TAM', 'kn': 'KAN', 'te': 'TEL', 'ml': 'MAL' };
        $('.vjs-lang-label').text(labels[langCode] || 'ENG');
        
        // Final cleanup of Google UI
        setTimeout(() => {
            $('.goog-te-banner-frame').css('visibility', 'hidden').css('display', 'none');
            document.body.style.top = '0';
        }, 500);
    } else {
        // If not ready, retry
        setTimeout(() => vjsTranslate(langCode), 500);
    }
}

// Global Styles for Translator
$("<style>")
    .prop("type", "text/css")
    .html(`
        iframe.goog-te-banner-frame { display: none !important; }
        body { top: 0px !important; }
        .goog-te-gadget { display: none !important; }
        .goog-text-highlight { background: transparent !important; box-shadow: none !important; }
    `)
    .appendTo("head");

// On Page Load
$(document).ready(function() {
    // Re-apply saved language if any
    const savedLang = localStorage.getItem('vjs-selected-lang');
    if (savedLang && savedLang !== 'en') {
        setTimeout(() => vjsTranslate(savedLang), 2000);
    }

    // Bind click events
    $(document).on('click', '.translate-btn', function(e) {
        e.preventDefault();
        const lang = $(this).attr('data-lang') || $(this).data('lang');
        vjsTranslate(lang);
    });
});

// Initialize Settings on Load
document.addEventListener('DOMContentLoaded', function () {
    const savedMode = localStorage.getItem('vjs-theme-mode');
    const savedSize = localStorage.getItem('vjs-font-size');

    if (savedMode) vjsSetMode(savedMode);
    if (savedSize) vjsSetFontSize(savedSize);
});
