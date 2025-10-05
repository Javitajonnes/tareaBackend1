/* 
Core App - JavaScript
Blogfiction.cl - Academia de duelos, feria de coleccionismo y tecnología lúdica

Autor: Equipo Blogfiction
Fecha: 2025
*/

// Funciones JavaScript para páginas core
document.addEventListener('DOMContentLoaded', function() {
    console.log('Core app JavaScript cargado correctamente');
    
    // Función para manejar navegación suave
    function smoothScroll() {
        const links = document.querySelectorAll('a[href^="#"]');
        links.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            });
        });
    }
    
    // Función para mostrar/ocultar elementos
    function toggleElement(elementId) {
        const element = document.getElementById(elementId);
        if (element) {
            element.style.display = element.style.display === 'none' ? 'block' : 'none';
        }
    }
    
    // Función para validar formularios básicos
    function validateForm(formId) {
        const form = document.getElementById(formId);
        if (form) {
            form.addEventListener('submit', function(e) {
                const requiredFields = form.querySelectorAll('[required]');
                let isValid = true;
                
                requiredFields.forEach(field => {
                    if (!field.value.trim()) {
                        isValid = false;
                        field.style.borderColor = 'red';
                    } else {
                        field.style.borderColor = '';
                    }
                });
                
                if (!isValid) {
                    e.preventDefault();
                    alert('Por favor completa todos los campos requeridos');
                }
            });
        }
    }
    
    // Inicializar funciones
    smoothScroll();
    
    // Exponer funciones globalmente para uso en templates
    window.toggleElement = toggleElement;
    window.validateForm = validateForm;
});

// Función para mostrar mensajes de éxito/error
function showMessage(message, type = 'info') {
    const messageDiv = document.createElement('div');
    messageDiv.className = `alert alert-${type}`;
    messageDiv.textContent = message;
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '20px';
    messageDiv.style.right = '20px';
    messageDiv.style.zIndex = '9999';
    messageDiv.style.padding = '10px 20px';
    messageDiv.style.borderRadius = '5px';
    
    document.body.appendChild(messageDiv);
    
    setTimeout(() => {
        messageDiv.remove();
    }, 3000);
}
