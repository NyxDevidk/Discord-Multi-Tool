// DMS Website - Main JavaScript
// Versão 2.0 - NYX DEV

class DMSWebsite {
    constructor() {
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.initializeAnimations();
        this.setupSmoothScrolling();
        this.setupMobileMenu();
        this.setupDownloadButtons();
        this.setupScrollEffects();
        this.setupTerminalAnimation();
        this.setupIntersectionObserver();
    }

    setupEventListeners() {
        // Mobile menu toggle
        const navToggle = document.querySelector('.nav-toggle');
        const navMenu = document.querySelector('.nav-menu');
        
        if (navToggle && navMenu) {
            navToggle.addEventListener('click', () => {
                navToggle.classList.toggle('active');
                navMenu.classList.toggle('active');
            });
        }

        // Close mobile menu when clicking on a link
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navToggle?.classList.remove('active');
                navMenu?.classList.remove('active');
            });
        });

        // Header scroll effect
        window.addEventListener('scroll', () => {
            this.handleHeaderScroll();
        });

        // Download buttons
        const downloadButtons = document.querySelectorAll('.download-btn');
        downloadButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                this.handleDownload(e);
            });
        });

        // Form submissions
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {
            form.addEventListener('submit', (e) => {
                this.handleFormSubmit(e);
            });
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            this.handleKeyboardShortcuts(e);
        });
    }

    setupMobileMenu() {
        const navToggle = document.querySelector('.nav-toggle');
        const navMenu = document.querySelector('.nav-menu');
        const overlay = document.createElement('div');
        overlay.className = 'mobile-overlay';
        
        if (navToggle && navMenu) {
            navToggle.addEventListener('click', () => {
                const isActive = navMenu.classList.contains('active');
                
                if (isActive) {
                    navMenu.classList.remove('active');
                    navToggle.classList.remove('active');
                    overlay.remove();
                } else {
                    navMenu.classList.add('active');
                    navToggle.classList.add('active');
                    document.body.appendChild(overlay);
                }
            });

            // Close menu when clicking overlay
            overlay.addEventListener('click', () => {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
                overlay.remove();
            });
        }
    }

    setupSmoothScrolling() {
        const links = document.querySelectorAll('a[href^="#"]');
        
        links.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    const headerHeight = document.querySelector('.header').offsetHeight;
                    const targetPosition = targetElement.offsetTop - headerHeight;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    setupDownloadButtons() {
        const downloadButtons = document.querySelectorAll('.download-btn');
        
        downloadButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                e.preventDefault();
                this.handleDownload(e);
            });
        });
    }

    handleDownload(e) {
        const button = e.currentTarget;
        const version = button.dataset.version;
        
        // Add loading state
        button.classList.add('loading');
        const originalText = button.innerHTML;
        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Baixando...';
        
        // Simulate download (replace with actual download logic)
        setTimeout(() => {
            button.classList.remove('loading');
            button.innerHTML = originalText;
            
            // Show success message
            this.showNotification('Download iniciado!', 'success');
            
            // Actual download logic would go here
            if (version === 'full') {
                window.open('https://github.com/NyxDevidk/Discord-Multi-Tool/releases/latest', '_blank');
            } else if (version === 'simple') {
                window.open('https://github.com/NyxDevidk/Discord-Multi-Tool/archive/refs/heads/main.zip', '_blank');
            }
        }, 2000);
    }

    setupScrollEffects() {
        // Parallax effect for hero section
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const hero = document.querySelector('.hero');
            
            if (hero) {
                const rate = scrolled * -0.5;
                hero.style.transform = `translateY(${rate}px)`;
            }
        });

        // Fade in elements on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-fade-in-up');
                }
            });
        }, observerOptions);

        const animateElements = document.querySelectorAll('.feature-card, .download-card, .docs-card, .stat-card');
        animateElements.forEach(el => observer.observe(el));
    }

    setupTerminalAnimation() {
        const terminal = document.querySelector('.terminal-window');
        if (!terminal) return;

        // Typewriter effect for terminal
        const commands = [
            'python main.py',
            'pip install -r requirements.txt',
            'python installer.py'
        ];

        let commandIndex = 0;
        let charIndex = 0;
        const commandElement = terminal.querySelector('.command');
        
        if (commandElement) {
            const typeCommand = () => {
                if (charIndex < commands[commandIndex].length) {
                    commandElement.textContent = commands[commandIndex].substring(0, charIndex + 1);
                    charIndex++;
                    setTimeout(typeCommand, 100);
                } else {
                    setTimeout(() => {
                        charIndex = 0;
                        commandIndex = (commandIndex + 1) % commands.length;
                        typeCommand();
                    }, 2000);
                }
            };
            
            setTimeout(typeCommand, 1000);
        }

        // Terminal cursor blink
        const cursor = terminal.querySelector('.cursor');
        if (cursor) {
            setInterval(() => {
                cursor.style.opacity = cursor.style.opacity === '0' ? '1' : '0';
            }, 500);
        }
    }

    setupIntersectionObserver() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-fade-in-up');
                    
                    // Animate counters if present
                    const counters = entry.target.querySelectorAll('.stat-number');
                    counters.forEach(counter => {
                        this.animateCounter(counter);
                    });
                }
            });
        }, observerOptions);

        // Observe sections
        const sections = document.querySelectorAll('section');
        sections.forEach(section => observer.observe(section));
    }

    animateCounter(element) {
        const target = parseInt(element.textContent.replace(/\D/g, ''));
        const suffix = element.textContent.replace(/\d/g, '');
        let current = 0;
        const increment = target / 50;
        
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            element.textContent = Math.floor(current) + suffix;
        }, 30);
    }

    handleHeaderScroll() {
        const header = document.querySelector('.header');
        const scrolled = window.pageYOffset > 100;
        
        if (header) {
            if (scrolled) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }
    }

    handleFormSubmit(e) {
        e.preventDefault();
        const form = e.target;
        const submitButton = form.querySelector('button[type="submit"]');
        
        if (submitButton) {
            submitButton.classList.add('loading');
            submitButton.disabled = true;
            
            // Simulate form submission
            setTimeout(() => {
                submitButton.classList.remove('loading');
                submitButton.disabled = false;
                this.showNotification('Formulário enviado com sucesso!', 'success');
                form.reset();
            }, 2000);
        }
    }

    handleKeyboardShortcuts(e) {
        // Ctrl/Cmd + K to focus search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            const searchInput = document.querySelector('input[type="search"]');
            if (searchInput) {
                searchInput.focus();
            }
        }

        // Escape to close mobile menu
        if (e.key === 'Escape') {
            const navMenu = document.querySelector('.nav-menu');
            const navToggle = document.querySelector('.nav-toggle');
            if (navMenu?.classList.contains('active')) {
                navMenu.classList.remove('active');
                navToggle?.classList.remove('active');
                document.querySelector('.mobile-overlay')?.remove();
            }
        }
    }

    showNotification(message, type = 'info') {
        // Remove existing notifications
        const existingNotifications = document.querySelectorAll('.notification');
        existingNotifications.forEach(notification => notification.remove());

        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <i class="fas fa-${this.getNotificationIcon(type)}"></i>
                <span>${message}</span>
                <button class="notification-close">
                    <i class="fas fa-times"></i>
                </button>
            </div>
        `;

        // Add styles
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${this.getNotificationColor(type)};
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            z-index: 10000;
            transform: translateX(100%);
            transition: transform 0.3s ease;
            max-width: 400px;
        `;

        // Add to page
        document.body.appendChild(notification);

        // Animate in
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
        }, 100);

        // Close button functionality
        const closeButton = notification.querySelector('.notification-close');
        closeButton.addEventListener('click', () => {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => notification.remove(), 300);
        });

        // Auto remove after 5 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.style.transform = 'translateX(100%)';
                setTimeout(() => notification.remove(), 300);
            }
        }, 5000);
    }

    getNotificationIcon(type) {
        const icons = {
            success: 'check-circle',
            error: 'exclamation-circle',
            warning: 'exclamation-triangle',
            info: 'info-circle'
        };
        return icons[type] || 'info-circle';
    }

    getNotificationColor(type) {
        const colors = {
            success: '#43b581',
            error: '#f04747',
            warning: '#faa61a',
            info: '#5865f2'
        };
        return colors[type] || '#5865f2';
    }

    initializeAnimations() {
        // Add CSS for animations
        const style = document.createElement('style');
        style.textContent = `
            .mobile-overlay {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.5);
                z-index: 999;
                backdrop-filter: blur(4px);
            }

            .header.scrolled {
                background: rgba(10, 10, 10, 0.98);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            }

            .notification-content {
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }

            .notification-close {
                background: none;
                border: none;
                color: white;
                cursor: pointer;
                padding: 0;
                margin-left: auto;
                opacity: 0.7;
                transition: opacity 0.2s;
            }

            .notification-close:hover {
                opacity: 1;
            }

            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            .animate-fade-in-up {
                animation: fadeInUp 0.6s ease-out forwards;
            }

            .feature-card, .download-card, .docs-card, .stat-card {
                opacity: 0;
                transform: translateY(30px);
            }

            .feature-card.animate-fade-in-up,
            .download-card.animate-fade-in-up,
            .docs-card.animate-fade-in-up,
            .stat-card.animate-fade-in-up {
                opacity: 1;
                transform: translateY(0);
            }
        `;
        document.head.appendChild(style);
    }
}

// Performance monitoring
class PerformanceMonitor {
    constructor() {
        this.metrics = {};
        this.init();
    }

    init() {
        // Monitor page load time
        window.addEventListener('load', () => {
            this.metrics.pageLoadTime = performance.now();
            this.logMetric('Page Load Time', this.metrics.pageLoadTime);
        });

        // Monitor scroll performance
        let scrollTimeout;
        window.addEventListener('scroll', () => {
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                this.metrics.scrollPerformance = performance.now();
            }, 100);
        });

        // Monitor click events
        document.addEventListener('click', (e) => {
            this.logMetric('Click Event', e.target.tagName);
        });
    }

    logMetric(name, value) {
        if (process.env.NODE_ENV === 'development') {
            console.log(`[Performance] ${name}:`, value);
        }
    }
}

// Analytics (simplified)
class Analytics {
    constructor() {
        this.events = [];
        this.init();
    }

    init() {
        // Track page views
        this.trackPageView();

        // Track button clicks
        document.addEventListener('click', (e) => {
            if (e.target.matches('a, button')) {
                this.trackEvent('click', {
                    element: e.target.tagName,
                    text: e.target.textContent?.trim(),
                    href: e.target.href
                });
            }
        });

        // Track scroll depth
        let maxScroll = 0;
        window.addEventListener('scroll', () => {
            const scrollPercent = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);
            if (scrollPercent > maxScroll) {
                maxScroll = scrollPercent;
                if (maxScroll % 25 === 0) { // Track every 25%
                    this.trackEvent('scroll_depth', { depth: maxScroll });
                }
            }
        });
    }

    trackPageView() {
        this.trackEvent('page_view', {
            page: window.location.pathname,
            title: document.title
        });
    }

    trackEvent(eventName, properties = {}) {
        const event = {
            name: eventName,
            properties,
            timestamp: new Date().toISOString(),
            url: window.location.href
        };

        this.events.push(event);

        // In a real implementation, you would send this to your analytics service
        if (process.env.NODE_ENV === 'development') {
            console.log('[Analytics]', event);
        }
    }
}

// Error handling
class ErrorHandler {
    constructor() {
        this.init();
    }

    init() {
        window.addEventListener('error', (e) => {
            this.handleError(e.error || e.message, e.filename, e.lineno);
        });

        window.addEventListener('unhandledrejection', (e) => {
            this.handleError(e.reason, 'Promise Rejection');
        });
    }

    handleError(error, filename = '', lineno = '') {
        const errorInfo = {
            message: error.message || error,
            filename,
            lineno,
            stack: error.stack,
            timestamp: new Date().toISOString(),
            url: window.location.href,
            userAgent: navigator.userAgent
        };

        // In a real implementation, you would send this to your error tracking service
        if (process.env.NODE_ENV === 'development') {
            console.error('[Error]', errorInfo);
        }
    }
}

// Initialize everything when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Initialize main website functionality
    window.dmsWebsite = new DMSWebsite();
    
    // Initialize performance monitoring
    window.performanceMonitor = new PerformanceMonitor();
    
    // Initialize analytics
    window.analytics = new Analytics();
    
    // Initialize error handling
    window.errorHandler = new ErrorHandler();
    
    // Log initialization
    console.log('🚀 DMS Website initialized successfully!');
    console.log('📊 Performance monitoring active');
    console.log('📈 Analytics tracking active');
    console.log('🛡️ Error handling active');
});

// Service Worker registration (for PWA features)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { DMSWebsite, PerformanceMonitor, Analytics, ErrorHandler };
} 