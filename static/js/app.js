// Common JavaScript functions for Newsletter App

/**
 * Copy text to clipboard with visual feedback
 * @param {string} text - Text to copy
 * @param {HTMLElement} button - Button element to show feedback on
 * @returns {Promise<boolean>} - Success status
 */
async function copyToClipboard(text, button = null) {
    try {
        await navigator.clipboard.writeText(text);
        
        if (button) {
            showButtonFeedback(button, 'Copié !', 'success');
        }
        
        return true;
    } catch (error) {
        console.error('Error copying to clipboard:', error);
        
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        
        try {
            document.execCommand('copy');
            if (button) {
                showButtonFeedback(button, 'Copié !', 'success');
            }
            return true;
        } catch (fallbackError) {
            console.error('Fallback copy failed:', fallbackError);
            if (button) {
                showButtonFeedback(button, 'Erreur !', 'danger');
            }
            return false;
        } finally {
            document.body.removeChild(textArea);
        }
    }
}

/**
 * Show temporary feedback on a button
 * @param {HTMLElement} button - Button element
 * @param {string} message - Message to show
 * @param {string} type - Type of feedback (success, danger, etc.)
 * @param {number} duration - Duration in milliseconds
 */
function showButtonFeedback(button, message, type = 'success', duration = 2000) {
    const originalHTML = button.innerHTML;
    const originalClasses = button.className;
    
    // Update button
    button.innerHTML = `<i class="fas fa-${type === 'success' ? 'check' : 'exclamation-triangle'} me-1"></i>${message}`;
    button.className = button.className.replace(/btn-\w+/g, `btn-${type}`);
    button.disabled = true;
    
    // Restore original state after duration
    setTimeout(() => {
        button.innerHTML = originalHTML;
        button.className = originalClasses;
        button.disabled = false;
    }, duration);
}

/**
 * Show notification toast
 * @param {string} message - Message to show
 * @param {string} type - Type of notification (success, error, info, warning)
 * @param {number} duration - Duration in milliseconds
 */
function showNotification(message, type = 'info', duration = 5000) {
    const toastContainer = getOrCreateToastContainer();
    
    const toastHTML = `
        <div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="toast-header">
                <i class="fas fa-${getIconForType(type)} text-${type} me-2"></i>
                <strong class="me-auto">${getTypeLabel(type)}</strong>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body">
                ${message}
            </div>
        </div>
    `;
    
    const toastElement = document.createElement('div');
    toastElement.innerHTML = toastHTML;
    const toast = toastElement.firstElementChild;
    
    toastContainer.appendChild(toast);
    
    // Auto remove after duration
    setTimeout(() => {
        if (toast.parentNode) {
            toast.classList.remove('show');
            setTimeout(() => {
                if (toast.parentNode) {
                    toastContainer.removeChild(toast);
                }
            }, 300);
        }
    }, duration);
}

/**
 * Get or create toast container
 * @returns {HTMLElement} - Toast container element
 */
function getOrCreateToastContainer() {
    let container = document.getElementById('toastContainer');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toastContainer';
        container.className = 'toast-container position-fixed top-0 end-0 p-3';
        container.style.zIndex = '1055';
        document.body.appendChild(container);
    }
    return container;
}

/**
 * Get icon class for notification type
 * @param {string} type - Notification type
 * @returns {string} - Icon class
 */
function getIconForType(type) {
    const icons = {
        success: 'check-circle',
        error: 'exclamation-triangle',
        warning: 'exclamation-triangle',
        info: 'info-circle'
    };
    return icons[type] || 'info-circle';
}

/**
 * Get label for notification type
 * @param {string} type - Notification type
 * @returns {string} - Type label
 */
function getTypeLabel(type) {
    const labels = {
        success: 'Succès',
        error: 'Erreur',
        warning: 'Attention',
        info: 'Information'
    };
    return labels[type] || 'Information';
}

/**
 * Format file size in human readable format
 * @param {number} bytes - File size in bytes
 * @returns {string} - Formatted file size
 */
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

/**
 * Validate file type
 * @param {File} file - File object
 * @param {string[]} allowedTypes - Array of allowed file extensions
 * @returns {boolean} - Validation result
 */
function validateFileType(file, allowedTypes) {
    const fileExtension = file.name.split('.').pop().toLowerCase();
    return allowedTypes.includes(fileExtension);
}

/**
 * Create loading overlay
 * @param {string} message - Loading message
 * @returns {HTMLElement} - Loading overlay element
 */
function createLoadingOverlay(message = 'Chargement...') {
    const overlay = document.createElement('div');
    overlay.className = 'loading-overlay position-fixed top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center';
    overlay.style.cssText = 'background-color: rgba(255, 255, 255, 0.9); z-index: 9999;';
    
    overlay.innerHTML = `
        <div class="text-center">
            <div class="spinner-border text-primary mb-3" role="status" style="width: 3rem; height: 3rem;">
                <span class="visually-hidden">Loading...</span>
            </div>
            <h5 class="text-primary">${message}</h5>
        </div>
    `;
    
    return overlay;
}

/**
 * Show loading overlay
 * @param {string} message - Loading message
 */
function showLoadingOverlay(message = 'Chargement...') {
    hideLoadingOverlay(); // Remove existing overlay
    const overlay = createLoadingOverlay(message);
    document.body.appendChild(overlay);
}

/**
 * Hide loading overlay
 */
function hideLoadingOverlay() {
    const existing = document.querySelector('.loading-overlay');
    if (existing) {
        existing.remove();
    }
}

/**
 * Debounce function to limit rapid function calls
 * @param {Function} func - Function to debounce
 * @param {number} wait - Wait time in milliseconds
 * @returns {Function} - Debounced function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Scroll to element smoothly
 * @param {HTMLElement|string} element - Element or selector
 * @param {number} offset - Offset from top in pixels
 */
function scrollToElement(element, offset = 0) {
    const target = typeof element === 'string' ? document.querySelector(element) : element;
    if (target) {
        const targetPosition = target.offsetTop - offset;
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    }
}

/**
 * Download text as file
 * @param {string} content - File content
 * @param {string} filename - File name
 * @param {string} mimeType - MIME type
 */
function downloadTextAsFile(content, filename, mimeType = 'text/plain') {
    const blob = new Blob([content], { type: mimeType });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
}

// Initialize common functionality when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Add fade-in animation to main content
    const mainContent = document.querySelector('main');
    if (mainContent) {
        mainContent.classList.add('fade-in');
    }
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            if (alert.parentNode) {
                alert.classList.remove('show');
                setTimeout(() => {
                    if (alert.parentNode) {
                        alert.remove();
                    }
                }, 300);
            }
        }, 5000);
    });
});

// Global error handler for unhandled promise rejections
window.addEventListener('unhandledrejection', function(event) {
    console.error('Unhandled promise rejection:', event.reason);
    showNotification('Une erreur inattendue s\'est produite. Veuillez réessayer.', 'error');
});

// Export functions for use in other scripts
window.NewsletterApp = {
    copyToClipboard,
    showButtonFeedback,
    showNotification,
    formatFileSize,
    validateFileType,
    showLoadingOverlay,
    hideLoadingOverlay,
    debounce,
    scrollToElement,
    downloadTextAsFile
};