// QR Code Generator functionality
document.addEventListener('DOMContentLoaded', function() {
    const qrForm = document.getElementById('qrForm');
    const loading = document.getElementById('loading');

    if (qrForm) {
        qrForm.addEventListener('submit', handleFormSubmit);
    }
});

async function handleFormSubmit(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    const userData = {
        first_name: formData.get('first_name'),
        last_name: formData.get('last_name'),
        email: formData.get('email'),
        student_id: parseInt(formData.get('student_id')),
        standard: parseInt(formData.get('standard')),
        streamORsection: formData.get('streamORsection')
    };

    // Show loading state
    showLoading(true);

    try {
        const response = await fetch('http://127.0.0.1:8000/api/qr-gen', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData)
        });

        if (!response.ok) {
            // Handle HTTP errors and extract detail from HTTPException
            let errorMessage = `HTTP error! status: ${response.status}`;
            
            try {
                const errorData = await response.json();
                if (errorData.detail) {
                    errorMessage = errorData.detail;
                } else if (errorData.message) {
                    errorMessage = errorData.message;
                }
            } catch (parseError) {
                console.log('Could not parse error response as JSON');
            }
            
            throw new Error(errorMessage);
        }

        // Get the image blob
        const imageBlob = await response.blob();
        console.log('Image blob received, size:', imageBlob.size);
        
        // Convert blob to base64 data URL for storage
        const reader = new FileReader();
        reader.onload = function() {
            const base64DataUrl = reader.result;
            console.log('Image converted to base64, storing...');
            
            // Store the base64 image data and user info
            sessionStorage.setItem('qrImageData', base64DataUrl);
            sessionStorage.setItem('userData', JSON.stringify(userData));
            
            // Redirect to display page
            window.location.href = 'show-qr-page.html';
        };
        
        reader.onerror = function() {
            throw new Error('Failed to process image data');
        };
        
        // Convert to base64
        reader.readAsDataURL(imageBlob);
        
    } catch (error) {
        console.error('Error generating QR code:', error);
        showError(error.message);
        showLoading(false);
    }
}

function showLoading(show) {
    const loading = document.getElementById('loading');
    const form = document.getElementById('qrForm');
    
    if (show) {
        loading.style.display = 'block';
        form.style.opacity = '0.5';
        form.style.pointerEvents = 'none';
    } else {
        loading.style.display = 'none';
        form.style.opacity = '1';
        form.style.pointerEvents = 'auto';
    }
}

function showError(message) {
    // Create or update error message
    let errorDiv = document.getElementById('errorMessage');
    if (!errorDiv) {
        errorDiv = document.createElement('div');
        errorDiv.id = 'errorMessage';
        errorDiv.className = 'error-message';
        document.querySelector('.qr-generator-section .feature-card').appendChild(errorDiv);
    }
    
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    
    // Hide error after 5 seconds
    setTimeout(() => {
        errorDiv.style.display = 'none';
    }, 5000);
}